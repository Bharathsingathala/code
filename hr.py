import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import download_plotlyjs,init_notebook_mode
sv')
test = pd.read_csv('aug_test.csv')
train = pd.read_csv('aug_train.csv')
train.info()
sim = train.duplicated()
sim.sum()
missing_value = 100 * train.isnull().sum()/len(train)
missing_value = missing_value.reset_index()
missing_value.columns = ['variables','missing values in percentage']

#import plotly.io as pio
#pio.templates.default = "none"


# heatmap
fig = px.imshow(train.isnull().T,template='ggplot2')
fig.update_layout(title='Missing values in data set')
fig.show()

# barplot
fig = px.bar(missing_value, y='missing values in percentage',x='variables',title='Missing values % in each column',
             template='ggplot2');
fig.show()
plot_city = train['city'].value_counts()[0:50].reset_index()
plot_city.columns = ['City','Count']
px.bar(plot_city,x='City',y='Count',template='gridon',title='City',color='Count')
plot_cdi =train['city_development_index'].value_counts().reset_index()[0:50]
plot_cdi.columns = ['cdi','Count']
plot_cdi['cdi'] = plot_cdi['cdi'].astype('str')
px.bar(plot_cdi,y="Count", x="cdi",color='Count',title='City development index')
plot_gender = train['enrolled_university'].value_counts().reset_index()
plot_gender.columns = ['enrolled_university','count']

px.pie(plot_gender,values='count',names='enrolled_university',template='simple_white',title='enrolled_university')
plot_gender = train['education_level'].value_counts().reset_index()
plot_gender.columns = ['education_level','count']

px.pie(plot_gender,values='count',names='education_level',template='ggplot2',title='education_level')
plot_gender = train['major_discipline'].value_counts().reset_index()
plot_gender.columns = ['major_discipline','count']

px.pie(plot_gender,values='count',names='major_discipline',template='plotly',title='Major discipline')
plot_gender = train['company_size'].value_counts().reset_index()
plot_gender.columns = ['company_size','count']

px.pie(plot_gender,values='count',names='company_size',template='plotly_white',title='company_size is determined by no. of people employees')