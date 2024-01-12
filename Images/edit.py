import os
#from logger import logger
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
from typing import Optional


iamge_path = '/home/kerod/Desktop/week_5/Algorand-NFTs-certificate/Images/image_2.png'

background_image = cv2.imread(iamge_path, cv2.IMREAD_UNCHANGED)

# Convert the background to a PIL Image
background_pil = Image.fromarray(cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(background_pil)

# Define font size and color
font_large = ImageFont.load_default()  # Adjust as needed
font_medium = ImageFont.load_default()  # Adjust as needed
font_color = (255, 255, 255)

# Add text to the certificate
draw.text((120, 100), 'Certificate of Completion', font=font_large, fill=font_color)
draw.text((120, 200), 'This certifies that', font=font_medium, fill=font_color)
draw.text((120, 300), 'Kerod Sisay', font=font_large, fill=font_color)
draw.text((120, 400), 'Has successfully completed the', font=font_medium, fill=font_color)
draw.text((120, 500), 'Intensive Training', font=font_large, fill=font_color)
draw.text((120, 600), 'Date of Issue:', font=font_medium, fill=font_color)
draw.text((320, 600), 'March 2024', font=font_medium, fill=font_color)

# Paste the academy logo onto the certificate
#logo_image_pil = Image.fromarray(logo_image)
#logo_image_pil = logo_image_pil.convert("RGBA")
#background_pil.paste(logo_image_pil, (50, 50), logo_image_pil)

# Add footer text
footer_text = 'This certificate is hereby issued in recognition of the successful completion of the specified challenge. Congratulations!'
draw.text((120, 700), footer_text, font=font_medium, fill=font_color)

# Convert back to CV2 image to save or display
final_certificate = cv2.cvtColor(np.array(background_pil), cv2.COLOR_RGB2BGR)
output_path = '/home/kerod/Desktop/week_5/Algorand-NFTs-certificate/Images/final_image.png'

#output_path = '../Images/final_certificate.png'
cv2.imwrite(output_path, final_certificate)
#logger.info(f"Customized certificate saved to {output_path}")


#final_certificate = customize_certificate(full_name="Birehan Anteneh", course_name='Web3 dApps Development', date_of_issue='April 1, 2023', academy_logo_path="../images/10x_logo.png", image_url=image_url)