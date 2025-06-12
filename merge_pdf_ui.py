import streamlit as st

st.set_page_config(
    page_title="Merge PDF",
    page_icon="📎",
    layout="centered"
)

# ========== SIDEBAR ==========
st.sidebar.title("📚 Navigasi")
page = st.sidebar.radio("Pilih halaman:", ["📎 Gabung PDF", "🕘 Riwayat", "ℹ️ Tentang"])

# ========== HEADER ==========
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #4CAF50;'>📎 Gabung PDF Otomatis</h1>
        <p style='font-size: 16px; color: gray;'>Gabungkan file PDF dari Spreadsheet atau unggah langsung ke sistem</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# ========== HALAMAN: GABUNG PDF ==========
if page == "📎 Gabung PDF":
    st.subheader("🧾 Metode 1: Gunakan Google Spreadsheet")
    
    col1, col2 = st.columns(2)
    with st.form("merge_form"):
        with col1:
            sheet_url = st.text_input("🔗 URL Spreadsheet", placeholder="https://docs.google.com/spreadsheets/...")
        with col2:
            folder_id = st.text_input("📁 ID Folder Google Drive", placeholder="1A2B3C4D...")

        st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 0.5em 2em;
                border-radius: 10px;
                border: none;
                margin-top: 1em;
            }
            </style>
        """, unsafe_allow_html=True)

        submitted = st.form_submit_button("🚀 Gabungkan & Upload")

    if submitted:
        if not sheet_url or not folder_id:
            st.warning("⚠️ Mohon isi semua kolom.")
        else:
            with st.spinner("🔄 Memproses..."):
                st.success("✅ Simulasi berhasil! (fungsi backend belum dihubungkan)")
                st.balloons()

    st.divider()
    st.subheader("📥 Metode 2: Upload File PDF Langsung")

    uploaded_files = st.file_uploader(
        "Tarik & lepas beberapa file PDF di sini",
        type="pdf",
        accept_multiple_files=True,
        help="File akan digabung sesuai urutan unggah."
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} file berhasil diunggah.")
        if st.button("🚀 Gabungkan File PDF"):
            with st.spinner("🔄 Menggabungkan file PDF..."):
                file_names = [f.name for f in uploaded_files]
                st.markdown("📄 <b>Daftar file:</b>", unsafe_allow_html=True)
                for name in file_names:
                    st.markdown(f"- {name}")
                st.success("✅ File berhasil digabung! (simulasi)")
                st.balloons()

# ========== HALAMAN: RIWAYAT ==========
elif page == "🕘 Riwayat":
    st.subheader("🕘 Riwayat Penggabungan PDF")
    st.info("Fitur ini akan menampilkan riwayat merge PDF yang sudah dilakukan. (masih dalam pengembangan)")

# ========== HALAMAN: TENTANG ==========
elif page == "ℹ️ Tentang":
    st.subheader("ℹ️ Tentang Aplikasi")
    st.write("""
    Aplikasi ini membantu Anda menggabungkan file PDF dari dua sumber:
    
    - Google Spreadsheet (berisi link PDF di Google Drive)
    - Upload langsung dari komputer Anda

    Dibuat dengan ❤️ oleh dee-dev.
    """)

# ========== FOOTER ==========
st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: gray;'>"
    "Dibuat oleh dee-dev | <strong>Versi UI: 1.0</strong> | © 2025"
    "</p>",
    unsafe_allow_html=True
)

