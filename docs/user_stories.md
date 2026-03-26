
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](/doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 26/03/2026 | 0.0.1   | Documento Inicial  | Elder |


### User Story US01 - Manter Usuário


:------------------------------------------------------------- |
| **Descrição** | O sistema deve manter o cadastro de usuário que tem acesso ao sistema via login e senha. Seus atributos para cadastro são: Nome, E-mail, Senha. Seu cadastro também deverá ter suas informações monetárias, os valores que atualmente estão em caixa (físico e/ou online). Para o login serão usados o E-mail e a Senha, permitindo o usuário acessar todos os módulos do sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF08          | Manter Usuário Administrador |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Elder                             | 
| **Desenvolvedor**         | Pedro                                  | 
| **Revisor**               | Felipe                               | 
| **Testador**              | Elder                                | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O usuário informa na tela de Cadastro as suas informações pessoais (Nome, E-mail, Senha); seus dados monetários e clica em Salvar, e é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso! |
| **TA01.02** | O usuário informa na tela de Cadastro as suas informações pessoais (Nome, E-mail, Senha) ou os dados monetários incorretamente, e clica em Salvar. E é notificado com a mensagem: Informações incorretas, tente novamente! |
| **TA01.03** | O usuário informa, na tela Login, os dados para logar incorretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. Mensagem: Informações incorretas, tente novamente. |
| **TA01.04** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA01.05** | O usuário, na tela Inicial, ao clicar no ícone do perfil é direcionado à tela do Perfil. Ao clicar em Editar ele poderá editar suas informações pessoais (Nome, E-mail, Senha). Ao editar, clica em Salvar e uma Mensagem é exibida: Dados salvos com sucesso! |