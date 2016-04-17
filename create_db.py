#!env python
# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect("database/database.sqlite")
cur = db.cursor()


#criação de tabelas
cur.execute('''create table Time (url text primary key, nome text)''')



cur.commit()
