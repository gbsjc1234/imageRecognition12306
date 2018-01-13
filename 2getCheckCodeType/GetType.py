from PIL import Image
for i in range(0,2000):
    im = Image.open("../images/"+str(i)+".jpg")
    img_size =im.size
    print i
    print img_size
    x=117
    y=0
    w=70
    h=30
    try:
        region = im.crop((x,y,x+w,y+h))
        region.save('../images/typeStr/'+str(i)+'.jpg')
    except Exception  as err:
        print(err)

