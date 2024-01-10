import os
from dotenv import load_dotenv
import openai
from pathlib import Path


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

image = Path("image_2.png")

with open(image, "rb") as image_file:
    images = image_file.read() 

response = openai.images.create_variation(
  image= images,
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url

print(image_url)