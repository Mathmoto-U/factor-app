import streamlit as st
import random

st.title("展開 1の1")

if "b" not in st.session_state:
    st.session_state.b=random.choice([i for i in range(-15,16) if i != 0])
    st.session_state.X=random.choice(['x','y','z','a'])

if st.button("新しい問題"):
    st.session_state.b=random.choice([i for i in range(-15,16) if i != 0])
    st.session_state.X=random.choice(['x','x','x','x','x','x','y','z','a','b','c','p','q'])
b=st.session_state.b
X=st.session_state.X

def 一次(x):
    if x>0:
        return f"+{x}{X}"
    else:
        return f"{x}{X}"
def 定数(x):
        return f"+{x}"

def 平方(y):
    if y>0:
        return f"({X}+{y})^2"
    else:
        return f"({X}{y})^2"

展開=f"{X}^2{一次(2*b)}{定数(b*b)}"
因数分解=平方(b)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
