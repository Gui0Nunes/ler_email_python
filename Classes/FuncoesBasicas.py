import os
from shutil import rmtree
from glob import glob
from base64 import b64encode

class FuncoesBasicas:
    def __init__(self, diretorio_pdf):
        self._diretorio_pdf = diretorio_pdf

    # Cria o diretório para os PDFs baixados
    def CriarDiretorioPdf(self):
        if not os.path.exists(self._diretorio_pdf):
            try:
                os.makedirs(self._diretorio_pdf)
            except:
                exit()

    # Exclui o diretório e os PDFs baixados
    def RemoverDiretorioPdf(self):
        if os.path.exists(self._diretorio_pdf):
            try:
                rmtree(self._diretorio_pdf)
            except:
                exit()

    # Pega os PDFs baixados
    def PegarPdf(self):
        arquivo = glob(self._diretorio_pdf + '*.pdf')
        return arquivo if arquivo else None
    
    # Transforma o mês de referência em número
    def DefinirRef(self, ref):
        mes = ref.split('/')[0]

        if mes == 'JAN':
            numero_mes = '01'
        elif mes == 'FEV':
            numero_mes = '02'
        elif mes == 'MAR':
            numero_mes = '03'
        elif mes == 'ABR':
            numero_mes = '04'
        elif mes == 'MAI':
            numero_mes = '05'
        elif mes == 'JUN':
            numero_mes = '06'
        elif mes == 'JUL':
            numero_mes = '07'
        elif mes == 'AGO':
            numero_mes = '08'
        elif mes == 'SET':
            numero_mes = '09'
        elif mes == 'OUT':
            numero_mes = '10'
        elif mes == 'NOV':
            numero_mes = '11'
        elif mes == 'DEZ':
            numero_mes = '12'
        else:
            numero_mes = '00'

        return f"{numero_mes}/{ref.split('/')[1]}"
    
    # Transforma o arquivo PDF em base64
    def TranformarPdfBase64(self, arquivo):
        with open(arquivo, 'rb') as pdf:
            conteudo_pdf = pdf.read()

        return b64encode(conteudo_pdf).decode('utf-8')