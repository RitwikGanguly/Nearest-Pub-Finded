import streamlit as st
from matplotlib import image
import os
import time
import pickle
import pandas as pd
import numpy as np
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

data_path = os.path.join(dir_of_interest, "data", "Cleaned_data.csv")

df = pd.read_csv(data_path)
IMAGE_PATH = os.path.join(dir_of_interest, "images", "nearest.jpeg")
# Image section of Laptop


st.set_page_config(page_title="FindTheNearestPub",
                   page_icon="📍",
                   layout="wide"
)

st.markdown("<h1 style='text-align: center; color: yellow;'>📌 Nearest Pub Finder 🗺️</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: greenyellow;'>🍺 Top 5 Pubs Near You 🍺</h2>", unsafe_allow_html=True)
st.markdown("<b><h4 style='text-align: center; color: red;'>🌍 The time has gone to rely only on Google Maps for Your Pubs 🌐</h4></b>", unsafe_allow_html=True)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/1267363/pexels-photo-1267363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
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
    st.image(img, width=400, caption="Keep Calm!!! Know your pub ")

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: chocolate;'>🧑‍💻 The Input Section 👩‍💻</h2>", unsafe_allow_html=True)
error_msg1 = f"Latitude value must be between 49.892485 and 60.764969."
lat = st.number_input("Enter Your Latitude:", min_value=49.892485, max_value=60.764969, step=0.000001, format="%.6f")

if not 49.892485 <= lat <= 60.764969:
    st.error(error_msg1)
error_msg2 = f"Latitude value must be between -7.384525 and 1.757763."
long = st.number_input("Enter Your Longitude:", min_value=-7.384525, max_value=1.757763, step=0.000001, format="%.6f")

if not -7.384525 <= long <= 1.757763:
    st.error(error_msg2)

st.markdown("<b><h7 style='text-align: center; color: tomato;'>1) After entering the values please press the Enter ⎆ key 🤔</h7></b>", unsafe_allow_html=True)
st.markdown("<b><h7 style='text-align: center; color: tomato;'>2) If Error occured i.e. the value is beyond of the renge then please currect that before entering further, this is because "
            "we are predicting that you are near about UK that's why you are finding the pubs near UK 😂😂</h7></b>", unsafe_allow_html=True)



ans = np.array((lat, long))

arr = np.transpose(np.array([df.latitude, df.longitude]))

dis = np.sqrt(np.sum((arr-ans)**2, axis=1))

dis = dis.tolist()

newdis = [round(i, 4) for i in dis]

df["Distance"] = newdis

top_5_pubs = df.sort_values(by='Distance').head(5)

st.markdown("<h4 style='text-align: center; color: orange;'>🤖 Hurrah‼️We found the 5 Nearest Pubs from your location 🤖</h4>", unsafe_allow_html=True)
butt = st.button("Do You Wanna SEE 🤩")
if butt:
    st.markdown(
        "<h5 style='text-align: center; color: violet;'>The List of 5 Nearest Pub 🍷>",
        unsafe_allow_html=True)
    rg = top_5_pubs[["name", "postcode", "latitude", "longitude", "local_authority", "Distance"]]
    st.dataframe(rg)
    m = folium.Map(location=[lat, long], zoom_start=13)
    folium.Marker(location=[lat, long], icon=folium.Icon(icon='star', color='red'), popup='Your Location').add_to(m)

    for i, row in top_5_pubs.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<strong>{row['name']}</strong><br>{row['postcode']}<br>{row['address']}<br>{row['Distance']} kelometers away",
            icon=folium.Icon(icon='beer', prefix='fa', color='green')
        ).add_to(m)

    folium_static(m)
    st.markdown(
        "<h5 style = 'color: indigo;'> 1) Squeeze/zoom out the map to view the all of your nearest pubs</h5>",
        unsafe_allow_html=True)
    st.markdown(
        "<h5 style = 'color: indigo;'> 2) Tap on the green pin to view the info regarding the Pubs and its address</h5>",
        unsafe_allow_html=True)










st.subheader("Hope You Enjoyed 🙄🙄")




