import cv2
import numpy as np

class Morfologia():
	def __init__(self):
		self.kernel = np.ones((5, 5), np.uint8)

	def Erosion(self,imagen):
		image = cv2.erode(imagen, self.kernel) 
		cv2.imshow('Original', imagen)
		cv2.imshow('Erosion', image)
		cv2.waitKey()

	def Dilacion(self,imagen):
		image = cv2.dilate(imagen, self.kernel) 
		cv2.imshow('Original', imagen)
		cv2.imshow('Dilacion', image)
		cv2.waitKey()

	def Apertura(self,imagen):
		image = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, self.kernel) 
		cv2.imshow('Original', imagen)
		cv2.imshow('Apertura', image)
		cv2.waitKey()

	def Cierre(self,imagen):
		image = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, self.kernel) 
		cv2.imshow('Original', imagen)
		cv2.imshow('Cierre', image)
		cv2.waitKey()

	def hit_or_miss(self,imagen):
		grayimg = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
		kernel = np.array((
        [1, 1, 1],
        [0, 1, -1],
        [0, 1, -1]), dtype="int")
		image = cv2.morphologyEx(grayimg, cv2.MORPH_HITMISS,kernel) 
		cv2.imshow('Original', imagen)
		cv2.imshow('hit_or_miss', image)
		cv2.waitKey()

	def Esqueleto(self,imagen,nimagen):
		img = cv2.imread(imagen, 0)
		ret, img = cv2.threshold(img, 127, 255, 0)
		size = np.size(img)
		skel = np.zeros(img.shape, np.uint8)

		element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
		while True:
			open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
			temp = cv2.subtract(img, open)
			eroded = cv2.erode(img, element)
			skel = cv2.bitwise_or(skel, temp)
			img = eroded.copy()
			if cv2.countNonZero(img) == 0:
				break

		cv2.imshow("Esqueleto", skel)
		cv2.imshow("Original", nimagen)
		cv2.waitKey(0)
		cv2.destroyAllWindows()



morfologia = Morfologia()
nimagen = input("Nombre de imagen: ")
imagen = cv2.imread(nimagen)
while(True):
	print(".....Morfologia.....")
	print("1. Erosion")
	print("2. Dilacion")
	print("3. Apertura")
	print("4. Cierre")
	print("5. hit_or_miss")
	print("6. Esqueleto")
	print("7. Salir\n")
	opcion = int(input("Ingresa una opcion: "))
	if opcion == 7:
		exit()
	elif opcion == 1:
		morfologia.Erosion(imagen)
	elif opcion == 2:
		morfologia.Dilacion(imagen)
	elif opcion == 3:
		morfologia.Apertura(imagen)
	elif opcion == 4:
		morfologia.Cierre(imagen)
	elif opcion == 5:
		morfologia.hit_or_miss(imagen)
	elif opcion == 6:
		morfologia.Esqueleto(nimagen,imagen)
	elif opcion > 7:
		print("Invalido")
		