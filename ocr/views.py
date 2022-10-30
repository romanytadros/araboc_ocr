import base64
import os

import numpy as np
import pytesseract
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from django.http import FileResponse, HttpResponse, JsonResponse
from ast import literal_eval
import json
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
# you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
# )


# pytesseract.pytesseract.tesseract_cmd = (
#     'tesseract'
# )


# @csrf_exempt
# @ensure_csrf_cookie
def homepage(request):
    img1=''
    img2=''
    img3=''
    img4=''
    img5=''
    txt1=''
    txt2=''
    txt3=''
    txt4=''
    txt5=''
    imgcount=0
    allinfo=[]

    if request.method == "POST":
        # try:
        print('ok')
        image = request.FILES.getlist("finalimg")
        # encode image to base64 string
        i=0
        
        for imgw in image:
            i=i+1
            imgcount+=1
            if i==1:
                img1=(base64.b64encode(imgw.read()).decode("utf-8"))
            if i==2:
                img2=(base64.b64encode(imgw.read()).decode("utf-8"))
            if i==3:
                img3=(base64.b64encode(imgw.read()).decode("utf-8"))
            if i==4:
                img4=(base64.b64encode(imgw.read()).decode("utf-8"))
            if i==5:
                img5=(base64.b64encode(imgw.read()).decode("utf-8"))
            
            # globals()[f"img{i}"] ="ffffffff"    #(base64.b64encode(imgw.read()).decode("utf-8"))  
            # # print(type(img1))
            
        # except:
        #     messages.add_message(
        #         request, messages.ERROR, "No image selected or uploaded"
        #     )
            # return render(request, "index.html")
        # lang = request.POST["language"]
        ii=0
        for imgws in image :
            ii+=1
            if ii==1:
                img = np.array(Image.open(imgws))
                text = pytesseract.image_to_string(img, lang='ara')
                txt1=text
            if ii==2:
                img = np.array(Image.open(imgws))
                text = pytesseract.image_to_string(img, lang='ara')
                txt2=text
            if ii==3:
                img = np.array(Image.open(imgws))
                text = pytesseract.image_to_string(img, lang='ara')
                txt3=text
            if ii==4:
                img = np.array(Image.open(imgws))
                text = pytesseract.image_to_string(img, lang='ara')
                txt4=text
            if ii==5:
                img = np.array(Image.open(imgws))
                text = pytesseract.image_to_string(img, lang='ara')
                txt5=text
        myinfo=zip([img1,img2,img3,img4,img5],[txt1,txt2,txt3,txt4,txt5])
        # return text to html
        return render(request, "index.html", {"imageaa":myinfo})
    
    
     
        

    return render(request, "index.html")

def webmains(request):
    return render(request, "index.html")
