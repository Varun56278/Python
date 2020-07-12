import cv2  
import os

def showimage():
    image = cv2.imread(r'C:\Users\varun\OneDrive\Desktop\ii.jpg') 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
    cv2.imshow('image', image) 
    cv2.imwrite(r'C:\Users\varun\OneDrive\Desktop\ii.jpg', image)





    
