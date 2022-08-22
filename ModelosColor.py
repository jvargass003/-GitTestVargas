import cv2
import numpy as np
class Modelos():
	def init(self):
		print("Nueva modificacion")
		
	def RGB(self,imagen):
		img = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
		negra = np.zeros(img.shape[:2], dtype='uint8')
		B,G,R = cv2.split(img)
		cv2.imshow("B", cv2.merge([B,negra,negra]))
		cv2.imshow("G", cv2.merge([negra,G,negra]))
		cv2.imshow("R", cv2.merge([negra,negra,R]))
		cv2.imshow("Original", cv2.merge([R,G,B]))
		cv2.waitKey()

	def HSI(self,imagen):
		img = cv2.cvtColor(imagen, cv2.COLOR_BGR2HLS)
		negra = np.zeros(img.shape[:2], dtype='uint8')
		H,S,I = cv2.split(img)
		cv2.imshow("H", cv2.merge([H,negra,negra]))
		cv2.imshow("S", cv2.merge([negra,S,negra]))
		cv2.imshow("I", cv2.merge([negra,negra,I]))
		cv2.imshow("Original", cv2.cvtColor(cv2.merge(cv2.split(img)),cv2.COLOR_HLS2BGR))
		cv2.waitKey()

	def YCbCr(self,imagen):
		img = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
		negra = np.zeros(img.shape[:2], dtype='uint8')
		Y,Cb,Cr = cv2.split(img)
		print(Y)
		cv2.imshow("Y", cv2.merge([Y,negra,negra]))
		cv2.imshow("Cb", cv2.merge([negra,Cb,negra]))
		cv2.imshow("Cr", cv2.merge([negra,negra,Cr]))
		cv2.imshow("Original", cv2.cvtColor(cv2.merge(cv2.split(img)),cv2.COLOR_YCrCb2BGR))
		cv2.waitKey()

	def CMYK(self,imagen):
		bgr = imagen
		rgb_scale = 255
		cmyk_scale = 100
		bgrdash = bgr.astype(np.float)/255.
		K = 1 - np.max(bgrdash, axis=2)
		C = (1-bgrdash[...,2] - K)/(1-K)
		M = (1-bgrdash[...,1] - K)/(1-K)
		Y = (1-bgrdash[...,0] - K)/(1-K)
		negra = np.zeros(imagen.shape[:2], dtype='uint8')
		CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
		k = (np.dstack((K,negra,negra,negra)) * 255).astype(np.uint8)
		c = (np.dstack((negra,C,negra,negra)) * 255).astype(np.uint8)
		m = (np.dstack((negra,negra,M,negra)) * 255).astype(np.uint8)
		y = (np.dstack((negra,negra,negra,Y)) * 255).astype(np.uint8)
		R = rgb_scale*(1.0-(c+k)/float(cmyk_scale))
		G = rgb_scale*(1.0-(m+k)/float(cmyk_scale))
		B = rgb_scale*(1.0-(y+k)/float(cmyk_scale))
		cv2.imshow("k",k)
		cv2.imshow("C",c)
		cv2.imshow("M",m)
		cv2.imshow("Y",y)
		cv2.imshow("CMYK", CMYK)
		cv2.imshow("Original", imagen)

		cv2.waitKey()

modelo = Modelos()
nimagen = input("Nombre de imagen: ")
imagen = cv2.imread(nimagen)
while(True):
	print(".....Modelo de color.....")
	print("1. RGB")
	print("2. HSI")
	print("3. YCbCr")
	print("4. CMYK")
	print("5. Salir\n")
	opcion = int(input("Ingresa una opcion: "))
	if opcion == 5:
		exit()
	elif opcion == 1:
		modelo.RGB(imagen)
	elif opcion == 2:
		modelo.HSI(imagen)
	elif opcion == 3:
		modelo.YCbCr(imagen)
	elif opcion == 4:
		modelo.CMYK(imagen)
	elif opcion > 5:
		print("Invalido")
