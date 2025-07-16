import streamlit as st
import random

st.title("展開Level.2")

if "b" not in st.session_state:
    st.session_state.b=random.randint(-12,12)

if st.button("新しい問題"):
    st.session_state.b=random.randint(-12,12)
b=st.session_state.b

def 定数(x):
    if x==0:
        return ""
    else:
        return x

def 根の積(y):
    if y==0:
        return "x^2"
    elif y>0:
        return f"(x+{y})(x-{y})"
    else:
        return f"(x{y})(x+{-y})"

展開=f"x^2{定数(-b*b)}"
因数分解=根の積(b)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
