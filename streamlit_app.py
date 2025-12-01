import streamlit as st
import math

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

func_str = st.text_input("Masukkan fungsi f(x): ")
a = st.number_input("Masukkan batas bawah a: ")
b = st.number_input("Masukkan batas atas b: ")
n = st.number_input("Masukkan jumlah pias n: ")

h = (b - a) / n

f0 = f(a, func_str)
fn = f(b, func_str)

sum_mid = 0
for i in range(1, n):
    xi = a + i*h
    sum_mid += f(xi, func_str)

hasil = (h/2) * (f0 + 2*sum_mid + fn)

print(f"lebar pias = ", h)
print(f"f0 = ", f0)
print(f"fn = ", fn)
print(f"Nilai integral ≈ ", hasil)
