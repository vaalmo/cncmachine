
from matplotlib import pyplot as plt
import numpy as np
from prueba import *
#simulador de puntos


lista = np.array ([
                  (252, 101), (276, 85), (280, 109), (276, 101), (276, 93), (260, 77), (276, 77), (276, 69), (276, 61), (276, 53), (284, 53), (284, 61), (284, 69), (284, 77), (284, 85), (284, 93), (288, 109), (284, 101), (288, 149), (280, 133), (260, 129), (288, 129), (252, 125), (246, 141), (268, 97), (260, 109), (236, 93), (236, 101), (228, 101), (228, 109), (228, 117), (228, 125), (220, 125), (212, 117), (204, 109), (180, 101), (180, 109), (172, 125), (164, 137), (180, 117), (196, 161), (180, 125), (196, 145), (204, 145), (212, 145), (220, 145), (228, 145), (236, 145), (270, 133), (256, 141), (256, 157), (246, 157), (228, 169), (236, 169), (228, 161), (220, 169), (212, 169), (188, 169), (204, 169), (196, 169), (164, 169), (148, 169), (172, 169), (140, 145), (156, 169), (140, 169), (132, 169), (124, 169), (116, 161), (104, 153), (104, 161), (104, 169), (90, 165), (80, 157), (64, 157), (64, 165), (56, 169), (56, 161), (56, 153), (56, 145), (56, 137), (56, 129), (40, 113), (56, 113), (32, 113), (56, 121), (40, 121), (40, 129), (40, 137), (40, 145), (40, 153), (40, 161), (40, 169), (32, 169), (32, 161), (32, 153), (32, 145), (32, 137), (32, 129), (32, 121), (16, 97), (16, 109), (24, 89), (8, 109), (8, 97), (8, 89), (8, 81), (8, 73), (8, 57), (8, 65), (16, 57), (8, 49), (8, 41), (32, 41), (24, 45), (44, 27), (32, 25), (24, 25), (16, 25), (16, 17), (24, 17), (32, 17), (44, 11), (56, 9), (56, 17), (56, 25), (44, 35), (44, 43), (40, 51), (40, 63), (56, 49), (56, 65), (40, 73), (32, 49), (32, 57), (32, 65), (40, 83), (48, 63), (56, 81), (32, 81), (32, 73), (32, 89), (32, 97), (40, 99), (48, 99), (56, 105), (56, 89), (48, 83), (56, 73), (48, 73), (56, 57), (48, 51), (72, 49), (56, 33), (56, 41), (72, 41), (64, 41), (80, 25), (80, 41), (72, 25), (80, 25), (64, 21), (72, 9), (80, 9), (92, 9), (104, 17), (104, 25), (104, 33), (104, 41), (104, 49), (104, 65), (88, 49), (104, 73), (104, 81), (104, 89), (124, 101), (56, 97), (104, 97), (104, 105), (104, 113), (104, 121), (104, 129), (104, 137), (104, 145), (116, 145), (124, 145), (148, 145), (156, 145), (164, 145), (172, 145), (188, 145), (156, 137), (148, 137), (140, 137), (132, 137), (132, 145), (124, 109), (124, 125), (124, 93), (124, 117), (124, 85), (148, 85), (124, 69), (124, 77), (164, 81), (132, 81), (140, 65), (104, 57), (132, 61), (124, 61), (124, 53), (124, 45), (124, 37), (124, 29), (132, 21), (124, 21), (120, 9), (128, 9), (136, 9), (148, 9), (162, 9), (180, 29), (156, 25), (172, 21), (180, 21), (180, 45), (172, 29), (172, 37), (180, 53), (172, 53), (172, 61), (172, 69), (172, 77), (172, 93), (172, 101), (172, 109), (172, 117), (180, 93), (188, 93), (196, 101), (172, 85), (180, 85), (180, 77), (180, 69), (180, 61), (172, 45), (180, 37), (188, 41), (196, 49), (204, 57), (212, 65), (220, 73), (228, 69), (236, 85), (228, 85), (228, 93), (260, 85), (228, 77), (236, 77), (236, 69), (236, 61), (228, 61), (228, 53), (236, 53), (236, 45), (228, 45), (228, 37), (236, 37), (236, 29), (228, 29), (228, 21), (236, 21), (252, 21), (260, 29), (260, 37), (260, 45), (260, 53), (260, 61), (260, 69), (260, 93), (260, 93)
    ], dtype="f,f")


#lista = np.empty(len(move_array), dtype=object)
#lista[:] = move_array


x, y = zip(*lista)


plt.title("Grafica con punto de inicio = 279")
plt.plot(x, y, color="red", linewidth=2)


#Visualizar puntos
#fig, ax = plt.subplots()


plt.plot(x,y)
plt.scatter(x, y) 
plt.show()
