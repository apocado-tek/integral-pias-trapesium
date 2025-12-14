import streamlit as st
import math
import pandas as pd

st.title("Web Solusi Integral dengan kaidah Pias Trapesium")
st.write("""
Aplikasi ini digunakan untuk **mendekati nilai integral** dari suatu fungsi
menggunakan **metode pias trapesium**.

Metode ini bekerja dengan **membagi daerah kurva menjadi beberapa trapesium kecil**
lalu menjumlahkan luasnya.
""")
def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

st.sidebar.header("Pengaturan Perhitungan")
func_str = st.sidebar.text_input(
    "Fungsi f(x)",
    value="x**2",
    help="Contoh: x**2, math.exp(x), math.sin(x)"
)
a = st.sidebar.number_input("Batas bawah (a)", value=0.0)
b = st.sidebar.number_input("Batas atas (b)", value=1.0)
n = st.sidebar.number_input(
    "Jumlah pias (n)",
    value=1,
    step=1,
    help="Semakin besar n, hasil semakin akurat"
)
st.sidebar.info(
    """
**Catatan Penting:**
- jumlah pias **n** harus bilangan bulat positif dan tidak boleh negatif.
- batas atas yaitu **b** harus lebih besar dari batas bawa yaitu **a**
"""
)

hitung = st.button("Hitung Integral")

    hasil = None  # supaya aman secara logika

if hitung:

    if n <= 0:
        st.error("Jumlah pias 'n' harus bilangan bulat positif.")
    elif a >= b:
        st.error("Batas atas 'b' harus lebih besar dari batas bawah 'a'.")
    else:
        try:
            n = int(n)
            h = (b - a) / n

            f0 = f(a, func_str)
            fn = f(b, func_str)

            sum_mid = 0
            data = []

            for i in range(n + 1):
                xi = a + i * h
                fxi = f(xi, func_str)

                if i != 0 and i != n:
                    sum_mid += fxi

                data.append({
                    "i": i,
                    "xᵢ": round(xi, 6),
                    "f(xᵢ)": round(fxi, 6)
                })

            hasil = (h / 2) * (f0 + 2 * sum_mid + fn)

            # ===============================
            # HASIL UTAMA (SELALU DITAMPILKAN)
            # ===============================
            st.success("Hasil Perhitungan Integral")
            st.latex(
                rf"\int_{{{a}}}^{{{b}}} {func_str}\,dx \approx {hasil:.6f}"
            )

            # ===============================
            # MODE BELAJAR (OPSIONAL)
            # ===============================
            if show_steps:
                st.divider()
                st.subheader("Penjelasan Langkah demi Langkah")

                st.markdown("### 1️⃣ Lebar pias")
                st.latex(r"h = \frac{b - a}{n}")
                st.latex(rf"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

                st.markdown("### 2️⃣ Titik dan nilai fungsi")
                st.dataframe(pd.DataFrame(data), use_container_width=True)

                st.markdown("### 3️⃣ Rumus trapesium")
                st.latex(
                    r"\int_a^b f(x)\,dx \approx \frac{h}{2}"
                    r"\left(f_0 + 2\sum_{i=1}^{n-1} f_i + f_n\right)"
                )

                st.markdown("### 4️⃣ Substitusi")
                st.latex(
                    rf"\frac{{{h}}}{{2}}"
                    rf"\left({f0} + 2({sum_mid}) + {fn}\right)"
                    rf" = {hasil}"
                )

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
