import torch
import torchvision
from torchvision import transforms as T

from PIL import Image
import cv2
model = torchvision.models.detection.ssd300_vgg16(pretained = True)
model.eval()
!wget 'http://images.cocodataset.org/val2017/000000037777.jpg'
from google.colab.patches import cv2_imshow
ig = Image.open("/content/000000037777.jpg")
with torch.no_grad():
   pred = model([img])
pred[0].keys()
num = torch.argwhere(scores > 0.5).shape[0]
num = torch.argwhere(scores > 0.5).shape[0]
    igg = cv2.imread("/content/000000037777.jpg")
for i in range(num):
  x1 , y1 , x2 , y2 = bboxes[i].numpy().astype("int")
  igg = cv2.rectangle(igg , (x1 , y1) , (x2 , y2) , (0, 255, 0) , 1)
  class_name = coco_names[labels.numpy()[i] - 1] 
  igg = cv2.putText(igg , class_name , (x1 , y1 - 10) , font , 0.5 , (255 , 0 , 0) , 1 , cv2.LINE_AA)
cv2_imshow(igg)
