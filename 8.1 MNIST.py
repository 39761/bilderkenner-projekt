# 8.1 MNIST
# Code 29

#Teil1
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from emnist import extract_training_samples
from emnist import extract_test_samples
import random
# Daten laden
print("Daten laden...")
X_train, y_train = extract_training_samples("letters")
X_test, y_test = extract_test_samples("letters")
# Daten vorbereiten
X_train = (X_train / 255.0).reshape((-1,28,28,1))
X_test = (X_test / 255.0).reshape((-1,28,28,1))
# Modell erstellen
print(X_train.shape)
model = keras.models.Sequential([
keras.layers.Input(shape=(28,28,1)),
keras.layers.Conv2D(4,(3,3),activation="relu"),
keras.layers.Conv2D(5,(3,3),activation="relu"),
keras.layers.Conv2D(6,(3,3),activation="relu"),
keras.layers.Flatten(),
keras.layers.Dense(26, activation="softmax")
])
# model.summary()8.2 Erkl¨ arung 47
# Code 30
#Teil2
# Modell kompilieren
model.compile(optimizer="adam",
loss="sparse_categorical_crossentropy",
metrics=["accuracy"])
# Modell trainieren
model.fit(X_train, y_train-1, epochs=1)
# Modell evaluieren
test_loss, test_acc = model.evaluate(X_test, y_test-1)
print("\nTest accuracy:", test_acc)
# Einige Vorhersagen anzeigen
predictions = model.predict(X_test)
plt.figure(figsize=(10,10))
for j in range(25):
i=random.randrange(0,X_test.shape[0])
plt.subplot(5,5,j+1)
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(X_test[i], cmap=plt.cm.binary)
plt.xlabel(chr(np.argmax(predictions[i])+97))
plt.show()
# und zum Ausf¨ uhren des Programms reicht es
# Code 31
# python emnist_classifier.py
# oder extern in Terminal
# Code 32
# python3 emnist_classifier.py
# 8.2 Erkl¨
# arung
# Daten laden und vorbereiten
# Der EMNIST-Datensatz wird geladen und die Pixelwerte der Bilder werden
# durch 255 geteilt, um sie zu normalisieren. Die Daten werden außerdem so um-
# geformt, dass sie eine zus¨ atzliche Dimension haben, die f¨ ur das CNN ben¨ otigt
# wird.8.2 Erkl¨ arung 48
# Code 33
import numpy as np
from emnist import extract_training_samples
from emnist import extract_test_samples
print("Daten laden...")
X_train, y_train = extract_training_samples("letters")
X_test, y_test = extract_test_samples("letters")
X_train = (X_train / 255.0).reshape((-1,28,28,1))
X_test = (X_test / 255.0).reshape((-1,28,28,1))
# Modell erstellen
# Ein Convolutional Neural Network (CNN) mit drei Conv2D-Layern wird er-
# stellt. Nach den Conv2D-Layern wird das Feature-Map mit dem Flatten-Layer
# flachgelegt und durch einen Dense-Layer mit Softmax-Aktivierung gef¨ uhrt, um
# die endg¨ ultige Klassifikation f¨ ur die 26 Buchstaben zu erhalten.
# Code 34
model = keras.models.Sequential([
keras.layers.Input(shape=(28,28,1)),
keras.layers.Conv2D(4,(3,3),activation="relu"),
keras.layers.Conv2D(5,(3,3),activation="relu"),
keras.layers.Conv2D(6,(3,3),activation="relu"),
keras.layers.Flatten(),
keras.layers.Dense(26, activation="softmax")
])
# Modell kompilieren und trainieren
# Das Modell wird mit dem Adam-Optimierer, der Kreuzentropie als Verlust-
# funktion und der Genauigkeit als Bewertungsmetrik kompiliert. Das Modell wird
# dann mit den Trainingsdaten trainiert.
# Code 35
model.compile(optimizer="adam",
loss="sparse_categorical_crossentropy",
metrics=["accuracy"])
model.fit(X_train, y_train-1, epochs=1)
# Modell evaluieren
# Die Genauigkeit des Modells wird auf den Testdaten evaluiert.8.2 Erkl¨ arung 49
# Code 36
test_loss, test_acc = model.evaluate(X_test, y_test-1)
print("\nTest accuracy:", test_acc)
# Einige Vorhersagen anzeigen
# Vorhersagen f¨ ur zuf¨ allig ausgew¨ ahlte Bilder aus dem Testdatensatz werden
# mithilfe des trainierten Modells gemacht und visualisiert.
# Code 37
predictions = model.predict(X_test)
plt.figure(figsize=(10,10))
for j in range(25):
i=random.randrange(0,X_test.shape[0])
plt.subplot(5,5,j+1)
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(X_test[i], cmap=plt.cm.binary)
plt.xlabel(chr(np.argmax(predictions[i])+97))
plt.show()