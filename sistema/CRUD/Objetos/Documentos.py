import CRUD.Objetos.Conexao as C
import re

class Documentos:
    
    def __init__(self, idDocumentos, RG, CPF):
        self.idDocumentos = idDocumentos
        self.RG = RG
        self.CPF = CPF


    def registro(rg, cpf):
        sql = "INSERT INTO documentos (RG, CPF) VALUES (%s, %s)"
        val = (rg, cpf)
        C.Conexao.cursor.execute(sql, val)
        return C.Conexao.cursor.lastrowid


    def delete(cpf):
        sql = "DELETE FROM documentos WHERE CPF = %s"
        C.Conexao.cursor.execute(sql, (cpf,))
        C.Conexao.db.commit()


    def busca(cpf):
        sql = "SELECT * FROM consulta WHERE CPF = %s"
        C.Conexao.cursor.execute(sql, (cpf,))
        result = C.Conexao.cursor.fetchone()
        return result


    def update(rg, cpf, idPessoa):
        sql = "UPDATE Documentos SET RG = %s, CPF = %s WHERE idDocumentos = (SELECT Documentos_idDocumentos FROM Pessoa WHERE idPessoa = %s)"
        val = (rg, cpf, idPessoa)
        C.Conexao.cursor.execute(sql, val)
        C.Conexao.db.commit()

    def validar_rg(rg):
        # Verificar se o RG possui 8 ou 9 dígitos, permitindo que o último seja "X" ou "x"
        return re.match(r'^\d{8,9}[0-9Xx]$', rg) is not None

    def validar_cpf(cpf):
        # Verificar se o CPF possui exatamente 11 dígitos
        return re.match(r'^\d{11}$', cpf) is not None