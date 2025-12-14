import streamlit as st
import math
import pandas as pd

st.title("Web Solusi Integral dengan kaidah Pias Trapesium")
st.write(
)
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})
    
func_str = st.text_input("Masukkan fungsi f(x) (contoh: math.exp(x) atau x**2)", value="x**2")
a = st.number_input("Masukkan batas bawah a", value=0.0)
b = st.number_input("Masukkan batas atas b", value=2.0)
n = st.number_input("Masukkan jumlah pias n (harus bilangan bulat > 0)", value=4, step=1)

if st.button("Hitung Integral"):
    
    if n <= 0:
        st.error("Jumlah pias 'n' harus bilangan bulat positif.")
    elif a >= b:
        st.error("Batas atas 'b' harus lebih besar dari batas bawah 'a'.")
    else:
        try:
            h = (b - a) / n

            f0 = f(a, func_str)
            fn = f(b, func_str)

            sum_mid = 0
            
            for i in range(1, int(n)): 
                xi = a + i * h
                sum_mid += f(xi, func_str)

            hasil = (h / 2) * (f0 + 2 * sum_mid + fn)
            
            st.success(f"### Hasil Integral")
            st.write(f"Fungsi: $f(x) = {func_str}$")
            st.write(f"Batas: $[{a}, {b}]$")
            st.write(f"Jumlah Pias ($n$): {n}")
            st.markdown(f"**Estimasi Nilai Integral $\\approx$ {hasil:.6f}**")
            
        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengevaluasi fungsi atau perhitungan: {e}")
