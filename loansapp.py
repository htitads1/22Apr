from flask import Blueprint
import pickle
from sklearn.preprocessing import StandardScaler
loansapp = Blueprint('loansapp',__name__,url_prefix="/loansapp")
from flask import request

@loansapp.route("/loans",methods =["POST"])
def get_loan_info():
    #loan_application = request.get_json()
    loan_application = {}
    data = request.form
    loan_application['Dependents'] = data['Dependents']
    loan_application['Education'] = data['Education']
    loan_application['ApplicantIncome'] = data['ApplicantIncome']
    loan_application['LoanAmount'] = data['LoanAmount']
    loan_application['Credit_History'] = data['Credit_History']
    #print(loan_application["Dependents"])
    return isEligibleForLoan(loan_application)



def isEligibleForLoan(loan_application):
     i1 = loan_application["Dependents"]
     i2 = loan_application["Education"]
     i3 = loan_application["ApplicantIncome"]
     i4 = loan_application["LoanAmount"]
     i5 = loan_application["Credit_History"]
     scalar = StandardScaler()
     with open('scalerloan.pkl','rb') as f1:
      scaler_model = pickle.load(f1)
      data = scaler_model.transform([[i3,i4]])

     #scalar.fit([[90,80]])
     #data = scalar.fit_transform([[4500,3000]])
     
     p1 =data[0,0]
     p2 = data[0,1]
     with open('logisticloannew.pkl','rb') as f:
       loans_model = pickle.load(f)
       #pridiction_result =loans_model.predict([[1,1,1,1,p1,p2,1,2]])
       pridiction_result =loans_model.predict([[int(i1),int(i2),int(p1),int(p2),int(i5)]])  
          
       return str(pridiction_result[0])