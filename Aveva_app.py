import streamlit as st

# 1. PAGINA CONFIGURATIE
# Dit moet altijd de eerste regel code zijn (na imports)
st.set_page_config(
    page_title="Aveva BIM Dashboard",
    page_icon="🏗️",
    layout="wide"
)

# 2. ZIJBALK (Voor navigatie en info)
st.sidebar.success("Selecteer een pagina hierboven.")
st.sidebar.title("Project Info")
st.sidebar.info(
    """
    **Project:** Aveva BIM3A4
    **Status:** In ontwikkeling 🚧
    """
)
st.sidebar.title("Teamleden")
st.sidebar.write("- Student 1")
st.sidebar.write("- Student 2")
st.sidebar.write("- Student 3")

# 3. HOOFDPAGINA INHOUD
st.title("🏗️ Welkom bij het Aveva BIM Dashboard")

st.markdown("""
### Over deze applicatie
Welkom op onze projectomgeving. Deze applicatie is ontwikkeld om **Aveva exports** te analyseren en te visualiseren voor het vak BIM.

**Wat kun je hier doen?**
👈 **Gebruik het menu aan de linkerkant** om naar de verschillende tools te navigeren:
""")

# Twee kolommen voor een nette layout
col1, col2 = st.columns(2)

with col1:
    st.info("📊 **Statistieken & Data**\n\nUpload exports en bekijk directe analyses van de modeldata.")

with col2:
    st.warning("🛠️ **Tools & Checks**\n\nControleer het model op consistentie en voer validaties uit.")

st.divider()

# Een interactief elementje om te testen
st.subheader("🚀 Aan de slag")
if st.button("Klik hier als je klaar bent om te starten"):
    st.balloons()
    st.success("Laten we beginnen!)
