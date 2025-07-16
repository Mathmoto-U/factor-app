import streamlit as st
import random

st.title("因数分解 Level.1")

if "b" not in st.session_state:
    st.session_state.b = random.randint(-9, 9)
    st.session_state.c = random.randint(-9, 9)

if st.button("新しい問題"):
    st.session_state.b = random.randint(-9, 9)
    st.session_state.c = random.randint(-9, 9)

b = st.session_state.b
c = st.session_state.c

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

st.markdown("次の式を因数分解せよ：")
st.latex(式)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(答)
