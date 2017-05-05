#!/usr/bin/env python
import sys
import os


def convertHtml(text):
    # A few HTML encodings replacements.
      # &amp;#39; to '
      # &amp;quot; to "
    return text.replace('&amp;#39;', "'").replace('&amp;quot;', '"')


def xml2srt(xmlfile):

    with open(xmlfile) as fin:
        text = fin.read()

    #print text
    end_time_pos = text.find("--> ")+4
    end_time = text[end_time_pos:end_time_pos+12]
    next_next_start_time_pos = text.find("--> ",text.find("--> ",end_time_pos)+4)
    next_next_start_time = text[next_next_start_time_pos-13:next_next_start_time_pos-1]
    print next_next_start_time
    pos = text.find("\n",end_time_pos)+1
    pos2 = text.find("\n",pos)+1
    for i in range(4):
        pos = text.find("\n",pos)+1
    
    print text[:pos2] + text[pos:next_next_start_time_pos-16]
    

    

            
if __name__ == '__main__':
    for pathname in sys.argv[1:]:
        xml2srt(pathname)
