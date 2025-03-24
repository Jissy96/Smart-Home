import cv2

cap = cv2.VideoCapture(0)  # Open camera

while True:
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)  # Show image

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
