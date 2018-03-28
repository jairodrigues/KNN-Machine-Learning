import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
#Colunas
# # print (iris.keys())
# # print(iris['DESCR'][:193]+'\n...')
# print(iris['data'].shape)
# print(iris['data'][:10])
print(iris['target'])
print(iris['data'][:1])

# O train set conterá 75% dos dados de nosso dataset.
# Ele servirá como combustível para ensinarmos o nosso código a prever novas informações no futuro.
# Já o test set será usado para testarmos nossa aplicação com informações que ela nunca viu antes, a
# fim de sabermos se ela previu corretamente o tipo de Íris. Para fazer isso, usaremos a função train_test_split do scikit-learn.

x_train, x_test, y_train, y_test = train_test_split(iris['data'],iris['target'], random_state = 0)
print(x_train.shape)
print(x_test.shape)

fig, ax = plt.subplots(3,3, figsize=(15,15))

for i in range(3):
  for j in range(3):
    ax[i,j].scatter(x_train[:,j],x_train[:,i+1] c=y_train, s=60)
    ax[i,j].set_xtricks(())
    ax[i,j].set_ytricks(())

    if i == 2:
      ax[i,j].set_xlabel(iris['feature_names'][j])
    if j == 0:
      ax[i,j].set_ylabel(iris['feature_names'][i+1])
    if j > i:
      ax[i,j].set_visible(False)
