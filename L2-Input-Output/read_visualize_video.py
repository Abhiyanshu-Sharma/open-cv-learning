import os, cv2

base_dir = os.path.dirname(os.path.abspath(__file__))

# read video
video_path = os.path.join(base_dir, 'data', 'monkey.mp4')

video = cv2.VideoCapture(video_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        resized_frame = cv2.resize(frame, (640, 480))  # (width, height)
        cv2.imshow('frame', resized_frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):  # optional: press 'q' to quit early
            break
        
video.release()
cv2.destroyAllWindows()