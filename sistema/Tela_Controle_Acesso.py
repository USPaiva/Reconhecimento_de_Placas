import CRUD.Objetos.Dispositivo as CD
import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import CRUD.Leitura_OCR_Placa as PL
import CRUD.Objetos.Log as log
import CRUD.Objetos.Dispositivo as Dis
#from Tela_login import Tela_login as TL
class Tela_Controle_Acesso:
    def __init__(self):
        self.nome = "cel"
        self.window = tk.Tk()
        self.window.title("Webcam App")
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.pack()
        self.capture_interval = 30  # Captura a cada 5 segundos
        self.last_capture_time = time.time()  # Inicializa o último tempo de captura
        self.dispositivo = CD.Dispositivo()
        
        
        
        # Obtenha a lista de nomes das câmeras do banco de dados
        nomes_cameras = CD.Dispositivo.buscar_nomes_cameras()

        # Variável de controle para armazenar a seleção do usuário
        self.var_nome_camera = tk.StringVar()
        self.var_nome_camera.set(nomes_cameras[0])  # Defina o valor padrão como o primeiro nome da lista

        # Crie o dropdown com os nomes das câmeras
        self.dropdown_nome_camera = tk.OptionMenu(self.window, self.var_nome_camera, *nomes_cameras)
        self.dropdown_nome_camera.pack()
        
        
        # Status de login
        self.status_label = tk.Label(text="", font=("Helvetica", 14))
        self.status_label.pack()

        self.button_confirmar_camera = tk.Button(self.window, text="Confirmar", command=self.iniciar)
        self.button_confirmar_camera.pack()
        
        self.liberar_button = tk.Button(self.window, text="Liberar Acesso", command=self.liberar)
        self.liberar_button.pack()
        
        #self.Login_button = tk.Button(self.window, text="Logar Acesso de controles", command=self.login)
        #self.Login_button.pack()
        
        self.close_button = tk.Button(self.window, text="Fechar", command=self.close)
        self.close_button.pack()
        
    def iniciar(self):
        nome_camera = self.var_nome_camera.get()
        self.dispositivo.video_source = CD.Dispositivo.busca(nome_camera)[1]
        self.window.after(0, self.update)  # Chame a função update imediatamente após a confirmação da câmera

    
    def update(self):
        caminho = self.dispositivo.connect_and_capture()
        status = log.Log.controle(PL.Leitura_OCR_Placa.Processamento(), Dis.Dispositivo.busca(self.nome)[0], caminho)
        print(status)
        if status != 0:
            self.status_label.config(text="Acesso Liberado", fg="green")
        else:
            self.status_label.config(text="Acesso Negado", fg="red")
        
        ret, frame = cv2.VideoCapture(self.dispositivo.video_source).read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            image = image.resize((640, 480))
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.window.after(60, self.update)  # Agende a próxima atualização após 60ms

        
    def close(self):
        self.window.destroy()
    
    def liberar(self):
        self.dispositivo.connect_and_capture()
        log.Log.controle2(PL.Leitura_OCR_Placa.Processamento(), Dis.Dispositivo.busca(self.nome)[0])
        self.status_label.config(text="Acesso Liberado", fg="green")
        tk.messagebox.showinfo(title="Liberação", message ="Liberado")

    #def login():
    #    TL.run()

    def run(self):
        #self.update()
        self.window.mainloop()

# Cria a instância da aplicação WebcamApp
Tela_Controle_Acesso().run()

