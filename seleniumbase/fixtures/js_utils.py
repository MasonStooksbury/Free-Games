"""
This module contains useful Javascript utility methods for base_case.py
These helper methods SHOULD NOT be called directly from tests.
"""
import re
import requests
import time
from selenium.common.exceptions import WebDriverException
from seleniumbase import config as sb_config
from seleniumbase.common import decorators
from seleniumbase.config import settings
from seleniumbase.fixtures import constants
from seleniumbase.fixtures import shared_utils


def wait_for_ready_state_complete(driver, timeout=settings.EXTREME_TIMEOUT):
    """
    The DOM (Document Object Model) has a property called "readyState".
    When the value of this becomes "complete", page resources are considered
    fully loaded (although AJAX and other loads might still be happening).
    This method will wait until document.readyState == "complete".
    """
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    for x in range(int(timeout * 10)):
        shared_utils.check_if_time_limit_exceeded()
        try:
            # If there's an alert, skip
            driver.switch_to.alert
            return
        except Exception:
            # If there's no alert, continue
            pass
        try:
            ready_state = driver.execute_script("return document.readyState")
        except WebDriverException:
            # Bug fix for: [Permission denied to access property "document"]
            time.sleep(0.03)
            return True
        if ready_state == u'complete':
            time.sleep(0.01)  # Better be sure everything is done loading
            return True
        else:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)
    raise Exception(
        "Page elements never fully loaded after %s seconds!" % timeout)


def execute_async_script(driver, script, timeout=settings.EXTREME_TIMEOUT):
    driver.set_script_timeout(timeout)
    return driver.execute_async_script(script)


def wait_for_angularjs(driver, timeout=settings.LARGE_TIMEOUT, **kwargs):
    try:
        # If there's an alert, skip
        driver.switch_to.alert
        return
    except Exception:
        # If there's no alert, continue
        pass
    if not settings.WAIT_FOR_ANGULARJS:
        return

    NG_WRAPPER = '%(prefix)s' \
                 'var $elm=document.querySelector(' \
                 '\'[data-ng-app],[ng-app],.ng-scope\')||document;' \
                 'if(window.angular && angular.getTestability){' \
                 'angular.getTestability($elm).whenStable(%(handler)s)' \
                 '}else{' \
                 'var $inj;try{$inj=angular.element($elm).injector()||' \
                 'angular.injector([\'ng\'])}catch(ex){' \
                 '$inj=angular.injector([\'ng\'])};$inj.get=$inj.get||' \
                 '$inj;$inj.get(\'$browser\').' \
                 'notifyWhenNoOutstandingRequests(%(handler)s)}' \
                 '%(suffix)s'
    def_pre = 'var cb=arguments[arguments.length-1];if(window.angular){'
    prefix = kwargs.pop('prefix', def_pre)
    handler = kwargs.pop('handler', 'function(){cb(true)}')
    suffix = kwargs.pop('suffix', '}else{cb(false)}')
    script = NG_WRAPPER % {'prefix': prefix,
                           'handler': handler,
                           'suffix': suffix}
    try:
        execute_async_script(driver, script, timeout=timeout)
    except Exception:
        time.sleep(0.05)


def is_html_inspector_activated(driver):
    try:
        driver.execute_script("HTMLInspector")  # Fails if not defined
        return True
    except Exception:
        return False


def is_jquery_activated(driver):
    try:
        driver.execute_script("jQuery('html')")  # Fails if jq is not defined
        return True
    except Exception:
        return False


def wait_for_jquery_active(driver, timeout=None):
    if not timeout:
        timeout = int(settings.MINI_TIMEOUT * 10.0)
    else:
        timeout = int(timeout * 10.0)
    for x in range(timeout):
        # jQuery needs a small amount of time to activate.
        try:
            driver.execute_script("jQuery('html')")
            wait_for_ready_state_complete(driver)
            wait_for_angularjs(driver)
            return
        except Exception:
            time.sleep(0.1)


