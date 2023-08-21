import cv2
import numpy as np
import math

path = 'filtered.png'
image = cv2.imread(path)

dst = cv2.Canny(image, 50, 200, None, 3)
linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]

        # Calculate the length of the line
        line_length = math.sqrt((l[2] - l[0]) ** 2 + (l[3] - l[1]) ** 2)

        # Check if the line length is above a threshold (e.g., 50 pixels)
        if line_length > 250:
            # Calculate the angle of the line
            angle_radiants = math.atan2(l[3] - l[1], l[2] - l[0])
            angle_degree = angle_radiants * 180 / math.pi

            print("line degree", angle_degree)

            if -15 < angle_degree < 15 or 165 < angle_degree < 195:
                # Dilate the line to close any gaps
                dilated_line = cv2.dilate(dst, np.ones((5, 5), np.uint8))

                # Check if the dilated line is still above the threshold
                if line_length > 250:
                    cv2.line(image, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("Source", image)

print("Press any key to close")
cv2.waitKey(0)
cv2.destroyAllWindows()
