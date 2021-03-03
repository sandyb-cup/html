# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/19
import requests
import os
try:
    os.mkdir('html5/form表单/images')
except FileExistsError:
    os.system('rm -rf images')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
url = 'https://www.runoob.com/try/demo_source/movie.mp4'
re = requests.get(headers = headers, url = url)
images_name = input('输入图片名字:')
re_content = re.content
with open(f'html/images/{images_name}.mp4', 'wb') as f:
    f.write(re_content)
