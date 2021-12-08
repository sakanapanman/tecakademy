import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time
st.title("Streamlit 入門")

st.write("Interactiv Widgets")

less=st.empty()
bar=st.progress(0)

for i in range(100):
    less.text(f"Less {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)







left,right=st.columns(2)
button=left.button("右")
if button:
    right.write("右やで")

ex1=st.expander("問い合わせ1")
ex1.write("1の回答")
ex2=st.expander("問い合わせ2")
ex2.write("2の回答")


# st.write("Display Image")
#if st.checkbox("Show Image"):
   #img=Image.open("ダウンロード.jfif")
   #st.image(img,caption="pokemon",use_column_width=True)