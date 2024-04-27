from pathlib import Path

import streamlit as st
from PIL import Image

#--- PATH SETTING ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Product_Ops.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"




# --- GENERAL ---
PAGE_TITLE = "Professional Curriculum Vitae | Mahardi Setyoso P."
PAGE_ICON = ":wave:"
NAME = "Mahardi Setyoso Pratomo"
DESCRIPTION = """
Product Operations and Analytical Specialist, Geospatial Analyts enthusiast, assisting enterprise by supporting data-driven decision making.
Proficient in Python, R, SQL , Geospatial and Data Analytic.

"""

EMAIL = "mahardisetyoso@gmail.com"
SOCIAL_MEDIA = {
    "LINKEDIN" : "https://www.linkedin.com/in/mahardi-setyoso-pratomo-5ab97432/",
    "GITHUB" : "https://github.com/mahardisetyoso",
    "TWITTER" : "https://twitter.com/MasMahardi",
    "DISCORD" : "https://discordapp.com/users/785121800525709324",
    "CODE BLOG" : "https://pekerjatechkomersial.netlify.app",
}

PROJECTS = {
    "📌 WebApp to convert Area into Geohash and Vice Versa (Python)" : "https://geohash-converter.streamlit.app/",
    "📌 Simple Streamlit Dashboard for Indonesia GDP per Province in Map Visualization (Python) " : "https://mahardisetyoso-streamlit-demo-hardy-app-pe8o0i.streamlit.app/",
    "📌 AIRBNB WebApp to search affordable Rent in US (R Languange)" : "https://mahardisetyoso.shinyapps.io/Shiny_AIRBNB_NYC_Mapdeck/",
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📑 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ 5 Years in Project Management and Product Operations.
    - ✅ 9 Years in Mapping and Geospatial Industry.
    - ✅ Proficient in Python, R, SQL, Openstreetmap and QGIS
    - ✅ 1.5 years experience in Sales and Business Development for Geospatial Industry.
    - ✅ Strong hands on experience and knowledge in Google Spreadsheet and Looker Studio.

    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Tech Skills")
st.write(
    """
    - 💻 Programming: Python, R, SQL, and Google Spreadsheet Formula.
    - 🌏 Geospatial Software: QGIS, Openstreetmap, JOSM, and ENVI.
    - 📊 Data Visualizations: Plotly, Seaborn, Folium, Pydeck
    - 🖥️ Web Framework: Streamlit and Shinyapps
    """
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚕", "**Product Operations - Senior Map Ops Associate | GRAB Holding**")
st.write("03/2018 - Present")    
st.write(
    """
    - 🟢 Manage POI collection from studio and vendor for Indonesia.
    - 🟢 Lead team consist of 5 - 10 members to assist POI collection, Tech Support, 
    and improve Product quality to serve Indonesia Market.
    - 🟢 Product and Tech problem solver for multiple stakeholder.
    - 🟢 Understand multiple Product feature such as POI, Navigation, Geofence and Geohash to
    solve multiple issues and improve GRAB service in multiple cities in Indonesia.
    """
)


# --- Porotofolio ---
st.write("#")
st.subheader("Product Data Analytics Portofolio")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")