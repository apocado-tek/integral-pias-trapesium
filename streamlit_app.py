import streamlit as st
import math
st.title("Web Solusi Integral dengan kaidah Pias Trapesium")
st.write(
 ""
)
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

func_str = st.text_input("Masukkan fungsi f(x)", value = 0)
a = st.number_input("Masukkan batas bawah a", value=0.0)
b = st.number_input("Masukkan batas atas b", value=0.0)
n = st.number_input("Masukkan jumlah pias n", value=0)

if st.button("Hitung Integral"):
        h = (b - a) / n

        f0 = f(a, func_str)
        fn = f(b, func_str)

        sum_mid = 0
        for i in range(1, int(n)):
            xi = a + i*h
            sum_mid += f(xi, func_str)

        hasil = (h/2) * (f0 + 2*sum_mid + fn)

        st.write("### Hasil Perhitungan")
        st.write(f"Lebar pias (h) = **{h}**")
        st.write(f"f(a) = **{f0}**")
        st.write(f"f(b) = **{fn}**")
        st.write(f"Jumlah bagian tengah = **{sum_mid}**")
        st.success(f"Nilai integral ≈ **{hasil}**")
