import sqlite3

from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd
from database import insert_history

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


@app.route('/predictAction', methods=['POST'])
def predictAction():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        maritalstatus = request.form['maritalstatus']
        worktype = request.form['Worktype']
        residence = request.form['Residence']
        gender = request.form['gender']
        bmi = request.form['bmi']
        gluclevel = request.form['gluclevel']
        smoke = request.form['Smoke']
        hypertension = request.form['Hypertension']
        heartdisease = request.form['Heartdisease']
        #model = pickle.load(open('stroke_new.pkl','wb'))

        res={'urban':1,'rural':0}
        gen={'Female':0,'Male':1}
        msts={'married':1,'not married':0}
        wktype={'privatejob':2,'govtemp':1,'selfemp':3}
        smke={'formerly-smoked':1,'non-smoker':2,'smoker':3}
        hypten={'hypten':1,'nohypten':0}
        hrtdis={'heartdis':1,'noheartdis':0}

        residence=res[residence]
        gender=gen[gender]
        maritalstatus=msts[maritalstatus]
        worktype=wktype[worktype]
        smoke=smke[smoke]
        hypertension=hypten[hypertension]
        heartdisease=hrtdis[heartdisease]


        model=pd.read_pickle('strokenew.pkl')

        array = [[gender,age,hypertension,heartdisease,maritalstatus,worktype,residence,gluclevel,bmi,smoke]]

        array = [np.array(array[0],dtype = 'float64')]
        pred_stroke = model.predict(array)
        result = int(pred_stroke[0])

        str=""
        if result ==0:
             str = name + ", you will not get stroke 😀"
        else:
            str = name + ", you will get stroke 😔"
        return render_template('predict.html',a = str)

        # if result == 1:
        #    str = name + ", you will get a stroke 😔"
        # elif result == 0:
        #    str = name + ", you will no  get a stroke 😀"
        # else:
        #    str = "Invalid result value! Please enter 0 or 1."

        insert_history(name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension,
                       heartdisease, str)

        # Return the result
        return render_template('predict.html', a=str)
@app.route('/cta')
def cta():
    return render_template('cta.html')

@app.route('/counsel')
def counsel():
    return render_template('counsel.html')

@app.route('/history')
def history():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prediction_history")
    records = cursor.fetchall()
    conn.close()
    return render_template('history.html', records=records)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_history(id):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prediction_history WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return ('', 204)  # Return an empty response with a 204 status code



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)