
#1. Здесь место для вашей ПЕРВОЙ гипотезы
# Гипотеза: учащиеся мужского пола в общем набрали баллов болььше, чем учащиеся женского пола

#2. Этап извлечения данных: убедитесь, что загрузили кейс с которым планируете работать.
# Здесь место, где вы обращаетесь к библиотеке Pandas и кейсу, с которым предстоит работать
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
#переменные
a = df.groupby(by = 'gender')['math score'].mean()
b = df.groupby(by = 'gender')['reading score'].mean()
c = df.groupby(by = 'gender')['writing score'].mean()

#код
d = (a+b+c)


d.plot(kind = 'bar', grid = True)
plt.show()
#гипотеза опровергнута 