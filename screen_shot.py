from PIL import ImageGrab
import time
while 1:
    pic=ImageGrab.grab()
    timeTemp=time.time()
    timeTempNext=time.localtime(timeTemp)
    timeNow=time.strftime("%Y-%m-%d-%H-%M-%S",timeTempNext)
    print timeNow
    path="E:\screen_shot\\"
    savePath=path+timeNow+".jpg"
    pic.save(savePath)
    time.sleep(1800)
