import urllib.request  
  
# 打开URL列表文件  
with open('https://github.com/songshua295/PanSo/tree/main/asset/网站.txt', 'r') as file:  
    # 读取URL列表  
    urls = file.read().splitlines()
print(urls)