import streamlit as st
import random
import math

#数式
def あ(x):
    if x==1:
        return f"+x"
    elif x==-1:
        return f"-x"
    elif x>0:
        return f"+{x}x"
    elif x==0:
        return ""
    else:
        return f"{x}x"
def い(x):
    if x==1:
        return f"+xy"
    elif x==-1:
        return f"-xy"
    elif x>0:
        return f"+{x}xy"
    elif x==0:
        return ""
    else:
        return f"{x}xy"
def う(x):
    if x==1:
        return "x^2"
    else:
        return f"{x}x^2"
def え(x):
    if x==1:
        return "+y^2"
    elif x==-1:
        return "-y^2"
    elif x==0:
        return ""
    elif x>0:
        return f"+{x}y^2"
    else:
        return f"{x}y^2"
def 定数(x):
    if x>0:
        return f"+{x}"
    elif x==0:
        return ""
    else:
        return f"{x}"

def 根(x,y,z):
    if x==y==1:
        return f"(x+y{定数(z)})"
    elif x==-y==1:
        return f"(x-y{定数(z)})"
    elif x==1 and y>0:
        return f"(x+{y}y{定数(z)})"
    elif x==1 and y==0:
        return f"(x{定数(z)})"
    elif x==1 and y<0:
        return f"(x{y}y{定数(z)})"
    elif y==-1:
        return f"({x}x-y{定数(z)})"
    elif y==1:
        return f"({x}x+y{定数(z)})"
    elif y>0:
        return f"({x}x+{y}y{定数(z)})"
    elif y<0:
        return f"({x}x{y}y{定数(z)})"
    elif y==0:
        return f"({x}x{定数(z)})"
    else:
        return f"({x}x+{y}y{定数(z)})"

def 因数分解(x,y,z,a,b):
    if y==a and z==b:
        return f"{根(x,y,z)}^2"
    else:
        return f"{根(x,y,z)}{根(x,a,b)}"

def 展開(x,y,z,a,b):
        return f"{う(x*x)}{い(x*y+x*a)}{あ(x*z+x*b)}{え(y*a)}{定数(z*b)}"

#アプリ切り替え
app0=st.selectbox("展開か因数分解かを選択する：",["展開","因数分解"])
if app0=="展開":
    app=st.selectbox("展開のタイプを選択する：",["展開１","展開２","展開３","展開４","展開５","展開６"])
else:
    app=st.selectbox("因数分解のタイプを選択する：",["因数分解１","因数分解２","因数分解３","因数分解４","因数分解５"])
st.title(app)

if app=="展開１":
    if "y1" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y1,a1=0,0
                z1,b1=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z1)!=abs(b1):
                    break
            else:
                z1,b1=0,0
                y1,a1=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(y1)!=abs(a1):
                    break
        st.session_state.y1=y1
        st.session_state.z1=z1
        st.session_state.a1=a1
        st.session_state.b1=b1
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y1,a1=0,0
                z1,b1=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z1)!=abs(b1):
                    break
            else:
                z1,b1=0,0
                y1,a1=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(y1)!=abs(a1):
                    break
        st.session_state.y1=y1
        st.session_state.z1=z1
        st.session_state.a1=a1
        st.session_state.b1=b1
    y=st.session_state.y1
    z=st.session_state.z1
    a=st.session_state.a1
    b=st.session_state.b1
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(1,y,z,a,b))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(1,y,z,a,b))

elif app=="展開２":
    if "y2" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y2=0
                z2=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z2=0
                y2=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y2=y2
        st.session_state.z2=z2
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y2=0
                z2=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z2=0
                y2=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y2=y2
        st.session_state.z2=z2
    y=st.session_state.y2
    z=st.session_state.z2
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(1,y,z,y,z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(1,y,z,y,z))

elif app=="展開３":
    if "y3" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y3=0
                z3=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z3=0
                y3=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y3=y3
        st.session_state.z3=z3
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y3=0
                z3=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z3=0
                y3=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y3=y3
        st.session_state.z3=z3
    y=st.session_state.y3
    z=st.session_state.z3
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(1,y,z,-y,-z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(1,y,z,-y,-z))
        
elif app=="展開４":
    if "x4" not in st.session_state:
        st.session_state.x4=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y4,a4=0,0
                z4,b4=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z4)!=abs(b4) and math.gcd(st.session_state.x4,z4)==math.gcd(st.session_state.x4,b4)==1:
                    break
            else:
                z4,b4=0,0
                y4,a4=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z4)!=abs(b4) and math.gcd(st.session_state.x4,y4)==math.gcd(st.session_state.x4,a4)==1:
                    break
        st.session_state.y4=y4
        st.session_state.z4=z4
        st.session_state.a4=a4
        st.session_state.b4=b4
    if st.button("新しい問題"):
        st.session_state.x4=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y4,a4=0,0
                z4,b4=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z4)!=abs(b4) and math.gcd(st.session_state.x4,z4)==math.gcd(st.session_state.x4,b4)==1:
                    break
            else:
                z4,b4=0,0
                y4,a4=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(y4)!=abs(y4) and math.gcd(st.session_state.x4,y4)==math.gcd(st.session_state.x4,a4)==1:
                    break
        st.session_state.y4=y4
        st.session_state.z4=z4
        st.session_state.a4=a4
        st.session_state.b4=b4
    x=st.session_state.x4
    y=st.session_state.y4
    z=st.session_state.z4
    a=st.session_state.a4
    b=st.session_state.b4
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(x,y,z,a,b))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(x,y,z,a,b))

