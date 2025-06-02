from dotenv import load_dotenv                      # Biblioteca para carregar variáveis de ambiente do arquivo .env
load_dotenv()                                       # Carregando arquivo .env da raiz do projeto

import imaplib                                      # Biblioteca para fazer conexão com o servidor de email
import email                                        # Biblioteca para fazer a leitura do email
import email.utils                                  # Biblioteca para fazer a leitura do email
from email.header import decode_header              # Biblioteca para fazer a leitura do cabeçalho do email

import smtplib                                      # Biblioteca para fazer o envio de email
from email.message import EmailMessage              # Biblioteca para fazer a mensagem para envio de email
from email.mime.multipart import MIMEMultipart      # Biblioteca para fazer a mensagem para envio de email
from email.mime.text import MIMEText                # Biblioteca para fazer a mensagem para envio de email
from email.mime.base import MIMEBase                # Biblioteca para fazer a mensagem para envio de email

import os                                           # Biblioteca para manipular o sistema operacional
from shutil import rmtree                           # Biblioteca para manipular diretórios
from time import sleep                              # Biblioteca para manipular segundos
from datetime import datetime                       # Biblioteca para manipular datas
from dateutil.relativedelta import relativedelta    # Biblioteca para manipular data, pula dia, mês e ano automático

import requests                                     # Biblioteca para manipular requisições
from requests.auth import HTTPBasicAuth             # Biblioteca para manipular Base64

# Minhas classes
from Classes.FuncoesBasicas import FuncoesBasicas   # Classe responsável pela manipulação de diretórios e arquivos
from Classes.EmailClass import EmailClass           # Classe responsável pela manipulação de emails
from Classes.ApiDados import ApiDados               # Classe responsável pelo envio de dados


######################################################################
# Teste leitura das variáveis de ambiente do arquivo .env
print('Verificação do arquivo .env')
if(os.getenv('EMAIL') == ''):
    print('Email vazio, programa encerrado até que seja preenchido no .env')
    #print(os.getenv('EMAIL'))
    exit()
###################################################################### CONSTANTES
DIRETORIO_PDF = os.path.dirname(__file__) + '/arquivos/'

# Configuração do servidor de email
EMAIL = 'teste@jmduque.com.br'
SENHA = 'JoaoGabriel@36'
SERVER = 'mail.jmduque.com.br'
PORTA = [993, 465]
###################################################################### CONSTANTES

###################################################################### INÍCIO DO CÓDIGO

# # Primeiro verifica se já existe arquivo na pasta "arquivos", caso sim, apaga todo o diretório e cria um novo com o mesmo nome.
funcoes_basicas = FuncoesBasicas(DIRETORIO_PDF)
# DESCOMMENTAR ABAIXO PARA TER A FUNÇÃO CITADA ACIMA FUNCIONANDO
# funcoes_basicas.RemoverDiretorioPdf()
# funcoes_basicas.CriarDiretorioPdf()
# sleep(2)

# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------
# ACESSA EMAIL - Verificando se possui algum PDF para ler e Baixar caso tenha um PDF
pegou_pdf_email = EmailClass(EMAIL, SENHA, SERVER, PORTA, DIRETORIO_PDF).PegarFatura()
if not pegou_pdf_email:
    print('Nenhum pdf encontrado')
    exit()
sleep(10)
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------

# Pegando os PDFs dentro do diretório "arquivos"
arquivos = funcoes_basicas.PegarPdf()
if not arquivos:
    print('Nenhum pdf encontrado')
    exit()

# Para ler os arquivos dentro da pasta "arquivos"    
for arquivo in arquivos:

    # Transforma o PDF em base64 para enviar para API
    try:
        pdf_base64 = funcoes_basicas.TranformarPdfBase64(arquivo)
    except Exception as e:
        print(e)
        pdf_base64 = None


    # api = ApiDados()
    # api.EnviarDadosFatura(dados_json)

    # sleep(10)
    print('\n-------------------------------------------------------------------\n')

# # Exclui os arquivos
# funcoes_basicas.RemoverDiretorioPdf()
