import CRUD.Objetos.Conexao as C

class Login:
    
    def init(self, idLogin, Usuario, Senha, Pessoa_idPessoa, Cargo_idCargo):
        self.idLogin = idLogin
        self.Usuario = Usuario
        self.Senha = Senha
        self.Pessoa_idPessoa = Pessoa_idPessoa
        self.Cargo_idCargo = Cargo_idCargo
        
    def login(Usuario, Senha):
        sql = "SELECT * FROM login WHERE user = %s and senha = %s"
        value = (Usuario,Senha)
        C.Conexao.cursor.execute(sql, value)
        result = C.Conexao.cursor.fetchone()
        return result    
    
    def registro(Usuario,Senha,pessoa,Cargo):
        sql3 = "INSERT INTO login (User, Senha, Pessoa_idPessoa, Cargo_idCargo) VALUES (%s, %s, %s,%s)"
        val3 = (Usuario,Senha,pessoa,Cargo)
        C.Conexao.cursor.execute(sql3, val3)
        C.Conexao.db.commit()
    
    def delete(IdLogin):
        # Monta o comando SQL para deletar o registro do banco de dados
        sql = "DELETE FROM login WHERE idLogin = %s"
        C.Conexao.cursor.execute(sql, (IdLogin,))
        C.Conexao.db.commit()
    

    def update(Usuario, Senha, Cargo, IdPessoa):
        sql5 = "UPDATE login SET User=%s, Senha=%s, Cargo_idCargo=%s WHERE Pessoa_idPessoa=%s "
        val5 = (Usuario, Senha, Cargo, IdPessoa)
        C.Conexao.cursor.execute(sql5, val5)
        C.Conexao.db.commit()