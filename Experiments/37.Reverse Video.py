import cv2

video = cv2.VideoCapture(r"C:\Users\yaswa\Downloads\sample-10s.mp4")

frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

# Play video in reverse
for frame in reversed(frames):

    # Resize video frame
    frame = cv2.resize(frame, (640, 480))

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
