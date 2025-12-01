import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
def f(x, func_str):
    """Evaluasi fungsi dengan input string"""
    try:
        return eval(func_str, {"x": x, "math": math, "np": np})
    except:
        return None

def metode_trapesium(func_str, a, b, n):
    """Hitung integral dengan metode Trapesium"""
    h = (b - a) / n
    
    f0 = f(a, func_str)
    fn = f(b, func_str)
    
    if f0 is None or fn is None:
        return None, None, None, None, None
    
    sum_mid = 0
    for i in range(1, n):
        xi = a + i*h
        fi = f(xi, func_str)
        if fi is None:
            return None, None, None, None, None
        sum_mid += fi
    
    hasil = (h/2) * (f0 + 2*sum_mid + fn)
    
    return h, f0, fn, sum_mid, hasil

def plot_fungsi(func_str, a, b, n):
    """Plot grafik fungsi dan trapesium"""
    try:
        x_smooth = np.linspace(a, b, 500)
        y_smooth = [f(xi, func_str) for xi in x_smooth]
        
        if None in y_smooth:
            return None
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot fungsi asli
        ax.plot(x_smooth, y_smooth, 'b-', linewidth=2, label='f(x)')
        
        # Plot trapesium
        h = (b - a) / n
        x_trap = [a + i*h for i in range(n+1)]
        y_trap = [f(xi, func_str) for xi in x_trap]
        
        for i in range(n):
            x_fill = [x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]]
            y_fill = [0, y_trap[i], y_trap[i+1], 0]
            ax.fill(x_fill, y_fill, alpha=0.3, edgecolor='red', facecolor='yellow')
        
        ax.plot(x_trap, y_trap, 'ro-', markersize=6, label='Titik Trapesium')
        
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title(f'Metode Trapesium: {func_str}', fontsize=14, fontweight='bold')
        ax.legend()
        
        return fig
    except:
        return None

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Integral Trapesium", page_icon="📊", layout="wide")

# Header
st.title("📊 Kalkulator Integral Numerik")
st.subheader("Metode Trapesium")
st.markdown("---")

# Sidebar untuk informasi
with st.sidebar:
    st.header("ℹ️ Informasi")
    st.write("""
    **Metode Trapesium** adalah metode numerik untuk menghitung integral tentu.
    
    **Rumus:**
    """)
    st.latex(r"\int_a^b f(x)dx \approx \frac{h}{2}[f_0 + 2\sum_{i=1}^{n-1}f_i + f_n]")
    
    st.write("""
    **Contoh Fungsi:**
    - `x**2` → x²
    - `math.sin(x)` → sin(x)
    - `math.exp(x)` → eˣ
    - `x**3 + 2*x` → x³ + 2x
    - `1/x` → 1/x
    """)

# Input Form
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Input Parameter")
    
    func_str = st.text_input(
        "Fungsi f(x):",
        value="x**2",
        help="Gunakan 'x' sebagai variabel dan 'math.' untuk fungsi matematika"
    )
    
    col_a, col_b = st.columns(2)
    with col_a:
        a = st.number_input("Batas bawah (a):", value=0.0, format="%.4f")
    with col_b:
        b = st.number_input("Batas atas (b):", value=1.0, format="%.4f")
    
    n = st.number_input("Jumlah pias (n):", min_value=1, value=4, step=1)
    
    hitung_btn = st.button("🔢 Hitung Integral", type="primary", use_container_width=True)

with col2:
    st.markdown("### 📈 Visualisasi")
    plot_placeholder = st.empty()

# Perhitungan
if hitung_btn:
    if b <= a:
        st.error("❌ Batas atas (b) harus lebih besar dari batas bawah (a)!")
    else:
        h, f0, fn, sum_mid, hasil = metode_trapesium(func_str, a, b, n)
        
        if hasil is None:
            st.error("❌ Terjadi kesalahan! Periksa kembali fungsi yang Anda masukkan.")
        else:
            # Hasil perhitungan
            st.markdown("---")
            st.markdown("### 🎯 Hasil Perhitungan")
            
            col_r1, col_r2, col_r3, col_r4 = st.columns(4)
            
            with col_r1:
                st.metric("Lebar Pias (h)", f"{h:.6f}")
            with col_r2:
                st.metric("f(a) = f₀", f"{f0:.6f}")
            with col_r3:
                st.metric("f(b) = fₙ", f"{fn:.6f}")
            with col_r4:
                st.metric("Σ f(xᵢ)", f"{sum_mid:.6f}")
            
            st.markdown("---")
            
            # Hasil akhir
            st.success(f"### ✅ Nilai Integral ≈ **{hasil:.8f}**")
            
            # Detail perhitungan
            with st.expander("📋 Lihat Detail Perhitungan"):
                st.write(f"**Fungsi:** f(x) = {func_str}")
                st.write(f"**Interval:** [{a}, {b}]")
                st.write(f"**Jumlah pias:** {n}")
                st.write(f"**Lebar tiap pias:** h = (b - a) / n = ({b} - {a}) / {n} = {h}")
                st.write("")
                st.write("**Langkah Perhitungan:**")
                st.write(f"1. f(a) = f({a}) = {f0}")
                st.write(f"2. f(b) = f({b}) = {fn}")
                st.write(f"3. Σ f(xᵢ) untuk i=1 hingga n-1 = {sum_mid}")
                st.write("")
                st.write("**Rumus Trapesium:**")
                st.latex(r"I \approx \frac{h}{2}[f_0 + 2\sum_{i=1}^{n-1}f_i + f_n]")
                st.write(f"I ≈ ({h}/2) × [{f0} + 2×{sum_mid} + {fn}]")
                st.write(f"I ≈ {h/2} × [{f0} + {2*sum_mid} + {fn}]")
                st.write(f"I ≈ {h/2} × {f0 + 2*sum_mid + fn}")
                st.write(f"**I ≈ {hasil}**")
            
            # Plot grafik
            with plot_placeholder:
                fig = plot_fungsi(func_str, a, b, n)
                if fig:
                    st.pyplot(fig)
                else:
                    st.warning("⚠️ Tidak dapat menampilkan grafik untuk fungsi ini.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Dibuat dengan Streamlit | Metode Numerik - Trapesium</p>
</div>
""", unsafe_allow_html=True)
