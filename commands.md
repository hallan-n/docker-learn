# Básico
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
 
`docker build Dockerfile`
\- Cria a sua imagem
 
`docker image`
\- Lista as imagens que você criou

`docker rmi 190b1425807c`
\- Apaga a imagem com ID passado

`docker top 190b1425807c`
\- Lista todos os processos do container

`docker stats`
\- Fala o consumo de hardware de todos os containers

`docker stats 190b1425807c`
\- Fala o consumo de hardware do container

`docker inspect 190b1425807c`
\- Lista todas as configurações do container
 
`docker network ls`
\- Lista todas as redes

`docker network create my_net`
\- Cria uma rede

`docker network create my_net --subnet 192.168.134.0/24 gateway 192.168.134.1`
\- Cria uma rede com range de ip especifico
 
`docker network inspect create my_net`
\- Lista as configurações da rede
 
`docker network rm my_net`
\- Remove a rede
`docker network prune`
\- Remove todas as redes não utilizadas

`docker run --name webhost -d --network my_net`
\- Sobe um container com uma rede associada
 
# Dockerfile


`FROM nginx`
\- Define a imagem base.
Dockerfile
Copy code
MAINTAINER

`MAINTAINER <nome>`
\- Define o autor ou mantenedor.

`ARG <variavel>`
\- Define variáveis de build.

`ENV <nome>=<valor>`
\- Define variáveis de ambiente.

`RUN <comando>`
\- Executa comandos durante a construção.

`COPY <origem> <destino>`
\- Copia arquivos do host para a imagem.

`ADD <origem> <destino>`
\- Similar ao COPY, mas com funcionalidades adicionais (pode extrair arquivos tar, copiar de URLs, etc.).

`WORKDIR <caminho>`
\- Define o diretório de trabalho.

`EXPOSE <porta>`
\- Informa as portas em que o contêiner escuta durante a execução.

`CMD ["<comando>", "<arg1>", "<arg2>"]`
\- Fornece argumentos padrão para a execução do contêiner.

`ENTRYPOINT ["<comando>", "<arg1>", "<arg2>"]`
\- Configura um executável padrão para o contêiner.

`VOLUME ["<caminho>"]`
\- Cria um ponto de montagem para volumes.

`USER <nome ou UID>`
\- Define o usuário ou UID a ser usado quando o contêiner é executado.

`LABEL <chave>=<valor>`
\- Adiciona metadados à imagem.

# Volume

`docker container run -ti --mount type=bind,src=/opt/giropops,dst=/giropops ubuntu`
\- Cria um volume do tipo bind
