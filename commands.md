`docker run -it ubuntu`
\- Sobe o ubuntu em um container no modo interativo

`docker run -d nginx`
\- Sobe o nginx em um container
 
`docker run -d -p 3000:3000 xginx`
\- Sobe o nginx em um container exporto na porta 3000
 
`docker run -d -p 3000:3000 --name nome-identificador xginx`
\- Sobe o nginx em um container com nome sugestivo exporto na porta 3000
 
`apt-get update`
\- Atualiza os pacores
 
`apt-get install vim`
\- Instala o vim
 
`exit`
\- Sai do modo interativo
 
`docker ps`
\- Lista todos os containers ativo.

`docker ps -a`
\- Lista todos os containers ativos e inativos.
 
`docker stop 190b1425807c`
\- Para o container que tem o ID/name passado
 
`docker start 190b1425807c`
\- Inicia o container que tem o ID passado
 
`docker logs 190b1425807c`
\- Mostra os logs do container com ID/name passado
 
`docker rm 190b1425807c`
\- Apaga o container com ID/name passado
 