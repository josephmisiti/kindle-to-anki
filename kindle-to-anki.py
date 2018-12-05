import argparse
import os

"""
Citizen-Protectors: The Everyday Politics of Guns in an Age of Decline (Carlson, Jennifer)
- Your Highlight on page 51 | Location 1027-1028 | Added on Sunday, April 15, 2018 1:39:44 PM

Jonathan Simon explains how crime acts as a social lens in his book Governing through Crime. He argues
==========
"""

DEFAULT_KINDLE_FILE_NAME = 'My Clippings.txt'
DEFAULT_KINDLE_HIGHLIGHT_BREAK = '=========='

def display_parsed_results(highlights):
    for hl in highlights:
        print '|'.join(hl)

def parse_kindle_file(args):
    highlights = []
    kindle_highlight = []
    for l in open(args['input']).readlines():
        l = l.strip('\r\n')
        if len(l) == 0: continue
        if l == DEFAULT_KINDLE_HIGHLIGHT_BREAK:
            highlights.append(kindle_highlight)
            kindle_highlight = []
        else:
            kindle_highlight.append(l)

    display_parsed_results(highlights)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", default=DEFAULT_KINDLE_FILE_NAME, type=str,
                  help="My Clippings.txt or other kindle file")
    parser.add_argument("--title", dest="title", default=None, type=str,
                  help="Title you are searching")

    args = vars(parser.parse_args())
    parse_kindle_file(args)
