import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
    cursor.execute("SELECT * FROM alunos") 
    print("Print1:", cursor.fetchall())
     
    
    cursor.execute("SELECT * FROM alunos")
    print("Segundo print:", cursor.fetchall())

    conexao.close() 
# Por que o segundo print não mostra absolutamente nada no console? 
# R= por que o fetchall( ) le e consome todos os registros da consulta do primeiro print, por isso o segundo retorna uma lista vazia ([ ])