#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
    Python cookbook chapter 1.19
    Date: 2015-12-05
'''

import os

nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
print('nums={}, s={}'.format(nums,s))

# Determie if any .py files exist in a directory
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
    
# Output a tuple as CSV
t = ('ACME', 50, 12.3)
print(','.join(str(x) for x in t))

# Date reduction accross fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL', 'shares':20}
]
min_shares = min(p['shares'] for p in portfolio)
print('min_shares={}'.format(min_shares))

