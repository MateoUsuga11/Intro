import streamlit as st
from PIL import Image

st.title("Que mas mis papus")

st.header("Cómo están")
st.write("papus")
image = Image.open('%3Fscar.webp')

st.image(image, caption='Foxy jumpscare')
