# import libraries

from matplotlib import use
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_profiling import ProfileReport

# setting page layout
st.set_page_config(
    page_title="Streamlit Practice",
    layout='wide',
    # intitial_sidebar_state='expanded', 
    
    


)
df = sns.load_dataset('titanic')
st.title('**Streamlit Practice**')

# assigning containers
header = st.container()
features = st.container()
dataset = st.container()

with header:
    st.header('Welcome to Streamlit')
    
with features:
    st.write('pata nahin kia featurs hain')
    
    
    

with dataset:
    mydataset = df
    st.write(mydataset.head(4))
    st.markdown('## **EDA**' )
    mydataset = mydataset.dropna()
    st.write('The shape of data is ', mydataset.shape)
    st.write('Printing data descripton'
             )
    st.write(mydataset.describe())
    st.write('Finding null values', mydataset.isnull().sum())
    
st.subheader('Visualizing') 
st.write(ProfileReport)