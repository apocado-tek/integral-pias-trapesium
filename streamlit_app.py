import streamlit as st
import math
import pandas as pd

st.title("Web Solusi Integral dengan Kaidah Pias Trapesium")

st.write("""
Website ini digunakan untuk **mendekati nilai integral** suatu fungsi
menggunakan **metode pias trapesium**.

Metode ini bekerja dengan cara **membagi daerah di bawah kurva menjadi beberapa
trapesium kecil**, lalu menjumlahkan luasnya.
""")

def f(x, func_str):
    return eval(func_str, {"x": x, "math": math})

# INPUT USER
st.sidebar.header("Pengaturan Perhitungan")

st.latex(
    r"\int_a^b f(x)\,dx \approx \frac{h}{2}"
)

func_str = st.sidebar.text_input(
    "Fungsi f(x)",
    value="x**2",
    help="Contoh: x**2, math.exp(x), math.sin(x)"
)

a = st.sidebar.number_input("Batas bawah (a)", value=0.0)
b = st.sidebar.number_input("Batas atas (b)", value=1.0)

n = st.sidebar.number_input(
    "Jumlah pias (n)",
    value=4,
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

show_steps = st.checkbox("Centang box ✅ kalau anda ingin menampilkan langkah demi langkah cara penyelesaiannya untuk bahan belajar anda")
hitung = st.button("Hitung Integral")

# PROSES PERHITUNGAN
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
            mid_values = []

            for i in range(n + 1):
                xi = a + i * h
                fxi = f(xi, func_str)

                if i == 0:
                    posisi = "Ujung kiri (f₀)"
                elif i == n:
                    posisi = "Ujung kanan (fₙ)"
                else:
                    posisi = "Bagian tengah"
                    mid_values.append(fxi)
                    sum_mid += fxi

                data.append({
                    "i": i,
                    "xᵢ": round(xi, 6),
                    "f(xᵢ)": round(fxi, 6),
                    "Keterangan": posisi
                })


            hasil = (h / 2) * (f0 + 2 * sum_mid + fn)

            st.success("Hasil Perhitungan Integral")
            st.latex(
                rf"\int_{{{a}}}^{{{b}}} {func_str}\,dx \approx {hasil:.6f}"
            )

            if show_steps:
                st.divider()
                st.subheader("Penjelasan Langkah demi Langkah")

                st.markdown("### 1️⃣ Menentukan lebar pias")
                st.latex(r"h = \frac{b - a}{n}")
                st.latex(rf"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

                st.markdown("### 2️⃣ Menentukan titik tengah dan nilai fungsi")
                st.dataframe(pd.DataFrame(data), use_container_width=True)

                if mid_values:
                    penjumlahan = " + ".join(f"{v:.6f}" for v in mid_values)
                    st.latex(
                        rf"\sum_{{i=1}}^{{{n-1}}} f(x_i)"
                        rf" = {penjumlahan}"
                        rf" = \mathbf{{{sum_mid}}}"
                    )

                st.markdown("### 3️⃣ Rumus metode trapesium")
                st.latex(
                    r"\int_a^b f(x)\,dx \approx \frac{h}{2}"
                    r"\left(f_0 + 2\sum_{i=1}^{n-1} f_i + f_n\right)"
                )

                st.markdown("### 4️⃣ Substitusi nilai")
                st.latex(
                    rf"\frac{{{h}}}{{2}}"
                    rf"\left({f0} + 2({sum_mid}) + {fn}\right)"
                    rf" = {hasil}"
                )

        except Exception as e:
            st.error(f"Terjadi kesalahan dalam perhitungan: {e}")
