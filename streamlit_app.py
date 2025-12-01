import streamlit as st
import math

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
def f(x, func_str):
    """Mengevaluasi fungsi matematika dari string."""
    return eval(func_str, {"x": x, "math": math})

def trapesium_method(func_str, a, b, n):
    """
    Menghitung integral tentu f(x) dari a ke b
    menggunakan metode trapesium dengan n pias.
    """
    try:
        if n <= 0:
            return None, "Jumlah pias (n) harus lebih besar dari 0."

        h = (b - a) / n

        # f(a) dan f(b)
        f0 = f(a, func_str)
        fn = f(b, func_str)

        # Jumlah f(xi) untuk i = 1 sampai n-1
        sum_mid = 0
        for i in range(1, n):
            xi = a + i * h
            sum_mid += f(xi, func_str)

        # Rumus Metode Trapesium
        hasil = (h / 2) * (f0 + 2 * sum_mid + fn)

        return hasil, h, f0, fn
    except (NameError, TypeError, ValueError, ZeroDivisionError) as e:
        return None, f"Terjadi kesalahan saat mengevaluasi fungsi atau input: {e}"
    except Exception as e:
        return None, f"Terjadi kesalahan yang tidak terduga: {e}"

# --- Aplikasi Streamlit ---

st.title("🧮 Kalkulator Integral Tentu (Metode Trapesium)")
st.markdown("Masukkan fungsi dan batas integral untuk menghitung nilai hampiran.")

st.sidebar.header("Petunjuk Fungsi")
st.sidebar.markdown(
    """
    **Fungsi harus dalam variabel 'x'.**
    
    * **Contoh:** `x**2` (untuk $x^2$), `math.sin(x)`, `1/x`, `math.exp(-x)`.
    * Gunakan `math.` untuk fungsi trigonometri, logaritma, dll.
    """
)

# 1. Input Fungsi (String)
func_str = st.text_input(
    "Masukkan fungsi f(x) (contoh: x**2, math.sin(x)):",
    value="x**2"  # Nilai default
)

# 2. Input Batas Bawah (a) dan Batas Atas (b) (Float)
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Masukkan batas bawah a:", value=0.0)
with col2:
    b = st.number_input("Masukkan batas atas b:", value=1.0)

# 3. Input Jumlah Pias (n) (Integer)
n = st.number_input("Masukkan jumlah pias n:", min_value=1, value=10, step=1)

st.write("---")

# 4. Tombol untuk Menghitung
if st.button("Hitung Integral"):
    if b <= a:
        st.error("Batas atas (b) harus lebih besar dari batas bawah (a).")
    else:
        # Panggil fungsi perhitungan
        result = trapesium_method(func_str, a, b, n)

        # Tampilkan hasil
        if result[0] is not None:
            hasil, h, f0, fn = result
            st.success("✅ Perhitungan Selesai!")
            st.markdown(f"#### Hasil Integrasi Hampiran")
            st.latex(r"\int_{" + str(a) + "}^{" + str(b) + "} " + func_str.replace("**", "^") + " \, dx \approx " + str(hasil))
            
            st.subheader("Detail Perhitungan")
            st.markdown(f"* **Lebar pias ($h$):** $h = \\frac{{b-a}}{{n}} = \\frac{{{b} - {a}}}{{{n}}} \\approx **{h:.6f}**$")
            st.markdown(f"* **$f(a)$ atau $f_0$:** $f({a}) \\approx **{f0:.6f}**$")
            st.markdown(f"* **$f(b)$ atau $f_n$:** $f({b}) \\approx **{fn:.6f}**$")
            st.markdown(f"* **Nilai Integral $\\approx$:** **{hasil:.6f}**")

        else:
            # Tampilkan pesan error jika perhitungan gagal
            st.error(f"❌ Error: {result[1]}")
