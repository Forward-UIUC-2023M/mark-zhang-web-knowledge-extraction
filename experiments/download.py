from utils import fetch_html

URL = "http://catalog.illinois.edu/courses-of-instruction/cs/"
FILE = "cs_courses.html"

html = fetch_html(URL)
with open(f"data/html/{FILE}", "w+", encoding="utf-8") as f:
    f.write(html)