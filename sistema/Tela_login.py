import tkinter as tk
from tkinter import messagebox
import Tela_menu as TM
import CRUD.Objetos.Login as C
import sys

class Tela_login:
    
    def __init__(self):
        # Criar a janela de login
        self.window = tk.Tk()
        self.window.title("Login")
        # Obter o tamanho do monitor
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calcular as coordenadas para centralizar a janela
        x = int((screen_width - self.window.winfo_reqwidth()) / 2)
        y = int((screen_height - self.window.winfo_reqheight()) / 2)

        # Definir a posição da janela no centro do monitor
        self.window.geometry(f"400x300+{x}+{y}")
        self.window.resizable(True,True)

        # Definir o comportamento do botão de fechar
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Criar os campos de entrada de usuário e senha
        username_label = tk.Label(text="User:", font=("Helvetica", 14))
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        password_label = tk.Label(text="Password:", font=("Helvetica", 14))
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(show="*", font=("Helvetica", 14))
        self.password_entry.pack(pady=5)

        # Botão de login
        login_button = tk.Button(text="Login", command=self.login, font=("Helvetica", 14), bg="green", fg="white")
        login_button.pack(pady=20)

        # Status de login
        self.status_label = tk.Label(text="", font=("Helvetica", 14))
        self.status_label.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Verificar o usuário e a senha
        login = C.Login.login(username,password)
        if login != None:
            self.status_label.config(text="Login bem sucedido", fg="green")
            self.window.withdraw()
            TM.Tela_menu(login[4]).run()
            self.limpar()
            self.window.deiconify()
        else:
            self.status_label.config(text="Usuário ou senha incorretos", fg="red")

    def on_closing(self):
        if tk.messagebox.askokcancel("Fechar", "Tem certeza que deseja encerrar o programa?"):
            self.window.destroy()
            sys.exit(0)

    def limpar(self):
            # Limpa os campos de entrada
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        
    def run(self):
        # Executar a janela
        self.window.mainloop()

##Debug

Tela_login().run()