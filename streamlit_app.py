import streamlit as st
import math

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Fungsi evaluator
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

st.title("Kalkulator Integral Metode Trapesium")

# Input dari user
func_str = st.text_input("Masukkan fungsi f(x)")
a = st.number_input("Masukkan batas bawah a", value=0.0)
b = st.number_input("Masukkan batas atas b", value=0.0)
n = st.number_input("Masukkan jumlah pias n", value=0)

# Tombol hitung
if st.button("Hitung Integral"):
    try:
        h = (b - a) / n

        f0 = f(a, func_str)
        fn = f(b, func_str)

        sum_mid = 0
        for i in range(1, int(n)):
            xi = a + i*h
            sum_mid += f(xi, func_str)

        hasil = (h/2) * (f0 + 2*sum_mid + fn)

        # Output ke UI
        st.write("### Hasil Perhitungan")
        st.write(f"Lebar pias (h) = **{h}**")
        st.write(f"f(a) = **{f0}**")
        st.write(f"f(b) = **{fn}**")
        st.write(f"Jumlah bagian tengah = **{sum_mid}**")
        st.success(f"Nilai integral ≈ **{hasil}**")

    except Exception as e:
        st.error(f"Terjadi error: {e}")
