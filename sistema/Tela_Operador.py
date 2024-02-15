import tkinter as tk
from tkinter import ttk
import CRUD.Objetos.Telefone as T;
import CRUD.Objetos.Pessoa as P;
import CRUD.Objetos.Endereco as E;
import CRUD.Objetos.Documentos as D;
import CRUD.Objetos.Login as L;

class Tela_Operador:
    def __init__(self):
        # Cria a janela principal da aplicação
        self.root = tk.Tk()
        self.root.title("Cadastro de Operadores")
        self.root.geometry("600x500")

        #O frame principal
        frame_principal = tk.Frame(self.root, padx=10, pady=10)
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("TLabel", font=("Helvetica", 12))
        
        #As labels e os campos de entrada de dados
        label_nome = ttk.Label(frame_principal, text="Nome:")
        label_nome.grid(row=1, column=0, pady=5)
        self.campo_nome = ttk.Entry(frame_principal)
        self.campo_nome.grid(row=1, column=1, pady=5)

        label_sobrenome = ttk.Label(frame_principal, text="Sobrenome:")
        label_sobrenome.grid(row=1, column=2, pady=5)
        self.campo_sobrenome = ttk.Entry(frame_principal)
        self.campo_sobrenome.grid(row=1, column=3, pady=5)

        label_rg = ttk.Label(frame_principal, text="RG:")
        label_rg.grid(row=2, column=0, pady=5)
        self.campo_rg = ttk.Entry(frame_principal)
        self.campo_rg.grid(row=2, column=1, pady=5)

        label_cpf = ttk.Label(frame_principal, text="CPF:")
        label_cpf.grid(row=2, column=2, pady=5)
        self.campo_cpf = ttk.Entry(frame_principal)
        self.campo_cpf.grid(row=2, column=3, pady=5)

        label_estado = ttk.Label(frame_principal, text="Estado:")
        label_estado.grid(row=3, column=0, pady=5)
        self.campo_estado = ttk.Entry(frame_principal)
        self.campo_estado.grid(row=3, column=1, pady=5)

        label_cidade = ttk.Label(frame_principal, text="Cidade:")
        label_cidade.grid(row=3, column=2, pady=5)
        self.campo_cidade = ttk.Entry(frame_principal)
        self.campo_cidade.grid(row=3, column=3, pady=5)

        label_cep = ttk.Label(frame_principal, text="CEP:")
        label_cep.grid(row=4, column=0, pady=5)
        self.campo_cep = ttk.Entry(frame_principal)
        self.campo_cep.grid(row=4, column=1, pady=5)

        label_rua = ttk.Label(frame_principal, text="Rua:")
        label_rua.grid(row=4, column=2, pady=5)
        self.campo_rua = ttk.Entry(frame_principal)
        self.campo_rua.grid(row=4, column=3, pady=5)

        label_complemento = ttk.Label(frame_principal, text="Complemento:")
        label_complemento.grid(row=5, column=0, pady=5)
        self.campo_complemento = ttk.Entry(frame_principal)
        self.campo_complemento.grid(row=5, column=1, pady=5)
        
        label_Telefone = ttk.Label(frame_principal, text="Telefone:")
        label_Telefone.grid(row=5, column=2, pady=5)
        self.campo_Telefone = ttk.Entry(frame_principal)
        self.campo_Telefone.grid(row=5, column=3, pady=5)
        #usuario
        label_Usuario = ttk.Label(frame_principal, text="Usuario:")
        label_Usuario.grid(row=6, column=0, pady=5)
        self.campo_Usuario = ttk.Entry(frame_principal)
        self.campo_Usuario.grid(row=6, column=1, pady=5)
        #cargo
        label_Senha = ttk.Label(frame_principal, text="Senha:")
        label_Senha.grid(row=7, column=2, pady=5)
        self.campo_Senha = ttk.Entry(frame_principal)
        self.campo_Senha.grid(row=7, column=3, pady=5)
        #Senha
        label_Cargo = ttk.Label(frame_principal, text="Cargo:")
        label_Cargo.grid(row=7, column=0, pady=5)
        self.campo_Cargo = ttk.Entry(frame_principal)
        self.campo_Cargo.grid(row=7, column=1, pady=5)

        label_busca = ttk.Label(frame_principal, text="buscar Funcionario (CPF):")
        label_busca.grid(row=0, column=0, padx=2)
        self.campo_busca = ttk.Entry(frame_principal)
        self.campo_busca.grid(row=0, column=1)
        

        #botões
        botao_cadastro = ttk.Button(frame_principal, text="Cadastrar", command= self.cadastrar)
        botao_cadastro.grid(row=12, column=0, pady=10)

        botao_editar = ttk.Button(frame_principal, text="buscar", command= self.buscar)
        botao_editar.grid(row=0, column=2, padx=5)

        botao_deletar = ttk.Button(frame_principal, text="Deletar", command= self.deletar)
        botao_deletar.grid(row=12, column=1, pady=10)

        botao_deletar = ttk.Button(frame_principal, text="Atualizar", command= self.Atualizar)
        botao_deletar.grid(row=12, column=2, pady=10)
        botao_deletar = ttk.Button(frame_principal, text="Limpar", command= self.limpar)
        botao_deletar.grid(row=12, column=3, pady=10)
        
    def limpar(self):
            # Limpa os campos de entrada
            self.campo_nome.delete(0, tk.END)
            self.campo_sobrenome.delete(0, tk.END)
            self.campo_rg.delete(0, tk.END)
            self.campo_cpf.delete(0, tk.END)
            self.campo_estado.delete(0, tk.END)
            self.campo_cidade.delete(0, tk.END)
            self.campo_cep.delete(0, tk.END)
            self.campo_rua.delete(0, tk.END)
            self.campo_complemento.delete(0, tk.END)
            self.campo_Telefone.delete(0, tk.END)
            self.campo_Usuario.delete(0,tk.END)
            self.campo_Senha.delete(0,tk.END)
            self.campo_Cargo.delete(0,tk.END)
        
            
    def cadastrar(self):
            nome = self.campo_nome.get()
            sobrenome = self.campo_sobrenome.get()
            rg = self.campo_rg.get()
            cpf = self.campo_cpf.get()
            estado = self.campo_estado.get()
            cidade = self.campo_cidade.get()
            cep = self.campo_cep.get()
            rua = self.campo_rua.get()
            complemento = self.campo_complemento.get()
            telefone = self.campo_Telefone.get()
            Usuario = self.campo_Usuario.get()
            Senha = self.campo_Senha.get()
            Cargo = self.campo_Cargo.get()
            
            if self.validação(nome,sobrenome,rg,cpf,estado,cidade,rua,cep,telefone)== False:
                pessoa = P.Pessoa.registro(rg, cpf, estado, cidade, cep, rua, complemento, nome, sobrenome)
                T.Telefone.registro_Operador(telefone,pessoa)
                L.Login.registro(Usuario,Senha,pessoa,Cargo)
                self.limpar()
            else:
                return
            
            
    def Atualizar(self):
            nome = self.campo_nome.get()
            sobrenome = self.campo_sobrenome.get()
            rg = self.campo_rg.get()
            cpf = self.campo_cpf.get()
            estado = self.campo_estado.get()
            cidade = self.campo_cidade.get()
            cep = self.campo_cep.get()
            rua = self.campo_rua.get()
            complemento = self.campo_complemento.get()
            telefone = self.campo_Telefone.get()
            Usuario = self.campo_Usuario.get()
            Senha = self.campo_Senha.get()
            Cargo = self.campo_Cargo.get()
            IdPessoa = D.Documentos.busca(self.campo_busca.get())[0]
            
            if self.validação(nome,sobrenome,rg,cpf,estado,cidade,rua,cep,telefone)== False:
                D.Documentos.update(rg, cpf,IdPessoa)
                P.Pessoa.update(nome, sobrenome,IdPessoa)
                E.Endereco.update(estado, cidade, cep, rua, complemento,IdPessoa)
                T.Telefone.update(telefone, IdPessoa)
                L.Login.update(Usuario, Senha, Cargo, IdPessoa)
                self.limpar()
            else:
                return
            
    def buscar(self):
            cpf = self.campo_busca.get()
            if D.Documentos.busca(cpf):
                # Preenche os campos de entrada com os dados do registro
                self.limpar()
                self.campo_nome.insert(0, D.Documentos.busca(cpf)[1])
                self.campo_sobrenome.insert(0, D.Documentos.busca(cpf)[2])
                self.campo_rg.insert(0, D.Documentos.busca(cpf)[5])
                self.campo_cpf.insert(0, D.Documentos.busca(cpf)[6])
                self.campo_estado.insert(0, D.Documentos.busca(cpf)[7])
                self.campo_cidade.insert(0, D.Documentos.busca(cpf)[8])
                self.campo_cep.insert(0, D.Documentos.busca(cpf)[9])
                self.campo_rua.insert(0, D.Documentos.busca(cpf)[10])
                self.campo_complemento.insert(0, D.Documentos.busca(cpf)[11])
                self.campo_Telefone.insert(0, D.Documentos.busca(cpf)[17])
                
                self.campo_Usuario.insert(0, D.Documentos.busca(cpf)[19])
                self.campo_Senha.insert(0, D.Documentos.busca(cpf)[20])
                self.campo_Cargo.insert(0, D.Documentos.busca(cpf)[21])
            else:
                # Exibe uma mensagem de erro se o registro não for encontrado
                self.limpar()
                tk.messagebox.showerror("Erro", "registro não encontrado.")
                
    def validação(self,nome,sobrenome,rg,cpf,estado,cidade,rua,cep,telefone):
        # Realizar a validação dos campos
            if not P.Pessoa.validar_nome(nome):
                # Nome inválido
                tk.messagebox.showerror("Erro", "Nome inválido. Apenas letras e espaços são permitidos.")
                return True
            
            # Realizar a validação dos campos
            elif not P.Pessoa.validar_nome(sobrenome):
                # Nome inválido
                tk.messagebox.showerror("Erro", "Sobrenome inválido. Apenas letras e espaços são permitidos.")
                return True

            elif not D.Documentos.validar_rg(rg):
                # RG inválido
                tk.messagebox.showerror("Erro", "RG inválido. Deve possuir exatamente 9 dígitos.")
                return True

            elif not D.Documentos.validar_cpf(cpf):
                # CPF inválido
                tk.messagebox.showerror("Erro", "CPF inválido. Deve possuir exatamente 11 dígitos.")
                return True
            
            elif not E.Endereco.validar_estado(estado):
                # Estado inválido
                tk.messagebox.showerror("Erro", "Estado inválido. Deve possuir exatamente 2 letras maiúsculas.")
                return True

            elif not E.Endereco.validar_cidade_rua(cidade):
                # Cidade inválida
                tk.messagebox.showerror("Erro", "Cidade inválida. Apenas letras e espaços são permitidos.")
                return True
            
            elif not E.Endereco.validar_cidade_rua(rua):
                # Cidade inválida
                tk.messagebox.showerror("Erro", "Rua inválida. Apenas letras e espaços são permitidos.")
                return True
            
            elif not E.Endereco.validar_cep(cep):
                # CEP inválido
                tk.messagebox.showerror("Erro", "CEP inválido. Deve possuir exatamente 8 dígitos.")
                return True

            elif not T.Telefone.validar_telefone(telefone):
                # Telefone inválido
                tk.messagebox.showerror("Erro", "Telefone inválido. Deve possuir exatamente 10 dígitos.")
                return True
            else:
                return False
            
    def deletar(self):
            # Obtém o valor do campo de cpf para deletar
            cpf = self.campo_cpf.get()
            if D.Documento.delete(cpf):
                idDocumento = D.Documentos.busca(cpf)[3]
                idEndereco = D.Documentos.busca(cpf)[4]
                idPessoa = D.Documentos.busca(cpf)[0]
                idTelefone = D.Documentos.busca(cpf)[16]
                idLogin = D.Documentos.busca(cpf)[18]
                E.Endereco.delete(idEndereco)
                P.Pessoa.delete(idPessoa)
                T.Telefone.delete(idTelefone)
                L.Login.delete(idLogin)
                D.Documento.delete(idDocumento)
                self.limpar() 

    def run(self):
        self.root.mainloop()

##DEbug
#Tela_Operador().run()