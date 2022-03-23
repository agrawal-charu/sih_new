import cv2
coordinates = []
cropped_images = []  
face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.imread("GroupPhoto.jpg")
#cap = cv2.resize(cap, (0, 0), fx = 0.8, fy = 0.8)
#gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
faces = face_detection.detectMultiScale(cap,1.1,4)
    
img_id = 0
#drawing the contours
for (x,y,w,h) in faces:
    #cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)
    coordinates.append([x,y,w,h])    
cv2.imshow('img',cap)
print(coordinates)
for i in coordinates:
    img_id +=1
    print(i[0],i[1],i[2],i[3])
    new_image = cap[i[1]-(int)(i[3]*0.25):(i[1]+i[3]),i[0]:(i[0]+i[2]+int(i[2]*0.25))]
    cropped_images.append(new_image)    
    #face = cv2.resize(new_image, (200,200))
    #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    file_name_path = "D:\Programming World\Hackaathon\Full Flask\Cropped Images/"+str(img_id)+'.jpg'
    cv2.imwrite(file_name_path, new_image)

for k in range(len(cropped_images)):
    cv2.imshow("new",cropped_images[k])
    
cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()


