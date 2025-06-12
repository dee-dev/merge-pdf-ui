import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Merge PDF",
    page_icon="📎",
    layout="centered"
)

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📎 Merge PDF Otomatis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Ambil link PDF dari Google Sheets & upload ke Google Drive</p>", unsafe_allow_html=True)
st.divider()

# Input Form
with st.form("merge_form"):
    st.subheader("📄 Masukkan Data")
    sheet_url = st.text_input("🔗 URL Google Spreadsheet (berisi link PDF)")
    folder_id = st.text_input("📁 ID Folder Google Drive (tujuan hasil PDF)")

    submitted = st.form_submit_button("Gabungkan & Upload")

# Aksi saat tombol ditekan
if submitted:
    if not sheet_url or not folder_id:
        st.warning("⚠️ Mohon lengkapi semua input terlebih dahulu.")
    else:
        # Belum ada proses backend
        st.success("✅ Proses berhasil dijalankan (simulasi UI saja).")
        st.info("🔧 Fitur penggabungan PDF belum aktif.")

# Footer
st.divider()
st.caption("Dibuat dengan Streamlit | Versi 0.3 | © 2025")

