import tkinter as tk
from tkinter import ttk
import CRUD.Objetos.Telefone as T;
import CRUD.Objetos.Veiculo as V; 
import CRUD.Objetos.Pessoa as P;
import CRUD.Objetos.Endereco as E;
import CRUD.Objetos.Documentos as D;
import CRUD.Leitura_OCR_Placa as PL;
import CRUD.Objetos.Dispositivo as CD;

class Tela_Cliente:
    
    def __init__(self):
            self.dispositivo = CD.Dispositivo()
            # Cria a janela principal da aplicação
            self.root = tk.Tk()
            self.root.title("Cadastro de Placas")
            self.root.geometry("600x500")

            #O frame principal
            frame_principal = tk.Frame(self.root, padx=10, pady=10)
            frame_principal.pack(fill=tk.BOTH, expand=True)
            # Estilos
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

            label_placa = ttk.Label(frame_principal, text="Placa:")
            label_placa.grid(row=6, column=0, pady=5)
            self.campo_placa = ttk.Entry(frame_principal)
            self.campo_placa.grid(row=6, column=1, pady=5)

            label_modelo = ttk.Label(frame_principal, text="Modelo:")
            label_modelo.grid(row=7, column=2, pady=5)
            self.campo_modelo = ttk.Entry(frame_principal)
            self.campo_modelo.grid(row=7, column=3, pady=5)

            label_marca = ttk.Label(frame_principal, text="Marca:")
            label_marca.grid(row=7, column=0, pady=5)
            self.campo_marca = ttk.Entry(frame_principal)
            self.campo_marca.grid(row=7, column=1, pady=5)

            label_busca = ttk.Label(frame_principal, text="buscar Placa:")
            label_busca.grid(row=0, column=0, padx=2)
            self.campo_busca = ttk.Entry(frame_principal)
            self.campo_busca.grid(row=0, column=1)
            
            # Obtenha a lista de nomes das câmeras do banco de dados
            nomes_cameras = CD.Dispositivo.buscar_nomes_cameras()

            # Variável de controle para armazenar a seleção do usuário
            self.var_nome_camera = tk.StringVar()
            self.var_nome_camera.set(nomes_cameras[0])  # Defina o valor padrão como o primeiro nome da lista

            # Crie o dropdown com os nomes das câmeras
            self.dropdown_nome_camera = tk.OptionMenu(frame_principal, self.var_nome_camera, *nomes_cameras)
            self.dropdown_nome_camera.grid(row=13, column=1, pady=10)

            #botões
            botao_cadastro = ttk.Button(frame_principal, text="Cadastrar", command= self.cadastrar)
            botao_cadastro.grid(row=12, column=0, pady=10)

            botao_editar = ttk.Button(frame_principal, text="buscar", command=self.buscar)
            botao_editar.grid(row=0, column=2, padx=5)

            botao_deletar = ttk.Button(frame_principal, text="Deletar", command=self.deletar)
            botao_deletar.grid(row=12, column=1, pady=10)

            botao_deletar = ttk.Button(frame_principal, text="Atualizar", command=self.Atualizar)
            botao_deletar.grid(row=12, column=2, pady=10)
            
            botao_deletar = ttk.Button(frame_principal, text="Limpar", command=self.limpar)
            botao_deletar.grid(row=12, column=3, pady=10)

            botao_captura = ttk.Button(frame_principal, text="Capturar Placa", command=self.capturar)
            botao_captura.grid(row=13, column=2, pady=10)
        
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
            self.limpar_Placa()
            self.campo_modelo.delete(0, tk.END)
            self.campo_marca.delete(0, tk.END)
            self.campo_Telefone.delete(0, tk.END)
    def limpar_Placa(self):
        self.campo_placa.delete(0, tk.END)
            
    def capturar(self):
        self.limpar_Placa()
        nome_camera = self.var_nome_camera.get()
        self.dispositivo.video_source = CD.Dispositivo.busca(nome_camera)[1]
        self.dispositivo.connect_and_capture()
        self.campo_placa.insert(0, PL.Leitura_OCR_Placa.Processamento())

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
            placa = self.campo_placa.get()
            modelo = self.campo_modelo.get()
            marca = self.campo_marca.get()
            telefone = self.campo_Telefone.get()
            
            if self.validação(nome,sobrenome,rg,cpf,estado,cidade,rua,cep,telefone)== False:
                print("Passou")
                pessoa = P.Pessoa.registro(rg, cpf, estado, cidade, cep, rua, complemento, nome, sobrenome)
                T.Telefone.registro(pessoa, placa, modelo, marca, telefone)
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
            placa = self.campo_placa.get()
            modelo = self.campo_modelo.get()
            marca = self.campo_marca.get()
            telefone = self.campo_Telefone.get()
            IdPessoa = V.Veiculo.busca(self.campo_busca.get())[0]
            
            if self.validação(nome,sobrenome,rg,cpf,estado,cidade,rua,cep,telefone)== False:
                D.Documentos.update(rg, cpf,IdPessoa)
                P.Pessoa.update(nome, sobrenome,IdPessoa)
                E.Endereco.update(estado, cidade, cep, rua, complemento,IdPessoa)
                V.Veiculo.update(placa, modelo, marca,IdPessoa)
                T.Telefone.update(telefone, IdPessoa)
                self.limpar()
            else:
                return
            
            
            
    def buscar(self):
            placa = self.campo_busca.get()
            if V.Veiculo.busca(placa):
                # Preenche os campos de entrada com os dados do registro
                self.limpar()
                self.campo_nome.insert(0, V.Veiculo.busca(placa)[1])
                self.campo_sobrenome.insert(0, V.Veiculo.busca(placa)[2])
                self.campo_rg.insert(0, V.Veiculo.busca(placa)[5])
                self.campo_cpf.insert(0, V.Veiculo.busca(placa)[6])
                self.campo_estado.insert(0, V.Veiculo.busca(placa)[7])
                self.campo_cidade.insert(0, V.Veiculo.busca(placa)[8])
                self.campo_cep.insert(0, V.Veiculo.busca(placa)[9])
                self.campo_rua.insert(0, V.Veiculo.busca(placa)[10])
                self.campo_complemento.insert(0, V.Veiculo.busca(placa)[11])
                self.campo_placa.insert(0, V.Veiculo.busca(placa)[13])
                self.campo_modelo.insert(0, V.Veiculo.busca(placa)[14])
                self.campo_marca.insert(0, V.Veiculo.busca(placa)[15])
                self.campo_Telefone.insert(0, V.Veiculo.busca(placa)[17])
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
        # Obtém o valor do campo de placa para deletar
        placa = self.campo_placa.get()
        if V.Veiculo.delete(placa):
            idDocumento = V.Veiculo.busca(placa)[3]
            idEndereco = V.Veiculo.busca(placa)[4]
            idPessoa = V.Veiculo.busca(placa)[0]
            idTelefone = V.Veiculo.busca(placa)[16]
            idrelacao = V.Veiculo.busca(placa)[18]
            idVeiculo = V.Veiculo.busca(placa)[12]
            D.Documentos.delete(idDocumento)
            E.Endereco.delete(idEndereco)
            P.Pessoa.delete(idPessoa)
            T.Telefone.delete(idTelefone, idrelacao)
            V.Veiculo.delete(idVeiculo)
            self.limpar()
        
    def run(self):
        self.root.mainloop()
    
##Debug

#Tela_Cliente().run()