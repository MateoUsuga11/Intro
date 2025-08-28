import streamlit as st
from PIL import Image

st.title("Dark Souls")

st.header("Oscar De Astora")
st.write("un caballero de alto rango de Astora, dispuesto de buscar en Lordran una vez que se volvió un no muerto")
image = Image.open('%3Fscar.webp')

st.image(image, caption='Oscar De Astora')
