from urllib import response
import uuid
import pdb
from cv2 import PSNR
#from PIL import Image
from rest_framework import status
from base64 import b64decode
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
import io
import cv2
from cv2 import imread
import numpy as np
from .models import Image_LSB,Audio_LSB
import wave
import bitarray

import base64

from django.core.cache import cache


@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': 'products/list/',
        'Detail View': 'products/detail/<str:pk>/',
        'Create': 'products/create/',
        'Create From List': 'products/create_list/',
        'Update': 'products/update/<str:pk>/',
        'Delete': 'products/delete/<str:pk>/',
        'decode':'image-decodeText/'
    }
    return Response(api_urls)



@api_view(['POST'])
def ImageEncode(request):
    #response = {}
    base64_image = request.data.get("img")
    stego_text = request.data.get("text")
    format, imgstr = base64_image.split(';base64,')
    with open("test3.jpg","wb") as f:
        f.write(b64decode(imgstr))
    
    img_name = f.name 
    
    image = Image_LSB()

    image.encode_text(img_name, stego_text, 'afterfoo.png')
    #with open("afterfoo.png", "rb") as image_file:
        #encoded_string = base64.b64encode(image_file.read())

    #response['data'] = encoded_string
    return Response("encoded")


@api_view(['GET'])
def ImagedecodeTwoLeast(request):
    response = {}
    image = Image_LSB()
    x= image.decode_text('afterlsb.png')
    response['data'] = x
    return Response(response)

@api_view(['POST'])
def ImagedecodeLeast(request):
    response = {}
    base64_image = request.data.get("img")
    format, imgstr = base64_image.split(';base64,')
    #ext = format.split('/')[-1] 
    #base64_image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    with open("foo.png","wb") as f:
        f.write(b64decode(imgstr))
    #image_64_decode = base64.b64decode(base64_image) 
    #image_result = open('deer_decode.png', 'wb') # create a writable image and write the decoding result
    #image_result.write(image_64_decode)
    image = Image_LSB()
    #image_name = "afterlsb.png"
    x= image.decode_textLeast('foo.png')
    response['data'] = x
    return Response(response)


@api_view(['POST'])
def AudioLeast(request):
    response = {}
    base64_audio = request.data.get("name")

    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(base64_audio)
    wav_file.write(decode_string)
    audio_name = wav_file.name
    music = Audio_LSB(audio_name)
    x=music.decode()
    response['data'] = x
    return Response(response)

@api_view(['POST'])
def AudioTwoLeast(request):
    response = {}
    base64_audio = request.data.get("name")

    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(base64_audio)
    wav_file.write(decode_string)
    audio_name = wav_file.name
    music = Audio_LSB(audio_name)
    x=music.twoDecode()
    response['data'] = x
    return Response(response)

@api_view(['POST'])
def AudioEncode(request ):
    base64_audio = request.data.get("name")
    decode_audio = base64.b64decode(base64_audio)
    wav_file = open("sample.wav" , "wb")
    wav_file.write(decode_audio)
    audio_name = wav_file.name

    

    string = request.data.get("text")
    music = Audio_LSB(audio_name)
    music.encode(string)
    """ with open(, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    output_audio = base64.b64encode(music.encode(string))
    print (output_audio)
    breakpoint()
 """

    
    return Response("encoded")

@api_view(['POST'])
def AudioTwoEncode(request ):
    base64_audio = request.data.get("name")

    decode_audio = base64.b64decode(base64_audio)
    wav_file = open("sample.wav" , "wb")
    wav_file.write(decode_audio)
    audio_name = wav_file.name


    string = request.data.get("text")
    music = Audio_LSB(audio_name)
    music.twoEncode(string)
    return Response("2 least encoded")



@api_view(['POST'])
def ImageDCTDecode(request):
    response = {}
    base64_image = request.data.get("img")
    format, imgstr = base64_image.split(';base64,')
    #ext = format.split('/')[-1] 
    #base64_image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    with open("foo.png","wb") as f:
        f.write(b64decode(imgstr))
    #image_64_decode = base64.b64decode(base64_image) 
    #image_result = open('deer_decode.png', 'wb') # create a writable image and write the decoding result
    #image_result.write(image_64_decode)
    image = Image_LSB()
    #image_name = "afterlsb.png"
    x= image.decode_textLeast('foo.png')
    response['data'] = x
    return Response(response)


@api_view(['POST'])
def ImageDCTEncode(request):
    #response = {}
    base64_image = request.data.get("img")
    stego_text = request.data.get("text")
    format, imgstr = base64_image.split(';base64,')
    with open("test3.jpg","wb") as f:
        f.write(b64decode(imgstr))
    
    img_name = f.name 
    
    image = Image_LSB()

    image.encode_text(img_name, stego_text, 'afterfoo.png')
    #with open("afterfoo.png", "rb") as image_file:
        #encoded_string = base64.b64encode(image_file.read())

    #response['data'] = encoded_string
    return Response("encoded") 


@api_view(['POST'])
def getPsnr(request):
    
    base64_image1 = request.data.get("img1")
    base64_image2 = request.data.get("img2")
    stego_text = request.data.get("text")
    format, imgstr = base64_image1.split(';base64,')
    with open("test3.jpg","wb") as f:
        f.write(b64decode(imgstr))
    
    imgstr2 = base64_image2.split(';base64,')
    with open("afterfoo.png", "wb") as o:
        o.write(b64decode(imgstr2))
    
    img_name1 = f.name 
    img_name2 = o.name
    
    psnr = PSNR()

    x = psnr.calculate_PSNR(img_name1, img_name2)

    response['data'] = x
    return Response(response) 