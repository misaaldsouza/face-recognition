import face_recognition

image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

face_locations = face_recognition.face_locations(image)

#Array Of Co-ordinates Of Each Face
print(face_locations)
print(f'There are {len(face_locations)} people in this image')

#An Array with the locations of each facial feature in each face 
face_landmarks = face_recognition.face_landmarks(image)
print(face_landmarks)

