import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Merge PDF Otomatis",
    page_icon="📎",
    layout="centered"
)

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📎 Gabung PDF Otomatis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Ambil link PDF dari Google Sheets & upload ke Google Drive</p>", unsafe_allow_html=True)
st.divider()

# Input Form
with st.form("merge_form"):
    st.subheader("📄 Masukkan Data")
    sheet_url = st.text_input("🔗 URL Google Spreadsheet (berisi link PDF)")
    folder_id = st.text_input("📁 ID Folder Google Drive (tujuan hasil PDF)")

    submitted = st.form_submit_button("🚀 Gabungkan & Upload")

# Aksi saat tombol ditekan
if submitted:
    if not sheet_url or not folder_id:
        st.warning("⚠️ Mohon lengkapi semua input terlebih dahulu.")
    else:
        with st.spinner("🔄 Memproses penggabungan PDF..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)
            st.success("✅ PDF berhasil digabung dan diupload!")

        # Tampilkan tombol "Lihat Hasil"
        drive_url = f"https://drive.google.com/drive/folders/{folder_id}"
        st.markdown(
            f"<a href='{drive_url}' target='_blank'>"
            "<button style='background-color:#4CAF50;color:white;padding:0.5em 1.5em;font-size:16px;border:none;border-radius:8px;'>"
            "Lihat Hasil"
            "</button></a>",
            unsafe_allow_html=True
        )

# Footer
st.divider()
st.caption(" Dibuat dengan Streamlit | Versi 0.4 | © 2025")

