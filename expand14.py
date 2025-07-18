import streamlit as st
import random

st.title("展開 1の4")

if "b" not in st.session_state:
    st.session_state.b=random.choice([i for i in range(-15, 16) if i != 0])
    st.session_state.X=random.choice('x','x','x','x','x','x','y','y','a','a','b','b','m','n')

if st.button("新しい問題"):
    st.session_state.b=random.choice([i for i in range(-15, 16) if i != 0])
    st.session_state.X=random.choice('x','x','x','x','x','x','y','y','a','a','b','b','m','n')
b=st.session_state.b
X=st.session_state.X

def 符号付(x):
    return f"+{x}" if x > 0 else str(x)

def 一次(x):
    if x == 1:
        return "+x"
    elif x == -1:
        return "-x"
    elif x == 0:
        return ""
    else:
        return f"{符号付(x)}x"

def 定数(x):
    return "" if x == 0 else 符号付(x)

def 根(x):
    return "x" if x == 0 else f"(x{符号付(x)})"

def 根の積(x, y):
    return f"{根(x)}^2" if x == y else f"{根(x)}{根(y)}"

式 = f"x^2{一次(b + c)}{定数(b * c)}"
答 = 根の積(b, c)

st.markdown("次の式を展開せよ：")
st.latex(答)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(式)
