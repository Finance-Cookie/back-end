# FINANCE COOKIE

Este repositório contém o back-end do sistema desenvolvido para gerenciar de forma eficiente uma empresa de cookies, centralizando todas as informações essenciais do negócio. A API é responsável por controlar o fluxo de caixa, registrar entradas e saídas, além de gerenciar produtos, clientes, compras e vendas, oferecendo dados e históricos que auxiliam na análise financeira e na tomada de decisões estratégicas.

## 📚 Documentação do Projeto (Artefatos)
Os documentos essenciais para entendermos a engenharia do sistema estão presentes na pasta `/docs`:
* [Documento de Visão](./docs/documento_visao.md)
* [Modelo de Dados e Dicionário](./docs/modelo_dados.md)
* [Lista de User Stories](./docs/user_stories.md)
## 🚀 Configuração do Backend
O backend usa Django e foi preparado para conectar a um banco PostgreSQL remoto.
As variáveis de ambiente devem ser definidas em `.env` ou no serviço de implantação.

### Variáveis importantes
- `DJANGO_DB_ENGINE=django.db.backends.postgresql`
- `DJANGO_DB_NAME` = nome do banco remoto
- `DJANGO_DB_USER` = usuário do banco remoto
- `DJANGO_DB_PASSWORD` = senha do banco remoto
- `DJANGO_DB_HOST` = host remoto do PostgreSQL
- `DJANGO_DB_PORT` = porta do PostgreSQL (normalmente `5432`)
- `CORS_ALLOWED_ORIGINS` deve incluir a URL do app Expo

## 📱 Expo Frontend
Para usar o frontend Expo, configure `CORS_ALLOWED_ORIGINS` com as URLs do app no simulador/expo.
## 📚 Playlists para Estudos
Abaixo encontra-se playslists sobre as tecnologias e ferramentas usadas nesse projeto:
* [Playlist Django](https://www.youtube.com/playlist?list=PLLVddSbilcumgeyk0z6ko5U_FYPfbRO2C)
* [Playlist React Native](https://www.youtube.com/playlist?list=PLdDT8if5attEd4sRnZBIkNihR-_tE612_&si=RkeldFCJSyf5l4nW)
