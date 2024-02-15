import CRUD.Objetos.Conexao as C
import re

class Endereco:
    
    def __init__(self, idEndereco, Estado, Cidade, CEP, Rua, Complemento):
        self.idEndereco = idEndereco
        self.Estado = Estado
        self.Cidade = Cidade
        self.CEP = CEP
        self.Rua = Rua
        self.Complemento = Complemento
    
    def registro(estado, cidade, cep, rua, complemento):
        sql2 = "INSERT INTO endereco (Estado, Cidade, CEP, Rua, Complemento) VALUES (%s, %s, %s, %s, %s)"
        val2 = (estado, cidade, cep, rua, complemento)
        C.Conexao.cursor.execute(sql2, val2)
        return C.Conexao.cursor.lastrowid
    
    def delete(IdEdenreco):
        sql4 = "DELETE FROM endereco WHERE idEndereco = %s"
        C.Conexao.cursor.execute(sql4, (IdEdenreco,))
        C.Conexao.db.commit()

    def update(estado, cidade, cep, rua, complemento, IdPessoa):
        sql2 = "UPDATE Endereco SET Estado=%s, Cidade=%s, CEP=%s, Rua=%s, Complemento=%s WHERE idEndereco=(SELECT Endereco_idEndereco FROM Pessoa WHERE idPessoa=%s)"
        val2 = (estado, cidade, cep, rua, complemento, IdPessoa)
        C.Conexao.cursor.execute(sql2, val2)
        C.Conexao.db.commit()
        
    def validar_estado(estado):
        # Verificar se o estado possui exatamente 2 letras maiúsculas
        return re.match(r'^[A-Z]{2}$', estado) is not None

    def validar_cidade_rua(cidade):
        # Verificar se a cidade possui apenas letras e espaços
        return re.match(r'^[a-zA-Z\s]{3,}$', cidade) is not None

    def validar_cep(cep):
        # Verificar se o CEP possui exatamente 8 dígitos
        return re.match(r'^\d{8}$', cep) is not None