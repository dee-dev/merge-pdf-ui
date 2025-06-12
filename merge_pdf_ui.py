import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Merge PDF",
    page_subtitle="gabungkan PDF dengan otomatis dan cepat"
    page_icon="📎",
    layout="centered"
)

# Header utama
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📎 Gabung PDF Otomatis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Ambil link PDF dari Google Sheets & upload hasilnya ke Google Drive</p>", unsafe_allow_html=True)

# Garis pemisah
st.divider()

# Form input user
with st.form("merge_form"):
    st.subheader("📄 Masukkan Data")
    sheet_url = st.text_input("🔗 URL Google Spreadsheet (berisi link PDF)")
    folder_id = st.text_input("📁 ID Folder Google Drive (tujuan hasil merge)")

    submitted = st.form_submit_button("🚀 Gabungkan & Upload")

# Aksi tombol
if submitted:
    if not sheet_url or not folder_id:
        st.warning("⚠️ Mohon lengkapi semua input terlebih dahulu.")
    else:
        st.success("✅ Simulasi sukses! (Fitur merge PDF belum aktif)")
        st.info("📌 Ini hanya tampilan UI. Backend akan dihubungkan nanti.")

# Divider akhir
st.divider()

# Footer / stempel versi
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: gray;'>"
    "Dibuat dengan ❤️ oleh dee-dev | <strong>Versi UI: 0.4</strong> | © 2025"
    "</p>",
    unsafe_allow_html=True
)

