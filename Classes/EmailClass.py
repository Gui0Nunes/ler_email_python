import imaplib                                  # Biblioteca para fazer conexão com o servidor de email
import email                                    # Biblioteca para fazer a leitura do email
import email.utils                              # Biblioteca para fazer a leitura do email
from email.header import decode_header          # Biblioteca para fazer a leitura do cabeçalho do email

import smtplib                                  # Biblioteca para fazer o envio de email
from email.message import EmailMessage          # Biblioteca para fazer a mensagem para envio de email
from email.mime.multipart import MIMEMultipart  # Biblioteca para fazer a mensagem para envio de email
from email.mime.text import MIMEText            # Biblioteca para fazer a mensagem para envio de email
from email.mime.base import MIMEBase            # Biblioteca para fazer a mensagem para envio de email

import os                                       # Biblioteca para criar o diretório no sistema operacional para baixar os anexos
from shutil import rmtree                       # Biblioteca para remover o diretório
from io import BytesIO                          # Biblioteca para converter arquivo em base64
from glob import glob                           # Biblioteca para pegar arquivos
from datetime import datetime                   # Biblioteca para pegar data e hora

from Classes.FuncoesBasicas import FuncoesBasicas

class EmailClass:
    def __init__(self, email, senha, server, porta, diretorio_pdf):
        self._email = email
        self._senha = senha
        self._server = server
        self._porta = porta
        self._diretorio_pdf = diretorio_pdf
        self._funcoes_basicas = FuncoesBasicas(self._diretorio_pdf)

    # Enviar e-mail para terceiros
   # def EnviarEmail(self):
        # try:
        #     arquivo_pdf = self._funcoes_basicas.PegarPdf()
        #     if arquivo_pdf:
        #         arquivo_pdf = arquivo_pdf[0]
        #         msg = MIMEMultipart()
        #         msg['Subject'] = 'Bot Leitura'
        #         msg['From'] = self._email
        #         msg['To'] = 'joaogabriel.silva@jmduque.com.br'
        #         msg.attach(MIMEText(f'Fatura baixada {datetime.now()}'))

        #         try:
        #             with smtplib.SMTP_SSL(self._server, self._porta[1]) as smtp:
        #                 smtp.login(self._email, self._senha)
        #                 smtp.sendmail(msg['From'], msg['To'], msg.as_string())

        #         except smtplib.SMTPException as e:
        #             print(f'Erro: {e}')

        # except Exception as e:
        #     print(f'Erro: {e}\n')

    def PegarFatura(self):
        try:
            # Conectar com o servidor de email
            mail = imaplib.IMAP4_SSL(self._server, self._porta[0])

            # Login 
            mail.login(self._email, self._senha)

            # Selecionar caixa de entrada
            mail.select('inbox')

            # Buscar mensagens não lidas
            status, messages = mail.search(None, 'UNSEEN')
            # Id das mensagens - Inser um ID para identificar as mensagens
            messages = messages[0].split()
            # Leitura dos emails - Executa a leitura de cada e-mail (verifica se tem mensagem antes de ir para o For)
            if len(messages) > 0:
                gt = 'indefinido'
                distribuidora = 'indefinido'
                pegou_pdf = 0
                
                # Abre cada e-amil por vez, seguindo os IDs que foram criados acima 
                for mail_id in messages:
                    try:
                        self._funcoes_basicas.CriarDiretorioPdf()
                        status, data = mail.fetch(mail_id, '(RFC822)')
                        
                        for response_part in data:
                            if isinstance(response_part, tuple):
                                mensagem = email.message_from_bytes(response_part[1])

                                assunto = decode_header(mensagem['subject'])[0][0]
                                if isinstance(assunto, bytes):
                                    assunto = assunto.decode('utf-8')
                                usuario_enviou = email.utils.parseaddr(mensagem['from'])[1]

                                # percorre a mensagem
                                for part in mensagem.walk():
                                    if part.get_content_type() == 'text/plain':
                                        conteudo = part.get_payload(decode=True).decode('utf-8')
                                        break

                                # print('--------------------------------')
                                # print(part)
                                # print('--------------------------------')
                                
                                print('--------------------------------')
                                print('Rementente: ')
                                print(usuario_enviou)


                                print('--------------------------------')
                                print('Assunto: ')
                                print(assunto)


                                print('--------------------------------')
                            
                                print('Conteúdo: ')
                                print(conteudo)
                                print('--------------------------------')

                                # # Percorrer toda a mensagem do email em busca de anexos
                                # for part in mensagem.walk():

                                    # # Verifica se possui anexo na mensagem do email
                                    # if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                                    #     continue

                                    # # Verifica se possui algum PDF em anexo - Senão achar PDF ele para essa execução do loop e vai para próxima mensagem
                                    # if part.get_content_type() == 'application/pdf':
                                    #     arquivo = part.get_filename()
                                    #     if not arquivo:
                                    #         continue  # Se não tem um nome de arquivo, pular
                                        
                                    # # Decodificação de cabeçalho do e-mail
                                    # arquivo = decode_header(arquivo)[0][0]
                                    # if isinstance(arquivo, bytes):
                                    #     arquivo = arquivo.decode('utf-8')
                                    
                                    # # Renomear o arquivo em anexo
                                    # arquivo = os.path.join(self._diretorio_pdf, f'{arquivo}')

                                    # # Converte o base64 para PDF e salva no diretório - atrelado ao trecho acima
                                    # with open(arquivo, 'wb') as anexo:
                                    #     anexo.write(part.get_payload(decode=True))

                                    # pegou_pdf += 1                                   

                        # parar aqui - die()
                        exit()
                        # Enviar email de logs para terceiros
                        # self.EnviarEmail()
                    
                    except Exception as e:
                        print(f'Erro: {e}\n')

                return True if pegou_pdf > 0 else False
            else:
                return False
            
        except Exception as e:
            print(f'Erro: {e}\n')
            
        
    