from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('house-prediction.html')

@app.route('/predict',methods=['POST'  ,'GET'])
def predict_placement():
    longitude  = float(request.form.get(' longitude '))
    latitude= float(request.form.get(' longitude '))
    housing_median_age= int(request.form.get(' total_rooms'))
    total_rooms=int(request.form.get(' total_rooms'))
    total_bedrooms = float(request.form.get('  total_bedrooms'))
    population= int(request.form.get('  population'))
    households = int(request.form.get(' households'))
    median_income = float(request.form.get(' median_income '))



    # prediction
median_house_value = model.predict(np.array(['longitude ', 'latitude','housing_median_age', 'total_rooms', 'total_bedrooms ','population', 'households ','median_income']))



#render_template('index.html', median_house_value= median_house_value)


if __name__ == '__main__':
    app.run(debug=True)