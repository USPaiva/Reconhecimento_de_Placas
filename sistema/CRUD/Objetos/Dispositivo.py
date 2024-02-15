import cv2
import os
import time
import CRUD.Objetos.Conexao as C

class Dispositivo:
    
    def __init__(self):
        self.video_source = Dispositivo.buscar_nomes_cameras() #Dispositivo.busca("cel")[1] #"http://172.17.29.229:8080/videofeed"
        self.create_output_folder()

    def create_output_folder(self):
        self.output_folder = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'Captura')
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def connect_and_capture(self):
        video_capture = cv2.VideoCapture(self.video_source)
        ret, frame = video_capture.read()
        if ret:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{self.output_folder}/photo_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            salvo = filename
            print(f"Foto capturada e salva em: {filename}")
        video_capture.release()
        return salvo
    
    def busca(nome):
        # Monta o comando SQL para buscar o registro
        sql = "SELECT * FROM dispositivo WHERE Nome = %s"
        C.Conexao.cursor.execute(sql, (nome,))
        result = C.Conexao.cursor.fetchone()
        return result
    
    def busca2(Dispositivo):
        # Monta o comando SQL para buscar o registro
        sql = "SELECT * FROM dispositivo WHERE Dispositivo = %s"
        C.Conexao.cursor.execute(sql, (Dispositivo,))
        result = C.Conexao.cursor.fetchone()
        return result

    def Registro(Dispositivo, Nome, In_Out):
        sql3 = "INSERT INTO dispositivo (Dispositivo, Nome, In_Out ) VALUES (%s,%s,%s)"
        val3 = (Dispositivo, Nome, In_Out)
        C.Conexao.cursor.execute(sql3, val3)
        C.Conexao.db.commit()
    
    def delete(nome):
        # Monta o comando SQL para deletar o registro do banco de dados
        sql = "DELETE FROM dispositivo WHERE Nome = %s"
        C.Conexao.cursor.execute(sql, (nome,))
        C.Conexao.db.commit()
    

    def update(Dispositivo, Nome, idDispositivo, In_Out):
        print(idDispositivo)
        sql5 = "UPDATE dispositivo SET Dispositivo=%s, Nome=%s, In_Out=%s WHERE idDispositivo = %s "
        val5 = (Dispositivo, Nome, In_Out, idDispositivo)
        C.Conexao.cursor.execute(sql5, val5)
        C.Conexao.db.commit()
    
    def busca_todas_cameras():
        sql = "SELECT dispositivo FROM dispositivo"
        C.Conexao.cursor.execute(sql)
        results = C.Conexao.cursor.fetchall()

        # Crie uma lista para armazenar os valores de vídeo encontrados no banco de dados
        video_sources = []

        # Itere sobre os resultados da consulta e adicione os valores à lista de video_sources
        for result in results:
            video_sources.append(result[0])

        return video_sources
    
    def buscar_nomes_cameras():
        sql = "SELECT Nome FROM dispositivo"
        C.Conexao.cursor.execute(sql)
        results = C.Conexao.cursor.fetchall()

        # Crie uma lista para armazenar os valores de vídeo encontrados no banco de dados
        video_sources = []

        # Itere sobre os resultados da consulta e adicione os valores à lista de video_sources
        for result in results:
            video_sources.append(result[0])

        return video_sources