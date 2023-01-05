import cv2

img = cv2.imread('solar-system.jpg')
font = cv2.FONT_HERSHEY_COMPLEX
color = (255, 255, 255)
thickness = 0.5




cv2.putText(img,'Sun',(50,300),font,thickness,color)
cv2.putText(img, 'Mercury', (100, 150), font, thickness, color)
cv2.putText(img, 'Venus', (200, 150), font, thickness, color)
cv2.putText(img, 'Earth', (300, 150), font, thickness, color)
cv2.putText(img, 'Mars', (400, 150), font, thickness, color)
cv2.putText(img, 'Jupiter', (500, 150), font, thickness, color)
cv2.putText(img, 'Saturn', (700, 150), font, thickness, color)
cv2.putText(img, 'Uranus', (900, 150), font, thickness, color)
cv2.putText(img, 'Neptune', (1100, 150), font, thickness, color)
cv2.imshow('Solar-system.jpg', img)
cv2.waitKey(0)
