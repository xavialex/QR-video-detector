import cv2
import numpy as np
import sys
import time

# Display barcode and QR code location
def display(img, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(img, tuple(bbox[j][0]), tuple(bbox[(j+1) % n][0]), (255,0,0), 3)
 
    # Display results
    return img

def detect_qr(img, qrDecoder): 
    # Detect and decode the qrcode
    data, bbox, rectified_image = qrDecoder.detectAndDecode(img)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        display(img, bbox)
        rectified_image = np.uint8(rectified_image)
        return bbox, rectified_image
    else:
        print("QR Code not detected")
        cv2.imshow("Results", img)
        return None, None
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    #input_image = cv2.imread("01.jpg")
    video = cv2.VideoCapture(1)
    qrDecoder = cv2.QRCodeDetector()
    while video.isOpened():
        _, frame = video.read()
        bbox, rectified_image = detect_qr(frame, qrDecoder)
        if bbox is not None:
            detections_img = display(frame, bbox)
            cv2.imshow("Results", detections_img)
            cv2.imshow("Rectified QRCode", rectified_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()