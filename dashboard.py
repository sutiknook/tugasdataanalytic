import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Judul
st.title("Dashboard Interaktif dengan Streamlit")

# Elemen Dasar
st.header("Dashboard Data")
st.text("Kelompok Bella Nurhasanah-240534003 Suktikno-240534004")

# Sidebar Layout
st.sidebar.title("Pengaturan")
num_points = st.sidebar.slider("Pilih jumlah data", min_value=10, max_value=100, value=50)
show_pie_chart = st.sidebar.checkbox("Tampilkan Pie Chart")
chart_type = st.sidebar.selectbox("Pilih jenis grafik", ["Line Chart", "Bar Chart"])

# Data Dummy
data = pd.DataFrame({
    'x': np.arange(1, num_points+1),
    'y': np.random.randint(1, 100, num_points)
})

# Dua Kolom Layout
col1, col2 = st.columns(2)

# Grafik Line atau Bar Chart
if chart_type == "Line Chart":
    col1.line_chart(data)
else:
    col1.bar_chart(data)

# Pie Chart di kolom 2
if show_pie_chart:
    pie_data = data['y'].value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
    ax.set_title("Distribusi Data")
    col2.pyplot(fig)

# Container Layout
with st.container():
    st.subheader("Statistik Data")
    st.write("Statistik Deskriptif:")
    st.write(data.describe())
