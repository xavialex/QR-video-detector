import cv2
import numpy as np
import sys
import time

inputImage = cv2.imread("01.jpg")

# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[(j+1) % n][0]), (255,0,0), 3)
 
    # Display results
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector()

def detect_qr(img): 
    # Detect and decode the qrcode
    data, bbox, rectified_image = qrDecoder.detectAndDecode(img)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        display(img, bbox)
        rectified_image = np.uint8(rectified_image)
        cv2.imshow("Rectified QRCode", rectified_image)
        return bbox, rectified_image
    else:
        print("QR Code not detected")
        cv2.imshow("Results", img)
        return None, None
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    video = cv2.VideoCapture(0)
    while video.isOpened():
        _, frame = video.read()
        bbox, rectified_image = detect_qr(frame)
        if bbox is not None:
            display(frame, bbox)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()