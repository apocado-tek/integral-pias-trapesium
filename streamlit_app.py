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

func_str = st.text_input(
    "Masukkan fungsi f(x) (contoh: math.exp(x) atau x**2)",
    value="x**2"
)
a = st.number_input("Masukkan batas bawah a", value=0.0)
b = st.number_input("Masukkan batas atas b", value=2.0)
n = st.number_input(
    "Masukkan jumlah pias n (harus bilangan bulat > 0)",
    value=4,
    step=1
)

if st.button("Hitung Integral"):

    if n <= 0:
        st.error("Jumlah pias 'n' harus bilangan bulat positif.")
    elif a >= b:
        st.error("Batas atas 'b' harus lebih besar dari batas bawah 'a'.")
    else:
        try:
            n = int(n)
            h = (b - a) / n

            st.subheader("Langkah 1: Menentukan lebar pias (h)")
            st.latex(r"h = \frac{b - a}{n}")
            st.latex(rf"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

            st.subheader("Langkah 2: Menentukan titik-titik xᵢ")

            data = []
            sum_mid = 0

            for i in range(n + 1):
                xi = a + i * h
                fxi = f(xi, func_str)

                posisi = "Ujung kiri (f₀)" if i == 0 else \
                          "Ujung kanan (fₙ)" if i == n else \
                          "Bagian tengah"

                if i != 0 and i != n:
                    sum_mid += fxi

                data.append({
                    "i": i,
                    "xᵢ": round(xi, 6),
                    "f(xᵢ)": round(fxi, 6),
                    "Keterangan": posisi
                })

            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)

            f0 = f(a, func_str)
            fn = f(b, func_str)

            st.subheader("Langkah 3: Menyusun komponen rumus")
            st.latex(r"\text{f}_0 = f(a), \quad \text{f}_n = f(b)")
            st.write(f"f₀ = {f0}")
            st.write(f"fₙ = {fn}")
            st.write(f"Jumlah f(xᵢ) bagian tengah = {sum_mid}")

            st.subheader("Langkah 4: Substitusi ke rumus trapesium")
            st.latex(
                r"\int_a^b f(x)\,dx \approx \frac{h}{2}"
                r"\left(f_0 + 2\sum_{i=1}^{n-1} f_i + f_n\right)"
            )

            hasil = (h / 2) * (f0 + 2 * sum_mid + fn)

            st.latex(
                rf"\frac{{{h}}}{{2}} \left({f0} + 2({sum_mid}) + {fn}\right)"
                rf" = {hasil}"
            )

            st.success("Hasil Akhir")
            st.markdown(f"**Estimasi Nilai Integral $\\approx$ {hasil:.6f}**")

            

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
