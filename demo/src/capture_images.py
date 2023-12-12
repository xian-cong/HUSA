import cv2
import os

name = 'Kelly'  # replace with your name

# Create the directory if it doesn't exist
save_dir = "dataset/" + name + "/"
os.makedirs(save_dir, exist_ok=True)

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = save_dir + "image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        print("Image saved to:", os.path.abspath(img_name))

        img_counter += 1

cam.release()
cv2.destroyAllWindows()
