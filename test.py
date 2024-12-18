import streamlit as st 
import pandas as pd 
import numpy as np 

data = pd.read_csv('DA-Technical Case.csv')
st.dataframe(data)
