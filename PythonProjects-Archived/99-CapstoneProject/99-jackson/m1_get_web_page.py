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

import requests  # You will need to install this library

def main():
    url = "http://web.mta.info/developers/turnstile.html"  # An example site
    response = requests.get(url)
    html = response.text

    print(html)


main()

# -----------------------------------------------------------------------------
# Brief explanation of the above:
#    Line 1 of   main   sets the URL whose HTML you want.
#    Line 2 connects to the URL and gets the response.
#    Line 3 accesses the TEXT (html) of the response.
#
# The above code uses (imports) the  requests  library that makes it easier
# to do URL requests (e.g. get the HTML of a web page).
# It is built on top of the Python library  urllib  that ships with Python.
#
# You will need to install this library.  In PyCharm:
#  File ~ Settings
#  Project Interpreter  [may be underneath Project 99-jackson]
#  Click on the   +   sign
#  Type   requests   [or whatever library you want to install]
#  Select   Install Package
# -----------------------------------------------------------------------------
