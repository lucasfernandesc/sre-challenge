# Exame - Bexs DevOps

## Desafio

Considerando as aplicações presentes neste repositório detalhadas abaixo, precisamos de uma stack que permita a comunicação entre ambas e o acesso de desenvolvedores.

* **Aplicação Frontend** - Aplicação em Python com Flask expondo na porta 8000 um formulário de criação de usuário contendo os campos ID e Name que realiza uma chamada Post com tais dados para a aplicação Backend.

* **Aplicação Backend** - Aplicação em Go (Golang) expondo na porta 8080 o CRUD de Usuários e armazena em um banco Sqlite3 local.

## Como entregar sua solução?

1) Clone do repositório

2) Realize as alterações necessárias para construção/automação da stack. Considere um ambiente local (máquina do desenvolvedor) ou algum provedor de cloud (AWS ou GCP).

3) Adicione e commit todos os arquivos criados/alterados (todos mesmo)

4) Gere um patch conforme comando de exemplo abaixo

5) Nos envie o patch através do email que entramos em contato

*Para gerar o patch:*
```
git format-patch origin/master --stdout > seu_nome.patch
```
## Requisitos

* Não publique sua solução. Apenas nos envie o que desenvolveu.
* Crie imagens Docker para ambas as aplicações. 
* Preencher este arquivo README.md com os detalhes, linha de raciocínio e dicas para os desenvolvedores que utilizarão sua solução.
* Considere que os desenvolvedores estão iniciando carreira e precisarão de mais detalhes de como executar sua solução.
* A Stack pode usar os recursos do próprio desenvolvedor(ex. VirtualBox, Docker, Docker-Compose) ou recursos de um provedor de cloud (Amazon Web Service ou Google Cloud)
* Não é necessário a criação de um pipeline. Considere que sua solução fará o bootstrap da Stack em questão.
* Não se preocupe em montar uma solução complexa. Dê preferência em montar uma solução simples que permita que o desenvolvedor realize melhorias.
* Apresente um desenho macro de arquitetura de sua solução.

## Bonus

* Sinta-se a vontade para realizar melhorias no código das aplicações, caso julgue necessário.

## Dúvidas

Entre em contato e nos questione.
_____________________________________

# Resolução

## Pré-requisitos:

* Sistema Operacional: Linux/Mac
* Docker
* Docker compose

## Racional

A ideia para esse desafio foi para que fosse uma soluçãos imples para o Desenvolvedor que está iniciando a carreira conseguir subir o ambiente em minutos, através de um único comando e em vários tipos de ambientes (Virtual box, Vmware, Máquinas EC2 etc...)

Antes criar o dockerfile e pensar nos steps para criação da imagem, fiz a subida dos ambientes de forma manual para entender o comportamento dos scripts e entender os pré-requisitos que cada imagem deveria ter.

Na pasta Frontend e Backend foram adicionados os respectivos Dockerfiles, facilitando o desenvolvedor caso o mesmo quisesse criar imagens separadas para diferentes tipos de cenários.

O arquivo docker-compose é a parte principal da solução, pois é nele que referenciamos os dockerfiles de Front e back, builda as imagens e sobe os containers de forma prática. Para isso, basta executar:

```
docker-compose up d
```

## Dicas

* Faça testes subindo localmente em sua máquina para facilitar o entendimento e pensar no que é necessário para subir em um container;
* Verifique se os pré-requisitos para o funcionamento estão configurados;
* Faça testes separados, primeiro execute um Dockerfile, se funcionou, pense qual seria a melhor forma de subir o ambiente de forma simples.

## Pontos de melhoria

* Eliminar os dockerfiles de cada pasta e adicionar todo o processo no docker compose;
* Adicionar volumes para facilitar edição de arquivos e ter facilidade em troubleshooting;
* adicionar um step na imagem da api com a crição de certificado Let's Encrypt e alterando a porta de exposição para 443;
* Criar um container separado para o banco de dados.

## O que imagens fazem no processo de build?

### Frontend
* Cria virtualenv em /opt/venv;
* Ativamos com uma variável de ambiente;
* Instalamos as dependências necessárias;
* Copiamos a pasta /opt/venv para o runner; 
* Adicionamos a pasta frontend ao container;
* A porta exposta é 8000;
* Dizemos que toda vez que subir um container que ele execute dentro da pasta /app/ o script frontend.py.

OBS: Isso ajuda a minimizar o tamanho da imagem do docker.

### Backend
* Cria pasta adicionarmos os arquivos;
* Adiciona a pasta backend para a pasta criada;
* Informamos que ele execute os processos no caminho $GOPATH/src/build;
* Importa os módulos;
* Builda arquivo main;
* A porta exposta é 8080;
* Dizemos que toda vez que subir um container que ele execute dentro da pasta $GOPATH/src/build o script main.

## Exemplo de execução:

![challenge](https://user-images.githubusercontent.com/34549251/161429053-0ee686de-da09-4ffa-852c-6eaef24d60e8.jpg)


## Como ficará após:

![challenge1](https://user-images.githubusercontent.com/34549251/161429088-f59ff50d-9ff3-40d6-8de9-af1cb2ed6a76.jpg)