import requests
import streamlit as st

st.title('Welcome To Image Generation AI')

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('Enter what you want:'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate'):
	st.image(image)