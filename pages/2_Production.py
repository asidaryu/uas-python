import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Rice Production",
    page_icon="🍚"
)
# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/31/56/7a/31567a2aea11c60f3792b2f9d09d1dde.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Judul pada page Data
st.markdown(
    '<div style="font-size: 40px; font-family: timesnewroman; margin-bottom: 50px;">Rice Production indonesia</div>',
    unsafe_allow_html=True
)

# Fungsi untuk menampilkan data pada tahun 2020-2022
year = st.sidebar.radio(
    "Pilih Tahun:",
    ('2020', '2021', '2022')
)

# Data berdasarkan Rice Production Indonesia Tahu 2020-2022
data = {
    "Provinsi": ["Aceh", "Riau", "Jambi", "Bengkulu", "Lampung", "Banten", "Bali", "Jawa Tengah"],
    "Productivity (kw/ha) Tahun 2020": [55.28, 37.64, 45.58, 45.66, 48.62, 50.88, 58.49, 56.93],
    "Productivity (kw/ha) Tahun 2021": [55.03, 40.98, 46.29, 48.67,  50.77, 50.38, 58.83, 56.69],
    "Productivity (kw/ha) Tahun 2022": [55.55, 41.83, 45.88, 49.27, 51.87, 53.04, 60.59, 55.41],
}
# Menambahkan tabs
lingkaran, batang, tabel = st.tabs(["GRAFIK LINGKARAN", "GRAFIK BATANG", "TABEL"])

# Aceh, Riau, Jambi, Bengkulu, Lampung, Banten, Bali, Jawa Tengah
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2', '#ff6666']

with lingkaran:
    # Data
    labels = data["Provinsi"]
    sizes = data[f"Productivity (kw/ha) Tahun {year}"]

    # Explode untuk bagian yang ditekankan
    explode = (0, 0, 0, 0, 0.1, 0, 0.1, 0.2)

    fig1, ax1 = plt.subplots()

    # Menambahkan labels, warna, dan explode
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, explode=explode)
    ax1.axis('equal')

    # Menampilkan grafik
    st.pyplot(fig1)

with batang:
    fig = px.bar(data, x="Provinsi", y=f"Productivity (kw/ha) Tahun {year}", color= colors)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

with tabel:
    df = pd.DataFrame(data)
    st.markdown(
        '<div style="margin-top: 20px;"></div>',
        unsafe_allow_html=True
    )
    filtered_df = df[["Provinsi", f"Productivity (kw/ha) Tahun {year}"]]  
    st.write(filtered_df)