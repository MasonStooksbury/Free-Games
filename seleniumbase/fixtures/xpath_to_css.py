"""
Convert XPath selectors into CSS selectors
"""

import re

_sub_regexes = {
    "tag": r"([a-zA-Z][a-zA-Z0-9]{0,10}|\*)",
    "attribute": r"[.a-zA-Z_:][-\w:.]*(\(\))?)",
    "value": r"\s*[\w/:][-/\w\s,:;.]*"
}

_validation_re = (
    r"(?P<node>"
    r"("
    r"^id\([\"\']?(?P<idvalue>%(value)s)[\"\']?\)"
    r"|"
    r"(?P<nav>//?)(?P<tag>%(tag)s)"
    r"(\[("
    r"(?P<matched>(?P<mattr>@?%(attribute)s=[\"\']"
    r"(?P<mvalue>%(value)s))[\"\']"
    r"|"
    r"(?P<contained>contains\((?P<cattr>@?%(attribute)s,\s*[\"\']"
    r"(?P<cvalue>%(value)s)[\"\']\))"
    r")\])?"
    r"(\[(?P<nth>\d)\])?"
    r")"
    r")" % _sub_regexes
)

prog = re.compile(_validation_re)


class XpathException(Exception):
    pass


def _handle_brackets_in_strings(xpath):
    # Edge Case: Brackets in strings.
    # Example from GitHub.com -
    # '<input type="text" id="user[login]">' => '//*[@id="user[login]"]'
    # Need to tell apart string-brackets from regular brackets
    new_xpath = ""
    chunks = xpath.split('"')
    len_chunks = len(chunks)
    for chunk_num in range(len_chunks):
        if chunk_num % 2 != 0:
            chunks[chunk_num] = chunks[chunk_num].replace(
                '[', '_STR_L_bracket_')
            chunks[chunk_num] = chunks[chunk_num].replace(
                ']', '_STR_R_bracket_')
        new_xpath += chunks[chunk_num]
        if chunk_num != len_chunks - 1:
            new_xpath += '"'
    return new_xpath


def _filter_xpath_grouping(xpath):
    """
    This method removes the outer parentheses for xpath grouping.
    The xpath converter will break otherwise.
    Example:
    "(//button[@type='submit'])[1]" becomes "//button[@type='submit'][1]"
    """

    # First remove the first open parentheses
    xpath = xpath[1:]

    # Next remove the last closed parentheses
    index = xpath.rfind(')')
    if index == -1:
        raise XpathException("Invalid or unsupported Xpath: %s" % xpath)
    xpath = xpath[:index] + xpath[index + 1:]
    return xpath


def _get_raw_css_from_xpath(xpath):
    css = ""
    position = 0

    while position < len(xpath):
        node = prog.match(xpath[position:])
        if node is None:
            raise XpathException("Invalid or unsupported Xpath: %s" % xpath)
        match = node.groupdict()

        if position != 0:
            nav = " " if match['nav'] == "//" else " > "
        else:
            nav = ""

        tag = "" if match['tag'] == "*" else match['tag'] or ""

        if match['idvalue']:
            attr = "#%s" % match['idvalue'].replace(" ", "#")
        elif match['matched']:
            if match['mattr'] == "@id":
                attr = "#%s" % match['mvalue'].replace(" ", "#")
            elif match['mattr'] == "@class":
                attr = ".%s" % match['mvalue'].replace(" ", ".")
            elif match['mattr'] in ["text()", "."]:
                attr = ":contains(^%s$)" % match['mvalue']
            elif match['mattr']:
                attr = '[%s="%s"]' % (match['mattr'].replace("@", ""),
                                      match['mvalue'])
        elif match['contained']:
            if match['cattr'].startswith("@"):
                attr = '[%s*="%s"]' % (match['cattr'].replace("@", ""),
                                       match['cvalue'])
            elif match['cattr'] == "text()":
                attr = ":contains(%s)" % match['cvalue']
        else:
            attr = ""

        if match['nth']:
            nth = ":nth-of-type(%s)" % match['nth']
        else:
            nth = ""

        node_css = nav + tag + attr + nth
        css += node_css
        position += node.end()
    else:
        css = css.strip()
        return css


def convert_xpath_to_css(xpath):
    if xpath[0] != '"' and xpath[-1] != '"' and xpath.count('"') % 2 == 0:
        xpath = _handle_brackets_in_strings(xpath)

    if xpath.startswith('('):
        xpath = _filter_xpath_grouping(xpath)

    css = _get_raw_css_from_xpath(xpath)

    attribute_defs = re.findall(r'(\[\w+\=\S+\])', css)
    for attr_def in attribute_defs:
        if (attr_def.count('[') == 1 and attr_def.count(']') == 1 and (
                attr_def.count('=') == 1) and attr_def.count('"') == 0 and (
                attr_def.count("'") == 0)) and attr_def.count(' ') == 0:
            # Now safe to manipulate
            q1 = attr_def.find('=') + 1
            q2 = attr_def.find(']')
            new_attr_def = attr_def[:q1] + "'" + attr_def[q1:q2] + "']"
            css = css.replace(attr_def, new_attr_def)

    # Replace the string-brackets with escaped ones
    css = css.replace('_STR_L_bracket_', '\\[')
    css = css.replace('_STR_R_bracket_', '\\]')

    return css
