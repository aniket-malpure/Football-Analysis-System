import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        # ret refers to the flag referring to whether there is a frame or the video has ended
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    # Defining the output format
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # The output will have VideoWriter with output video path, its format, 
    # no. of frames per second, width and height of each frame
    out = cv2.VideoWriter(output_video_path, fourcc, 24, 
                          (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()