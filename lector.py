import glob
import json
import mysql.connector

conexion = mysql.connector.connect(user = "root", database = "clases")
cursor = conexion.cursor()

files = glob.glob("*.json")


for file in files:
    with open(file, encoding = "utf-8") as f:
        clases = json.load(f)
        
