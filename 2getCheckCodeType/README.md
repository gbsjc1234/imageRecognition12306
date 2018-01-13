1. 首先需要安装Pillow, Pillow包在packages目录下
    pip install Pillow***.whl

Traceback (most recent call last):
  File "E:/python/imageReconition/2getCheckCodeType/GetType.py", line 11, in <module>
    region = im.crop((x,y,x+w,y+h))
  File "C:\python\python2.7\lib\site-packages\PIL\Image.py", line 1075, in crop
    self.load()
  File "C:\python\python2.7\lib\site-packages\PIL\ImageFile.py", line 255, in load
    raise_ioerror(err_code)
  File "C:\python\python2.7\lib\site-packages\PIL\ImageFile.py", line 59, in raise_ioerror
    raise IOError(message + " when reading image file")
IOError: broken data stream when reading image file

Process finished with exit code 1
