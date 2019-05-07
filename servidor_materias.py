from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(user = "root", database = "clases")

cursor = conexion.cursor()
cursor_profe = conexion.cursor()
cursor_materia = conexion.cursor()
cursor_aula = conexion.cursor()
cursor_edificio = conexion.cursor()

@app.route("/api/v1/clases/")

def sacar_clases():
    query = "SELECT * FROM clase"
    cursor.execute(query)
    clases = cursor.fetchall()
    lista_clases = []

    for clase in clases:
        c={
        "NRC" : clase[0],
        "Seccion" : clase[1],
        "Cupos" : clase[2],
        "Cupos disponibles" : clase[3],
        "Horario" : clase[4],
        "Dias" : clase[5],
        "Periodo" : clase[6],
        "Profesor" : clase[7],
        "Materia" : clase[8],
        "Aula" : clase[9]
        }
        query_prof = "SELECT * FROM profesor"
        cursor_profe.execute(query_prof)
        profesores = cursor_profe.fetchall()
        for profe in profesores:
            if c["Profesor"] == profe[0]:
                c["Profesor"] = profe[1]

        query_materia = "SELECT * FROM materia"
        cursor_materia.execute(query_materia)
        materias = cursor_materia.fetchall()
        for materia in materias:
            if c["Materia"] == materia[0]:
                c["Materia"] = m={
                    "Clave" : materia[1],
                    "Nombre" : materia[2],
                    "Creditos" : materia[3]
                }

        query_aula = "SELECT * FROM aula"
        cursor_aula.execute(query_aula)
        aulas = cursor_aula.fetchall()
        for aula in aulas:
            if c["Aula"] == aula[0]:
                c["Aula"] = a={
                    "Salon" : aula[1],
                    "Edificio" : aula[2]
                }
        query_edif = "SELECT * FROM edificio"
        cursor_edificio.execute(query_edif)
        edificios = cursor_edificio.fetchall()
        for edificio in edificios:
            if a["Edificio"] == edificio[0]:
                a["Edificio"] = edificio[1]

        lista_clases.append(c)

    return jsonify(lista_clases)

app.run()
