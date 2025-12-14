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
            
            st.success("Hasil Integral")
            st.latex(
                rf"\int_{{{a}}}^{{{b}}} {func_str}\,dx \approx {hasil:.6f}"
            )
            if show_steps:
                st.subheader("Penjelasan Metode Pias Trapesium")

                st.markdown("**Langkah 1: Lebar pias**")
                st.latex(r"h = \frac{b - a}{n}")
                st.latex(rf"h = \frac{{{b} - {a}}}{{{n}}} = {h}")

                st.markdown("**Langkah 2: Titik dan nilai fungsi**")
                st.dataframe(data, use_container_width=True)

                st.markdown("**Langkah 3: Susun rumus trapesium**")
                st.latex(
                    r"\int_a^b f(x)\,dx \approx \frac{h}{2}"
                    r"\left(f_0 + 2\sum_{i=1}^{n-1} f_i + f_n\right)"
                )

                st.markdown("**Langkah 4: Substitusi nilai**")
                st.latex(
                    rf"\frac{{{h}}}{{2}}"
                    rf"\left({f0} + 2({sum_mid}) + {fn}\right)"
                    rf" = {hasil}"
                )

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
