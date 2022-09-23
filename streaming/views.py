from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
from rest_framework.response import Response
import cv2 ,time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
     "haarcascade_frontalface_default.xml")

def get_frame():
	while True:
		ret, frame = cap.read()
		if ret:
		   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		   (flag, encodedImage) = cv2.imencode(".jpg", frame)
		   if not flag:
		        continue
		   yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
		        bytearray(encodedImage) + b'\r\n')

def index(request):
	return render(request,'index.html')

@gzip.gzip_page
def dynamic_stream(request):
    try :
        return StreamingHttpResponse(get_frame(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"

