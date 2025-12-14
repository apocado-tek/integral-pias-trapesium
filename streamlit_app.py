import streamlit as st
import math

st.title("Web Solusi Integral dengan kaidah Pias Trapesium")
st.write(
)

def f(x, func_str):
    """Fungsi untuk mengevaluasi rumus dari string."""
    return eval(func_str, {"x": x, "math": math})

st.title("Kalkulator Integral Kaidah Trapesium Detail")

# --- Input Pengguna ---
func_str = st.text_input("Masukkan fungsi f(x) (contoh: math.exp(x) atau x**2)", value="x**2")
a = st.number_input("Masukkan batas bawah a", value=0.0)
b = st.number_input("Masukkan batas atas b", value=2.0)
n = st.number_input("Masukkan jumlah pias n (harus bilangan bulat > 0)", value=4, step=1)

# --- Tombol Hitung ---
if st.button("Hitung Integral Rinci"):
    
    if n <= 0:
        st.error("Jumlah pias 'n' harus bilangan bulat positif.")
    elif a >= b:
        st.error("Batas atas 'b' harus lebih besar dari batas bawah 'a'.")
    else:
        try:
            # 1. Perhitungan Dasar
            h = (b - a) / n

            f0 = f(a, func_str)
            fn = f(b, func_str)

            # 2. Mengumpulkan Nilai Tengah secara Rinci
            # Kita menggunakan list untuk menyimpan setiap nilai f(xi)
            nilai_tengah_list = []
            
            for i in range(1, int(n)): 
                xi = a + i * h
                f_xi = f(xi, func_str)
                nilai_tengah_list.append(f_xi)
            
            # 3. Menghitung Penjumlahan Akhir
            sum_mid = sum(nilai_tengah_list)
            hasil = (h / 2) * (f0 + 2 * sum_mid + fn)
            
            
            # --- TAMPILAN RINCI (OUTPUT) ---
            st.success("### 📜 Hasil Perhitungan Detail Kaidah Trapesium")
            
            st.markdown(f"**Fungsi:** $f(x) = {func_str}$")
            st.write(f"**Batas:** $[{a}, {b}]$")
            st.write(f"**Jumlah Pias ($n$):** {n}")
            st.markdown(f"**Lebar Pias ($h$):** $h = \\frac{{b-a}}{{n}} = \\frac{{{b} - {a}}}{{{n}}} = {h:.4f}$")
            
            st.subheader("1. Ketinggian Titik Ujung")
            st.code(f"f(x₀) = f({a:.4f}) = {f0:.6f} \n"
                    f"f(xₙ) = f({b:.4f}) = {fn:.6f}")

            st.subheader("2. Ketinggian Titik Tengah (Diulang 2x)")
            
            perhitungan_string = []
            for i, val in enumerate(nilai_tengah_list):
                xi = a + (i + 1) * h
                perhitungan_string.append(f"f(x{i+1}) = f({xi:.4f}) = {val:.6f}")
            
            st.text('\n'.join(perhitungan_string))
            
            st.markdown(f"**Total Penjumlahan Titik Tengah ($ \\sum f(x_i) $):** {sum_mid:.6f}")

            st.subheader("3. Penerapan Rumus Akhir")
            
            rumus_akhir = (
                f"$$\\text{{Integral}} \\approx \\frac{{h}}{{2}} [f(x_0) + 2 \\sum f(x_i) + f(x_n)] $$"
                f"$$\\approx \\frac{{{h:.4f}}}{{2}} [{f0:.6f} + 2 \\times {sum_mid:.6f} + {fn:.6f}] $$"
                f"$$\\approx {h/2:.4f} \\times ({f0:.6f} + {2*sum_mid:.6f} + {fn:.6f}) $$"
                f"$$\\approx {hasil:.6f}$$"
            )
            st.markdown(rumus_akhir)
            
            st.subheader("✅ Estimasi Akhir")
            st.markdown(f"**Estimasi Nilai Integral $\\approx$ {hasil:.6f}**")
            
        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengevaluasi fungsi atau perhitungan: {e}")
