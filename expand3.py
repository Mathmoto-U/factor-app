import streamlit as st
import random

st.title("展開Level.3")

if "b" not in st.session_state:
    st.session_state.b=random.choice([i for i in range(-15, 16) if i != 0])
    st.session_state.X=random.choice(['x','y','z','a'])

if st.button("新しい問題"):
    st.session_state.b=random.choice([i for i in range(-15, 16) if i != 0])
    st.session_state.X=random.choice(['x','y','z','a','b','c','p','q'])
b=st.session_state.b
X=st.session_state.X

def 定数(x):
        return f"{x}"

def 根の積(y):
    if y>0:
        return f"({X}+{y})({X}-{y})"
    else:
        return f"({X}{y})({X}+{-y})"

展開=f"{X}^2{定数(-b*b)}"
因数分解=根の積(b)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
