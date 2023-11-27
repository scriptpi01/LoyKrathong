# Loy Krathong ASCII Video Converter

## Project Overview
This Python script transforms any video into a real-time ASCII art display, specifically designed to celebrate the Thai festival of Loy Krathong. By converting video frames into ASCII characters, it creates a unique and culturally resonant way to engage with this traditional festival.

## Features
- **Video to ASCII Conversion:** Transforms each frame of the video into ASCII art in real-time.
- **Custom ASCII Characters:** Utilizes a set of ASCII characters to best represent different shades of gray.
- **Frame Rate Control:** Syncs ASCII display with the original video's frame rate for a smooth viewing experience.
- **Dynamic Resizing:** Automatically adjusts the size of the ASCII output based on the video's dimensions.

## Requirements
- Python 3.x
- OpenCV (`cv2`) Python library
- NumPy Python library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install necessary Python libraries:
pip install opencv-python numpy

markdown
Copy code

## Usage
1. Place the video file you wish to convert into the same directory as the script. Rename it to `LoyKrathongVDO.mp4` or modify the `video_path` variable in the script.
2. Run the script:
python ascii_video_converter.py

yaml
Copy code
3. Watch as your video is transformed into a stream of ASCII art in real-time.

## Customization
- **ASCII Characters:** Modify the `ASCII_CHARS` string in the `pixel_to_ascii` function to change the ASCII characters used.
- **Output Dimensions:** Adjust the `width` variable to scale the ASCII output. The height is automatically adjusted to maintain aspect ratio.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is open-source and available under the MIT License.

---

Celebrate Loy Krathong in a novel digital way with this Python ASCII video converter. Enjoy the festival of lights uniquely! 🏮✨
