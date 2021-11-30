from dt_apriltags import Detector
import sys
import os
import cv2
import numpy as np

# 
# ffmpeg -i gooddeploy.ogg -vcodec mpeg4 -qscale 0 -acodec libmp3lame my-demo-video.avi

def main(filepath):

    detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)

    cap = cv2.VideoCapture(filepath)

    if not cap.isOpened():
        print("Failed to open file!")
        return None

    while True:

        ret, frame = cap.read()

        cv2.imwrite("test.jpg", frame)

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        tags = detector.detect(gray, False)
        for tag in tags:
            cv2.line(frame, (tag.corners[0][0], tag.corners[0][1]), (tag.corners[1][0], tag.corners[1][1]), (255, 0, 0), 5)
            cv2.line(frame, (tag.corners[1][0], tag.corners[1][1]), (tag.corners[2][0], tag.corners[2][1]), (255, 0, 0), 5)
            cv2.line(frame, (tag.corners[2][0], tag.corners[2][1]), (tag.corners[3][0], tag.corners[3][1]), (255, 0, 0), 5)
            cv2.line(frame, (tag.corners[3][0], tag.corners[3][1]), (tag.corners[0][0], tag.corners[0][1]), (255, 0, 0), 5)


            cv2.putText(frame, str(tag.tag_id),
                        org=(tag.corners[0, 0].astype(int),tag.corners[0, 1].astype(int)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=(0, 0, 255))


            cv2.imshow("Frame", frame)












if __name__ == "__main__":
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py /home/user/path/to/video/file")
        exit(-1)

    path = os.path.abspath(sys.argv[1])
    if not os.path.isfile(path):
        print("Must input valid file!")
        exit(-1)

    """

    path = "/home/gstrenge/Projects/apriltag-bounding-box/gooddeploy4.avi"
    main(path)

