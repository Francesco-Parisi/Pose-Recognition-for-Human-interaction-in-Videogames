import face_alignment
import matplotlib.pyplot as plt
from skimage import io
import collections
import socket
import time
import math
import cv2
import re

# String formatting
def man_string(string):
    string += '&'
    string = re.sub(r'\s+', ' ', string)
    string = string.strip()
    return string

# Calculation of three-dimensional distance between points
def Distance(a, b, preds, predt):
    x = pow(preds[a][0] - predt[b][0], 2)
    y = pow(preds[a][1] - predt[b][1], 2)
    z = pow(preds[a][2] - predt[b][2], 2)
    p = x + y + z
    rp = math.sqrt(p)
    if (rp > 0):
        print("Dot Distance " + str(a+1) + ": " + str(rp))


# Run the 3D face alignment on a test image, without CUDA.
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0
ListImage = []

while True:
    ret, img = cam.read()
    cv2.imshow("ImageCapture", img)
    if not ret:
        break
    k=cv2.waitKey(2)
    if k%256 == 27:
        break
    else:
        print("Image "+str(count)+" saved...")
        path='../test/assets/'+str(count)+'.jpg'
        cv2.imwrite(path, img)
        ListImage.append(path)
        time.sleep(1)
        count +=1
cam.release()
cv2.destroyAllWindows()

l = 0
while l<len(ListImage):
    try:
        print("Avvio Rilevamento Volto n."+str(l))
        input_img = io.imread(ListImage[l])
    except FileNotFoundError:
        input_img = io.imread('../test/assets/aflw-test.jpg')

    preds = fa.get_landmarks(input_img)[-1]

    # 2D-Plot
    plot_style = dict(marker='o',
                      markersize=4,
                      linestyle='-',
                      lw=2)

    pred_type = collections.namedtuple('prediction_type', ['slice', 'color'])
    pred_types = {'face': pred_type(slice(0, 17), (0.682, 0.780, 0.909, 0.5)),
                  'eyebrow1': pred_type(slice(17, 22), (1.0, 0.498, 0.055, 0.4)),
                  'eyebrow2': pred_type(slice(22, 27), (1.0, 0.498, 0.055, 0.4)),
                  'nose': pred_type(slice(27, 31), (0.345, 0.239, 0.443, 0.4)),
                  'nostril': pred_type(slice(31, 36), (0.345, 0.239, 0.443, 0.4)),
                  'eye1': pred_type(slice(36, 42), (0.596, 0.875, 0.541, 0.3)),
                  'eye2': pred_type(slice(42, 48), (0.596, 0.875, 0.541, 0.3)),
                  'lips': pred_type(slice(48, 60), (0.596, 0.875, 0.541, 0.3)),
                  'teeth': pred_type(slice(60, 68), (0.596, 0.875, 0.541, 0.4))
                  }

    fig = plt.figure(figsize=plt.figaspect(.5))
    ax = fig.add_subplot(1, 2, 1)
    ax.imshow(input_img)

    for pred_type in pred_types.values():
        ax.plot(preds[pred_type.slice, 0],
                preds[pred_type.slice, 1],
                color=pred_type.color, **plot_style)


    ax.axis('off')

    # 3D-Plot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    surf = ax.scatter(preds[:, 0] * 1.2,
                      preds[:, 1],
                      preds[:, 2],
                      c='cyan',
                      alpha=1.0,
                      edgecolor='b')


    for pred_type in pred_types.values():
        ax.plot3D(preds[pred_type.slice, 0] * 1.2,
                  preds[pred_type.slice, 1],
                  preds[pred_type.slice, 2], color='blue')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 13000))
        i = 0
        while i < len(preds):
            string = re.sub('[^A-Za-z0-9 .\-+\']+', '', str(preds[i]))
            msg = bytes(man_string(string), 'utf-8')
            s.sendall(msg)
            time.sleep(0.2)
            i = i + 1
        l = l + 1
        s.shutdown(socket.SHUT_RDWR)
        s.close()

ax.view_init(elev=90., azim=90.)
ax.set_xlim(ax.get_xlim()[::-1])
plt.show()