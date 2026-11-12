
def remove_html_markup(s):
    tag = False
    out = ""
    texto = s.replace('"','')
    for c in texto:
        if c == "<":
            tag = True
        elif c == ">":
            tag = False
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