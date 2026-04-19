import cv2
import numpy as np
# Start webcam
cap = cv2.VideoCapture(0)

# Color ranges (HSV)
colors = {
    "blue": ([100, 60, 60], [140, 255, 255], (255, 0, 0)),
    "green": ([40, 70, 70], [80, 255, 255], (0, 255, 0)),
    "red": ([0, 120, 70], [10, 255, 255], (0, 0, 255))
}

current_color = "blue"
canvas = None
prev_x, prev_y = 0, 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # UI Buttons
    cv2.rectangle(frame, (0, 0), (100, 50), (255, 0, 0), -1)    # Blue
    cv2.rectangle(frame, (100, 0), (200, 50), (0, 255, 0), -1)  # Green
    cv2.rectangle(frame, (200, 0), (300, 50), (0, 0, 255), -1)  # Red
    cv2.rectangle(frame, (300, 0), (400, 50), (0, 0, 0), -1)    # Erase
    cv2.rectangle(frame, (400, 0), (500, 50), (255, 255, 255), -1)  # Clear

    # Get selected color range
    if current_color in colors:
        lower, upper, draw_color = colors[current_color]
    else:
        lower, upper = colors["blue"][0], colors["blue"][1]
        draw_color = (255, 0, 0)

    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)

        if cv2.contourArea(c) > 1000:
            x, y, w, h = cv2.boundingRect(c)
            cx, cy = x + w // 2, y + h // 2

            # Draw tracking dot
            cv2.circle(frame, (cx, cy), 10, (255, 255, 255), -1)

            # Button click detection
            if cy < 50:
                if cx < 100:
                    current_color = "blue"
                elif cx < 200:
                    current_color = "green"
                elif cx < 300:
                    current_color = "red"
                elif cx < 400:
                    current_color = "erase"
                elif cx < 500:
                    canvas = np.zeros_like(frame)
            else:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = cx, cy

                if current_color == "erase":
                    cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0, 0, 0), 20)
                else:
                    cv2.line(canvas, (prev_x, prev_y), (cx, cy), draw_color, 5)

                prev_x, prev_y = cx, cy
    else:
        prev_x, prev_y = 0, 0

    # Merge canvas and frame
    combined = cv2.add(frame, canvas)

    cv2.imshow("AirCanvas AI", combined)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
