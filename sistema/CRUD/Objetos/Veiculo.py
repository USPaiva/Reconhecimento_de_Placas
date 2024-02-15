import CRUD.Objetos.Conexao as C
import re
class Veiculo:
    
    def init(self, idVeiculo, Modelo, Marca, Cor, Placa, Tipo, Proprietario):
        self.idVeiculo = idVeiculo
        self.Modelo = Modelo
        self.Marca = Marca
        self.Cor = Cor
        self.Placa = Placa
        self.Tipo = Tipo
        self.Proprietario = Proprietario
    
    def registro(placa, modelo, marca):
        sql4 = "INSERT INTO veiculo (Placa, Modelo, Marca) VALUES (%s, %s, %s)"
        val4 = (placa, modelo, marca)
        C.Conexao.cursor.execute(sql4, val4)
        return C.Conexao.cursor.lastrowid
    
    def delete(Placa):
        sql6 = "delete FROM veiculo WHERE Placa = %s"
        C.Conexao.cursor.execute(sql6, (Placa,))
        C.Conexao.db.commit()
    
    def busca(placa):
        # Monta o comando SQL para buscar o registro
        sql = "SELECT * FROM consulta WHERE Placa = %s"
        C.Conexao.cursor.execute(sql, (placa,))
        result = C.Conexao.cursor.fetchone()
        return result
    
    def update(placa, modelo, marca, IdPessoa):
        sql4 = "UPDATE Veiculo SET Placa=%s, Modelo=%s, Marca=%s WHERE idVeiculo=(SELECT Veiculo_idVeiculo FROM relacao WHERE Pessoa_idPessoa=%s)"
        val4 = (placa, modelo, marca, IdPessoa)
        C.Conexao.cursor.execute(sql4, val4) 
        C.Conexao.db.commit()
    
    def validar_marca_modelo(marca_modelo):
        # Verificar se a cidade possui apenas letras e espaços
        return re.match(r'^[a-zA-Z\s]{3,}$', marca_modelo) is not None