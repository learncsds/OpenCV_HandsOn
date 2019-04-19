import cv2

img = cv2.imread('lena.jpg')
print(img[0,0,0])
B,G,R = img[0,0]

print(B, G, R)
print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
print(gray)