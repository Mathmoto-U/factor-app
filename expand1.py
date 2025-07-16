import streamlit as st
import random

st.title("展開Level.1")

if "b" not in st.session_state:
    st.session_state.b=random.randint(-5,5)
    st.session_state.c=random.randint(-5,5)

if st.button("新しい問題"):
    st.session_state.b=random.randint(-5,5)
    st.session_state.c=random.randint(-5,5)
b=st.session_state.b
c=st.session_state.c

def 一次(x):
    if x==1:
        return "+x"
    elif x==-1:
        return "-x"
    elif x==0:
        return ""
    elif x>0:
        return f"+{x}x"
    else:
        return f"{x}x"
def 定数(x):
    if x>0:
        return f"+{x}"
    elif x==0:
        return ""
    else:
        return f"{x}"

def 根(y):
    if y==0:
        return f"x"
    elif y>0:
        return f"(x+{y})"
    else:
        return f"(x{y})"

def 根の積(y,z):
    if y==z==0:
        return f"({根(y)})^2"
    if y==z:
        return f"{根(y)}^2"
    else:
        return f"{根(y)}{根(z)}"

展開=f"x^2{一次(b+c)}{定数(b*c)}"
因数分解=根の積(b,c)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
