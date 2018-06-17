from django.shortcuts import render
from .models import Img
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11330122'
API_KEY = 'XbXEdbQcot7646CrTOt2pnSl'
SECRET_KEY = '9Wc70fR89AbD3rIW4rtdLOWc6s1XiTWU'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.img_url.name = 'gq.jpeg'
        img.save()
        
        image = get_file_content('/Users/gq/Documents/workspace/Django_demo/media/img/gq.jpeg')
        result = client.basicGeneral(image)
        print(result)
        
    return render(request, 'imgupload.html')