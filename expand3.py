import streamlit as st
import random

st.title("展開 Level.2")

if "a" not in st.session_state:
    st.session_state.a=random.randint(1, 9)
    st.session_state.b=random.randint(-9, 9)
    st.session_state.c=random.randint(-9, 9)

if st.button("新しい問題"):
    st.session_state.a=random.randint(2, 9)
    st.session_state.b=random.randint(-9, 9)
    st.session_state.c=random.randint(-9, 9)

a=st.session_state.a
b=st.session_state.b
c=st.session_state.c

def 符号付(x):
    if x>0:
        return f"+{x}"
    else:
        return x

def 一次(x):
    if x==1:
        return "+x"
    elif x==-1:
        return "-x"
    elif x==0:
        return ""
    else:
        return f"{符号付(x)}x"

def 定数(x):
    if x == 0:
        return ""
    else:
        return 符号付(x)

def 根(x,y):
    if y==0:
        return f"{x}x"
    else:
        return f"({x}x{符号付(y)})"

def 根の積(x,y,z):
    if y==z:
        return f"{根(x,y)}^2"
    else:
        f"{根(x,y)}{根(x,z)}"

展開=f"{a*a}x^2{一次(a*b+a*c)}{定数(a*b*c)}"
因数分解=根の積(a,b,c)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
