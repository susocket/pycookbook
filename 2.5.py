#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
    Python cookbook chapter 2.5
    Date: 2015-12-05
'''
import re
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    
def replace_text():
    text = 'yeah, but no, yeah, but no, yeah, but no'
    r_text = text.replace('yeah', 'OK')
    print()
    print("=" * 50)
    print("orignal:",text)
    print("result:", r_text)
    
    text2 = 'Today is 12/05/2015. PyCon starts 3/13/2013'
    r_text2 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
    print()
    print("=" * 50)
    print("orignal:", text2)
    print("result:", r_text2)
    
    r_textx = re.sub(r'\d+/\d+/\d+', r'yyyy-mm-dd', text2)
    print()
    print("=" * 50)
    print("orignal:", text2)
    print("result:", r_textx)
    
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    r_text3 = datepat.sub(r'\3-\1-\2', text2)
    print()
    print("=" * 50)
    print("orignal:", text2)
    print("result:", r_text3)
    
    r_text4 = datepat.sub(change_date, text2)
    print()
    print("=" * 50)
    print("orignal:", text2)
    print("result:", r_text4)
    
    r_text5, n = datepat.subn(change_date, text2)
    print()
    print("=" * 50)
    print("orignal:", text2)
    print("result:", r_text5)
    print("replace times:%d" % n)
if __name__ == '__main__':
    replace_text()