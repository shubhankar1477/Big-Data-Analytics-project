import os
from PIL import Image
import numpy as np
import boto3
import io
class ClsCommonUtils:

    @staticmethod
    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image
    
    @staticmethod 
    def get_textract_object():
        objTextract = boto3.client('textract')
        return objTextract
    
    @staticmethod
    def pil_image_to_byte_array(image):
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, "PNG")
        return imgByteArr.getvalue()
    



