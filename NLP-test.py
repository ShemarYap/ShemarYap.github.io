
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
from textblob import  TextBlob

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

# ------------------------------------------- Assignment # 3 ---------------------------------------

#loc[] choose rows by label , iloc[] choose columns by label

m_df.dtypes
# The type object will cause issues and needs to be converted

m_df.applymap(str)
# converts all of the entries to a string

m_cf = m_df.applymap(str)
f_cf = f_df.applymap(str)

m_cf.dtypes

m_text = TextBlob(str(m_cf.iloc[0,]))
m_text.sentiment.polarity
# The test data shows that the sentiment of this sentence is negative 
# This is how we will sort by sentiment
sentrank_m = []
sentrank_f = []

# makes  an empty list

for i in range(0,len(m_cf)):
    
   
    temp_mtxt = TextBlob(str(m_cf.iloc[i,]))
    m_score = temp_mtxt.sentiment.polarity
    sentrank_m.append(m_score)
    
# for females
    
 for i in range(0,len(f_cf)):
    
    temp_ftxt = TextBlob(str(f_cf.iloc[i,]))
    f_score = temp_ftxt.sentiment.polarity
    sentrank_f.append(f_score)   
    
