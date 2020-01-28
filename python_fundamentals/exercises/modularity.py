#!/usr/local/opt/python/bin python3.7
"""Words module.

Fetches words from a url passed as parameter and then print those words.
"""
import sys
from urllib.request import urlopen

def fetch_words (url):
  """Fetch a lists of words from a url.

  Args:
    url: the url to retrieve the content from.

  Returns:
    the list of words.
  """
  with urlopen(url) as story:
    story_words = []

    for line in story:
      line_words = line.decode('utf-8').split()

      for word in line_words:
        story_words.append(word)

  return story_words


def print_items (items):
  """Print items from a list.

  Args:
    items: list of items to print.
  """
  for item in items:
    print(item)


def main (url):
  """Main control function

  Args:
    url: the url to retrieve the content from.
  """
  print_items(fetch_words(url))


if __name__ == '__main__':
  # you should invoke the script with the url as first param:
  #   $ python3.7 modularity.py 'http://sixty-north.com/c/t.txt'
  main(sys.argv[1])

