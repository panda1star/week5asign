
# Importing the libraries
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Importing the dataset
dataset = pd.read_csv('water_potability.csv')

dataset = dataset.dropna()


X=dataset[['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes' ]]
y = dataset['Potability']

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 101)

regressor = LinearRegression()

regressor.fit(X_train,y_train)


pickle.dump(regressor,open('model.pickle','wb'))