def raise_unable_to_load_jquery_exception(driver):
    """ The most-likely reason for jQuery not loading on web pages. """
    raise Exception(
        '''Unable to load jQuery on "%s" due to a possible violation '''
        '''of the website's Content Security Policy directive. '''
        '''To override this policy, add "--disable-csp" on the '''
        '''command-line when running your tests.''' % driver.current_url)


def activate_jquery(driver):
    """ If "jQuery is not defined", use this method to activate it for use.
        This happens because jQuery is not always defined on web sites. """
    try:
        # Let's first find out if jQuery is already defined.
        driver.execute_script("jQuery('html')")
        # Since that command worked, jQuery is defined. Let's return.
        return
    except Exception:
        # jQuery is not currently defined. Let's proceed by defining it.
        pass
    jquery_js = constants.JQuery.MIN_JS
    activate_jquery_script = (
        '''var script = document.createElement('script');'''
        '''script.src = "%s";document.getElementsByTagName('head')[0]'''
        '''.appendChild(script);''' % jquery_js)
    driver.execute_script(activate_jquery_script)
    for x in range(int(settings.MINI_TIMEOUT * 10.0)):
        # jQuery needs a small amount of time to activate.
        try:
            driver.execute_script("jQuery('html')")
            return
        except Exception:
            time.sleep(0.1)
    # Since jQuery still isn't activating, give up and raise an exception
    raise_unable_to_load_jquery_exception(driver)


def are_quotes_escaped(string):
    if (string.count("\\'") != string.count("'") or (
            string.count('\\"') != string.count('"'))):
        return True
    return False


def escape_quotes_if_needed(string):
    """
    re.escape() works differently in Python 3.7.0 than earlier versions:

    Python 3.6.5:
    >>> import re
    >>> re.escape('"')
    '\\"'

    Python 3.7.0:
    >>> import re
    >>> re.escape('"')
    '"'

    SeleniumBase needs quotes to be properly escaped for Javascript calls.
    """
    if are_quotes_escaped(string):
        if string.count("'") != string.count("\\'"):
            string = string.replace("'", "\\'")
        if string.count('"') != string.count('\\"'):
            string = string.replace('"', '\\"')
    return string


def safe_execute_script(driver, script):
    """ When executing a script that contains a jQuery command,
        it's important that the jQuery library has been loaded first.
        This method will load jQuery if it wasn't already loaded. """
    try:
        driver.execute_script(script)
    except Exception:
        # The likely reason this fails is because: "jQuery is not defined"
        activate_jquery(driver)  # It's a good thing we can define it here
        driver.execute_script(script)


def wait_for_css_query_selector(
        driver, selector, timeout=settings.SMALL_TIMEOUT):
    element = None
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    for x in range(int(timeout * 10)):
        try:
            selector = re.escape(selector)
            selector = escape_quotes_if_needed(selector)
            element = driver.execute_script(
                """return document.querySelector('%s')""" % selector)
            if element:
                return element
        except Exception:
            element = None
        if not element:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)

    raise Exception(
        "Element {%s} was not present after %s seconds!" % (
            selector, timeout))


