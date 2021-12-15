import streamlit as st
import pandas as pd
import numpy as np
y=100
x=200
z=50
st.title("器械")
if st.checkbox("紫鉄砂"):
    number=st.selectbox("kasu",list(range(1,301)))
    st.write(f"赤銅は{y*number}",f"錬鉄は{x*number}",f"ニスは{y*number}",
    f"石材は{y*number}")
if st.checkbox("紫オスマン"):
    number=st.selectbox("kasu",list(range(1,301)))
    st.write(f"赤銅は{x*number}",f"錬鉄は{x*number}",f"ニスは{y*number}",
    f"石材は{y*number}")
if st.checkbox("青オス"):
    number=st.selectbox("kasu",list(range(1,301)))
    st.write(f"赤銅は{y*number}",f"錬鉄は{y*number}",f"ニスは{z*number}",
    f"石材は{z*number}")
if st.checkbox("青鉄砂"):
    number=st.selectbox("kasu",list(range(1,301)))
    st.write(f"赤銅は{z*number}",f"錬鉄は{y*number}",f"ニスは{z*number}",
    f"石材は{z*number}")