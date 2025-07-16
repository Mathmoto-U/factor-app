import streamlit as st
import random

st.title("展開 Level.5")

if "b" not in st.session_state:
    st.session_state.b=random.randint(-9,9)
    st.session_state.c=random.randint(-9,9)

if st.button("新しい問題"):
    st.session_state.b=random.randint(-9,9)
    st.session_state.c=random.randint(-9,9)

b=st.session_state.b
c=st.session_state.c

def 一次(x):
    if x==1:
        return "+xy"
    elif x==-1:
        return "-xy"
    elif x==0:
        return ""
    elif x>0:
        return f"+{x}xy"
    else:
        return f"{x}xy"

def 定数(x):
    if x==1:
        return "+y^2"
    elif x==-1:
        return "-y^2"
    elif x>0:
        return f"+{x}y^2"
    elif x==0:
        return ""
    else:
        return f"{x}y^2"

def 根(y):
    if y==1:
        return "(x+y)"
    elif y==-1:
        return "(x-y)"
    elif y>0:
        return f"(x+{y}y)"
    elif y==0:
        return "x"
    else:
        return f"(x{y}y)"

def 根の積(y,z):
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
