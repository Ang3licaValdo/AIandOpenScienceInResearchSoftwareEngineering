import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from  sklearn import preprocessing



class vectores_positivos_negativos:
    def __init__(self, x_positivo, x_negativo):
        self.x_positivo = x_positivo
        self.x_negativo = x_negativo


i = 0
def prediccion(calculo_obtenido, c_magnitud):
    #arr_pred = np.array([])
    
    if(calculo_obtenido < c_magnitud):
        i = 0
        #np.append(arr_pred, 0)
    elif(calculo_obtenido > c_magnitud):
        #np.append(1)
        i = 1
    return i #arr_pred

def prediccion_previa(vector_test,vector_c,magnitud_c):
    #p = np.array([])
    p = 0.0
    p = np.dot(vector_test,vector_c)/magnitud_c
    return p
def clasificar_valores(x_train, y_train, m):
    array_positivos = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0]])
    array_negativos = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0]])
    for i in range(m):
        if(y_train[i] == 1):
            
            array_positivos = np.append(array_positivos,np.array([x_train[i]]),axis = 0)
            # print("el x_train[i] es: ",x_train[i])
            # print("Array positivos for: ",array_positivos)
            # print("y_train[i]: ", y_train[i])
        elif(y_train[i] == 0):
            array_negativos = np.append(array_negativos,np.array([x_train[i]]),axis = 0)
            # print("Array negativos for: ",array_positivos)
            # print("y_train[i]: ", y_train[i])

    return vectores_positivos_negativos(array_positivos, array_negativos)


pred_vec = np.array([])
##LOADING THE DATASET##
df = pd.read_csv('heart.csv', sep=',', engine='python')
X = df.drop(['target'],axis=1).values #estructura X del mismo tamaño que y
y = df['target'].values  
	
#Separa el corpus cargado en el DataFrame en el 50% para entrenamiento y el 50% para pruebas
#~ X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle = False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle = True, random_state = 0 )

#escalando los datos:
x_escalado_train = preprocessing.StandardScaler().fit_transform(X_train)
print("Datos escalados train: ", x_escalado_train)
print("Datos sin escalar: ", X_train)
x_escalado_test = preprocessing.StandardScaler().fit_transform(X_test)

###Con el entrenamiento###
tupla = X_train.shape
m = tupla[0]
print("el tamaño de las x de entrenamiento es: ",m)

print("Este es el x_train: ", X_train)
# print(X_train[0])
print("Este es el y_train: ",y_train)
# print(y_train[0])

print("Los vectores clasificados: ")
valores = clasificar_valores(X_train, y_train, m)#recuerda cambiar el tercer argumento por m

valores.x_positivo = np.delete(valores.x_positivo, 0, axis = 0)
valores.x_negativo = np.delete(valores.x_negativo, 0, axis = 0)
print("Los valores positivos son: ")
n = 0
for a in valores.x_positivo:
    print(a)
    n = n+1
    print(n)
print("Los valores negativos son",valores.x_negativo)

#Calulado tamaños del conjunto de los postivos y negativos
tupla2 = valores.x_positivo.shape
m2 = tupla2[0]
print("tamano de los positivos: ", m2)
tupla3 = valores.x_negativo.shape
m3 = tupla3[0]
print("tamano de los negativos: ", m3)

#Promedios positivos y negativos c
c_promedio_positivo = valores.x_positivo.sum(axis=0)/m2
print("promedio c+: ", c_promedio_positivo)
c_promedio_negativo = valores.x_negativo.sum(axis=0)/m3
print("promedio c-: ", c_promedio_negativo)

#Obteniendo el w
w = c_promedio_positivo - c_promedio_negativo
print("El w vale: ",w)

#Calculando el c general
c = (c_promedio_positivo + c_promedio_negativo)/2
print("El c vale: ", c)

#Magnitud del c
magnitud_c = np.linalg.norm(c)
print("La magnitud de c es",magnitud_c)

#print("y_test", y_test)
 
for elemen_prueba in X_test:
    #print(elemen_prueba)
    p_1 = prediccion_previa(elemen_prueba,c,magnitud_c)
    print(type(p_1))
    print("La prediccion previa es: ", p_1)

    print("El valor pertenece a: ",prediccion(p_1,magnitud_c))
    pred_vec = np.append(pred_vec,prediccion(p_1,magnitud_c),axis = None)
    #print(pred_vec)
print("y predicho",pred_vec)

y_test = np.float64(y_test)
print("y verdadero", y_test)


accuracy = accuracy_score(y_test, pred_vec)
print("y verdadero type: ", type(y_test))


print ('final accuracy', accuracy)

print(classification_report(y_test, pred_vec, target_names=['0','1']))
cm = confusion_matrix(y_test, pred_vec, labels=[0,1])
print (cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['0','1'])
disp.plot()
plt.show()