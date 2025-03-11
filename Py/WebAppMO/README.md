Task:
How to Build A Machine Learning Web App with Python
From scratch, we will deploy a linear regression model using Flask, a Python framework for developing web applications
# Разработка A Machine Learning Web App.
Decision:
tuser@kvmubuntu:~$ python3 -m venv Py-FrankAndrade-WebAppMO-Env
tuser@kvmubuntu:~$ mkdir Py-FrankAndrade-WebAppMO-Project
tuser@kvmubuntu:~$ source Py-FrankAndrade-WebAppMO-Env/bin/activate
tuser@kvmubuntu:~$ pip list
Package    Version
---------- -------
pip        22.0.2
setuptools 59.6.0
tuser@kvmubuntu:~$ pip install flask
tuser@kvmubuntu:~$ pip list
Package      Version
------------ -------
click        8.1.3
Flask        2.1.2
itsdangerous 2.1.2
Jinja2       3.1.2
MarkupSafe   2.1.1
pip          22.0.2
setuptools   59.6.0
Werkzeug     2.1.2
tuser@kvmubuntu:~$ vim Py-FrankAndrade-WebAppMO-Project/app.py
tuser@kvmubuntu:~$ cat Py-FrankAndrade-WebAppMO-Project/app.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run()
tuser@kvmubuntu:~$ cd Py-FrankAndrade-WebAppMO-Project/
tuser@kvmubuntu:~$ python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
- Заходим в браузер и пишем адрес: http://127.0.0.1:5000. должно появиться приветсвие
tuser@kvmubuntu:~$ pip install sklearn
tuser@kvmubuntu:~$ pip install pandas
tuser@kvmubuntu:~$ cd templates/
/templates$ vim index.html
rade-WebAppMO/Py-FrankAndrade-WebAppMO-Project/templates$ cat index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title> Web App MO </title>
</head>
<body>
    <h1>My first WebSite</h1>
</body>
</html>
tuser@kvmubuntu:~$ cat model.py
from sklearn import linear_model
import pandas as pd
import pickle
df = pd.read_csv('prices.csv')
y = df['Value'] # dependent variable
X = df[['Rooms', 'Distance']] # independent variable
lm = linear_model.LinearRegression()
lm.fit(X, y) # fitting the model
pickle.dump(lm, open('model.pkl','wb')) # save the model
print(lm.predict([[15, 61]]))  # format of input
print(f'score: {lm.score(X, y)}')
tuser@kvmubuntu:~$ python app.py
/home/user/Py-FrankAndrade-WebAppMO/Py-FrankAndrade-WebAppMO-Env/lib/python3.10/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator LinearRegression from version 1.0.2 when using version 1.1.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
- Заходим в браузер и пишем адрес: http://127.0.0.1:5000.
tuser@kvmubuntu:~$ vim templates/index.html
tuser@kvmubuntu:~$ cat templates/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title> Web App MO </title>
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>    
</head>
<body>
    <!--<h1>My first WebSite</h1>-->
</body>
</html>
tuser@kvmubuntu:~$ python app.py
/home/user/Py-FrankAndrade-WebAppMO/Py-FrankAndrade-WebAppMO-Env/lib/python3.10/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator LinearRegression from version 1.0.2 when using version 1.1.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
- Заходим в браузер и пишем адрес: http://127.0.0.1:5000.
tuser@kvmubuntu:~$ vim templates/index.html
tuser@kvmubuntu:~$ cat templates/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title> Web App MO </title>
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>    
</head>
<body>
    <!--<h1>My first WebSite</h1>-->
    <div class="login">
        <h2>Price Prediction</h2>
            <p>Introduce the number of rooms and distance:</p>
            <form action="{{url_for('predict')}}" method="post">
                <input type="text" name="rooms" placeholder="Rooms" required="required">
                <input type="text" name="distance" placeholder="Distance" required="required">
                <button type="submit" class="btn btn-primary btn-block btn-large"> Predict Value!</button>
            </form>
            <br>
            <br>    
        <b>{{prediction_text}}</b>
    </div>
</body>
</html>
tuser@kvmubuntu:~$ vim app.py
tuser@kvmubuntu:~$ cat app.py
from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))
@app.route("/")
#def hello_world():
def hello():
    #return "<p>Hello, World!</p>"
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'A house with {rooms} rooms per dwelling and located {distance} km to employment centers has a value of ${output}K')
if __name__ == "__main__":
    app.run()
tuser@kvmubuntu:~$ python app.py
/home/user/Py-FrankAndrade-WebAppMO/Py-FrankAndrade-WebAppMO-Env/lib/python3.10/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator LinearRegression from version 1.0.2 when using version 1.1.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
- Заходим в браузер и пишем адрес: http://127.0.0.1:5000.
Source:
# https://www.youtube.com/c/FrankAndrade5/videos