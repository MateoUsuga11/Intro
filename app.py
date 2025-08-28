import streamlit as st
from PIL import Image

st.title("Que mas mis papus")

st.header("Cómo están")
st.write("papus")
image = Image.open('fnaf-memes.gif')

st.image(image, caption='Foxy jumpscare')
