import cv2
import numpy as np
import time

def pixel_to_ascii(pixel_intensity):
    ASCII_CHARS = "   ._-=+*!&#%$@"
    return ASCII_CHARS[pixel_intensity * len(ASCII_CHARS) // 256]

def main():
    video_path = "LoyKrathongVDO.mp4"  
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)

    frame_duration_ms = 1000 / fps

    width = 250
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(frame_width, frame_height)

    height = int((width * frame_height / frame_width) * 0.4194)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, (width, height), interpolation=cv2.INTER_LINEAR)

        ascii_frame = ""
        for i in range(height):
            for j in range(width):
                ascii_frame += pixel_to_ascii(resized_frame[i, j])
            ascii_frame += "\n"

        print("\033c", end="")  
        print(ascii_frame)
        time.sleep(frame_duration_ms / 1000)

    cap.release()

if __name__ == "__main__":
    main()
