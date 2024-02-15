import CRUD.Objetos.Conexao as C
import CRUD.Objetos.Veiculo as V
import time
class Log:
    
    def __init__(self, idLog, Data_hora, In_Out, Acesso_idAcesso, CodigoLeitura, Status, Veiculo_idVeiculo, Dispositivo_idDispositivo):
        self.idLog = idLog
        self.Data_hora = Data_hora
        self.In_Out = In_Out
        self.Acesso_idAcesso = Acesso_idAcesso
        self.CodigoLeitura = CodigoLeitura
        self.Status = Status
        self.Veiculo_idVeiculo = Veiculo_idVeiculo
        self.Dispositivo_idDispositivo = Dispositivo_idDispositivo

    def acesso(Placa):
        if V.Veiculo.busca(Placa) != None:
            return V.Veiculo.busca(Placa)[12]
        else:
            return False
    
    def controle(Placa, IDdispositivo, caminho):
        idveiculo = Log.acesso(Placa)
        print(idveiculo)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp)
        if idveiculo != False:
            status = 1 
            sql3 = "INSERT INTO Log (Data_hora, CodigoLeitura, Status, Veiculo_idVeiculo, Dispositivo_idDispositivo, Caminho) VALUES (%s, %s, %s, %s,%s,%s)"
            val3 = (timestamp,Placa,status,idveiculo,IDdispositivo, caminho)
            C.Conexao.cursor.execute(sql3, val3)
            C.Conexao.db.commit()
        else:
            status = 0
            sql3 = "INSERT INTO Log (Data_hora, CodigoLeitura, Status, Dispositivo_idDispositivo, Caminho) VALUES (%s, %s, %s,%s,%s)"
            val3 = (timestamp,Placa,status,IDdispositivo, caminho)
            C.Conexao.cursor.execute(sql3, val3)
            C.Conexao.db.commit()
        return status

    def controle2(Placa, IDdispositivo, caminho):
        idveiculo = Log.acesso(Placa)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        status = 1 
        sql3 = "INSERT INTO Log (Data_hora, CodigoLeitura, Status, Dispositivo_idDispositivo, Caminho) VALUES (%s, %s, %s,%s,%s)"
        val3 = (timestamp,Placa,status,IDdispositivo, caminho)
        C.Conexao.cursor.execute(sql3, val3)
        C.Conexao.db.commit()
        return status