from django.shortcuts import render

# import pytesseract to convert text in image to string
import pytesseract

from .forms import ImageForm
import os

# import Image from PIL to read image
from PIL import Image as P_Image

from django.conf import settings

from django.views import View
from django.http import HttpResponse
from .models import Image


# Create your views here.

class OcrIndex(View):

    def get(self,request):
        form = ImageForm()
        context = {
            'form':form
        }
        return render(request,'index.html',context)
    
    def post(self,request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                
                image = request.FILES['image']
                img = Image.objects.create(image=image)
                img_path = img.image.path
                # you need to install tesseract before this
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                text = pytesseract.image_to_string(P_Image.open(img_path))
                text = text.encode("ascii", "ignore")
                text = text.decode()

                os.remove(img_path) 
                

            except Exception as e:
                print(e)
                text = str(e)
            
            return HttpResponse(text)
            



