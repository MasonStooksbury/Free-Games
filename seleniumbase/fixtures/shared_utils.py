"""
This module contains shared utility methods.
"""
import time
from selenium.webdriver.remote.errorhandler import ElementNotVisibleException
from selenium.webdriver.remote.errorhandler import NoSuchElementException
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from selenium.webdriver.remote.errorhandler import NoSuchFrameException
from selenium.webdriver.remote.errorhandler import NoSuchWindowException
from seleniumbase.common.exceptions import NoSuchFileException
from seleniumbase.common.exceptions import TimeLimitExceededException
from seleniumbase import config as sb_config


def format_exc(exception, message):
    """
    Formats an exception message to make the output cleaner.
    """
    if exception == Exception:
        exc = Exception
        return exc, message
    elif exception == ElementNotVisibleException:
        exc = ElementNotVisibleException
    elif exception == "ElementNotVisibleException":
        exc = ElementNotVisibleException
    elif exception == NoSuchElementException:
        exc = NoSuchElementException
    elif exception == "NoSuchElementException":
        exc = NoSuchElementException
    elif exception == NoAlertPresentException:
        exc = NoAlertPresentException
    elif exception == "NoAlertPresentException":
        exc = NoAlertPresentException
    elif exception == NoSuchFrameException:
        exc = NoSuchFrameException
    elif exception == "NoSuchFrameException":
        exc = NoSuchFrameException
    elif exception == NoSuchWindowException:
        exc = NoSuchWindowException
    elif exception == "NoSuchWindowException":
        exc = NoSuchWindowException
    elif exception == "NoSuchFileException":
        exc = NoSuchFileException
    elif type(exception) is str:
        exc = Exception
        message = "%s: %s" % (exception, message)
        return exc, message
    else:
        exc = Exception
        return exc, message
    message = _format_message(message)
    return exc, message


def _format_message(message):
    message = "\n " + message
    return message


def __time_limit_exceeded(message):
    raise TimeLimitExceededException(message)


def check_if_time_limit_exceeded():
    if sb_config.time_limit:
        time_limit = sb_config.time_limit
        now_ms = int(time.time() * 1000)
        if now_ms > sb_config.start_time_ms + sb_config.time_limit_ms:
            display_time_limit = time_limit
            plural = "s"
            if float(int(time_limit)) == float(time_limit):
                display_time_limit = int(time_limit)
                if display_time_limit == 1:
                    plural = ""
            message = (
                "This test has exceeded the time limit of %s second%s!"
                "" % (display_time_limit, plural))
            message = _format_message(message)
            __time_limit_exceeded(message)
