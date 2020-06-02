from mtcnn import MTCNN
import cv2
from os import listdir
from os.path import isfile, join, isdir, basename
import pprint
import csv

myPath = "./test"
directories = [join(myPath, d) for d in listdir(myPath) if isdir(join(myPath, d))]

pp = pprint.PrettyPrinter()
faceList = []
with open('eggs.csv', 'w', newline='') as csvfile:
    spamWriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamWriter.writerow(['filename', 'subject_id', 'xmin', 'ymin', 'width', 'height'])

detector = MTCNN()
for directory in directories:
    images = [f for f in listdir(directory) if isfile(join(directory, f))]
    for imageFile in images:
        subjectID = basename(directory).replace("n", "")
        fileName = imageFile
        print(imageFile)
        img = cv2.cvtColor(cv2.imread(directory + "/" + imageFile), cv2.COLOR_BGR2RGB)
        faceData = detector.detect_faces(img)
        print(faceData)
        if len(faceData) == 0:
            continue
        box = faceData[0]['box']
        face = {
            'filename': fileName,
            'subject_id': subjectID,
            'xmin': box[0],
            'ymin': box[1],
            'width': box[2],
            'height': box[3]
        }
        with open("eggs.csv", 'a', newline='') as csvfile:
            spamWriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamWriter.writerow(face.values())
        # row = face.keys()
        # rowValue = face.values()
        # faceList.append({
        #     'filename': fileName,
        #     'subject_id': subjectID,
        #     'xmin': box[0],
        #     'ymin': box[1],
        #     'width': box[2],
        #     'height': box[3]
        # })
#
# # faceList = [face for face in faceList if len(face) != 0]
# pp = pprint.PrettyPrinter()
# pp.pprint(faceList)
