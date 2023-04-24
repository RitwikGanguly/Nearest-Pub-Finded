import streamlit as st
from PIL import Image
import os

from pathlib import Path


# cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# prof_pic = cur_dir / "assets" / "ricky.jpg"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "mypic.jpg"
background = cur_dir / "resources" / "images" /"cool_background.jpg"

# Description
PAGE_TITLE = "Nearest Pub Finder"
PAGE_ICON = "🗺️"
NAME = "Ritwik Ganguly"
DESCRIPTION = """
I am a CSE student, currently in 3rd year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing at every second. 
"""
EMAIL = "gangulyritwik2003@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ritwikganguly003",
    "GitHub": "https://github.com/RitwikGanguly",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/255377/pexels-photo-255377.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: cover;
background-position: top center;
}
</style>
'''


side_bgimg = '''
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/2680270/pexels-photo-2680270.jpeg?auto=compress&cs=tinysrgb&w=600");
background-size: cover;
background-position: left;
}
</style>
'''
st.sidebar.markdown(side_bgimg, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Hi!! :red[Everyone]")
st.subheader("welcome all, let's enjoy together😎😎😎😎")

# Load css, pdf and profile pic

# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Knowledge & Self-declaration ")
st.write(
    """
- ✔️ Currently a student, studied in 3rd year
- ✔️ Intermediate knowledge in python, still exploring and trying to grasp a good hand in python
- ✔️ Has understanding in data science and trying to find the hardness behind the easy word ML 
- ✔️ Has team management and problem solving capability
- ✔️ Always try to learn new things through challenges and tasks 
- ✔️ Always try to improve my task than the previous task which I did
- ✔️ Some time get confused to himself and has somewhat little patience
"""
)
st.subheader("Project Name - Nearest Pub 🍷 Finder in UK")
st.subheader("Project Requirements ...............")
st.write(
    """
- 🍿🍿 The Things are done so far for this project......
- 🏆 All the information/data are given in a .csv file
- 🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe
- 🏆 Done All the Mapping Viz by folium
- 🏆 Done other visualization task through plotly library of python
- 🏆 Finding the nearest pub by taking the euclidean distance of the user input latitude and longitude to the dataset info 📈
- 🏆 Last but not the list make the website through streamlit framework through python and deploy in 
streamlit app 🙃"

"""
)


st.subheader("👉 THE GITHUB LINK OF THIS PROJECT:-")
st.subheader("https://github.com/RitwikGanguly/Nearest-Pub-Finded")






