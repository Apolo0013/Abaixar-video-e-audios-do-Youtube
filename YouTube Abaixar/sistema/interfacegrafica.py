from tkinter import *
from tkinter import ttk
from tkinter import  filedialog , messagebox
from tkinter.ttk import Combobox
from .abaixar import *


class InterFaceGrafica():
    caminho = ''

    def __init__(self):
        self.Gui()


    def Gui(self):

        cor_botao = '#1473E6'
        font_erro = 'Arial 10 bold'
        fonte = 'Arial 13 bold'
        cor_erro = '#FA542A'

        self.janela = Tk()
        self.janela.title('Instalar Video e Musica do YouTube')
        self.janela.config(bg = '#21272A')
        self.janela.geometry('350x170')
        self.janela.iconphoto(False , PhotoImage(file=r'YouTube Abaixar\sistema\imagens\download_icone.png'))
        '''
        Autor da imagem:

        https://br.freepik.com/icone/baixar_5344720#fromView=search&page=1&position=93&uuid=117246c5-b3a7-4845-a6f6-763cfffec98c'''
        self.janela.resizable(width = False , height= False)

        #Label indicando o local de coloca a url
        
        self.url_label = Label(self.janela , width = 5 , height= 1 ,text='*Url', font='Arial 15 bold' , bg = '#21272A', fg = 'white' , relief = 'flat')
        self.url_label.place(x = 5 ,y=13)

        #ondem serar inserido a url
        self.varUrl = StringVar()
        self.url_entry = Entry(self.janela , width = 50 , bg = '#6D6D6D' , relief = 'flat', textvariable=self.varUrl ,state='disabled')
        self.url_entry.place(x = 10 , y = 40)

        #Aviso de erro url vazia ou incorreta e etc
        self.url_erro = Label(self.janela , width = 25 , height = 1 , text = '' , font = font_erro , bg = '#21272A' , fg = cor_erro , relief='flat' , anchor='w')
        self.url_erro.place(x = 10 , y = 60)

        #oque vai abaixar video o musica?
        self.varFormato = StringVar()
        self.formato = Combobox(self.janela , width = 15 , state='disabled' , textvariable=self.varFormato)
        self.formato['value'] = ['Mp4','Mp3']
        self.formato.current(0)
        self.formato.place(x = 200 , y = 70)

        #aqui o usuario tem a opcao de escolher a qualidade
        self.varQualidade = StringVar()
        self.Qualidade = Combobox(self.janela , width=15 , state='disabled' , textvariable = self.varQualidade)
        self.Qualidade['value'] = ['144p', '240p', '360p', '480p', '720p', '1080p']
        self.Qualidade.place(x = 200 , y = 100)

        #Procurar Pasta ondem sera salva os bagui
        self.Procurar_pasta = Button(self.janela , width = 15 , height = 1 ,text = 'Procurar Diretorio' , font = fonte , bg = cor_botao , fg = 'white' , relief = 'flat', command = self.Caminho_Pasta)
        self.Procurar_pasta.place(x = 10 , y = 90)

        #Para quando ele nao achar a pasta ou sei la.
        self.procurar_erro = Label(self.janela , width = 15 , height = 1 , text = '' , font= font_erro , bg = '#21272A' , fg = cor_erro , anchor='w')
        self.procurar_erro.place(x = 10 , y = 125)

        # Botao de Abaixa
        self.abaixar = Button(self.janela , width = 15 , height = 1,text = 'Abaixar' , font = fonte , bg = cor_botao , fg = 'White',  relief = 'flat' , command= self.Instalação)
        self.abaixar.place(x = 176 , y = 130)

        self.Mudar_qualidade()
        self.varFormato.trace_add('write' , self.Mudar_qualidade)
        self.varUrl.trace_add('write' , self.Mudar_qualidade)


        self.janela.mainloop()


    def Mudar_qualidade(self , *args):
        from time import sleep

        anima = 0
        for c in range(0 , 2):

            if anima == 0:
                self.url_erro['text'] = 'Pegando informações'
            elif anima == 1:
                self.url_erro['text'] = 'Pegando informações.'
            elif anima == 2:
                self.url_erro['text'] = 'Pegando informações..'
            elif anima == 3:
                self.url_erro['text'] = 'Pegando informações...'
                anima = -1
            anima+=1

            self.url_erro.update()
            sleep(0.7)
        self.formato['state'] = 'readonly'
        self.Qualidade['state'] = 'readonly'
        self.url_entry['state'] = 'normal'
        self.url_erro['text'] = ''
        self.janela.update()

        formatos = self.formato.get()
        url_uso = self.url_entry.get()

        url = AbaixarVideoEMusica(url = url_uso)

        if formatos == 'Mp4':
            qualidade = url.MostrarResolucaoVideo() # Mostrar quais são as resolucao disponiveis

            if qualidade is None and qualidade != '':
                self.url_erro['text'] = 'URL invalida!!!'

            if qualidade == None: 
                qualidade = ['144p', '240p', '360p', '480p'] # caso se o usuario nao tenha botado o url ele botar essa resolucao ai so para efeita

        elif formatos == 'Mp3': # a mesma coisa aqui
            qualidade = url.MostrarResolucaoMusica()
            if qualidade == None:
                qualidade = ['128kbps',
                            '160kbps',
                            '192kbps',
                            '256kbps',
                            '320kbps'
                            ]

        self.Qualidade['value'] = qualidade
        if len(qualidade) > 0:
            indice = (len(qualidade)-1)/2
            self.Qualidade.current(int(indice))
        self.Qualidade.update()


    def Caminho_Pasta(self):
        self.caminho = ''
        try:
            self.caminho = filedialog.askdirectory()
        except Exception:
            print('algo deu errado')
        else:
            if self.caminho != '':
                self.procurar_erro['text'] = ''    
                diretorio = ''
                for valores in self.caminho:
                    if valores == '/':
                        diretorio += '\\\\'

                    else:
                        diretorio += valores
                self.caminho = diretorio


    def Instalação(self):
        erro = False
        
        if self.caminho == '':
            erro = True
            self.procurar_erro['text'] = '*Selcione a pasta'

        if self.url_entry.get() == '':
            self.url_erro['text'] = '*Insira uma URL'

        if not erro:
            self.procurar_erro['text'] = ''
            self.url_erro['text'] = ''
            self.abaixar['text'] = 'Abaixando...'
            self.abaixar.update()
            if self.formato.get() == 'Mp4':    
                resolucao = self.Qualidade.get()
                urls = self.url_entry.get()
                video = AbaixarVideoEMusica(url = urls , diretorio = self.caminho , qualidade=resolucao).Abaixa_Video()

                if video:
                    messagebox.askokcancel('Aviso',f'O Video insatalador com sucesso: {self.caminho.replace('\\\\','\\')}.')

                else:
                    messagebox.askokcancel('Aviso' , 'Algo deu errado. Tente novamente')
            
            else:
                resolucao = self.Qualidade.get()
                urls = self.url_entry.get()
                audio = AbaixarVideoEMusica(url = urls , diretorio = self.caminho , qualidade= resolucao).Abaixa_Audio()

                if audio:
                    messagebox.askokcancel('Aviso',f'O Audio insatalador com sucesso: {self.caminho.replace('\\\\','\\')}.')

                else:
                    messagebox.askokcancel('Aviso','Algo deu errado. Tente Novamente.')

            self.abaixar['text'] = 'Abaixar'
            self.abaixar.update()



if __name__ == '__main__':
    InterFaceGrafica()