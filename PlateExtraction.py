import Model

import cv2
import numpy as np
import math

import pytesseract

from PIL import Image

import easygui

def extractChar():

    img = cv2.imread("frameVideo.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    topHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    add = cv2.add(gray, topHat)
    subtract = cv2.subtract(add, blackHat)

    blur = cv2.GaussianBlur(subtract, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 19, 9)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    height, width = thresh.shape

    imageContours = np.zeros((height, width, 3), dtype=np.uint8)

    possibleChars = []
    countOfPossibleChars = 0

    for i in range(0, len(contours)):

        cv2.drawContours(imageContours, contours, i, (255, 255, 255))

        possibleChar = Model.ifChar(contours[i])

        if Model.checkIfChar(possibleChar) is True:
            countOfPossibleChars = countOfPossibleChars + 1
            possibleChars.append(possibleChar)

    imageContours = np.zeros((height, width, 3), np.uint8)

    ctrs = []

    for char in possibleChars:
        ctrs.append(char.contour)

    cv2.drawContours(imageContours, ctrs, -1, (255, 255, 255))

    plates_list = []
    listOfListsOfMatchingChars = []

    for possibleC in possibleChars:
        def matchingChars(possibleC, possibleChars):
            listOfMatchingChars = []

            for possibleMatchingChar in possibleChars:
                if possibleMatchingChar == possibleC:
                    continue

                distanceBetweenChars = Model.distanceBetweenChars(possibleC, possibleMatchingChar)

                angleBetweenChars = Model.angleBetweenChars(possibleC, possibleMatchingChar)

                changeInArea = float(abs(possibleMatchingChar.boundingRectArea - possibleC.boundingRectArea)) / float(
                    possibleC.boundingRectArea)

                changeInWidth = float(abs(possibleMatchingChar.boundingRectWidth - possibleC.boundingRectWidth)) / float(
                    possibleC.boundingRectWidth)

                changeInHeight = float(abs(possibleMatchingChar.boundingRectHeight - possibleC.boundingRectHeight)) / float(
                    possibleC.boundingRectHeight)

                if distanceBetweenChars < (possibleC.diagonalSize * 5) and \
                        angleBetweenChars < 12.0 and \
                        changeInArea < 0.5 and \
                        changeInWidth < 0.8 and \
                        changeInHeight < 0.2:
                    listOfMatchingChars.append(possibleMatchingChar)

            return listOfMatchingChars

        listOfMatchingChars = matchingChars(possibleC, possibleChars)

        listOfMatchingChars.append(possibleC)

        if len(listOfMatchingChars) < 3:
            continue

        listOfListsOfMatchingChars.append(listOfMatchingChars)

        listOfPossibleCharsWithCurrentMatchesRemoved = list(set(possibleChars) - set(listOfMatchingChars))

        recursiveListOfListsOfMatchingChars = []

        for recursiveListOfMatchingChars in recursiveListOfListsOfMatchingChars:
            listOfListsOfMatchingChars.append(recursiveListOfMatchingChars)

        break

    imageContours = np.zeros((height, width, 3), np.uint8)

    for listOfMatchingChars in listOfListsOfMatchingChars:
        contoursColor = (255, 0, 255)

        contours = []

        for matchingChar in listOfMatchingChars:
            contours.append(matchingChar.contour)

        cv2.drawContours(imageContours, contours, -1, contoursColor)

    for listOfMatchingChars in listOfListsOfMatchingChars:
        possiblePlate = Model.PossiblePlate()

        listOfMatchingChars.sort(key=lambda matchingChar: matchingChar.centerX)

        plateCenterX = (listOfMatchingChars[0].centerX + listOfMatchingChars[len(listOfMatchingChars) - 1].centerX) / 2.0
        plateCenterY = (listOfMatchingChars[0].centerY + listOfMatchingChars[len(listOfMatchingChars) - 1].centerY) / 2.0

        plateCenter = plateCenterX, plateCenterY

        plateWidth = int((listOfMatchingChars[len(listOfMatchingChars) - 1].boundingRectX + listOfMatchingChars[
            len(listOfMatchingChars) - 1].boundingRectWidth - listOfMatchingChars[0].boundingRectX) * 1.3)

        totalOfCharHeights = 0

        for matchingChar in listOfMatchingChars:
            totalOfCharHeights = totalOfCharHeights + matchingChar.boundingRectHeight

        averageCharHeight = totalOfCharHeights / len(listOfMatchingChars)

        plateHeight = int(averageCharHeight * 1.5)

        opposite = listOfMatchingChars[len(listOfMatchingChars) - 1].centerY - listOfMatchingChars[0].centerY

        hypotenuse = Model.distanceBetweenChars(listOfMatchingChars[0],
                                                    listOfMatchingChars[len(listOfMatchingChars) - 1])
        correctionAngleInRad = math.asin(opposite / hypotenuse)
        correctionAngleInDeg = correctionAngleInRad * (180.0 / math.pi)

        possiblePlate.rrLocationOfPlateInScene = (tuple(plateCenter), (plateWidth, plateHeight), correctionAngleInDeg)

        rotationMatrix = cv2.getRotationMatrix2D(tuple(plateCenter), correctionAngleInDeg, 1.0)

        height, width, numChannels = img.shape

        imgRotated = cv2.warpAffine(img, rotationMatrix, (width, height))

        imgCropped = cv2.getRectSubPix(imgRotated, (plateWidth, plateHeight), tuple(plateCenter))

        possiblePlate.Plate = imgCropped

        if possiblePlate.Plate is not None:
            plates_list.append(possiblePlate)

        for i in range(0, len(plates_list)):
            p2fRectPoints = cv2.boxPoints(plates_list[i].rrLocationOfPlateInScene)

            rectColour = (0, 255, 0)

            cv2.line(imageContours, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), rectColour, 2)
            cv2.line(imageContours, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), rectColour, 2)
            cv2.line(imageContours, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), rectColour, 2)
            cv2.line(imageContours, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), rectColour, 2)

            cv2.line(img, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), rectColour, 2)
            cv2.line(img, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), rectColour, 2)
            cv2.line(img, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), rectColour, 2)
            cv2.line(img, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), rectColour, 2)

            cv2.imwrite('plate.png', plates_list[i].Plate)

        plateImg = cv2.imread('plate.png')

        grayPlate = cv2.cvtColor(plateImg, cv2.COLOR_BGR2GRAY)

        (thresh, binaryPlate) = cv2.threshold(grayPlate, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thresh = 140
        binaryPlate = cv2.threshold(grayPlate, thresh, 255, cv2.THRESH_BINARY)[1]

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        phrase = pytesseract.image_to_string(binaryPlate, lang='eng')
        
        phraseTranslate = phrase.translate({ord(c): "" for c in "!@#$%^&*()[]}{;-:,./<>?\/|`~-=_+ "})

        phraseArray = list(phraseTranslate)

        for i in range(0, len(phraseArray)):
            if i < 3:
                phraseArray[i] = phraseArray[i].replace("1", "I")
                phraseArray[i] = phraseArray[i].replace("0", "O")
            else:
                phraseArray[i] = phraseArray[i].replace("I", "1")
                phraseArray[i] = phraseArray[i].replace("O", "0")

        ocrPhrase = ''.join(str(e) for e in phraseArray)   
        
        return ocrPhrase