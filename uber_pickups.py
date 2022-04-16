# importing libraries
import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber Pick ups App')

DATE_COLUMUN = 'date/time'
DATA_URL =('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# creating function for data uploading...
@st.cache
def upload_data(nrows):
    data = pd.read_csv(DATA_URL,  nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMUN] = pd.to_datetime(data[DATE_COLUMUN])
    return data

# informing user data is loading..
data_load_state = st.text('loading data...')
# converting nrows to 10000 rows
data = upload_data(10000)
# notify that data is loaded
data_load_state.text('Done! (using st.cache)')

# Examin the raw data
# st.subheader('Raw Data')
st.subheader('Number of pickups by hour')
# st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)
hist_values = np.histogram(data[DATE_COLUMUN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')

# st.map(data)

hour_to_filter = st.slider('hour',0,23,17)
filtered_data = data[data[DATE_COLUMUN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')