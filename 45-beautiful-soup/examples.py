from bs4 import BeautifulSoup
#import lxml # if "html.parser" doesn't work

with open("45-beautiful-soup/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
# to have the text in the a tag
# print(tag.getText())
# to have the href in the a tag
# print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

companu_url = soup.select_one("p a")
# print(companu_url)

headings = soup.select(".heading")
print(headings)
