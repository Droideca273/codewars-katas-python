
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == "<" and not quote:
            tag = True
        elif c == ">" and not quote:
            tag = False
        elif c == '"':
            quote = not quote
        elif not tag:
            out = out + c
        else:
            pass
    return out

'''
if __name__ == "__main__":
    assert remove_html_markup("<b>foo</b>") == "foo"
    assert remove_html_markup('<b>"foo"</b>') == "foo"
    assert remove_html_markup('"<b>foo</b>"') == "foo"
    assert remove_html_markup('<"b">foo</"b">') == "foo"
'''
print(remove_html_markup("<b>foo</b>"))
print(remove_html_markup('<b>"foo"</b>'))
print(remove_html_markup('"<b>foo</b>"'))
print(remove_html_markup('<"b">foo</"b">'))