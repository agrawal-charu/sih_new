from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
import pickle
import numpy as np
import tensorflow as tf
import cv2
import keras

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
def names_photo():
    names = []
    serial = ""
    img_rows = 224
    img_cols = 224
    path = "D:\\Programming World\\Hackaathon\\Full Flask\\upload\\ishika.jpg"
    img = cv2.imread(path)
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
    
    return names
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/',methods=['GET','POST'])
def myApp():
    return render_template('homepage.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    return render_template('list.html',names=names_photo())

@app.route('/upload',methods=['GET','POST'])
def uploadFile():
    img = request.files['img']
    imgname = secure_filename("ishika."+img.filename.split(".")[-1:][0] )
    img.save(os.path.join(app.config['UPLOAD_FOLDER'],imgname))
    return render_template('homepage.html')
    
@app.route('/results/<attendees>')
def showAttendace(attendees):
    dict = eval(attendees)
    print(dict)
    return "T"

if __name__ == '__main__':
   app.run(debug =True)