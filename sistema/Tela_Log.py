from tkinter import Tk, Label, Entry, Button, Listbox, Frame
from CRUD.Objetos.Conexao import Conexao

class RelatorioPlaca:
    def __init__(self):
        self.conexao = Conexao()
        self.cursor = self.conexao.cursor()

    def obter_dados_relatorio(self, data=None, placa=None):
        if data and placa:
            query = "SELECT * FROM relatorio WHERE Data_hora = ? AND placa = ?"
            params = (data, placa)
        elif data:
            query = "SELECT * FROM relatorio WHERE Data_hora = ?"
            params = (data,)
        elif placa:
            query = "SELECT * FROM relatorio WHERE placa = ?"
            params = (placa,)
        else:
            query = "SELECT * FROM relatorio"
            params = None

        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def gerar_relatorio(self):
        janela = Tk()
        janela.title("Relatório de Placas")

        # Campos de busca
        frame_busca = Frame(janela)
        frame_busca.pack()

        label_data = Label(frame_busca, text="Buscar por data:")
        label_data.grid(row=0, column=0)
        entry_data = Entry(frame_busca)
        entry_data.grid(row=0, column=1)

        label_placa = Label(frame_busca, text="Buscar por placa:")
        label_placa.grid(row=1, column=0)
        entry_placa = Entry(frame_busca)
        entry_placa.grid(row=1, column=1)

        botao_buscar = Button(frame_busca, text="Buscar", command=lambda: self.realizar_busca(entry_data.get(), entry_placa.get(), lista))
        botao_buscar.grid(row=2, column=0, columnspan=2)

        # Lista dos registros
        frame_lista = Frame(janela)
        frame_lista.pack()

        lista = Listbox(frame_lista)
        lista.pack()

        self.atualizar_relatorio(lista)

        janela.mainloop()
        self.conexao.close()

    def realizar_busca(self, data, placa, lista):
        lista.delete(0, "end")
        registros = self.obter_dados_relatorio(data, placa)
        for registro in registros:
            lista.insert("end", registro)

    def atualizar_relatorio(self, lista):
        lista.delete(0, "end")
        registros = self.obter_dados_relatorio()
        for registro in registros[:10]:
            lista.insert("end", registro)
