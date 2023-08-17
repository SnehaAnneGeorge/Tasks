import cv2

input_video_path = 'testVideo.mp4'
cap = cv2.VideoCapture(input_video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video_path = 'output_slow_reverse_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

slow_factor = 4 
for frame in frames[::-1]:
    for _ in range(slow_factor):
        out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()


