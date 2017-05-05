#!/usr/bin/env python
import sys
import os
#import datetime as dt
import glob
from bs4 import BeautifulSoup
from datetime import timedelta

def strfdelta(tdelta, fmt="{hours:02}:{minutes:02}:{seconds:02},{microseconds:03}"):
    d = {}
    d["microseconds"] = tdelta.microseconds%1000
    seconds = tdelta.microseconds//1000
    d["hours"],rem = divmod(seconds,3600)
    d["minutes"], d["seconds"] = divmod(rem, 60) 
    
    return fmt.format(**d)


def convertHtml(text):
    # A few HTML encodings replacements.
      # &amp;#39; to '
      # &amp;quot; to "
    return text.replace('&amp;#39;', "'").replace('&amp;quot;', '"')


def xml2srt(xmlfile):
    root, _ = os.path.splitext(pathname)
    if os.path.exists('%s.srt' % root):
        print "SRT file already exist"
        return

    with open(xmlfile) as fin:
        text = fin.read()
        text = text.replace('-1:', '00:') # broken xml
        #print text
        soup = BeautifulSoup(text,"html.parser")

    #print soup

    with open('%s.srt'%root, 'w') as fout:
        i = 0
        for p in soup.findAll('p'):
            #print p
            if p.has_attr('d'):
                #print p['t'],p['d']
                begin = float(p['t'])
                dur = float(p['d'])

                #print p.text
                print p.string

                if p.string:
                    fout.write("""{num}\n{start} --> {end}\n{content}\n\n""".format(num=i+1,
                            start=strfdelta(timedelta(microseconds=begin)),
                            end=strfdelta(timedelta(microseconds=begin+dur)),
                            content=convertHtml(p.text.encode("u8"))))
                    i += 1

    print "Done Converting to {}.srt".format(root)       

            
if __name__ == '__main__':
    for pathname in sys.argv[1:]:
        xml2srt(pathname)
