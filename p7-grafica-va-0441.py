import matplotlib.pyplot as plt
import numpy as np
# Ramirez Azul NC 0441

no_lista=[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,90,100]
plt.plot(no_lista,califa_ml,label="califa ML")
plt.plot(no_lista,califa_va,label="califa VA")
plt.title("Calificaciones materias 0441")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion ")
plt.legend()
plt.show()