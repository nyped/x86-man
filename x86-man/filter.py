#!/usr/bin/env python
"""Clean up the AST so we can feed md2man."""

from pandocfilters import toJSONFilter, Header, Link, stringify, Str, Span, Subscript


# pylint: disable=unused-argument inconsistent-return-statements
def to_man(key, value, form, meta):
    """Fix the AST in order to get a man."""
    if key == "Div":
        return []

    if key == "Link":
        return Str(stringify(Link(*value)))

    if key == "Span":
        return Str(stringify(Span(*value)))

    if key == "Subscript":
        return Str(stringify(Subscript(value)))

    if key == "Header" and value[2][-1]["t"] == "Link":
        return Header(value[0], ["", [], []], value[2][:-2])


if __name__ == "__main__":
    toJSONFilter(to_man)

# vim: set ts=4 sts=4 sw=4 et :
