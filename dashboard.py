import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Dashboard Sederhana dengan Streamlit")
st.text("Bella Nurhasanah-240534003 Sutikno-240534003.")

# Sidebar widget
st.sidebar.header("Pengaturan Data")
data_size = st.sidebar.slider("Ukuran Data", min_value=10, max_value=100, value=50)
chart_type = st.sidebar.selectbox("Pilih Jenis Grafik", ["Line Chart", "Bar Chart", "Pie Chart"])
show_markdown = st.sidebar.checkbox("Tampilkan Markdown")

# Generate sample data
data = pd.DataFrame({
    "Kategori": [f"Siswa {i}" for i in range(1, 6)],
    "Nilai": np.random.randint(10, 100, 5)
})

data_full = pd.DataFrame(
    np.random.randn(data_size, 3),
    columns=["A", "B", "C"]
)

# Tabs layout
tab1, tab2 = st.tabs(["Grafik", "Data"])

with tab1:
    st.subheader("Visualisasi Data")

    # Display chart based on selection
    if chart_type == "Line Chart":
        st.line_chart(data_full)
    elif chart_type == "Bar Chart":
        st.bar_chart(data_full)
    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        ax.pie(data["Nilai"], labels=data["Kategori"], autopct="%1.1f%%")
        st.pyplot(fig)

with tab2:
    st.subheader("Tabel Data")
    st.dataframe(data)

# Markdown element
if show_markdown:
    st.markdown(""" 
    ### Markdown Contoh
    - Item 1
    - Item 2
    - Item 3
    """)

