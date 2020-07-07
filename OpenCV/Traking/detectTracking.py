import cv2
import numpy as np

captura = cv2.VideoCapture('video.mp4')

# 0 especifica la camara que se va a usar
# HSV
azulBajo = np.array([80,50,100], np.uint8)
azulAlto = np.array([105,200,220], np.uint8)

# pelotaBajo = np.array([0,50,100], np.uint8)
# pelotaAlto = np.array([1,220,220], np.uint8)


while True:
    ret,frame = captura.read()
    cv2.namedWindow("frame", 0)
    cv2.resizeWindow("frame", 1024,720)
    cv2.moveWindow("frame", 30, 30)

    # gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # bordes = cv2.Canny(gris, 255, 255)
    # _,th = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY_INV)
    # cv2.namedWindow("bordes", 0)
    # cv2.resizeWindow("bordes", 1024,720)

    # ret puede ser true cuando se leyo la imagen
    if ret == True:
        # hay que transformalas ya que OpenCV reconoce en BGR
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV, azulBajo, azulAlto)
        # mask = cv2.inRange(frameHSV, pelotaBajo, pelotaAlto)

        contornos,hierachy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        # _, contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # puede generar mucho ruido
        # cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
        # el -1 es que va a dibujar todos los contornos
        # 255,0,0 pintamos de azul BGR

        # Clasificamos los contornos 
        for c in contornos:
            area = cv2.contourArea(c)
            #si el area es myor de 3000 la dibujo
            if area > 200:
                # print(f'Cantidad de contornos: {len(contornos)}')
                # Obtengo las coordenadas
                x,y,w,h = cv2.boundingRect(c)
                # Agrego los contornos
                M = cv2.moments(c)
                if  (M['m00']==0): M['m00'] = 1
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                # cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                # cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y), (x+10, y), font, 0.75, (255,0, 0), 1, cv2.LINE_AA)
                # suavizo los contornos
                # nuevoContornoSuavizado = cv2.convexHull(c)

                epsilon = 0.001*cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, epsilon, True)

                # nuevoContornoSuavizado = cv2.convexHull(approx)

                cv2.drawContours(frame, [approx], 0, (255,0,0), 3)
        


        # Muestra lo colores segun la mascara
        # cv2.imshow('maskAzul', mask)
        

        cv2.imshow('frame', frame)

        # cv2.imshow('bordes', bordes)

        # Muestra lo colores reales
        # cv2.imshow('maskRedvis', maskRedvis)
        
        # cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            # ord es la tecla para salir
            break
    else: break

# Tenemos que finalizar la captura
captura.release()


# Para poder cerrar las ventanas abiertas durante el proceso
cv2.destroyAllWindows()