
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Noida, Uttar Pradesh, India**, or **India** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Noida, Uttar Pradesh, India** to Ann Arbor, USA. In that case at least one source file must be about **Noida, Uttar Pradesh, India**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Noida, Uttar Pradesh, India** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[4]:

import pandas as pd

uttar_pradesh_data = pd.read_excel('DDWC-090009.xls')

india_data = pd.read_excel('DDWC-000009.xls')

india_data = india_data.where(india_data['Area Name'] == 'INDIA').dropna()
india_data = india_data.where(india_data['Age-group'] == 'Total').dropna()
india_data = india_data.where(india_data['Total/ Rural/ Urban'] == 'Total').dropna()

uttar_pradesh_data = uttar_pradesh_data.where(uttar_pradesh_data['Area Name'] == 'State - UTTAR PRADESH  09').dropna()
uttar_pradesh_data = uttar_pradesh_data.where(uttar_pradesh_data['Age-group'] == 'Total').dropna()
uttar_pradesh_data = uttar_pradesh_data.where(uttar_pradesh_data['Total/ Rural/ Urban'] == 'Total').dropna()


# In[50]:

import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')



up = uttar_pradesh_data
india = india_data

up['Literacy ratio'] = up['Literate - Persons']/up['Total population - Persons']

india['Literacy ratio'] = india['Literate - Persons']/india['Total population - Persons']

cols = uttar_pradesh_data.columns

keep_cols = ['Area Name','Religion','Literacy ratio']

india = india[keep_cols]
up = up[keep_cols]

up['Indian rates'] = india['Literacy ratio']



# In[90]:

plt.style.use('fivethirtyeight')

up[['Literacy ratio','Indian rates']].plot(up['Religion'],kind = 'bar',
                            width =0.4, figsize=(12,10),alpha=0.8,
                            legend=True, fontsize=12)

ax = plt.gca()

ax.set_ylabel('Literacy ratio')
ax.set_title("Literacy rates of religious communities in Uttar Pradesh compared to the national average ",size=14)

x = ax.xaxis
index = 0
for item in x.get_ticklabels():
    item.set_rotation(45)

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0] = 'All'
labels[7] = 'Others'

ax.set_xticklabels(labels)


legend_labels = ['','']
    
legend_labels[0] = 'Uttar Pradesh (State) Literacy rates'
legend_labels[1] = 'India (Country) Literacy rates'

ax.legend(legend_labels,loc='best')

plt.subplots_adjust(bottom=0.1)






# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



