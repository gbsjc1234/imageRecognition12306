from PIL import Image
import os
import sys
for i in range(0,2000):
    path="../images/"+str(i)+".jpg"
    if os.path.exists(path):
        im = Image.open(path)
        img_size =im.size
        print i
        x=0
        y=37
        w=73
        h=73
        try:
            currentDir = sys.path[0]
            os.chdir('../images/typeImages')
            changeDir = os.getcwd()
            if os.path.exists(changeDir+'\\'+str(i)) == False:
                os.mkdir(str(i))
            os.chdir(currentDir)

            region0=im.crop()
            region0.save('../images/typeImages/' + str(i)+'/0' + '.jpg')

            region1 = im.crop((x,y,x+w,y+h))
            region1.save('../images/typeImages/' + str(i)+'/1' + '.jpg')

            region2 = im.crop((x+w, y, x + 2*w, y + h))
            region2.save('../images/typeImages/' + str(i) + '/2' + '.jpg')

            region3 = im.crop((x+2*w, y, x + 3*w, y + h))
            region3.save('../images/typeImages/' + str(i) + '/3' + '.jpg')

            region4 = im.crop((x+3*w, y, x + 4*w, y + h))
            region4.save('../images/typeImages/' + str(i) + '/4' + '.jpg')

            region5 = im.crop((x, y+h, x + w, y + 2*h))
            region5.save('../images/typeImages/' + str(i) + '/5' + '.jpg')

            region6 = im.crop((x+w, y + h, x + 2*w, y + 2 * h))
            region6.save('../images/typeImages/' + str(i) + '/6' + '.jpg')

            region7 = im.crop((x+2*w, y + h, x + 3*w, y + 2 * h))
            region7.save('../images/typeImages/' + str(i) + '/7' + '.jpg')

            region8 = im.crop((x+3*w, y + h, x + 4*w, y + 2 * h))
            region8.save('../images/typeImages/' + str(i) + '/8' + '.jpg')

        except Exception  as err:
            print(err)

