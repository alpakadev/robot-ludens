import cv2
import numpy as np

class BoardcasesPipeline:
    def __init__(self, img, lowerBounds, upperBounds):
        self.img = img.copy()
        self.lowerBounds = np.array(lowerBounds)
        self.upperBounds = np.array(upperBounds)

    def _detectBoard(self, img, lowerBounds, upperBounds):
        print(lowerBounds, type(lowerBounds))
        # Bounds in Form: (h, s, v)
        # Sucht nach Farben innerhalb der Bounds
        # Gibt Bild mit allem Schwarz außer der gesuchten Farbe
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerBounds, upperBounds)
        imask = mask>0
        cFilter = np.zeros_like(img, np.uint8)
        cFilter[imask] = img[imask]

        return cFilter

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

    def _getCornerMidwaypoints(self, start, end):
        # Berechnet die Punkte (O) zwischen zwei Ecken (X):
        # x -- O -- O -- X
        # |              |
        # O              O
        # |              |
        # O              O
        # |              |
        # X -- O -- O -- X
        # Gibt die Koordinaten der Midway Points zurück: [[x1, y1], [x2, y2]]

        xMidway1 = int((1 - 0.33) * start[0] + 0.33 * end[0])
        xMidway2 = int((1 - 0.66) * start[0] + 0.66 * end[0])
        yMidway1 = int((1 - 0.33) * start[1] + 0.33 * end[1])
        yMidway2 = int((1 - 0.66) * start[1] + 0.66 * end[1])
        midwayPoints = [[xMidway1, yMidway1], [xMidway2, yMidway2]]
        return midwayPoints
    
    def _getContourBounds(self, contour):
        # Sucht nach den Punkten der Kontur, die am wahrscheinlichsten die Ecken darstellen
        # TODO: Testen, wie das mit dem Board als Raute funktioniert
        # Gibt einen Array mit allen wichtigen Punkten auf dem Rand des Boards zurück
        # [[corner, midway1, midway2, corner], [...], [...], [...]]
        # Index 0 = Untere horizontale Grenze des Boards, 1 = Obere horizontale Grenze des Boards, 2 = linke vertikale Grenze des Boards, 3 = rechte vertikale Grenze des Boards

        corners = self._findCorners(contour) #eine corners = [[ax1 ay1], [bx2 by2]]
        midwayPUnten = self._getCornerMidwaypoints(corners[0], corners[1])
        midwayPOben = self._getCornerMidwaypoints(corners[2], corners[3])
        midwayPRechts = self._getCornerMidwaypoints(corners[1], corners[3])
        midwayPLinks = self._getCornerMidwaypoints(corners[0], corners[2])

        anchorsUnten = [corners[0], midwayPUnten[0], midwayPUnten[1], corners[1]]
        anchorsOben = [corners[2], midwayPOben[0], midwayPOben[1], corners[3]]
        anchorsLinks = [corners[0], midwayPLinks[0], midwayPLinks[1], corners[2]]
        anchorsRechts = [corners[1], midwayPRechts[0], midwayPRechts[1], corners[3]]

        return [anchorsUnten, anchorsOben, anchorsLinks, anchorsRechts]
        
    def _findCorners(self, contour):
        # Unnesting von der Contour:
        # Bisher [[[x1, y1]]], Nachher: [[x1, y1], [...]]
        cntr = contour[0]
        simpleCntr = []
        for i in range(0, len(cntr)):
            simpleCntr.append(cntr[i][0])
        self._sort(simpleCntr, 1)
        bLC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] <= bLC[0] and point[1] >= bLC[1]:
                bLC = point

        bRC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] >= bRC[0] and point[1] >= bRC[1]:
                bRC = point

        tLC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] <= tLC[0] and point[1] <= tLC[1]:
                tLC = point
        
        tRC = simpleCntr[0]
        for point in simpleCntr:
            if point[0] >= tRC[0] and point[1] <= tRC[1]:
                tRC = point

        return [bLC, bRC, tLC, tRC]

    def _lineIntersection(self, verticalLine, horizontalLine):
        # Berechnet Geradengleichungen von zwei horizontal und zwei vertikal gegenüberliegenden Punkten, um Schnittpunkte an den Ecken der Quadrate innerhalb des Spielfeld zu berechnen
        # Gibt den Schnittpunkt dieser zwei Geraden zurück:
        # [x1, y1]
        xdiff = (verticalLine[0][0] - verticalLine[1][0], horizontalLine[0][0] - horizontalLine[1][0])
        ydiff = (verticalLine[0][1] - verticalLine[1][1], horizontalLine[0][1] - horizontalLine[1][1])

        def _det( a, b):
            return a[0] * b[1] - a[1] * b[0]
        div = _det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (_det(*verticalLine), _det(*horizontalLine))
        x = _det(d, xdiff) / div
        y = _det(d, ydiff) / div
        return [int(x), int(y)]

    def _squares(self, anchors):
        # 2 - 3
        # 0 - 1
        #anchors = [[corner, mW1, mW2, corner], []...], Reihenfolge: Unten, Oben, Links, Rechts
        # Berechnet Koordinaten der Board Felder
        # Gibt Dictionary mit den einzelnen Feldern zurück
        upLeftIntersect = self._lineIntersection([anchors[0][1], anchors[1][1]], [anchors[2][2], anchors[3][2]])
        upRightIntersect = self._lineIntersection([anchors[0][2], anchors[1][2]], [anchors[2][2], anchors[3][2]])
        downLeftIntersect = self._lineIntersection([anchors[0][1], anchors[1][1]], [anchors[2][1], anchors[3][1]])
        downRightIntersect = self._lineIntersection([anchors[0][2], anchors[1][2]], [anchors[2][1], anchors[3][1]])

        squares = {"tL": [anchors[1][0], anchors[1][1], anchors[2][2], upLeftIntersect], 
                "tM": [anchors[1][1], anchors[1][2], upLeftIntersect, upRightIntersect], 
                "tR": [anchors[1][2], anchors[1][-1], upRightIntersect, anchors[3][2]], 
                "mL": [anchors[2][2], upLeftIntersect, anchors[2][1], downLeftIntersect], 
                "mM": [upLeftIntersect, upRightIntersect, downLeftIntersect, downRightIntersect], 
                "mR": [upRightIntersect, anchors[3][2], downRightIntersect, anchors[3][1]], 
                "bL": [anchors[2][1], downLeftIntersect, anchors[0][0], anchors[0][1]], 
                "bM": [downLeftIntersect, downRightIntersect, anchors[0][1], anchors[0][2]],
                "bR": [downRightIntersect, anchors[3][1], anchors[0][2], anchors[0][3]]}
        return squares

    def getBoardCases(self):
        color = (255, 0, 0)
        cFilteredImg = self._detectBoard(self.img, self.lowerBounds, self.upperBounds)
        boardCntr = self._getBoardContour(cFilteredImg, self.lowerBounds, self.upperBounds)
        boardCntrBounds = self._getContourBounds(boardCntr)
        sqrs = self._squares(boardCntrBounds)

        for square, values in sqrs.items():
            cv2.rectangle(cFilteredImg, (values[0][0], values[0][1]), (values[-1][0], values[-1][1]), color, 2)
            cv2.putText(cFilteredImg, square, (values[0][0], values[0][1]), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1, cv2.LINE_AA)
        

        #cv2.imshow("test", cFilteredImg)
        #cv2.waitKey()
        return sqrs