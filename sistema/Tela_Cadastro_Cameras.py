import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import CRUD.Objetos.Dispositivo as cameras

class Tela_Cadastro_Cameras:
    
    def __init__(self):
        self.cameras = []
        self.window = tk.Tk()
        self.window.title("Registro de Câmeras IP")

        # Centralizar a janela no meio do monitor
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = int((screen_width - 400) / 2)
        y = int((screen_height - 300) / 2)
        self.window.geometry(f"600x300+{x}+{y}")

        # Estilos
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("TLabel", font=("Helvetica", 12))

        # Labels e campos de entrada
        nome_label = ttk.Label(self.window, text="Nome:")
        nome_label.pack()
        self.nome_entry = ttk.Entry(self.window)
        self.nome_entry.pack()
        self.ID = 0
        ip_label = ttk.Label(self.window, text="IP:")
        ip_label.pack()
        self.ip_entry = ttk.Entry(self.window)
        self.ip_entry.pack()

        posicao_label = ttk.Label(self.window, text="Posição:")
        posicao_label.pack()
        self.posicao_entry = ttk.Entry(self.window)
        self.posicao_entry.pack()
        
        # Frame para os botões
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        # Botões
        registrar_button = ttk.Button(button_frame, text="Registrar", command=self.registrar_camera)
        registrar_button.pack(side=tk.LEFT, padx=5)

        buscar_button = ttk.Button(button_frame, text="Buscar", command=self.buscar_camera)
        buscar_button.pack(side=tk.LEFT, padx=5)

        atualizar_button = ttk.Button(button_frame, text="Atualizar", command=self.atualizar_camera)
        atualizar_button.pack(side=tk.LEFT, padx=5)

        deletar_button = ttk.Button(button_frame, text="Deletar", command=self.deletar_camera)
        deletar_button.pack(side=tk.LEFT, padx=5)

    def registrar_camera(self):
        nome = self.nome_entry.get()
        ip = self.ip_entry.get()
        posicao = self.posicao_entry.get()
        
        if nome.strip() == "" or ip.strip() == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
        cameras.Dispositivo.Registro(ip,nome,posicao)

        messagebox.showinfo("Registro", "Câmera IP registrada com sucesso!")

        self.limpar_campos()

    def buscar_camera(self):
        nome_busca = self.nome_entry.get()
        IP_busca = self.ip_entry.get()
        
        if cameras.Dispositivo.busca(nome_busca):
            self.ID = cameras.Dispositivo.busca(nome_busca)[0]
            self.ip_entry.insert(0, cameras.Dispositivo.busca(nome_busca)[1])
            self.posicao_entry.insert(0, cameras.Dispositivo.busca(nome_busca)[3])
            print(self.ID)  
        elif cameras.Dispositivo.busca2(IP_busca):
            self.ID = cameras.Dispositivo.busca(nome_busca)[0]
            self.nome_entry.insert(0, cameras.Dispositivo.busca(nome_busca)[2])
            self.posicao_entry.insert(0, cameras.Dispositivo.busca(nome_busca)[3])
        else:   
            messagebox.showerror("Câmera Não Encontrada", "A câmera não foi encontrada.")

    def atualizar_camera(self):
        nome_busca = self.nome_entry.get()
        ip = self.ip_entry.get()
        posicao = self.posicao_entry.get()
        idDispositivo = self.ID
        cameras.Dispositivo.update(ip, nome_busca, idDispositivo, posicao)
        messagebox.showinfo("Atualização", "Câmera IP atualizada com sucesso.")
        self.limpar_campos()


    def deletar_camera(self):
        nome_busca = self.nome_entry.get()
        cameras.Dispositivo.delete(nome_busca)
        messagebox.showinfo("Deletado", "Câmera IP Deletada com sucesso.")
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.ip_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()
               

##Debug

#Tela_Cadastro_Cameras().run()