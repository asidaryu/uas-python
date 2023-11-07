import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Best Selling Manga",
    page_icon="🤖"
)

# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/31/56/7a/31567a2aea11c60f3792b2f9d09d1dde.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Filter berdasarkan kategori
category = st.sidebar.selectbox('Pilih Publisher', ['Shueisha', 'Shogakukan', 'Kodansha'])

# Judul pada page Data
st.markdown(
    '<div style="font-size: 40px; font-family: timesnewroman; margin-bottom: 50px;">Best Selling Manga</div>',
    unsafe_allow_html=True
)
st.caption('Demographic : Shonen')

# Data berdasarkan Pendidikan Tertinggi Yang Ditamatkan dan Tahunnya
data = {
     "Category Shueisha": ["One Piece", "Dragon Ball", "Naruto", "Slam Dunk", "Captain Tsubasa", "Kimetsu no Yaiba", "Bleach", "JoJo's Bizare"],
     "Category Shogakukan": ["Doraemon", "Inuyasha", "Kyo Kara Ore Wa", "Pokemon", "Flame of Recca", "Monster", "Zatch Bell", "Golgo 13"],
     "Category Kodansha": ["Attack on Titan", "Hajime no Ipo", "Vagabond", "Fairy Tail", "Tokyo Revengers", "Initial D", "Devilman", "Shoot!"],
     "Author Shueisha": ["Eiichiro Oda", "Akira Toriyama", "Masashi Kishimoto", "Takehiko Inoue", "Yoichi Takahashi", "Koyoharu Gotouge", "Tite Kubo", "Hirohiko Araki"],
     "Author Shogakukan": ["Fujiko", "Rumiko Takahashi", "Hiroyuki Nishimori", "Hidenori Kusaka", "Nobuyuki Anzai", "Naoki Urasawa", "Makoto Raiku", "Takao Saito"],
     "Author Kodansha": ["Hajime Isayama", "George Morikawa", "Takehiko Inoue", "Hiro Mashima", "Ken Wakui", "Shuichi Shigeno", "Go Nagai", "Tsukasa Oshima"],
     "Penjualan rata2 per volume(juta) Shueisha" : [6.54, 1.22, 1.75, 0.92, 3.23, 4.35, 3.7, 0.74],
     "Penjualan rata2 per volume(juta) Shogakukan" : [1.11, 3.85, 1.42, 0.83, 1.91, 0.59, 2.29, 2.33],
     "Penjualan rata2 per volume(juta) Kodansha" : [2.33, 2.21, 2.96, 1.33, 4.1, 0.96, 1.14, 2.57],
}


# Menambahkan tabs
lingkaran, batang, tabel = st.tabs(["GRAFIK LINGKARAN", "GRAFIK BATANG", "TABEL"])

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2', '#ff6666']

with lingkaran:
    # Data
    labels = data[f"Category {category}"]
    sizes = data[f"Penjualan rata2 per volume(juta) {category}"] 

    # Explode untuk bagian yang ditekankan
    explode = (0, 0, 0, 0, 0.1, 0, 0.1, 0.2)

    fig1, ax1 = plt.subplots()

    # Menambahkan labels, warna, dan explode
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, explode=explode)
    ax1.axis('equal')

    # Menampilkan grafik
    st.pyplot(fig1)

with batang:
    fig = px.bar(data, x=f"Category {category}", y= f"Penjualan rata2 per volume(juta) {category}", color=colors)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

with tabel:
    df = pd.DataFrame(data)
    st.markdown(
        '<div style="margin-top: 20px;"></div>',
        unsafe_allow_html=True
    )
    filtered_df = df[[f"Category {category}", f"Author {category}", f"Penjualan rata2 per volume(juta) {category}"]]
    st.write(filtered_df)
