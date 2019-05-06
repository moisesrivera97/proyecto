import glob
import json
import mysql.connector

conexion = mysql.connector.connect(user = "root", database = "clases")
cursor = conexion.cursor()

files = glob.glob("*.json")

def existe_profesor(clase):
    select = "SELECT * FROM profesor WHERE nombre = %s"
    cursor.execute(select, (clase["Profesor"],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_profesor(clase):
    insert = "INSERT INTO profesor(nombre) VALUES(%s)"
    cursor.execute(insert, (clase["Profesor"],))
    conexion.commit()

    return cursor.lastrowid

def existe_edificio(clase):
    select = "SELECT * FROM edificio WHERE nombre = %s"
    cursor.execute(select, (clase["Edificio"],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_edificio(clase):
    insert = "INSERT INTO edificio(nombre) VALUES(%s)"
    cursor.execute(insert, (clase["Edificio"],))
    conexion.commit()

    return cursor.lastrowid

def get_id_edificio(edificio):
    select = "SELECT id from edificio WHERE nombre = %s"
    cursor.execute(select, (edificio,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_materia(clase):
    select = "SELECT * FROM materia WHERE nombre = %s"
    cursor.execute(select, (clase["Nombre"],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_materia(clase):
    insert = "INSERT INTO materia(clave, nombre, creditos) VALUES(%s, %s, %s)"
    cursor.execute(insert, (clase["Clave"], clase["Nombre"], clase["Creditos"]))
    conexion.commit()

    return cursor.lastrowid

def existe_aula(clase):
    select = "SELECT * from aula WHERE nombre = %s"
    cursor.execute(select, (clase["Aula"],))
    rows = cursor.fetchall()
    if len(rows) > 0:
        for aula in rows:
            if aula[2] == get_id_edificio(clase["Edificio"]):
                return True
        return False
    else:
        return False

def insertar_aula(clase, id):
    insert = "INSERT INTO aula(nombre, id_edificio) VALUES(%s, %s)"
    cursor.execute(insert, (clase["Aula"], id))
    conexion.commit()
    return cursor.lastrowid

def get_id_aula(aula, edificio):
    select = "SELECT * from aula WHERE nombre = %s"
    cursor.execute(select, (aula,))

    rows = cursor.fetchall()
    for aula in rows:
        if aula[2] == get_id_edificio(edificio):
            return aula[0]
    return rows[0][0]

def get_id_profesor(profesor):
    select = "SELECT id from profesor WHERE nombre = %s"
    cursor.execute(select, (profesor,))
    rows = cursor.fetchall()
    return rows[0][0]

def get_id_materia(materia):
    select = "SELECT id from materia WHERE nombre = %s"
    cursor.execute(select, (materia,))
    rows = cursor.fetchall()
    return rows[0][0]

def insertar_clase(clase, id_profe, id_materia ,id_aula):
    insert = "INSERT INTO clase(nrc, seccion, cupos, cupos_disp, horario, dias, periodo, id_profe, id_materia, id_aula) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert, (clase["NRC"], clase["Seccion"], clase["Cupos"], clase["Cupos disponibles"], clase["Horario"], clase["Dias"], clase["Periodo"], id_profe, id_materia, id_aula))
    conexion.commit()

def existe_clase(clase):
    select = "SELECT * FROM clase WHERE nrc = %s"
    cursor.execute(select, (clase["NRC"],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False


for file in files:
    with open(file, encoding = "utf8") as f:
        clases = json.load(f)
        for clase in clases:
            id_edif = 0
            id_profesor = 0
            id_aula = 0
            id_materia = 0
            if not existe_profesor(clase):
                id_profesor = insertar_profesor(clase)
            else:
                id_profesor = get_id_profesor(clase["Profesor"])
            if not existe_edificio(clase):
                id_edif = insertar_edificio(clase)
            else:
                id_edif = get_id_edificio(clase["Edificio"])
            if not existe_materia(clase):
                id_materia = insertar_materia(clase)
            else:
                id_materia = get_id_materia(clase["Nombre"])
            if not existe_aula(clase):
                id_aula = insertar_aula(clase, id_edif)
            else:
                id_aula = get_id_aula(clase["Aula"], clase["Edificio"])

            if not existe_clase(clase):
                insertar_clase(clase, id_profesor, id_materia,id_aula)