elif app=="展開５":
    if "x5" not in st.session_state:
        st.session_state.x5=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y5=0
                z5=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x5,z5)==1:
                    break
            else:
                z5=0
                y5=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x5,y5)==1:
                    break
        st.session_state.y5=y5
        st.session_state.z5=z5
    if st.button("新しい問題"):
        st.session_state.x5=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y5=0
                z5=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x5,z5)==1:
                    break
            else:
                z5=0
                y5=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x5,y5)==1:
                    break
        st.session_state.y5=y5
        st.session_state.z5=z5
    x=st.session_state.x5
    y=st.session_state.y5
    z=st.session_state.z5
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(x,y,z,y,z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(x,y,z,y,z))
elif app=="展開６":
    if "x6" not in st.session_state:
        st.session_state.x6=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y6=0
                z6=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x6,z6)==1:
                    break
            else:
                z6=0
                y6=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x6,y6)==1:
                    break
        st.session_state.y6=y6
        st.session_state.z6=z6
    if st.button("新しい問題"):
        st.session_state.x6=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y6=0
                z6=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x6,z6)==1:
                    break
            else:
                z6=0
                y6=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x6,y6)==1:
                    break
        st.session_state.y6=y6
        st.session_state.z6=z6
    x=st.session_state.x6
    y=st.session_state.y6
    z=st.session_state.z6
    st.markdown("次の式を展開せよ：")
    st.latex(因数分解(x,y,z,-y,-z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(展開(x,y,z,-y,-z))

elif app=="因数分解３":
    if "y7" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y7,a7=0,0
                z7,b7=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z7)!=abs(b7):
                    break
            else:
                z7,b7=0,0
                y7,a7=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(y7)!=abs(a7):
                    break
        st.session_state.y7=y7
        st.session_state.z7=z7
        st.session_state.a7=a7
        st.session_state.b7=b7
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y7,a7=0,0
                z7,b7=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(z7)!=abs(b7):
                    break
            else:
                z7,b7=0,0
                y7,a7=random.sample([i for i in range(-9, 10) if i != 0],2)
                if abs(y7)!=abs(a7):
                    break
        st.session_state.y7=y7
        st.session_state.z7=z7
        st.session_state.a7=a7
        st.session_state.b7=b7
    y=st.session_state.y7
    z=st.session_state.z7
    a=st.session_state.a7
    b=st.session_state.b7
    st.markdown("次の式を因数分解せよ：")
    st.latex(展開(1,y,z,a,b))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(因数分解(1,y,z,a,b))

elif app=="因数分解２":
    if "y8" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y8=0
                z8=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z8=0
                y8=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y8=y8
        st.session_state.z8=z8
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y8=0
                z8=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z8=0
                y8=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y8=y8
        st.session_state.z8=z8
    y=st.session_state.y8
    z=st.session_state.z8
    st.markdown("次の式を因数分解せよ：")
    st.latex(展開(1,y,z,y,z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(因数分解(1,y,z,y,z))

elif app=="因数分解１":
    if "y9" not in st.session_state:
        while True:
            if random.choice([True, False]):
                y9=0
                z9=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z9=0
                y9=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y9=y9
        st.session_state.z9=z9
    if st.button("新しい問題"):
        while True:
            if random.choice([True, False]):
                y9=0
                z9=random.choice([i for i in range(-9, 10) if i != 0])
                break
            else:
                z9=0
                y9=random.choice([i for i in range(-9, 10) if i != 0])
                break
        st.session_state.y9=y9
        st.session_state.z9=z9
    y=st.session_state.y9
    z=st.session_state.z9
    st.markdown("次の式を因数分解せよ：")
    st.latex(展開(1,y,z,-y,-z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(因数分解(1,abs(y),abs(z),-abs(y),-abs(z)))
        
elif app=="因数分解５":
    if "x10" not in st.session_state:
        st.session_state.x10=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y10=0
                z10=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x10,z10)==1:
                    break
            else:
                z10=0
                y10=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x10,y10)==1:
                    break
        st.session_state.y10=y10
        st.session_state.z10=z10
    if st.button("新しい問題"):
        st.session_state.x10=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y10=0
                z10=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x10,z10)==1:
                    break
            else:
                z10=0
                y10=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x10,y10)==1:
                    break
        st.session_state.y10=y10
        st.session_state.z10=z10
    x=st.session_state.x10
    y=st.session_state.y10
    z=st.session_state.z10
    st.markdown("次の式を因数分解せよ：")
    st.latex(展開(x,y,z,y,z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(因数分解(x,y,z,y,z))
elif app=="因数分解４":
    if "x11" not in st.session_state:
        st.session_state.x11=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y11=0
                z11=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x11,z11)==1:
                    break
            else:
                z11=0
                y11=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x11,y11)==1:
                    break
        st.session_state.y11=y11
        st.session_state.z11=z11
    if st.button("新しい問題"):
        st.session_state.x11=random.randint(2,6)
        while True:
            if random.choice([True, False]):
                y11=0
                z11=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x11,z11)==1:
                    break
            else:
                z11=0
                y11=random.choice([i for i in range(-9, 10) if i != 0])
                if math.gcd(st.session_state.x11,y11)==1:
                    break
        st.session_state.y11=y11
        st.session_state.z11=z11
    x=st.session_state.x11
    y=st.session_state.y11
    z=st.session_state.z11
    st.markdown("次の式を因数分解せよ：")
    st.latex(展開(x,y,z,-y,-z))
    if st.button("答えを見る"):
        st.markdown("答え：")
        st.latex(因数分解(x,abs(y),abs(z),-abs(y),-abs(z)))
