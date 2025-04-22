from flask import Blueprint,render_template,url_for,redirect,request
import pickle
import json
app3 = Blueprint('app3',__name__);
@app3.route("/employee", methods=['POST'])
def read_data():
    #data=request.get_json();
    data = request.form
    salary ={}
    salary['years'] = data['years']
    salary['expsal'] = get_salary(data['years']);
    json_sal = json.dumps(salary);
    #response  = app3.response_class(response=json_sal,status=200,mimetype='application/json')
    #return render_template('sal_output?sal='+str(salary['expsal']))
    return str(salary['expsal']),200
    #return render_template('sal_output')




def get_salary(years):
   with open('model_pickle','rb') as f :
      m  = pickle.load(f);
      x= m.predict([[float(years)]])
      return x[0]