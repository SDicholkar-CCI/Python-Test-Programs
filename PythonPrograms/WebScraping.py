import requests
from bs4 import BeautifulSoup, NavigableString


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, "", str(text))


def recursiveChildren(x):
    if "childGenerator" in dir(x):
        for child in x.childGenerator():
            name = getattr(child, "name", None)
            if name is not None:
                count = child.findChildren()
                """print('next', child.next)"""
                if type(child.next) is NavigableString and child.next != '\n' and name != 'script':
                    print(child.get_text())
                recursiveChildren(child)
    else:
        if not x.isspace():  # Just to avoid printing "\n" parsed from document.
            print("[Terminal Node]", x)


page = requests.get('https://www.moralstories.org/the-thirsty-crow/')
soup = BeautifulSoup(page.content, 'lxml')
"""print(soup.find(class_='posts').get_text())
print(soup.find('body').get_text())"""
bodyData = soup.find('body')
for child in bodyData.childGenerator():
    recursiveChildren(child)
