import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

# Kullanılanveri seti, araçlara ait teknik özellikler,
# yakıt tüketimi değerleri ve CO₂ emisyonlarını içermektedir.

df = pd.read_csv("FuelConsumption.csv")

print(df.head())
print(df.head(10))

# veri seti özet
print(df.describe())


# Analizde kullanılacak bağımsız değişkenler ve hedef değişken 
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(10))

cdf.hist()
plt.show()

# Yakıt tüketimi ile CO2 emisyonu arasındaki ilişki grafigi
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

# Engine size ile CO2 emisyonu arasındaki ilişki grafigi
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

# Cylinders ile CO2 emisyonu arasındaki ilişki grafigi
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='red')
plt.xlabel("CYLINDERS")
plt.xlabel("Emission")
plt.show()

# Veri seti, model eğitimi ve değerlendirmesi için eğitim ve test olarak ayrılır

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
ax1.scatter(test.ENGINESIZE, test.CO2EMISSIONS,  color='red')
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)

print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)


print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ -test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )