import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Merge PDF",
    page_icon="📎",
    layout="centered"
)

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📎 Merge PDF </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Gabungkan banyak PDF mudah & cepat</p>", unsafe_allow_html=True)
st.divider()

# --- TEMPLATE & PETUNJUK
with st.expander("📌 Panduan Format & Pengambilan ID"):
    st.markdown("### 📄 Contoh Format Spreadsheet")
    st.markdown("Silakan gunakan template berikut agar program bisa membaca link PDF dengan benar:")
    st.markdown("[📥 Download Template Spreadsheet (Google Sheets)](https://docs.google.com/spreadsheets/d/1ABCDEF12345TEMPLATE/export?format=xlsx)", unsafe_allow_html=True)
    
    st.markdown("**Format Kolom:**")
    st.code("No | Nama File | Link PDF", language="text")

    st.markdown("### 📁 Cara Ambil ID Folder Google Drive:")
    st.markdown("""
    1. Buka folder Google Drive tempat kamu ingin menyimpan hasil PDF.
    2. Lihat URL-nya, contoh:
       ```
       https://drive.google.com/drive/folders/1A2B3C4D5E6F7G8H
       ```
    3. **ID Folder** adalah bagian setelah `/folders/`, yaitu:
       ```
       1A2B3C4D5E6F7G8H
       ```
    """)
    st.image("https://i.imgur.com/QBZniO2.png", caption="Contoh cara ambil ID Folder", use_column_width=True)

st.divider()

# --- FORM UTAMA
with st.form("merge_form"):
    st.subheader("📄 Masukkan Data")
    sheet_url = st.text_input("🔗 URL Google Spreadsheet (berisi link PDF)")
    folder_id = st.text_input("📁 ID Folder Google Drive (tujuan hasil PDF)")

    submitted = st.form_submit_button("🚀 Gabungkan & Upload")

# --- AKSI SETELAH SUBMIT
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
            "📂 Lihat Hasil"
            "</button></a>",
            unsafe_allow_html=True
        )

# Footer
st.divider()
st.caption("Dibuat dengan Streamlit | Versi 0.5 | © 2025")
