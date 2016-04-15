

Scraping o site do Globo Esporte
================================

O objetivo desse projeto é processar as paginas do [site do Globo Esporte](http://globoesporte.globo.com) e armazená-las em um banco de dados.

Ferramentas utilizadas
----------------------

* Scrapy  
    Modulo python para scraping de paginas

* sqlite3  
    Banco de dados onde os dados serão armazenados

* Requests  
    Modulo python para o carregamento das paginas

* outros? Work in progress.



Schema
------

Tabelas e uma breve descrição de onde esses dados vem.  
To do list, Work in progress, tudo ainda pode mudar.  
Provavelmente mais colunas serão adicionadas.  


- [ ] Jogador: ID, Apelido, Nome, Sobrenome, Data de Nascimento  
    ID -> presente no link  
    Apelido -> normalmente há, na pagina do jogador  
    Nome,Sobrenome,Data de Nascimento -> Pagina do Jogador.  
- [ ] Notícia: Titulo, link(ID), data  
    Titulo, Link, Data -> Lista de Notícias.  
- [ ] Jogador Mencionado: ID(jogador), ID(noticia)  
- [ ] Time: ID, Nome  
- [ ] Time Mencionado: ID time, ID noticia  
- [ ] Jogador no Time: ID time, ID jogador
Repensar:  
- [ ] Campeonato: ID, nome  
- [ ] Grupo de Campeonato: ID(Campeonato), link(id?)  
- [ ] Times do Grupo de Campeonato: ID(campeonato), ID(time)  
- [ ] Rodada: ID, ID(Campeonato)  
- [ ] Jogos da Rodada: ID(Rodada),ID(Time1), ID(Time2), Placar(dois times), penalti?(foi pros penaltis), placar penalti? (quantos gols nos penaltis)  