def highlight_with_js(driver, selector, loops, o_bs):
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(128, 128, 128, 0.5)';"""
              % selector)
    try:
        driver.execute_script(script)
    except Exception:
        return
    for n in range(loops):
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(255, 0, 0, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(128, 0, 128, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(0, 0, 255, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(0, 255, 0, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(128, 128, 0, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
        script = ("""document.querySelector('%s').style.boxShadow =
                  '0px 0px 6px 6px rgba(128, 0, 128, 1)';"""
                  % selector)
        driver.execute_script(script)
        time.sleep(0.0181)
    script = ("""document.querySelector('%s').style.boxShadow =
              '%s';"""
              % (selector, o_bs))
    driver.execute_script(script)


def highlight_with_jquery(driver, selector, loops, o_bs):
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(128, 128, 128, 0.5)');""" % selector
    safe_execute_script(driver, script)
    for n in range(loops):
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(255, 0, 0, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(128, 0, 128, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(0, 0, 255, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(0, 255, 0, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(128, 128, 0, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
        script = """jQuery('%s').css('box-shadow',
            '0px 0px 6px 6px rgba(128, 0, 128, 1)');""" % selector
        driver.execute_script(script)
        time.sleep(0.0181)
    script = """jQuery('%s').css('box-shadow', '%s');""" % (selector, o_bs)
    driver.execute_script(script)


def add_css_link(driver, css_link):
    script_to_add_css = (
        """function injectCSS(css) {
              var head = document.getElementsByTagName("head")[0];
              var link = document.createElement("link");
              link.rel = "stylesheet";
              link.type = "text/css";
              link.href = css;
              link.crossorigin = "anonymous";
              head.appendChild(link);
           }
           injectCSS("%s");""")
    css_link = escape_quotes_if_needed(css_link)
    driver.execute_script(script_to_add_css % css_link)


def add_js_link(driver, js_link):
    script_to_add_js = (
        """function injectJS(link) {
              var body = document.getElementsByTagName("body")[0];
              var script = document.createElement("script");
              script.src = link;
              script.defer;
              script.type="text/javascript";
              script.crossorigin = "anonymous";
              script.onload = function() { null };
              body.appendChild(script);
           }
           injectJS("%s");""")
    js_link = escape_quotes_if_needed(js_link)
    driver.execute_script(script_to_add_js % js_link)


def add_css_style(driver, css_style):
    add_css_style_script = (
        """function injectStyle(css) {
              var head = document.getElementsByTagName("head")[0];
              var style = document.createElement("style");
              style.type = "text/css";
              style.appendChild(document.createTextNode(css));
              head.appendChild(style);
           }
           injectStyle("%s");""")
    css_style = css_style.replace('\n', '')
    css_style = escape_quotes_if_needed(css_style)
    driver.execute_script(add_css_style_script % css_style)


def add_js_code_from_link(driver, js_link):
    if js_link.startswith("//"):
        js_link = "http:" + js_link
    js_code = requests.get(js_link).text
    add_js_code_script = (
        '''var body = document.getElementsByTagName('body').item(0);'''
        '''var script = document.createElement("script");'''
        '''script.type = "text/javascript";'''
        '''script.onload = function() { null };'''
        '''script.appendChild(document.createTextNode("%s"));'''
        '''body.appendChild(script);''')
    js_code = js_code.replace('\n', ' ')
    js_code = escape_quotes_if_needed(js_code)
    driver.execute_script(add_js_code_script % js_code)


def add_js_code(driver, js_code):
    add_js_code_script = (
        '''var body = document.getElementsByTagName('body').item(0);'''
        '''var script = document.createElement("script");'''
        '''script.type = "text/javascript";'''
        '''script.onload = function() { null };'''
        '''script.appendChild(document.createTextNode("%s"));'''
        '''body.appendChild(script);''')
    js_code = js_code.replace('\n', ' ')
    js_code = escape_quotes_if_needed(js_code)
    driver.execute_script(add_js_code_script % js_code)


def add_meta_tag(driver, http_equiv=None, content=None):
    if http_equiv is None:
        http_equiv = "Content-Security-Policy"
    if content is None:
        content = ("default-src *; style-src 'self' 'unsafe-inline'; "
                   "script-src: 'self' 'unsafe-inline' 'unsafe-eval'")
    script_to_add_meta = (
        """function injectMeta() {
           var meta = document.createElement('meta');
           meta.httpEquiv = "%s";
           meta.content = "%s";
           document.getElementsByTagName('head')[0].appendChild(meta);
        }
        injectMeta();""" % (http_equiv, content))
    driver.execute_script(script_to_add_meta)


def is_jquery_confirm_activated(driver):
    try:
        driver.execute_script("jconfirm")  # Fails if jq_confirm is not defined
        return True
    except Exception:
        return False


def activate_jquery_confirm(driver):
    jquery_js = constants.JQuery.MIN_JS
    jq_confirm_css = constants.JqueryConfirm.MIN_CSS
    jq_confirm_js = constants.JqueryConfirm.MIN_JS

    if not is_jquery_activated(driver):
        add_js_link(driver, jquery_js)
        wait_for_jquery_active(driver, timeout=0.9)
    add_css_link(driver, jq_confirm_css)
    add_js_link(driver, jq_confirm_js)

    for x in range(15):
        # jQuery-Confirm needs a small amount of time to load & activate.
        try:
            driver.execute_script("jconfirm")
            wait_for_ready_state_complete(driver)
            wait_for_angularjs(driver)
            return
        except Exception:
            time.sleep(0.1)


def activate_html_inspector(driver):
    jquery_js = constants.JQuery.MIN_JS
    html_inspector_js = constants.HtmlInspector.MIN_JS

    if is_html_inspector_activated(driver):
        return
    if not is_jquery_activated(driver):
        add_js_link(driver, jquery_js)
        wait_for_ready_state_complete(driver)
        wait_for_angularjs(driver)
        wait_for_jquery_active(driver, timeout=1.5)
    add_js_link(driver, html_inspector_js)
    wait_for_ready_state_complete(driver)
    wait_for_angularjs(driver)

    for x in range(15):
        # HTML-Inspector needs a small amount of time to load & activate.
        try:
            driver.execute_script("HTMLInspector")
            wait_for_ready_state_complete(driver)
            wait_for_angularjs(driver)
            return
        except Exception:
            time.sleep(0.1)
    wait_for_ready_state_complete(driver)
    wait_for_angularjs(driver)


def activate_messenger(driver):
    jquery_js = constants.JQuery.MIN_JS
    messenger_css = constants.Messenger.MIN_CSS
    messenger_js = constants.Messenger.MIN_JS
    msgr_theme_flat_js = constants.Messenger.THEME_FLAT_JS
    msgr_theme_future_js = constants.Messenger.THEME_FUTURE_JS
    msgr_theme_flat_css = constants.Messenger.THEME_FLAT_CSS
    msgr_theme_future_css = constants.Messenger.THEME_FUTURE_CSS
    msgr_theme_block_css = constants.Messenger.THEME_BLOCK_CSS
    msgr_theme_air_css = constants.Messenger.THEME_AIR_CSS
    msgr_theme_ice_css = constants.Messenger.THEME_ICE_CSS
    spinner_css = constants.Messenger.SPINNER_CSS
    underscore_js = constants.Underscore.MIN_JS
    backbone_js = constants.Backbone.MIN_JS

    msg_style = ("Messenger.options = {'maxMessages': 8, "
                 "extraClasses: 'messenger-fixed "
                 "messenger-on-bottom messenger-on-right', "
                 "theme: 'future'}")

    add_js_link(driver, jquery_js)
    wait_for_jquery_active(driver, timeout=0.2)
    add_css_link(driver, messenger_css)
    add_css_link(driver, msgr_theme_flat_css)
    add_css_link(driver, msgr_theme_future_css)
    add_css_link(driver, msgr_theme_block_css)
    add_css_link(driver, msgr_theme_air_css)
    add_css_link(driver, msgr_theme_ice_css)
    add_js_link(driver, underscore_js)
    add_js_link(driver, backbone_js)
    add_css_link(driver, spinner_css)
    add_js_link(driver, messenger_js)
    add_js_link(driver, msgr_theme_flat_js)
    add_js_link(driver, msgr_theme_future_js)
    from seleniumbase.core import style_sheet
    add_css_style(driver, style_sheet.messenger_style)

    for x in range(int(settings.MINI_TIMEOUT * 10.0)):
        # Messenger needs a small amount of time to load & activate.
        try:
            driver.execute_script(msg_style)
            wait_for_ready_state_complete(driver)
            wait_for_angularjs(driver)
            return
        except Exception:
            time.sleep(0.1)


def set_messenger_theme(driver, theme="default", location="default",
                        max_messages="default"):
    if theme == "default":
        theme = "future"
    if location == "default":
        location = "bottom_right"
    if max_messages == "default":
        max_messages = "8"

    valid_themes = ['flat', 'future', 'block', 'air', 'ice']
    if theme not in valid_themes:
        raise Exception("Theme: %s is not in %s!" % (theme, valid_themes))
    valid_locations = (['top_left', 'top_center', 'top_right'
                        'bottom_left', 'bottom_center', 'bottom_right'])
    if location not in valid_locations:
        raise Exception(
            "Location: %s is not in %s!" % (location, valid_locations))

    if location == 'top_left':
        messenger_location = "messenger-on-top messenger-on-left"
    elif location == 'top_center':
        messenger_location = "messenger-on-top"
    elif location == 'top_right':
        messenger_location = "messenger-on-top messenger-on-right"
    elif location == 'bottom_left':
        messenger_location = "messenger-on-bottom messenger-on-left"
    elif location == 'bottom_center':
        messenger_location = "messenger-on-bottom"
    elif location == 'bottom_right':
        messenger_location = "messenger-on-bottom messenger-on-right"

    msg_style = ("Messenger.options = {'maxMessages': %s, "
                 "extraClasses: 'messenger-fixed %s', theme: '%s'}"
                 % (max_messages, messenger_location, theme))
    try:
        driver.execute_script(msg_style)
    except Exception:
        activate_messenger(driver)
        driver.execute_script(msg_style)
    time.sleep(0.1)


def post_message(driver, message, msg_dur, style="info"):
    """ A helper method to post a message on the screen with Messenger.
        (Should only be called from post_message() in base_case.py) """
    if not msg_dur:
        msg_dur = settings.DEFAULT_MESSAGE_DURATION
    msg_dur = float(msg_dur)
    message = re.escape(message)
    message = escape_quotes_if_needed(message)
    messenger_script = ('''Messenger().post({message: "%s", type: "%s", '''
                        '''hideAfter: %s, hideOnNavigate: true});'''
                        % (message, style, msg_dur))
    try:
        driver.execute_script(messenger_script)
    except Exception:
        activate_messenger(driver)
        set_messenger_theme(driver)
        try:
            driver.execute_script(messenger_script)
        except Exception:
            time.sleep(0.2)
            activate_messenger(driver)
            time.sleep(0.2)
            set_messenger_theme(driver)
            time.sleep(0.5)
            driver.execute_script(messenger_script)


def post_messenger_success_message(driver, message, msg_dur):
    if not msg_dur:
        msg_dur = settings.DEFAULT_MESSAGE_DURATION
    msg_dur = float(msg_dur)
    try:
        theme = "future"
        location = "bottom_right"
        if sb_config.mobile_emulator:
            theme = "block"
            location = "top_center"
        set_messenger_theme(driver, theme=theme, location=location)
        post_message(
            driver, message, msg_dur, style="success")
        time.sleep(msg_dur + 0.07)
    except Exception:
        pass


def post_messenger_error_message(driver, message, msg_dur):
    if not msg_dur:
        msg_dur = settings.DEFAULT_MESSAGE_DURATION
    msg_dur = float(msg_dur)
    try:
        set_messenger_theme(driver, theme="block", location="top_center")
        post_message(
            driver, message, msg_dur, style="error")
        time.sleep(msg_dur + 0.07)
    except Exception:
        pass


def highlight_with_js_2(driver, message, selector, o_bs, msg_dur):
    if selector == "html":
        selector = "body"
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(128, 128, 128, 0.5)';"""
              % selector)
    try:
        driver.execute_script(script)
    except Exception:
        return
    time.sleep(0.0181)
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(205, 30, 0, 1)';"""
              % selector)
    driver.execute_script(script)
    time.sleep(0.0181)
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(128, 0, 128, 1)';"""
              % selector)
    driver.execute_script(script)
    time.sleep(0.0181)
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(50, 50, 128, 1)';"""
              % selector)
    driver.execute_script(script)
    time.sleep(0.0181)
    script = ("""document.querySelector('%s').style.boxShadow =
              '0px 0px 6px 6px rgba(50, 205, 50, 1)';"""
              % selector)
    driver.execute_script(script)
    time.sleep(0.0181)

    post_messenger_success_message(driver, message, msg_dur)

    script = ("""document.querySelector('%s').style.boxShadow =
              '%s';""" % (selector, o_bs))
    driver.execute_script(script)


def highlight_with_jquery_2(driver, message, selector, o_bs, msg_dur):
    if selector == "html":
        selector = "body"
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(128, 128, 128, 0.5)');""" % selector
    try:
        safe_execute_script(driver, script)
    except Exception:
        return
    time.sleep(0.0181)
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(205, 30, 0, 1)');""" % selector
    driver.execute_script(script)
    time.sleep(0.0181)
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(128, 0, 128, 1)');""" % selector
    driver.execute_script(script)
    time.sleep(0.0181)
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(50, 50, 200, 1)');""" % selector
    driver.execute_script(script)
    time.sleep(0.0181)
    script = """jQuery('%s').css('box-shadow',
        '0px 0px 6px 6px rgba(50, 205, 50, 1)');""" % selector
    driver.execute_script(script)
    time.sleep(0.0181)

    post_messenger_success_message(driver, message, msg_dur)

    script = """jQuery('%s').css('box-shadow', '%s');""" % (selector, o_bs)
    driver.execute_script(script)


def scroll_to_element(driver, element):
    element_location = None
    try:
        element_location = element.location['y']
    except Exception:
        # element.location_once_scrolled_into_view  # Old hack
        return False
    element_location = element_location - 130
    if element_location < 0:
        element_location = 0
    scroll_script = "window.scrollTo(0, %s);" % element_location
    # The old jQuery scroll_script required by=By.CSS_SELECTOR
    # scroll_script = "jQuery('%s')[0].scrollIntoView()" % selector
    try:
        driver.execute_script(scroll_script)
        return True
    except Exception:
        return False


def slow_scroll_to_element(driver, element, browser):
    if browser == 'ie':
        # IE breaks on slow-scrolling. Do a fast scroll instead.
        scroll_to_element(driver, element)
        return
    scroll_position = driver.execute_script("return window.scrollY;")
    element_location = None
    try:
        element_location = element.location['y']
    except Exception:
        element.location_once_scrolled_into_view
        return
    element_location = element_location - 130
    if element_location < 0:
        element_location = 0
    distance = element_location - scroll_position
    if distance != 0:
        total_steps = int(abs(distance) / 50.0) + 2.0
        step_value = float(distance) / total_steps
        new_position = scroll_position
        for y in range(int(total_steps)):
            time.sleep(0.0114)
            new_position += step_value
            scroll_script = "window.scrollTo(0, %s);" % new_position
            driver.execute_script(scroll_script)
    time.sleep(0.01)
    scroll_script = "window.scrollTo(0, %s);" % element_location
    driver.execute_script(scroll_script)
    time.sleep(0.01)
    if distance > 430 or distance < -300:
        # Add small recovery time for long-distance slow-scrolling
        time.sleep(0.162)


@decorators.deprecated("Use re.escape() instead, which does what you want!")
def _jq_format(code):
    """
    DEPRECATED - Use re.escape() instead, which performs the intended action.
    Use before throwing raw code such as 'div[tab="advanced"]' into jQuery.
    Selectors with quotes inside of quotes would otherwise break jQuery.
    If you just want to escape quotes, there's escape_quotes_if_needed().
    This is similar to "json.dumps(value)", but with one less layer of quotes.
    """
    code = code.replace('\\', '\\\\').replace('\t', '\\t').replace('\n', '\\n')
    code = code.replace('\"', '\\\"').replace('\'', '\\\'')
    code = code.replace('\v', '\\v').replace('\a', '\\a').replace('\f', '\\f')
    code = code.replace('\b', '\\b').replace(r'\u', '\\u').replace('\r', '\\r')
    return code
