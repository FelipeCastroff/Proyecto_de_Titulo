#from flask.globals import session
#from sqlalchemy import schema
#from .entities.entity import Session, engine, Base
#from .entities.exam import Exam, ExamSchema
from dis import dis
from flask import Flask, jsonify, request, flash
from flask.wrappers import Response
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import base64
import scipy.io as sio
from typing import List, Dict
import shutil
import sys
import os
import json
import mysql.connector
sys.path.insert(1, 'Reidmen Fenics/ipnyb propagation')
from dotenv import load_dotenv
load_dotenv()
###### Se utiliza la linea 22 en vez de la 18 cuando se utiliza docker #####
#sys.path.insert(1, 'src/Reidmen Fenics/ipnyb propagation')
from TimeSimTransIsoMatCij2D_test import fmain
# creating the Flask application
app = Flask(__name__)


### INICIO DE BASE DE DATOS CON DISTINTAS FORMAS ###

### FORMA 1 ###

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PORT'] =  os.getenv('MYSQL_PORT')
#app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'proyecto_v01' # proyecto-v01 para win y proyecto_v01 para linux
app.config['CORS_HEADERS'] = 'Content-Type'

### FORMA 2 ###
### Trae la informacion del .env ###

# app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') #localhost or 172.20.0.3
# app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
# app.config['MYSQL_PORT'] =  os.getenv('MYSQL_PORT')
# app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
# app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
# app.config['CORS_HEADERS'] = os.getenv('CORS_HEADERS')

### FORMA 3 ###

# config = {
#         'user': 'UserBDAT',
#         'password': 'informatica110997',
#         'host': 'basedatos',
#         'port': '3306',
#         'database': 'BDAT_FE_simulations'
#     }

####### Prueba para ver el problema con docker y la base de datos #####

##### Creacion de la config para la prueba que realizo en @app.route(/test) ######

# def favorite_colors() -> List[Dict]:
#     config = {
#         'user': 'UserBDAT',
#         'password': 'informatica110997',
#         'host': 'basedatos',
#         'port': '3306',
#         'database': 'knights'
#         #'host': '0.0.0.0'
#     }
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM favorite_colors')
#     results = [{name: color} for (name, color) in cursor]
#     cursor.close()
#     connection.close()

#     return results

# def getMysqlConnection():
#     return mysql.connector.connect( user='UserBDAT', 
#                                     password='informatica110997', 
#                                     host='mysql', 
#                                     port='3306', 
#                                     database='knights')

mysql = MySQL(app)
CORS(app)




@app.route('/')
def Index():
    # print("test", config)
    # connection = mysql.connector.connect(**config)
    # cursor = connection.cursor()
    # #cursor.execute('SELECT * FROM testtable')
    # # cursor.execute('''CREATE TABLE IF NOT EXISTS timesimtransisomat_first_step01 (
    # # id int NOT NULL AUTO_INCREMENT,
    # # n_transmitter int NOT NULL,
    # # n_receiver int NOT NULL,
    # # distance float DEFAULT NULL,
    # # plate_thickness int NOT NULL,
    # # porosity decimal(10,0) NOT NULL,
    # # result_step_01 text,
    # # p_status text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
    # # time time DEFAULT NULL,
    # # image blob,
    # # PRIMARY KEY (`id`)
    # # )''')
    # #results = [{name: color} for (name, color) in cursor]
    # # cursor.close()
    # # connection.close()

    # connection = mysql.connector.connect(**config)
    # cursor = connection.cursor()
    # cursor.execute("INSERT INTO timesimtransisomat_first_step01 (n_transmitter, n_receiver, distance, plate_thickness, porosity, p_status) VALUES (%s,%s,%s,%s,%s,%s)",
    #             (9, 9, 9, 9, 9, 9))

    # cursor.close()
    # connection.close()
    
    # cur = mysql.connection.cursor()
    # mysql.connection.commit()
    # cur.close()
    #return '<h1>Hello world<h1>'
    return "ok"
###Backup###
# @app.route('/Test')
# def test() -> str:
#     return json.dumps({'favorite_colors': favorite_colors()})

############


@app.route('/Test')
def test():
    db = getMysqlConnection()
    print(db)
    try:
        sqlstr = "'SELECT * FROM favorite_colors'"
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
        output_json = "rip"
    finally:
        db.close()
    return jsonify(results=output_json)

    #return json.dumps({'favorite_colors': favorite_colors()})


@app.route('/Input_data', methods=['POST'])
def input_data():
    #print(request.json['status'])
    #print(request)
    n_transmitter = request.json['n_transmitter'],
    n_receiver = request.json['n_receiver'],
    distance = request.json['distance'],
    plate_thickness = request.json['plate_thickness'],
    porosity = request.json['porosity']
    status = request.json['status']
    print("Distance", distance)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO timesimtransisomat_first_step01 (n_transmitter, n_receiver, distance, plate_thickness, porosity, p_status) VALUES (%s,%s,%s,%s,%s,%s)",
                (n_transmitter, n_receiver, distance, plate_thickness, porosity, status))
    mysql.connection.commit()

    flash('data Added successfully')
    return 'ok'


