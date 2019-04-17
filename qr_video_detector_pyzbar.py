import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import sys
import time

def draw_detections(img, qr_code):
    """Draws the detection bounding boxes of QR codes in an image.

    Args:
        img (ndarray): OpenCV original image with some QR codes in it.
        qr_code (pyzbar.Decoded): Info related to the QR code detected.

    Returns:
        result_img (ndarray): OpenCV image with the detection boxes drawn.

    """
    x_min = qr_code.rect[0]
    y_min = qr_code.rect[1]
    x_max = qr_code.rect[2] + x_min
    y_max = qr_code.rect[3] + y_min
    result_img = cv2.rectangle(img, (x_min,y_min), (x_max,y_max), (0,255,0), 3)

    return result_img

def main():
    video = cv2.VideoCapture(1)
    # Video loop
    try:
        while video.isOpened():
            _, frame = video.read()
            frame = cv2.resize(frame, (400, 400))
            qr_codes = decode(frame, symbols=[ZBarSymbol.QRCODE])
            # Iterate through every detected QR code
            for qr_code in qr_codes:
                frame = draw_detections(frame, qr_code)
                print(qr_code)
            cv2.imshow("Detections", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:   
        pass

    print("Ending resources")
    video.release()
    cv2.destroyAllWindows()
    sys.exit()

if __name__ == '__main__':
    main()
