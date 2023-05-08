import cv2
import numpy as np

# README: Bei der Bearbeitung daran denken, dass das Koordinaten System verkehrt herum ist
# Statt:        Ist es:
# x              __x
# |__y          |y
# 
# X-Werte werden vom Ursprung gesehen nach Links größer, Y-Werte vom Ursprung gesehen nach Oben. Daher ergibt sich die UpDown-LeftRight Notation

class BoardcasesPipeline:
    def __init__(self, lowerBounds, upperBounds):
        self.lowerBounds = np.array(lowerBounds)
        self.upperBounds = np.array(upperBounds)

    def _detectBoard(self, img, lowerBounds, upperBounds):
        # Bounds in Form: (h, s, v)
        # Sucht nach Farben innerhalb der Bounds
        # Gibt Bild mit allem Schwarz außer der gesuchten Farbe (s. Pipeline Bilder/colour_filter.png)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerBounds, upperBounds)
        imask = mask>0
        colorFilter = np.zeros_like(img, np.uint8)
        colorFilter[imask] = img[imask]

        return colorFilter

    def _sort(self, array, index):
        # Bubblesort für 2D Array. Index bestimmt welche Stelle der Subarrays als Kriterium genutzt wird
        n = len(array)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if array[j][index] > array[j + 1][index]:
                    arrayCopy = array.copy()
                    swapped = True
                    array[j] = arrayCopy[j+1]
                    array[j+1] = arrayCopy[j]
            if not swapped:
                return

    def _getBoardContour(self, img, lowerBounds, upperBounds):
        # Sucht das Bild mit der gefilterten Farbe nach Konturen ab
        # Die größte Zusammenhängende Kontur wird ausgewählt, da am wahrscheinlichsten das Board
        # TODO: Bild Ausschnitt einschränken um Treffersicherheit zu erhöhen
        # Gibt Punkte der Kontour zurück: [np.array([x, y], dtype=float32), np.array(...)]

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerBounds, upperBounds)
        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        biggerContour = contours[0]
        for contour in contours:
            if len(contour) > len(biggerContour):
                biggerContour = contour
        
        contour = biggerContour
        return contour

    def _addBetweenAnchors(self, corners):
        # Berechnet die Punkte (O) zwischen zwei Ecken (X) und updatet das Corner Dictionary um die entsprechenden Koordinaten
        # Der Weg ziwschne zwei Punkten wird gedrittelt. Der erste Punkt (firstAnchor) befindet sich auf 33% der Strecke und der zweite bei 66%
        # (0,0)
            # x -- O -- O -- X
            # |              |
            # O              O -> LEFT
            # |              |
            # O              O
            # |              |
            # X -- O -- O -- X
            #        |
            #        v
            #       UP

        borderlines = {"upperBorder": {"start": corners["upRightCorner"], "end": corners["upLeftCorner"]}, 
                       "lowerBorder": {"start": corners["downRightCorner"], "end": corners["downLeftCorner"]}, 
                       "leftBorder": {"start": corners["downLeftCorner"], "end": corners["upLeftCorner"]}, 
                       "rightBorder": {"start": corners["downRightCorner"], "end": corners["upRightCorner"]}}
        
        anchors = corners

        for key, line in borderlines.items():
            firstAnchor = {"x": int((1 - 0.33) * line["start"]["x"] + 0.33 * line["end"]["x"]), "y": int((1 - 0.33) * line["start"]["y"] + 0.33 * line["end"]["y"])}
            secondAnchor = {"x": int((1 - 0.66) * line["start"]["x"] + 0.66 * line["end"]["x"]), "y": int((1 - 0.66) * line["start"]["y"] + 0.66 * line["end"]["y"])}
            anchors[key + "Between1"] = firstAnchor
            anchors[key + "Between2"] = secondAnchor

        return anchors
        
    def _findCorners(self, contour):
        # Findet die Punkte der Kontur, die am weitesten Oben-Links, Oben-Rechts, Unten-Links und Unten-Rechts sind
        cntr = contour[0]
        simpleCntr = []
        for i in range(0, len(cntr)):
            simpleCntr.append(cntr[i][0])
        
        self._sort(simpleCntr, 1)

        bLC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] >= bLC[0] and point[1] <= bLC[1]:
                bLC = point

        bRC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] <= bRC[0] and point[1] <= bRC[1]:
                bRC = point

        tLC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] >= tLC[0] and point[1] >= tLC[1]:
                tLC = point
        
        tRC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] <= tRC[0] and point[1] >= tRC[1]:
                tRC = point

        return {"downLeftCorner": {"x": bLC[0], "y": bLC[1]}, "downRightCorner": {"x": bRC[0], "y": bRC[1]}, "upLeftCorner": {"x": tLC[0], "y": tLC[1]}, "upRightCorner": {"x": tRC[0], "y": tRC[1]}}

    def _lineIntersection(self, hLine, vLine, img):
        # Berechnet Geradengleichungen von zwei horizontal und zwei vertikal gegenüberliegenden Punkten, 
        # um durch die Schnittpunkte die Eckpunkte des mittleren Quadrats bestimmen zu können
        # vLine und hLine sind Arrays mit je zwei Punkten: [{x: x, y: y}, {x2: x2, y2: y2}]

        if vLine[0]["x"] > vLine[1]["x"]:
            temp = vLine[0]
            vLine[0] = vLine[1]
            vLine[1] = temp
        if hLine[0]["x"] > hLine[1]["x"]:
            temp = hLine[0]
            hLine[0] = hLine[1]
            hLine[1] = temp
               
        mVert = (vLine[1]["y"] - vLine[0]["y"]) / (vLine[1]["x"] - vLine[0]["x"])
        mHorizont = (hLine[1]["y"] - hLine[0]["y"]) / (hLine[1]["x"] - hLine[0]["x"])
        nVert = vLine[0]["y"] - (mVert * vLine[0]["x"])
        nHorizont = hLine[0]["y"] - (mHorizont * hLine[0]["x"])
        x = (nVert - nHorizont) / (mHorizont - mVert)
        y = mVert * x + nVert

        return {"x": int(x), "y": int(y)}

    def _addLineintersectionAnchors(self, anchors, img):
        # Ergänzt das Anchor Dictionary um die Eckpunkte des Quadrats in der Mitte des Boards
        # Dazu werden Geradenschnittpunkte verwendet (s.u.)
        # Berechnet die Schnittpunkte (DL, DR, TL, TR) zwischen zwei BetweenPoints (1 oder 2):
        # x -- 1 -- 2 -- X
        # |    |    |    |
        # 1 -- DR   DL-- 1 -> LEFT
        # |              |
        # 2 -- UR   UL-- 2
        # |    |    |    |
        # X -- 1 -- 2 -- X
        #        |
        #       UP
        upLeftIntersect = self._lineIntersection([anchors["rightBorderBetween2"], anchors["leftBorderBetween2"]], [anchors["lowerBorderBetween2"], anchors["upperBorderBetween2"]], img)
        upRightIntersect = self._lineIntersection([anchors["rightBorderBetween2"], anchors["leftBorderBetween2"]], [anchors["lowerBorderBetween1"], anchors["upperBorderBetween1"]], img)
        downLeftIntersect = self._lineIntersection([anchors["rightBorderBetween1"], anchors["leftBorderBetween1"]], [anchors["lowerBorderBetween2"], anchors["upperBorderBetween2"]], img)
        downRightIntersect = self._lineIntersection([anchors["rightBorderBetween1"], anchors["leftBorderBetween1"]], [anchors["lowerBorderBetween1"], anchors["upperBorderBetween1"]], img)
        anchors.update({"upRightIntersect": {"x": upRightIntersect["x"], "y": upRightIntersect["y"]}, 
                        "upLeftIntersect": {"x": upLeftIntersect["x"], "y": upLeftIntersect["y"]}, 
                        "downRightIntersect": {"x": downRightIntersect["x"], "y": downRightIntersect["y"]}, 
                        "downLeftIntersect": {"x": downLeftIntersect["x"], "y": downLeftIntersect["y"]}})
        
        return anchors

    def _squares(self, anchors):
        # Definiert die Eckpunkte der einzelnen Bildquadrate. Die Richtungsangaben sind vom Ursprung ausgesehen
        squares = {"upL": {"upLeft": anchors["upLeftCorner"], "upRight": anchors["upperBorderBetween2"], "downLeft": anchors["leftBorderBetween2"], "downRight": anchors["upLeftIntersect"]}, 
                "upMid": {"upLeft": anchors["upperBorderBetween2"], "upRight": anchors["upperBorderBetween1"], "downLeft": anchors["upLeftIntersect"], "downRight": anchors["upRightIntersect"]}, 
                "upR": {"upLeft": anchors["upperBorderBetween1"], "upRight": anchors["upRightCorner"], "downLeft": anchors["upRightIntersect"], "downRight": anchors["rightBorderBetween2"]}, 
                "midL": {"upLeft": anchors["leftBorderBetween2"], "upRight": anchors["upLeftIntersect"], "downLeft": anchors["leftBorderBetween1"], "downRight": anchors["downLeftIntersect"]}, 
                "midMid": {"upLeft": anchors["upLeftIntersect"], "upRight": anchors["upRightIntersect"], "downLeft": anchors["downLeftIntersect"], "downRight": anchors["downRightIntersect"]}, 
                "midR": {"upLeft": anchors["upRightIntersect"], "upRight": anchors["rightBorderBetween2"], "downLeft": anchors["downRightIntersect"], "downRight": anchors["rightBorderBetween1"]}, 
                "downL": {"upLeft": anchors["leftBorderBetween1"], "upRight": anchors["downLeftIntersect"], "downLeft": anchors["downLeftCorner"], "downRight": anchors["lowerBorderBetween2"]}, 
                "downMid": {"upLeft": anchors["downLeftIntersect"], "upRight": anchors["downRightIntersect"], "downLeft": anchors["lowerBorderBetween2"], "downRight": anchors["lowerBorderBetween1"]},
                "downR": {"upLeft": anchors["downRightIntersect"], "upRight": anchors["rightBorderBetween1"], "downLeft": anchors["lowerBorderBetween1"], "downRight": anchors["downRightCorner"]}}
        return squares

    def getBoardCases(self, img):
        # Nur für das Showcase
        color = (255, 0, 0)

        # Bild nach Farbe Filtern
        colorFilteredImg = self._detectBoard(img, self.lowerBounds, self.upperBounds)
        # Kontur der gefilterten Figur finden
        boardCntr = self._getBoardContour(colorFilteredImg, self.lowerBounds, self.upperBounds)
        # Eindeutige Eckpunkte finden
        boardCorners = self._findCorners(boardCntr)
        # Eckpunkte um Punkte zwischen den Ecken ergänzen
        anchors  = self._addBetweenAnchors(boardCorners)
        # Ankerpunkte um die Punkte in der Mitte des Boards ergänzen
        allAnchors = self._addLineintersectionAnchors(anchors, colorFilteredImg)
        # Koordinaten der Board Quadrate bestimmen
        sqrs = self._squares(allAnchors)

        # Darstellen der Quadrate für das Showcase
        for square, values in sqrs.items():
            print(values)
            cv2.rectangle(colorFilteredImg, (values["upLeft"]["x"], values["upLeft"]["y"]), (values["downRight"]["x"], values["downRight"]["y"]), color, 2)
            cv2.putText(colorFilteredImg, square, (values["upRight"]["x"], values["upRight"]["y"]), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1, cv2.LINE_AA)
        
        cv2.imshow("squares.png", colorFilteredImg)
        cv2.waitKey()

        return sqrs