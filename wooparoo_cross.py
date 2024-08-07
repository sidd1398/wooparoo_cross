#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# 애플리케이션 제목
st.title("가상 크로스")

# 사용자 입력 받기
left = st.text_input("왼쪽 우파루:")
right = st.text_input("오른쪽 우파루:")

# 버튼을 눌렀을 때 실행되는 코드
if st.button("Submit"):
    st.write(f"Hello, {left} and {right}!")


# In[ ]:




