import streamlit as st 
import time
import numpy as np
import pandas as pd

st.title("Ravens")

def load_data():
    data = pd.read_csv('headwinds_twitter_friends.csv')
    return data

friends_df = load_data()
total_friends = len(friends_df)

if (st.checkbox("view data")):
    st.subheader("Headwinds Friends List {}".format(total_friends) )
    st.write(friends_df)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
