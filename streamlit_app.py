import streamlit as st
import math

st.title("Web Solusi Integral dengan Kaidah Pias Trapesium")
st.write("Masukkan fungsi seperti: 2x^2 + 3x - 1 atau math.sin(x)")

# Fungsi evaluator yang aman
def f(x, func_str):
    # Ganti tanda ^ menjadi ** agar sesuai Python
    func_str = func_str.replace("^", "**")
    return eval(func_str, {"x": x, "math": math})

# Input fungsi dan parameter
func_str = st.text_input("Masukkan fungsi f(x)", value="2x^2")
a = st.number_input("Masukkan batas bawah a", value=0.0, format="%.6f")
b = st.number_input("Masukkan batas atas b", value=1.0, format="%.6f")
n = st.number_input("Masukkan jumlah pias n", value=10, step=1)

if st.button("Hitung Integral"):

    if n <= 0:
        st.error("Jumlah pias (n) harus lebih dari 0!")
    else:
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
