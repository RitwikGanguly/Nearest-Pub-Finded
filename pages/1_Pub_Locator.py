import streamlit as st
from matplotlib import image
import os
import time
import pickle
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import plotly.express as px


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub_front.jpg")


st.set_page_config(page_title="PubLocator",
                   page_icon="🍺",
                   layout="wide"
)
st.markdown("<h1 style='text-align: center; color: violet;'>Know Nearest Pub in UK</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: cyan;'>Enjoy Your Drink 🤠</h2>", unsafe_allow_html=True)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/2680270/pexels-photo-2680270.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: cover;
background-position: top center;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
img = image.imread(IMAGE_PATH)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image(img, width=400, caption="It's PUB, it's relief 😋")

with col3:
    st.write(' ')


data_path = os.path.join(dir_of_interest, "data", "Cleaned_data.csv")


df = pd.read_csv(data_path)

def uk_bar(a):
    st.markdown("<h4 style='text-align: center; color: red;'>📊 Now It's the time to another Viz 📊</h4>",
                unsafe_allow_html=True)
    bar = df[a].value_counts()[:10]
    fig = px.bar(df, x=bar.index, y=bar.values, color=bar.index)
    fig.update_layout(
        title="<b> Numbers of Pubs in {} Wise (TOP 10) </b>".format(a),
        xaxis_title="{}s".format(a),
        yaxis_title="Count of Pubs",
        legend_title="{}".format(a),
        paper_bgcolor="lightgreen",
        plot_bgcolor="cyan"

    )
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Visit the next page for Your Nearest Pub Finder 🗺️")



st.markdown("<h2 style='text-align: center; color: red;'>🧑‍💻 The Input Section 👩‍💻</h2>", unsafe_allow_html=True)
option = st.radio(label="💫 What Option Do You Have, to Find Your Pubs 💫",
                options=["name", "postcode", "local_authority"], horizontal=False)
def uk_viz(a, b):
    num = df[df[a] == b]
    st.markdown("<span style='text-align: center; color: yellow;'>**There are total ${}$ Pubs available at Your entered {} {}**</span>".format(len(num), a, b), unsafe_allow_html=True)
    m = folium.Map(location=[num.latitude.mean(), num.longitude.mean()], zoom_start=13)
    folium.Marker(location=[num.latitude.mean(), num.longitude.mean()], icon=folium.Icon(icon='star', color='red'),
                  popup='Your Location', size=155).add_to(m)

    for i, row in num.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<strong>{row['name']}</strong><br>{row['postcode']}<br> address is - <br>{row['address']}",
            icon=folium.Icon(icon='beer', prefix='fa', color='green')
        ).add_to(m)

    st.subheader("🍹 Now See the Pubs on Map and find where You wanna go 🍷")
    st.markdown("<b><h5 style='color: yellow;'>Your Entered {} - {}</h5></b>".format(a, b), unsafe_allow_html=True)
    folium_static(m)
    st.markdown("<h6 style = 'color: yellow;'> 1) Squeeze/zoom out the map to view the all of your pubs located in your choice</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style = 'color: yellow;'> 2) Tap on the green pin to view the info regarding the Pubs and its address</h6>", unsafe_allow_html=True)




if option == "name":
    loc = df["name"].unique()
    st.markdown("<h2 style='text-align: center; color: red;'>🍻 KNOW the Pubs PubName-wise 🍻</h2>", unsafe_allow_html=True)
    locality = st.selectbox("📩 select the Pub Name to find Your Desired PUB 💌:- ", loc)
    st.write(":red[Wanna See The VIZ 🤩]")
    butt = st.button("Yeah ‼")
    if butt:

        uk_viz("name", locality)

        uk_bar("name")




elif option == "postcode":
    loc = df["postcode"].unique()
    st.markdown("<h2 style='text-align: center; color: red;'>🍻 KNOW the Pubs Postal Code-wise 🍻</h2>",
                unsafe_allow_html=True)
    locality = st.selectbox("👉 select the Postal Code to find Your Desired PUB 💌:- ", loc)
    st.write(":red[Wanna See The VIZ 🤩]")
    butt = st.button("Yeah ‼")
    if butt:
        uk_viz("postcode", locality)
        uk_bar("postcode")

elif option == "local_authority":
    loc = df["local_authority"].unique()
    st.markdown("<h2 style='text-align: center; color: red;'>🍻 KNOW the Pubs locality-wise 🍻</h2>",
                unsafe_allow_html=True)
    locality = st.selectbox("👉 select the Locality to find Your Desired PUB 💌:- ", loc)
    st.write(":red[Wanna See The VIZ 🤩]")
    butt = st.button("Yeah ‼")
    if butt:
        uk_viz("local_authority", locality)
        uk_bar("local_authority")




















