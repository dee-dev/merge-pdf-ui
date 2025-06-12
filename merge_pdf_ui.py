import streamlit as st

st.set_page_config(page_title="Gabung PDF", page_icon="🧩")
st.title("🧩 Gabungkan PDF dari Google Sheet dan Upload ke Drive")

st.markdown("Silakan masukkan URL Spreadsheet dan Folder Google Drive")

sheet_url = st.text_input("🔗 URL Google Spreadsheet berisi link PDF")
folder_id = st.text_input("📁 ID Folder Google Drive (tempat upload hasil)")

if st.button("🚀 Gabungkan dan Upload"):
    if not sheet_url or not folder_id:
        st.warning("Mohon lengkapi semua input.")
    else:
        st.info("🔧 Fitur merge belum diaktifkan. Ini hanya tampilan antarmuka.")
        st.success("✅ Antarmuka siap!")

