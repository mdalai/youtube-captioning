#!/usr/bin/env python
import sys
import os
from datetime import datetime


def new_srt_text(text):
    txt = ""
    i = 0
    while True:
        txt2line, endpos = get_next_target(text)
        if txt2line:
            txt = txt + "{num}\n".format(num=i+1) + txt2line
            i += 1
            if endpos == None:
                break
            text = text[endpos:]

        else:
            break
    return txt

def get_next_target(text):
    end_time_pos = text.find("--> ")+4
    
    if end_time_pos == -1:
        return None,None
    
    if text.find("--> ",end_time_pos) == -1:
        return text[end_time_pos-17:],None   
    
    end_time = text[end_time_pos:end_time_pos+12]

    # check if we need to process
    line2_start_time = text[text.find("--> ",end_time_pos)-13:text.find("--> ",end_time_pos)-1]
    if datetime.strptime(end_time, '%H:%M:%S,%f') <= datetime.strptime(line2_start_time, '%H:%M:%S,%f'):
        return None, None


    line3_start_time_pos = text.find("--> ",text.find("--> ",end_time_pos)+4)
    if line3_start_time_pos == -1:
        line3_start_time_pos = text.find("--> ",end_time_pos)+4
        return text[2:find_nth_index(text,"\n",end_time_pos,2)] + text[line3_start_time_pos+13:], None
    
    line3_start_time = text[line3_start_time_pos-13:line3_start_time_pos-1]

    if datetime.strptime(end_time, '%H:%M:%S,%f') < datetime.strptime(line3_start_time, '%H:%M:%S,%f'):
        end_time = line3_start_time
    
    end_line_pos = text.find("\n",end_time_pos)+1
    end_line_pos1 = find_nth_index(text,"\n",end_line_pos,1)
    end_line_pos2 = find_nth_index(text,"\n",end_line_pos,4)
    end_line_pos3 = find_nth_index(text,"\n",end_line_pos,5)+1
    
    txt2line = text[2:end_time_pos] + end_time +'\n' + text[end_line_pos:end_line_pos1] + text[end_line_pos2:end_line_pos3]

    return txt2line, line3_start_time_pos-15
    

def find_nth_index(text, seach_str, startpos, n):
    pos = text.find(seach_str,startpos) + 1
    for i in range(n-1):
        pos = text.find(seach_str,pos) + 1

    return pos

def merge2srt(srtfile):
    root, _ = os.path.splitext(srtfile)
    if os.path.exists('%s-2.srt' % root):
        print "%s.srt -- has already updated!"%root
        return

    with open(srtfile) as fin:
        text = fin.read()

    
    new_srt = new_srt_text(text)
    #print new_srt

    if not new_srt:
        print "%s.srt -- has No time-overlapping problem!"%root
        return

    with open('%s-2.srt'%root, 'w') as fout:
        fout.write(new_srt)

    

            
if __name__ == '__main__':
    for pathname in sys.argv[1:]:
        merge2srt(pathname)