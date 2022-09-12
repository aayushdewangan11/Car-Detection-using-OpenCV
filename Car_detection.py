import cv2

cap = cv2.VideoCapture("C:\\Users\\aayus\\Downloads\\Video\\Traffic - 20581.mp4")

car_cascade = cv2.CascadeClassifier("C:\\Users\\aayus\\Downloads\\haarcascade_car.xml")

while True:
    respose, color_img = cap.read()
    
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray_img, 1.1,1)
    
    
    i = 0
    for (x,y,w,h) in cars:
        if i%2 ==0:
            cv2.rectangle(color_img,(x,y),(x+w,y+h),(0,0,255),3)
            i += 1
        else:
            cv2.rectangle(color_img, (x,y), (x+w, y+h), (0,255, 0), 3)
            i += 1
    
    
    cv2.imshow('Image', color_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()
