#!env python
# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect("database/database.sqlite")
cur = db.cursor()


#criação de tabelas
cur.execute('''create table Time (url_suffix text primary key, nome text)''')
cur.execute('''create table Jogador (url_suffix text primary key, apelido text, nome text, sobrenome text)''')
cur.execute('''create table Noticia (url_suffix text primary key, titulo text,subtitulo text)''')
cur.execute('''create table JogadorNoTime (url_suffix_time text, url_suffix_jogador text)''')

db.commit()
