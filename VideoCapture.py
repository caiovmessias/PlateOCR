import cv2
import time
import PlateExtraction
import easygui
import Model        

video = cv2.VideoCapture('VideoTeste.mp4')

while True:
    try:
        _, frame = video.read()
        cv2.imshow('Video Sendo Exibido', frame)
        cv2.waitKey(1)
        cv2.imwrite('frameVideo.jpg', frame)


        ocrPhrase = PlateExtraction.extractChar()

        if ocrPhrase is None:
            pass
        else:
            ocrLen = len(ocrPhrase)
            if ocrLen == 7:
                extractionArray = list(ocrPhrase)

                for i in range(0, len(extractionArray) + 1):
                    if i < 3:
                        if extractionArray[i].isalpha() == True:
                            pass
                        else:
                            break
                    else:
                        if i == len(extractionArray):
                            easygui.msgbox(Model.buscaInformacoes(ocrPhrase), title="Output")
                            video.release()
                        else:
                            if extractionArray[i].isdigit() == True:
                                pass
                            else:
                                break                       
    except:
        break