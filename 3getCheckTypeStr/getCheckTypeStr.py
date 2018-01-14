from aip import AipOcr
import os, json,sys
from time import sleep
reload(sys)
sys.setdefaultencoding('utf8')
# APP_ID = '10685351'
# API_KEY = 'YhZjuH7ImkYn2rkpvbngHUK9'
# SECRET_KEY = '49GRXlOQUkFriYdESqfkfjqcNe2vINGd'

APP_ID = '10689311'
API_KEY = 'gfbVqOSh0OfrBgLbIDIDN3LG'
SECRET_KEY = '8x1QS8zRdUZg8CMi3qAiXtC87GdlrTyh'

# APP_ID = '10689317'
# API_KEY = 'SuI3zXXgCIQkFaRe7nTIBz39'
# SECRET_KEY = 'Nxn6WkpQ3Aef2iGeKy4bY8Gy55bG7GTe'

# APP_ID = '10686902'
# API_KEY = 'f0OoGIltwse62zOu7ZBzbchw'
# SECRET_KEY = 'oxrXXhBylkpd3pZ07nsr5OhBGaeMxQEi'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
result_path = '../images/typeStr/0014.txt'
result_file = open(result_path, 'wb')
for i in range(1400,1900):
    filePath = '../images/typeStr/'+str(i)+'.jpg'
    if os.path.exists(filePath):
        file=open(filePath,'rb')
        image = file.read()
        file.close()
        response=client.basicGeneral(image)
        print(response)
        result_num = response[u'words_result_num']
        result_words = response[u'words_result']
        result_str = str(i)+":"
        for words in result_words:
            result_str = result_str + words[u'words'].encode('utf-8')
        print(result_str+"\r\n")
        result_file.write(result_str+"\r\n")
        sleep(1)
result_file.close()