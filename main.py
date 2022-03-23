import tensorflow as tf
#from tensorflow.keras.applications import 
import cv2
import keras
import numpy as np
from PIL import Image


def names_photo():
    names = []
    serial = ""
    img_rows = 224
    img_cols = 224
    path = 'D:\\Programming World\\Hackaathon\\Full Flask\\upload\\ishika.jpg'
    img = cv2.imread(path)
    #img = cv2.imread("Ishika.jpg")
    img = cv2.resize(img,(img_rows,img_cols))     # resize image to match model's expected sizing
    img = img.reshape(1,img_rows,img_cols,3)

    #image = cv2.resize(image,(img_rows,img_cols))
    model = keras.models.load_model("face_rec.h5")
    for (i,layer) in enumerate(model.layers):
        print(str(i) + " "+ layer.__class__.__name__, layer.trainable)
    #image.shape
    print(model.predict(img))
    predict = model.predict(img)
    #print(np.argmax(predict))
    if np.argmax(predict) == 0:
        print("Ishika")
        names.append("Ishika")
    elif np.argmax(predict) ==1:
        print("Deepan")
        names.append("Deepan")
    
    for name in names:
        serial=serial+str(name)
        serial=serial+"$"
    print(names)
    
    return serial
#cv2.imshow("image",img)
print(names_photo())