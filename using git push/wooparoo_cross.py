#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# 애플리케이션 제목
st.title("My Streamlit App")

# 사용자 입력 받기
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120)

# 버튼을 눌렀을 때 실행되는 코드
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")


# In[ ]:




