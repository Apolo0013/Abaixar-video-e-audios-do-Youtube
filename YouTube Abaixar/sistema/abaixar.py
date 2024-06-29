from pytube import YouTube

class AbaixarVideoEMusica():
    def __init__(self, url = None ,qualidade = None, diretorio = None):
        self.url = url 
        self.qualidade = qualidade
        self.diretorio = diretorio


    def Abaixa_Video(self):
        try:
            yt = YouTube(url= self.url)
            qualidades = yt.streams.get_by_resolution(self.qualidade)
            if qualidades == None:
                qualidades = yt.streams.get_highest_resolution()
            video = qualidades.download(output_path=self.diretorio)
            

        except Exception as error:
            print(f'Algo deu errado {error}')
            return False
        else:
            return True
        

    def Abaixa_Audio(self):
        try:
            yt = YouTube(url = self.url)
            audio_streams = yt.streams.filter(only_audio=True)
            audio_stream = audio_streams.filter(abr=self.qualidade).first()

            audio_caminho = audio_stream.download(output_path=self.diretorio)
        except Exception:
            return False
        else:
            return True


    def MostrarResolucaoVideo(self): #Mostrar a resolucoes disponivel do video, trata as resolucao e deixa em ondem etc
        qualidades = None
        try:
            # Tratamento de erro caso a url esteja errado ou seila oque vai fuder
            try:
                yt = YouTube(url = self.url)

            except Exception as error:
                print(f'Algo de errado {error}')
                return None

            qualidades = [] # ondem vai ficar as resolucao tratada
            if self.url != '':    
                lista_qualidadeTemp = [] # uma lista temporaria, para trata as resolucões
                qualidadesTemp = [] # uma lista temporaria para a guardar as qualidade para depois botar na variavel qualidade
                

                for qualidade in yt.streams: # aqui vou lista e trata as resolucao disponiveis
                    if qualidade.resolution != None and qualidade.resolution not in lista_qualidadeTemp: 
                        lista_qualidadeTemp.append(qualidade.resolution)


                for valor in lista_qualidadeTemp: # aqui vamos tirar o do final das resolucao ex: 140p para 140 com inteiro
                    indice = int(len(valor)-1)
                    qualidadesTemp.append(int(valor[:indice])) # tirando o p no final e definido o mesmo com inteiro
                
                for valor in sorted(qualidadesTemp): # aqui finalmente deixamos em ondem e denovo botamos o p de volta no final
                    qualidades.append(str(f'{valor}p'))
                
                #Limpando as variavels temporaria
                qualidadesTemp.clear() 
                lista_qualidadeTemp.clear()
        except Exception:
                print('algo de errado nessa porra')
        finally:
            return qualidades # retornado o resultado do tratamento
            

    def MostrarResolucaoMusica(self): # Mostar a resolucoes disposnovel da musica, trata as resolucao deixa em ondem e etc
        # Tratamento de erro caso a url esteja errado ou seila oque vai fuder
        try:
            yt = YouTube(url = self.url)
        except Exception as error:
            print(f'algo de errado: {error}')

        if self.url != '':
            lista_qualidadeTemp = [] #  lista temporaria para trata
            qualidadeTemp = [] #mais uma vez, outra lista temporaria para guardar os resultado tratado e botar na variavel que sera retornada
            qualidade = [] # variavel que irar receber as resoluções tratada

            for qualidades in yt.streams.filter(only_audio=True): # aqui nos vai pegar as resolucao disponiveis do video no caso o audio que o usuario vai abaixar
                if qualidades.abr != None and qualidades.abr not in lista_qualidadeTemp:
                    lista_qualidadeTemp.append(qualidades.abr)

            abr_temp = '' #ondem vai ficar as resolucao temporario, para trata

            for abr in lista_qualidadeTemp:
                for valor in abr:
                    if valor in ('1','2','3','4','5','6','7','8','9','0'):
                        abr_temp += valor
                qualidadeTemp.append(int(abr_temp))
                abr_temp = ''

            for abrs in sorted(qualidadeTemp):
                qualidade.append(str(f'{abrs}kbps'))

            return qualidade

            





if __name__ == '__main__':
    AbaixarVideoEMusica(url = 'https://www.youtube.com/watch?v=iywaBOMvYLI' , qualidade = '160kbps').Abaixa_Audio()
    
