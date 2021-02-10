from bs4 import BeautifulSoup


def parse_li(html, level):
    soup = BeautifulSoup(html, features="html.parser")
    li = soup.findChildren(recursive=False)[0]
    li['class'] = "nav-item nav-level-" + str(level)
    for child in li.findChildren(recursive=False):
        if child.name == "a":
            child['class'] = "nav-link"
            new_tag = soup.new_tag('span')
            new_tag['class'] = "nav-text"
            new_tag.string = child.string
            child.string = ""
            child.append(new_tag)
        elif child.name == "ul":
            child.replace_with(parse_ol(child.__str__(), level+1))
    return soup


def parse_ol(html, level):
    soup = BeautifulSoup(html, features="html.parser")
    ol = soup.findChildren(recursive=False)[0]
    ol.name = 'ol'
    if level == 1:
        ol['class'] = "nav"
    else:
        ol['class'] = 'nav-child'

    for li in ol.findChildren(recursive=False):
        li.replace_with(parse_li(li.__str__(), level))
    return soup


def convert_toc(toc):
    return parse_ol(toc, 1).prettify()


# print(convert_toc('''<ul>
#   <li><a href="#fdas">fdas</a>
#   <ul>
#     <li><a href="#fjdaskjfldka">fjdaskjfldka</a></li>
#   </ul>
#   </li>
#     <li><a href="#fdas">fdas</a>
#   </li>
# </ul>'''))
