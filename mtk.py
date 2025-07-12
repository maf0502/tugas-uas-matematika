import streamlit as st
import matplotlib.pyplot as plt

# Fungsi perhitungan model M/M/1
def hitung_mm1(lambda_, mu):
    if lambda_ >= mu:
        raise ValueError("Sistem tidak stabil: λ harus lebih kecil dari μ")

    rho = lambda_ / mu
    L = lambda_ / (mu - lambda_)
    Lq = (lambda_ ** 2) / (mu * (mu - lambda_))
    W = 1 / (mu - lambda_)
    Wq = lambda_ / (mu * (mu - lambda_))

    return rho, L, Lq, W, Wq

# Fungsi visualisasi diagram blok antrian
def plot_diagram_antrian():
    fig, ax = plt.subplots()
    ax.text(0.1, 0.5, "λ", fontsize=12)
    ax.arrow(0.2, 0.5, 0.2, 0, head_width=0.03, head_length=0.03, fc='k', ec='k')

    ax.add_patch(plt.Rectangle((0.4, 0.4), 0.15, 0.2, fill=True, color='lightgray'))
    ax.text(0.475, 0.5, "Antrian", ha='center', va='center')

    ax.arrow(0.55, 0.5, 0.2, 0, head_width=0.03, head_length=0.03, fc='k', ec='k')

    ax.add_patch(plt.Rectangle((0.75, 0.4), 0.15, 0.2, fill=True, color='lightblue'))
    ax.text(0.83, 0.5, "Server\nμ", ha='center', va='center')

    ax.arrow(0.9, 0.5, 0.2, 0, head_width=0.03, head_length=0.03, fc='k', ec='k')
    ax.text(1.1, 0.5, "Keluar", fontsize=12)

    ax.set_xlim(0, 1.3)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.title("Diagram Antrian M/M/1")
    st.pyplot(fig)

# Streamlit App
st.title("📊 Simulasi Antrian - Model M/M/1")
st.write("Aplikasi ini mensimulasikan model antrian satu server berdasarkan teori antrian M/M/1.")

# Input dari user
lambda_ = st.number_input("Masukkan rata-rata kedatangan (λ)", min_value=0.01, step=0.1, format="%.2f")
mu = st.number_input("Masukkan rata-rata layanan (μ)", min_value=0.01, step=0.1, format="%.2f")

# Tombol Hitung
if st.button("Hitung"):
    try:
        rho, L, Lq, W, Wq = hitung_mm1(lambda_, mu)

        st.success("✅ Perhitungan Berhasil!")
        st.metric("ρ (Utilisasi)", f"{rho:.4f}")
        st.metric("L (Jumlah pelanggan dalam sistem)", f"{L:.4f}")
        st.metric("Lq (Jumlah pelanggan dalam antrian)", f"{Lq:.4f}")
        st.metric("W (Waktu dalam sistem)", f"{W:.4f}")
        st.metric("Wq (Waktu tunggu dalam antrian)", f"{Wq:.4f}")

        st.subheader("📈 Diagram Alur Antrian")
        plot_diagram_antrian()

    except ValueError as e:
        st.error(f"❌ Error: {e}")
