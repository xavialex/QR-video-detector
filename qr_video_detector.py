from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(img) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(img)

  # Print results
  print("{} qr codes detected".format(len(decodedObjects)))
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
    
  return decodedObjects


# Display barcode and QR code location  
def display(img, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points
    
    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(img, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Display results 
  cv2.imshow("Results", img)
  cv2.waitKey(0)

  
# Main 
if __name__ == '__main__':

  # Read image
  img = cv2.imread('zbar-test.jpg')

  decodedObjects = decode(img)
  display(img, decodedObjects)

#   video = cv2.VideoCapture(0)
#   while video.isOpened():
#       _, frame = video.read()
#       decodedObjects = decode(frame)
#       display(frame, decodedObjects)

#       if cv2.waitKey(1) & 0xFF == ord('q'):
#         break