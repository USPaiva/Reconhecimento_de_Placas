import mysql.connector

##from interface import Ui_MainWindow
class Conexao:
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Placa"
            )
        cursor = db.cursor()