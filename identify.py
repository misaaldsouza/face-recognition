import tkinter as tk
import face_recognition
from PIL import Image, ImageDraw

image_of_albert = face_recognition.load_image_file('./img/known/Albert Einstein.jpg')
albert_face_encoding = face_recognition.face_encodings(image_of_albert)[0]

image_of_alexander = face_recognition.load_image_file('./img/known/Srinivasa Ramanujan.jpg')
alexander_face_encoding = face_recognition.face_encodings(image_of_alexander)[0]

image_of_kalam = face_recognition.load_image_file('./img/known/APJ Abdul Kalam.jpg')
kalam_face_encoding = face_recognition.face_encodings(image_of_kalam)[0]

image_of_raman = face_recognition.load_image_file('./img/known/CV Raman.jpg')
raman_face_encoding = face_recognition.face_encodings(image_of_raman)[0]

image_of_galileo = face_recognition.load_image_file('./img/known/Galileo.jpg')
galileo_face_encoding = face_recognition.face_encodings(image_of_galileo)[0]

image_of_newton = face_recognition.load_image_file('./img/known/Isaac Newton.jpg')
newton_face_encoding = face_recognition.face_encodings(image_of_newton)[0]

image_of_marie = face_recognition.load_image_file('./img/known/Marie Curie.jpg')
marie_face_encoding = face_recognition.face_encodings(image_of_marie)[0]

image_of_thomas = face_recognition.load_image_file('./img/known/Thomas Edison.jpg')
thomas_face_encoding = face_recognition.face_encodings(image_of_thomas)[0]

image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

image_of_elon = face_recognition.load_image_file('./img/known/Elon Musk.jpg')
elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

#  Create arrays of encodings and names
known_face_encodings = [albert_face_encoding,
                        alexander_face_encoding,
                        kalam_face_encoding,
                        raman_face_encoding,
                        galileo_face_encoding,
                        newton_face_encoding,
                        marie_face_encoding,
                        thomas_face_encoding,
                        bill_face_encoding,
                        steve_face_encoding,
                        elon_face_encoding
                        ]

known_face_names = ["Albert Einstein",
                    "Alexander Graham Bell",
                    "APJ Abdul Kalam",
                    "CV Raman",
                    "Galileo",
                    "Isaac Newton",
                    "Marie Curie",
                    "Thomas Edison",
                    "Bill Gates",
                    "Steve Jobs",
                    "Elon Musk"
                    ]

# Load test image to find faces in
address=[]
n=int(input("\nHow many images do you want to scan: "))
for i in range(n):
  c=input("Image Address: ")
  address.append(f'./img/groups/{c}.jpg')
for i in range(0,len(address)):
  test_image = face_recognition.load_image_file(address[i])

# Find faces in test image
  face_locations = face_recognition.face_locations(test_image)
  face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
  pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
  draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
  for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown\nPerson"

  # If match
    if True in matches:
      first_match_index = matches.index(True)
      name = known_face_names[first_match_index]
  
  # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

  del draw

# Display image
  pil_image.show()

# Save image
  pil_image.save('identify.jpg')