@app.route('/Load_data', methods=['GET'])
def load_data():
    data_t = []
    # connection = mysql.connector.connect(**config)
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM timesimtransisomat_first_step01')
    # data = cursor.fetchall()
    # cursor.close()
    # connection.close()
    #connection = mysql.connector.connect(**config)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM timesimtransisomat_first_step01')
    data = cur.fetchall()
    #mysql.connection.commit()
    cur.close()
    #connection.close()
    for doc in data:
        data_t.append({
            'id': doc[0],
            'n_transmitter': doc[1],
            'n_receiver': doc[2],
            'distance': doc[3],
            'plate_thickness': doc[4],
            'porosity': float(doc[5]),
            'p_status' : doc[7]
        })
    print("aaa", data)
    
    #return (data)
    #return  json.dump(data_t)
    #return data_t
    return jsonify(data_t)

@app.route('/Load_data/<id>', methods=['GET'])
def load_data_id(id):
    data_t = []
    sub_id = id
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM timesimtransisomat_first_step01 WHERE id = {0}".format(sub_id))
    data = cur.fetchall()
    cur.close()
    for doc in data:
        data_t.append({
            'id': doc[0],
            'n_transmitter': doc[1],
            'n_receiver': doc[2],
            'distance': doc[3],
            'plate_thickness': doc[4],
            'porosity': float(doc[5]),
            'p_status' : doc[7],
            'time' : str(doc[8])
        })
    return jsonify(data_t)

@app.route('/Load_data/porosity/<v>', methods=['GET'])
def load_data_porosity(v):
    #print(request)
    data_t = []
    poro = v
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM timesimtransisomat_first_step01 WHERE porosity = {0}".format(poro))
    data = cur.fetchall()
    print(data)
    cur.close()
    for doc in data:
        data_t.append({
            'id': doc[0],
            'n_transmitter': doc[1],
            'n_receiver': doc[2],
            'distance': doc[3],
            'plate_thickness': doc[4],
            'porosity': float(doc[5]),
            'p_status' : doc[7]
        })
    return jsonify(data_t)
    #print (data)

@app.route('/Load_data/distance/<v>', methods=['GET'])
def load_data_distance(v):
    #print(request)
    data_t = []
    distance = v
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM timesimtransisomat_first_step01 WHERE distance like {0}".format(distance))
    data = cur.fetchall()
    cur.close()
    for doc in data:
        data_t.append({
            'id': doc[0],
            'n_transmitter': doc[1],
            'n_receiver': doc[2],
            'distance': doc[3],
            'plate_thickness': doc[4],
            'porosity': float(doc[5]),
            'p_status' : doc[7]
        })
    return jsonify(data_t)

@app.route('/Load_data/download/<v>', methods=['GET'])
def load_data_download(v):
    cur = mysql.connection.cursor()
    cur.execute("select result_step_01 from timesimtransisomat_first_step01 WHERE id = {0}".format(v))
    datadownload = cur.fetchone()
    datadownload1 = datadownload[0]
    print("aber:", datadownload1)
    shutil.copy("Reidmen Fenics/ipnyb propagation/Files_mat/"+datadownload1, "../../frontend/src/Components/download/matfile.mat")
    return jsonify(datadownload1)

@app.route('/load_data_PUT/<id>', methods=['PUT'])
def load_result_id_put(id):
    sub_id = id

    n_transmitter = request.json['n_transmitter']
    n_receiver = request.json['n_receiver']
    distance = request.json['distance']
    plate_thickness = request.json['plate_thickness']
    porosity = request.json['porosity']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE timesimtransisomat_first_step01 SET p_status = 'In progress'  WHERE id = {0};".format(sub_id))
    mysql.connection.commit()
    filename,time = fmain(n_transmitter,n_receiver,distance,plate_thickness,porosity,sub_id)
    print("Nombre archivo",filename)
    cur = mysql.connection.cursor()
    sql = "UPDATE timesimtransisomat_first_step01 SET result_step_01 = %s, p_status = 'Done', time = %s  WHERE id = %s;"
    cur.execute(sql,(filename,time,sub_id))
    mysql.connection.commit()
    return('Ok')


@app.route('/Load_data_test/<id>', methods=['GET'])
def load_data_id_test(id):
    data_t = []
    sub_id = id
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM timesimtransisomat_first_step01 WHERE id = {0}".format(sub_id))
    data = cur.fetchall()
    cur.close()
    for doc in data:
        data_t.append({
            'id': doc[0],
            'n_transmitter': doc[1],
            'n_receiver': doc[2],
            'distance': doc[3],
            'plate_thickness': doc[4],
            'porosity': float(doc[5]),
            'result_step_01': doc[6],
            'p_status' : doc[7],
            'time' : str(doc[8])
        })
    return jsonify(data_t)





@app.route('/Result')
def result():
    return 'result'

if __name__ == '__main__':
    # port=80 cuando se levanta con docker #
    app.run(port=3000, debug=True, host="0.0.0.0")
