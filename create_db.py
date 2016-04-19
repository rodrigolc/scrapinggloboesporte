#!env python
# -*- coding: utf-8 -*-

import sqlite3
import os
import os.path

if not os.path.exists("./database"):
    os.mkdir("./database")

db = sqlite3.connect("database/database.sqlite")
cur = db.cursor()


#criação de tabelas
cur.execute('''create table Time (url_suffix text primary key, nome text)''')
cur.execute('''create table Jogador (url_suffix text primary key, nome_popular text, nome text, sobrenome text)''')
cur.execute('''create table Noticia (url_suffix text primary key, titulo text,subtitulo text)''')
cur.execute('''create table JogadorNoTime (url_suffix_time text, url_suffix_jogador text)''')
cur.execute('''create table JogadorMencionado (url_suffix_noticia text, url_suffix_jogador text)''')
cur.execute('''create table TimeMencionado (url_suffix_noticia text, url_suffix_time text)''')

db.commit()
db.close()
