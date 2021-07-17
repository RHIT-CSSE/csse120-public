"""
Scraping the Web, Step 1: Get the HTML from a web page.
Summary:
  1. install the   requests   library
  2. Then the code to get the HTML from a web page is just:

        import requests

        url = "http://whatever_URL_you_want
        response = requests.get(url)
        html = response.text

See:
 towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

for a good, simple tutorial on Scraping the Web.
The examples herein are taken from that site.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import requests  # You will need to install: requests
import bs4
from bs4 import BeautifulSoup  # You will need to install: beautifulsoup4

def main():
    # Get the HTML of a page:
    url = "http://web.mta.info/developers/turnstile.html"  # An example site
    response = requests.get(url)
    html = response.text

    print(html)  # Just so that you can see what you are working with.

    # Process the HTML.  Lots of ways to do so.  Here are some examples.

    # Find a LINE of the HTML that contains a specific string:
    lines = html.split("\n")
    index_of_line = -1
    for k in range(len(lines)):
        line = lines[k]
        if "October 08, 2011" in line:
            index_of_line = k
            break
    if index_of_line < 0:
        print("No line contained the string")
    else:
        print("This line contained the string:")
        print(lines[index_of_line])

    # Find a TAG with an ATTRIBUTE of the HTML
    # that contains a specific string, as follows:

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(html, "html.parser")

    # Loop through the  <a> tags, examining the TEXT of each:
    index_of_atag = -1
    a_tags = soup.findAll("a")
    for k in range(len(a_tags)):
        a_tag = a_tags[k]
        if "October 08, 2011" in a_tag.text:
            index_of_atag = k
            break
    if index_of_atag < 0:
        print("No a-tag had TEXT that contained the string")
    else:
        print("This a-tag contained the string:")
        a_tag = a_tags[index_of_atag]
        print(a_tag)
        print("Its HREF is:")
        print(a_tag["href"])


main()