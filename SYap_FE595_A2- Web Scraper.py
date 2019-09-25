# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:13:23 2019

@author: StevensUser
"""

# Install executed as shown below:
"""
---- from command line ----

python -m pip install requests

"""
import numpy as np
import requests as rq
import pandas as pd
import re

r_session = rq.session()

raw_html = r_session.get('http://theyfightcrime.org')
# Out[9]: <Response [200]>
# This denotes a sucessful request

# headers give a brief description of the requested page
raw_html.headers

# isolate the body of the web page for string extraction
main = raw_html.text[740:1270]
result = print(main)

#body = raw_html.html.find('<FONT FACE="Verdana,Arial,Helvetica,sans-serif" SIZE="-1"><P>', first = True)
# ------------------------------------------------------------------------------------------------------
# for loop implementation for autmomation (extract 50 times)

i = 0
r_list = []
m_list, f_list = [] , []

for i in range(0, 50):
   r_post = rq.post('http://theyfightcrime.org')
   
   raw_main = r_post.text[740:1250]
   
   w_main = re.search("He's(.*)\w+\.", raw_main)
   wf_main = w_main.group(0)
   grab = re.split("\w+\.", wf_main)
   
   m_index = m_list.extend([grab[0]])
   f_index = f_list.extend([grab[1]])

  # r_index = r_list.extend(grab)

# -----------------------------------------------------------------------------------------------------
# Final result is store in the  dataframes below:
m_df = pd.DataFrame(m_list)
f_df = pd.DataFrame(f_list)

# the female dataframe is experiencing issues with the whitespaces
# I will be dropping themusing drop duplicates, since they are all whitespaces

f_df.drop_duplicates(inplace = True)
np.savetxt(r'C:\Users\StevensUSer\Desktop\FE-595 FinTech\M_CrimeFighter.txt', m_df, fmt = '%s')
np.savetxt(r'C:\Users\StevensUSer\Desktop\FE-595 FinTech\F_CrimeFighter.txt', f_df, fmt = '%s')

"""
r_df = pd.DataFrame(r_list)
r_df.drop_duplicates(inplace = True)
   
   
r_post = rq.post('http://theyfightcrime.org')
print(r_post.text)

# Regular expression matching for separating the main text
mainf = re.search("He's(.*) [A-Za-z]+\.", main)
print(mainf.group(0))

# alernative testing for above:
# male2 = re.search("He's(.*) \w+\.", main)
# print(male2.group(0))

# Since the first regex function matched the string after the last word with a period
# We will use this feature to split the characters into classes male and female for the dictionary
x = mainf.group(0)

# splits the data adn stores into the variable
alt = re.split("\w+\.", x)
alt
female = alt[1]
male = alt[0]
male

str(male.group(0))
female = re.search("She's(.*).", main)
print(female.group(1))
"""
