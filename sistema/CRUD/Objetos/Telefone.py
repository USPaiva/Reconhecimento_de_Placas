import CRUD.Objetos.Conexao as C
import CRUD.Objetos.Veiculo as V
import re

class Telefone:
    
    def init(self, idTelefone, telefone, Pessoa_idPessoa):
        self.idTelefone = idTelefone
        self.telefone = telefone
        self.Pessoa_idPessoa = Pessoa_idPessoa

    def registro(pessoa, placa, modelo, marca, telefone):
        sql5 = "INSERT INTO relacao (Pessoa_idPessoa, Veiculo_idVeiculo) VALUES (%s, %s)"
        val5 = (pessoa,V.Veiculo.registro(placa, modelo, marca))
        C.Conexao.cursor.execute(sql5, val5)
        sql6 = "INSERT INTO telefone (telefone, Pessoa_idPessoa) VALUES (%s, %s)"
        val6 = (telefone,pessoa)
        C.Conexao.cursor.execute(sql6, val6)
        C.Conexao.db.commit()
    
    def registro_Operador(telefone,pessoa):
        sql6 = "INSERT INTO telefone (telefone, Pessoa_idPessoa) VALUES (%s, %s)"
        val6 = (telefone,pessoa)
        C.Conexao.cursor.execute(sql6, val6)
        C.Conexao.db.commit()

    def delete(IdTelefone, IdRelacao):
        # Monta o comando SQL para deletar o registro do banco de dados
        sql = "DELETE FROM telefone WHERE idTelefone = %s"
        C.Conexao.cursor.execute(sql, (IdTelefone,))
        sql5 = "DELETE FROM relacao WHERE idRelacao = %s"
        C.Conexao.cursor.execute(sql5, (IdRelacao,))
        C.Conexao.db.commit()
    
    def delete(IdTelefone):
        # Monta o comando SQL para deletar o registro do banco de dados
        sql = "DELETE FROM telefone WHERE idTelefone = %s"
        C.Conexao.cursor.execute(sql, (IdTelefone,))
        C.Conexao.db.commit()

    def update(telefone, IdPessoa):
        sql5 = "UPDATE telefone SET telefone=%s WHERE Pessoa_idPessoa=%s "
        val5 = (telefone, IdPessoa)
        C.Conexao.cursor.execute(sql5, val5)
        C.Conexao.db.commit()
    
    def validar_telefone(telefone):
        # Verificar se o telefone possui exatamente 10 dígitos
        return re.match(r'^\d{10,11}$', telefone) is not None
