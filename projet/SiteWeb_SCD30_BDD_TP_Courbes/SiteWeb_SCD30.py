from flask import Flask, render_template,request
import socket
import time
import sqlite3
# *******pour tracer les courbes*****
from io import BytesIO
import base64
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
#************************************
global Nrecords
Nrecords  =  50
def recupération_dernière_valeur():
    connexion = sqlite3.connect('BDD\Capteurs.db')
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM DHT11_data ORDER BY ROWID DESC LIMIT 1")
    for record in curseur:
        numero =record[0]
        temps = record[1][0:16]
        humidité  = record[2];température = record[3];CO2 = record[4]        
    connexion.close()
    return temps,humidité,température,CO2
def recuperation_historique_BDD(Nrecords):
    connexion = sqlite3.connect('BDD\Capteurs.db')
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM DHT11_data ORDER BY ROWID DESC LIMIT "+str(Nrecords))
    # de la plus récente à la plus ancienne valeur donc à  inverser pour les courbes
    données  = curseur.fetchall()
    numéro  = [];temps= [];humidité = [];température = [];dioxyde_carbone = []
    for row in reversed(données):
        numéro.append(row[0])
        temps.append(row[1])
        humidité.append(row[2])
        température.append(row[3])
        dioxyde_carbone.append(row[4])
    return numéro,temps, humidité,température,dioxyde_carbone      
    connexion.close()   
def courbes(Nrecords):
    img = BytesIO()
    numéro,temps,humidité,température,CO2  = recuperation_historique_BDD(Nrecords)
    plt.figure(figsize=(10,4))
    plt.rcParams['font.size'] = '7'
    plt.subplot(131)
    plt.plot(numéro,humidité)
    plt.title("humidité en %")
    plt.ylim(0,100)
    plt.grid()
    plt.subplot(132)
    plt.plot(numéro,température)
    plt.title("température en ° C")
    plt.ylim(10,30)
    plt.grid()
    plt.subplot(133)
    plt.plot(numéro,CO2)
    plt.ylim(0,5000)
    plt.grid()
    plt.title("TAUX DE CO2  en ppm")
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot = base64.b64encode(img.getvalue()).decode('utf8')
    return plot
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index_TP10_Courbes():
     global Nrecords
     temps,humidité,température,dioxyde_carbone = recupération_dernière_valeur()
     if request.method == 'POST':
         Nrecords  = int(request.form['NENREG'])
     plot  = courbes(Nrecords)
     return render_template("index_SCD30_Courbes.html",HEURE =  temps,TEMP = température ,HUM = humidité,CO2  = dioxyde_carbone ,NENREG  = Nrecords,plot_url = plot)
if __name__ == "__main__":
    hostname = socket.gethostname()
    app.run(host='127.0.0.1',debug=False,port=5000)