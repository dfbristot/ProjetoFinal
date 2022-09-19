"""
Projeto Final

Autor: Daniel Francisco Bristot
19/09/2022
Versão: 0.0.1
"""
#importando os módulos necessários
import requests
import csv
import pandas
import openpyxl

#Inicialização
print('Iniciando')
#abrindo a página e armazenando o conteúdo na variável "dados"
#pagina = "http://dados.tce.rs.gov.br/dados/municipal/balancete-verificacao/2021/88414.csv"
pagina = "http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv"
req = requests.get(pagina)
dados = req.content

#gravando a variável "dados" em arquivo csv

csv_file = open('balancete.csv', 'wb')
csv_file.write(dados)
csv_file.close()

#lendo o csv em variável

balancete = pandas.read_csv('balancete.csv')

#gravando o balancete.xlsx

#writer = pandas.ExcelWriter('balancete.xlsx', engine='xlsxwriter')
writer = pandas.ExcelWriter('balancete.xlsx')
balancete.to_excel(writer, sheet_name='Balancete', index=False)
writer.save()
wkbk = openpyxl.load_workbook('balancete.xlsx')
novo_balancete = wkbk

#gravando o novo_balancete em novo arquivo novo_balancete.xlsx
novo_balancete.save('novo_balancete.xlsx')

#Final do programa
print('Programa final')




