import sofa
import sys
import json
import requests
from flask import Flask, jsonify, request
from pandas.io.json import json_normalize

app = Flask(__name__)

@app.route('/run', methods = ['POST'])
def run():
    if request.headers['Content-Type'] == 'application/json':
        content = json.loads(json.dumps(request.json))
        pao_fio =  None
        if( "pao_fio" in content ):
            pao_fio = content["pao_fio"]
            if (pao_fio < 10 or pao_fio > 600):
                return "415 Unsupported Value -- pao_fio \n"
        vent = False
        if( "vent" in content ):
            vent = content["vent"]
            print(vent)
            if ( not (vent == True or vent == False)):
                return "415 Unsupported Value -- vent \n"
        glasgow = None
        MAP = None
        dopamine = None
        dobutamine = None
        epinephrine = None
        norepinephrine = None
        bilirubin = None
        platelets =  None
        creatinine = None
        sscore = sofa.sofa(pao_fio, vent, glasgow,
                            MAP, dopamine, dobutamine,
                            epinephrine, norepinephrine,
                            bilirubin, platelets, creatinine)
        data = {
            'sscore' : sscore,
        }
        json_str = json.dumps(data)
        return json_str + "\n"
    else:
        return "415 Unsupported Media Type ;)"

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    """
    Create a heartbeat function that tests if the sofa function is actually working properly,
    in a production app, this would be an entire unit test suite that would test all boundary conditions for the model
    """
    pao_fio =  80
    vent = False
    glasgow = 7
    MAP = 77 
    dopamine = None
    dobutamine = None
    epinephrine = None
    norepinephrine = None 
    bilirubin = 1.0 
    platelets =  250
    creatinine = 0.75
    sscore = sofa.sofa(pao_fio, vent, glasgow,
         MAP, dopamine, dobutamine,
         epinephrine, norepinephrine,
         bilirubin, platelets, creatinine)
    if (sscore == 5):
        return "App is up and running\n" + str(sscore)
    else:
        return "App is up, but sofa library is not working correctly"

if __name__ == '__main__':
    app.run(debug=True)
