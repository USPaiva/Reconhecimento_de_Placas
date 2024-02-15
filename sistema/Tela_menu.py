import PySimpleGUI as sg
import multiprocessing as mp
import os
import Tela_Cliente as cliente
import Tela_Operador as Operador
import Tela_Cadastro_Cameras as Cameras
#import Tela_Controle_Acesso as Acesso
#import tkinter as tk
class Tela_menu:
    def __init__(self, cargo):
        # Definir temas e configurações de janela
        sg.theme('LightBlue2')  # Tema da janela
        sg.set_options(font=('Arial', 12))  # Configurações de fonte
        imagens_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Imagens')
        image_funcionario = os.path.join(imagens_dir, 'funcionario2.png')
        carro = os.path.join(imagens_dir, 'carro2.png')
        dispositivo = os.path.join(imagens_dir, 'catraca2.png')
        logoff = os.path.join(imagens_dir, 'logout2.png')
        conta = os.path.join(imagens_dir, 'catraca3.png')

        # Definir layout da janela
        if cargo ==1:
            layout = [
                [sg.Text('Menu de Cadastros', font=('Arial', 20), justification='center', size=(40, 1))],
                [sg.Column([
                        [sg.Button(image_filename=image_funcionario, size=(80, 80), tooltip='Área Funcionário', key='funcionario')],
                        [sg.Text('Área Funcionário', font=('Arial', 12), justification='center')]
                    ], element_justification='c', pad=((110, 0), 0)),
                sg.Column([
                    [sg.Button(image_filename=carro, size=(80, 80), tooltip='Área Cliente', key='cliente')],
                    [sg.Text('Área Cliente', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((0, 0), 0)),
                sg.Column([
                    [sg.Button(image_filename=dispositivo, size=(80, 80), tooltip='Novos Dispositivos', key='dispositivos')],
                    [sg.Text('Novos Dispositivos', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((0, 0), 0)),
                #sg.Column([
                #    [sg.Button(image_filename=conta, size=(80, 80), tooltip='Monitoramento', key='Monitoramento')],
                #    [sg.Text('Monitoramento', font=('Arial', 12), justification='center')]
                #], element_justification='c', pad=((0, 0), 0)),
                
                ],
                [
                
                sg.Column([
                    [sg.Button(image_filename=logoff, size=(80, 80), tooltip='Logoff', key='logoff')],
                    [sg.Text('Logoff', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((250, 0), 0))]
            ]
        elif cargo == 2:
            layout = [
                [sg.Text('Menu de Cadastros', font=('Arial', 20), justification='center', size=(40, 1))],
                [sg.Column([
                        [sg.Button(image_filename=image_funcionario, size=(80, 80), tooltip='Área Funcionário', key='funcionario')],
                        [sg.Text('Área Funcionário', font=('Arial', 12), justification='center')]
                    ], element_justification='c', pad=((190, 0), 0)),
                sg.Column([
                    [sg.Button(image_filename=carro, size=(80, 80), tooltip='Área Cliente', key='cliente')],
                    [sg.Text('Área Cliente', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((0, 0), 0)),
                #sg.Column([
                #    [sg.Button(image_filename=conta, size=(80, 80), tooltip='Monitoramento', key='Monitoramento')],
                #    [sg.Text('Monitoramento', font=('Arial', 12), justification='center')]
                #], element_justification='c', pad=((0, 0), 0)),
                
                ],
                [
                
                sg.Column([
                    [sg.Button(image_filename=logoff, size=(80, 80), tooltip='Logoff', key='logoff')],
                    [sg.Text('Logoff', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((250, 0), 0))]
            ]
        else:
            layout = [
                [sg.Text('Menu de Cadastros', font=('Arial', 20), justification='center', size=(40, 1))],
                [sg.Column([
                    [sg.Button(image_filename=carro, size=(80, 80), tooltip='Área Cliente', key='cliente')],
                    [sg.Text('Área Cliente', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((250, 0), 0)),
                #sg.Column([
                #    [sg.Button(image_filename=conta, size=(80, 80), tooltip='Monitoramento', key='Monitoramento')],
                #    [sg.Text('Monitoramento', font=('Arial', 12), justification='center')]
                #], element_justification='c', pad=((0, 0), 0)),
                
                ],
                [
                sg.Column([
                    [sg.Button(image_filename=logoff, size=(80, 80), tooltip='Logoff', key='logoff')],
                    [sg.Text('Logoff', font=('Arial', 12), justification='center')]
                ], element_justification='c', pad=((250, 0), 0))]
            ]   
        # Criar janela
        self.window = sg.Window('Menu Principal', layout, size=(600, 300), resizable=True)

        
        
    # Definir funções de eventos
    #def Monitoramento(self):
    #    print("gg")
        #Acesso.Tela_Controle_Acesso().run()
        # Crie um processo separado para executar a classe Tela_Controle_Acesso
        #p = mp.Process(target=Acesso.Tela_Controle_Acesso().run)
        #p.start()

    def cadastro_funcionario(self):
        Operador.Tela_Operador().run()

    def cadastro_cliente(self):
        cliente.Tela_Cliente().run()

    def cadastro_dispositivos(self):
        # Instanciar a aplicação e iniciar
        Cameras.Tela_Cadastro_Cameras().run()   
        
    def run(self):
        # Loop principal da janela
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'logoff':
                break
            elif event == 'funcionario':
                self.cadastro_funcionario()
            elif event == 'cliente':
                self.cadastro_cliente()
            elif event == 'dispositivos':
                self.cadastro_dispositivos()
            #elif event == 'Monitoramento':
            #    self.Monitoramento()
        self.window.close()
        
##Debug

#Tela_menu().run()