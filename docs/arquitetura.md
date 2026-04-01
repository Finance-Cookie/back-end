# Projeto Arquitetural do Software

Documento construído a partido do **Modelo BSI - Doc 005 - Documento de Projeto Arquitetual do Software** que pode ser encontrado no
link:https://docs.google.com/document/d/1i80vPaInPi5lSpI7rk4QExnO86iEmrsHBfmYRy6RDSM/edit?usp=sharing

## Descrição da Arquitetura do Projeto

O sistema Finance Cookie segue uma arquitetura do tipo cliente-servidor, onde o front-end e o back-end são desacoplados e se comunicam por meio de uma API.

A aplicação adota o modelo monolítico no back-end, desenvolvido com Django, concentrando toda a lógica de negócio, regras do sistema e acesso ao banco de dados em uma única aplicação. A comunicação entre o cliente e o servidor ocorre através de uma API REST, implementada com Django REST Framework, utilizando o padrão de troca de dados em formato JSON.

O front-end é desenvolvido em React Native, funcionando como cliente da aplicação, sendo responsável pela interface com o usuário e consumo dos serviços disponibilizados pela API.

Essa arquitetura permite:

- Separação de responsabilidades (frontend/backend)
- Facilidade de manutenção
- Escalabilidade futura (possível migração para microsserviços)

## Visão Geral da Arquitetura

Imagem com a organização geral dos componentes da arquitetura do projeto:

![Arquitetura Django Framework](/django-arquitetura.jpg)

## Requisitos Não-Funcionais

Requisito  | Detalhes
---------- | -------------------------------------------- 
Desempenho | 1. As requisições da API devem responder em até 2 segundos em condições normais de uso. <br />2. Listagens devem utilizar paginação para otimizar consultas. <br />3. O sistema deve suportar múltiplas requisições simultâneas sem degradação significativa.<br />
Usabilidade | 1. A interface deve ser intuitiva e de fácil navegação. <br/>2. O usuário deve conseguir realizar operações básicas com poucos cliques.<br/>
Portabilidade | 1. O sistema deve funcionar em diferentes dispositivos móveis (Android e futuramente iOS).<br/>2. O backend deve ser executável em ambientes Linux.<br/>
Segurança | 1. O acesso à API deve ser protegido por autenticação.<br/>2. Os dados sensíveis devem ser tratados de forma segura.

## Mecanismos arquiteturais

| Mecanismo de Análise | Mecanismo de Design        | Mecanismo de Implementação        | Justificativa/Responsabilidade |
|----------------------|---------------------------|----------------------------------|--------------------------------|
| Persistência         | Banco de dados relacional | PostgreSQL                       | Utilizado para armazenar os dados de forma estruturada, garantindo integridade, consistência e suporte a transações, essenciais para controle financeiro. |
| Camada de Dados      | ORM                       | Django ORM                       | Facilita a interação com o banco de dados, abstraindo comandos SQL e aumentando a produtividade e segurança no desenvolvimento. |
| Backend              | API REST                  | Django + Django REST Framework   | Responsável pelas regras de negócio e exposição dos dados através de uma API padronizada, permitindo integração com diferentes clientes. |
| Frontend             | Interface Mobile          | React Native                     | Responsável pela interface do usuário, proporcionando uma experiência mobile moderna e permitindo o consumo da API de forma eficiente. |
| Comunicação          | HTTP/JSON                 | API REST                         | Define o padrão de troca de dados entre cliente e servidor, utilizando protocolo HTTP e formato JSON, garantindo interoperabilidade e leveza. |
| Build                | Containerização           | Docker                           | Permite padronizar o ambiente de desenvolvimento e execução, evitando problemas de configuração entre diferentes máquinas. |
| Deploy               | Containers                | Docker Compose                   | Facilita a orquestração e execução dos serviços da aplicação (backend e banco de dados), simplificando o processo de implantação. |

# Implantação

O sistema será implantado seguindo o modelo cliente-servidor:

- Frontend (React Native):
Executado em dispositivos móveis (Android inicialmente)
Consome a API via requisições HTTP
- Backend (Django):
Hospedado em servidor Linux ou ambiente em nuvem
Responsável pelo processamento das regras de negócio
- Banco de Dados:
PostgreSQL
Armazena todas as informações do sistema
- Comunicação:
Realizada via API REST utilizando protocolo HTTP

# Referências

Links utilizados como referência sobre Arquitetura de Software e documentação de Arquiteturas.

https://edisciplinas.usp.br/pluginfile.php/134335/mod_resource/content/1/Aula13_ArquiteturaSoftware_02_Documentacao.pdf

http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx

http://diatinf.ifrn.edu.br/prof/lib/exe/fetch.php?media=user:1301182:disciplinas:arquitetura:exemplo-arquitetura-01.pdf

Peter Eeles; Peter Cripps. The Process of Software Architecting, Addison-Wesley Professional, 2009.

Paul Clements; Felix Bachmann; Len Bass; David Garlan; James Ivers; Reed Little; Paulo Merson; Robert Nord; Judith Stafford. Documenting Software Architectures: Views and Beyond, Second Edition, Addison-Wesley Professional, 2010.