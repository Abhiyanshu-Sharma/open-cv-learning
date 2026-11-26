import os, cv2

base_dir = os.path.dirname(os.path.abspath(__file__))

#read image
image_path = os.path.join(base_dir, 'data', 'bird.jpg') 

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join(base_dir, 'data', 'bird_out.jpg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(3000)