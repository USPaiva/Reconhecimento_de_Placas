import CRUD.Objetos.Conexao as C
import CRUD.Objetos.Documentos as D
import CRUD.Objetos.Endereco as E
import re

class Pessoa:
    
    def __init__(self, idPessoa, Nome, Sobrenome, Documentos_idDocumentos, Endereco_idEndereco, RG, CPF, Estado, Cidade, CEP, Rua, Complemento, idVeiculo, Placa, Modelo, Marca, idTelefone, telefone, idrelacao):
        self.idPessoa = idPessoa
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.Documentos_idDocumentos = Documentos_idDocumentos
        self.Endereco_idEndereco = Endereco_idEndereco
        self.RG = RG
        self.CPF = CPF
        self.Estado = Estado
        self.Cidade = Cidade
        self.CEP = CEP
        self.Rua = Rua
        self.Complemento = Complemento
        self.idVeiculo = idVeiculo
        self.Placa = Placa
        self.Modelo = Modelo
        self.Marca = Marca
        self.idTelefone = idTelefone
        self.telefone = telefone
        self.idrelacao = idrelacao

    def validar_nome(nome):
        # Verificar se o nome possui apenas letras e espaços
        return re.match(r'^[a-zA-Z\s]{3,}$', nome) is not None
    
    def registro(rg, cpf, estado, cidade, cep, rua, complemento, nome, sobrenome):
        sql3 = "INSERT INTO pessoa (Nome, Sobrenome, Documentos_idDocumentos, Endereco_idEndereco) VALUES (%s, %s, %s, %s)"
        val3 = (nome, sobrenome, D.Documentos.registro(rg,cpf), E.Endereco.registro(estado, cidade, cep, rua, complemento))
        C.Conexao.cursor.execute(sql3, val3)
        return C.Conexao.cursor.lastrowid
    
    def delete(IdPessoa):
        sql2 = "DELETE FROM pessoa WHERE idPessoa = %s"
        C.Conexao.cursor.execute(sql2, (IdPessoa,))
        C.Conexao.db.commit()

    def update(nome, sobrenome, IdPessoa):
        sql3 = "UPDATE Pessoa SET Nome=%s, Sobrenome=%s WHERE idPessoa=%s"
        val3 = (nome, sobrenome, IdPessoa)
        C.Conexao.cursor.execute(sql3, val3)
        C.Conexao.db.commit()