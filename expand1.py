import streamlit as st
import random

st.title("展開Level.1")

if "b" not in st.session_state:
    while True:
        b, c = random.sample([i for i in range(-9, 10) if i != 0], 2)
        if abs(b) != abs(c):
            st.session_state.b = b
            st.session_state.c = c
            break
    st.write(f"b = {st.session_state.b}, c = {st.session_state.c}")
    st.session_state.X=random.choice(['x','x','x','x','y','y','a','a','b','m','n','x','x','x','x','y','y','a','a','b','m','n','♡'])

if st.button("新しい問題"):
    while True:
        b, c = random.sample([i for i in range(-9, 9) if i != 0], 2)
        if abs(b) != abs(c):
            st.session_state.b = b
            st.session_state.c = c
            break
    st.session_state.X=random.choice(['x','x','x','x','y','y','a','a','b','m','n','x','x','x','x','y','y','a','a','b','m','n','♡'])
b=st.session_state.b
c=st.session_state.c
X=st.session_state.X

def 一次(x):
    if x==1:
        return f"+{X}"
    elif x==-1:
        return f"-{X}"
    elif x>0:
        return f"+{x}{X}"
    else:
        return f"{x}{X}"
def 定数(x):
    if x>0:
        return f"+{x}"
    else:
        return f"{x}"

def 根(y):
    if y>0:
        return f"({X}+{y})"
    else:
        return f"({X}{y})"

def 根の積(y,z):
        return f"{根(y)}{根(z)}"

展開=f"{X}^2{一次(b+c)}{定数(b*c)}"
因数分解=根の積(b,c)

st.markdown("次の式を展開せよ：")
st.latex(因数分解)

if st.button("答えを見る"):
    st.markdown("答え：")
    st.latex(展開)
