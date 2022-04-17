# import libraries
from re import X
import streamlit as st
import numpy as np
import pandas as pd

st.title('Multiply Table')

st.header('An app which calcualte multipy table up to 100')

st.subheader('Input Number')

x = st.number_input(label='Enter Number',min_value=1,max_value=100)
st.write('Please Enter value between 1 to 100')


for i in range(10):
    i = i+1
    st.write(x,'x',i,'=',x*i)
    



    

    
        
        

    
           
    
    
        
        
