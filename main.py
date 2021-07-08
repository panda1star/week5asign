#Using flask to make an API
#Import necessary libraries
from flask import Flask, jsonify, request
import pickle
import pandas as pd

#Creating a flask app

app = Flask(__name__)


@app.route('/', methods= ['GET','POST'])
def index():
    if(request.method == 'GET'):

        data = "Hello World"
        return jsonify({'data':data})

@app.route('/predict/', methods= ['GET','POST'])
def potability_predict():
    model = pickle.load(open('model.pickle','rb'))

    ph = request.args.get('ph')
    Hardness = request.args.get('Hardness')
    Solids = request.args.get('Solids')
    Chloramines = request.args.get('Chloramines')
    Sulfate = request.args.get('Sulfate')
    Conductivity = request.args.get('Conductivity')
    Organic_carbon = request.args.get('Organic_carbon')
    Trihalomethanes = request.args.get('Trihalomethanes')

    test_df = pd.DataFrame({'ph':[ph],'Hardness':[Hardness],'Solids':[Solids],'Chloramines':[Chloramines],'Sulfate':[Sulfate]
    ,'Conductivity':[Conductivity],'Organic_carbon':[Organic_carbon],'Trihalomethanes':[Trihalomethanes]})
 
    pred_potability = model.predict(test_df)
    return jsonify({'Water Potability':str(pred_potability)})

# # Driver function
# if __name__ == '__main__':
#      app.run(debug=True)




