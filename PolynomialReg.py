import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

# Kullanılanveri seti, araçlara ait teknik özellikler,
# yakıt tüketimi değerleri ve CO₂ emisyonlarını içermektedir.

df = pd.read_csv("FuelConsumption.csv")

print(df.head())
# Analizde kullanılacak bağımsız değişkenler ve hedef değişken 
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(10))

# Engine size ile CO2 emisyonu arasındaki ilişki grafigi
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

# Veri seti, model eğitimi ve değerlendirmesi için eğitim ve test olarak ayrılır

msk= np.random.rand(len(df)) < 0.8
train= cdf[msk]
test= cdf[~msk]

'''
Polynomial regresyon, veriler arasındaki ilişkinin düz bir doğru ile ifade edilemediği
durumlarda kullanılır. Bu yöntemde ENGINESIZE değişkeninden x, x² (gerekirse x³ vb.)
gibi yeni özellikler türetilir ve böylece modelin eğri bir ilişkiyi öğrenmesi sağlanır.
Aslında hâlâ lineer regresyon uygulanır, ancak polinom terimler sayesinde doğrusal
olmayan (eğrisel) veri yapısı daha iyi temsil edilir.

'''
from sklearn.preprocessing import PolynomialFeatures
   
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])

# ENGINESIZE verisinden 2. dereceden polinom özellikler (1, x ve x²) üreterek
# doğrusal olmayan (eğrisel) ilişkiyi modelleyebilmek için yeni bir özellik matrisi oluşturur
poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
print(train_x_poly)

from sklearn.linear_model import LinearRegression

clf= LinearRegression()
clf.fit(train_x_poly, train_y)

print("Coefficients:", clf.coef_)
print("Intercept:", clf.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
XX = np.arange(0.0, 10.0, 0.1)
yy = clf.intercept_[0]+ clf.coef_[0][1]*XX+ clf.coef_[0][2]*np.power(XX, 2)
plt.plot(XX, yy, '-r' )
plt.xlabel("Engine size")
plt.ylabel("Emission")

from sklearn.metrics import r2_score

test_x_poly = poly.fit_transform(test_x)
test_y_ = clf.predict(test_x_poly)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y,test_y_ ) )