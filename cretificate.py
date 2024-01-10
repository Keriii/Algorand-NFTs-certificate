from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt = "create a beautiful certificate for 10 Academy with a white backgroundand and red strips. The 10 Academy trains in Web3, Data engineering, machine learning, and data science. Make the certificate simple and avoide any irrelevant components. make sure to live some space for the logo",
  #prompt="A beautiful, smart certificate background with a space for full name date and other information, Make the certificate clear and avoide any irrelevant components. use the colors red and white more than other colors",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print (image_url)