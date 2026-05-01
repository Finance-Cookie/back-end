
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](/doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 26/03/2026 | 0.0.1   | Documento Inicial  | Elder |
| 26/03/2026 | 0.0.2   | Documento Inicial  | Pedro |


### User Story US01 - Manter Usuário


| **Descrição** | O sistema deve manter o cadastro de usuário que tem acesso ao sistema via login e senha. Seus atributos para cadastro são: Nome, E-mail, Senha. Seu cadastro também deverá ter suas informações monetárias, os valores que atualmente estão em caixa (físico e/ou online). Para o login serão usados o E-mail e a Senha, permitindo o usuário acessar todos os módulos do sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF08          | Manter Usuário Administrador |

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


### User Story US02 - Manter Produto

| **Descrição** | O sistema deve permitir manter o cadastro de produtos. Para cadastro, os atributos são: Nome, Descrição e Valor. Os produtos poderam ser incluídos, alterados, listados, visualizados e excluídos. |

| **Requisitos envolvidos** |                |
| ------------------------- | :------------- |
| RF05                      | Manter Produto |

| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 6 h       |
| **Tempo Gasto (real):** |           |
| **Tamanho Funcional**   | 5 PF      |
| **Analista**            | Elder     |
| **Desenvolvedor**       | Pedro     |
| **Revisor**             | Felipe    |
| **Testador**            | Elder     |

---

| Testes de Aceitação (TA) |                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código**               | **Descrição**                                                                                                                                      |
| **TA02.01**              | São informados Nome, Descrição e Valor na tela de cadastro de produto e clicado em Salvar. O sistema exibe: Produto cadastrado com sucesso! |
| **TA02.02**              | São informados dados inválidos ou incompletos e clicado em Salvar. O sistema exibe: Informações incorretas, tente novamente!                |
| **TA02.03**              | A listagem de produtos é acessada e todos os produtos cadastrados são visualizados.                                                           |
| **TA02.04**              | Um produto é selecionado e seus detalhes (Nome, Descrição e Valor) são visualizados.                                                |
| **TA02.05**              | Os dados de um produto são alterados e clicado em Salvar. O sistema exibe: Produto atualizado com sucesso!                                  |
| **TA02.06**              | Um produto é excluído e o sistema exibe: Produto excluído com sucesso!                                                                 |


### User Story US03 - Manter Entrada


| **Descrição** | O sistema deve permitir o gerenciamento de entradas financeiras, possibilitando ao administrador registrar, visualizar, alterar, listar e excluir entradas. Cada entrada possui os seguintes atributos: Data, Valor Total, Descrição, Forma de Pagamento e Tipo de Entrada. O sistema deve garantir o controle adequado dessas informações para apoiar a gestão financeira da empresa. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Manter Entrada |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 5 PF                                | 
| **Analista**              | Elder                               | 
| **Desenvolvedor**         | Felipe                               | 
| **Revisor**               | Elder                              | 
| **Testador**              | Pedro                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA03.01** | O administrador informa os dados da entrada (Data, Valor Total, Descrição, Forma de Pagamento e Tipo) corretamente e clica em Salvar. O sistema exibe a mensagem: Entrada cadastrada com sucesso! |
| **TA03.02** | O administrador informa dados inválidos ou incompletos ao cadastrar uma entrada e clica em Salvar. O sistema exibe a mensagem: Informações inválidas, tente novamente! |
| **TA03.03** | O administrador acessa a listagem de entradas e visualiza todas as entradas cadastradas, podendo aplicar filtros por Data, Forma de Pagamento e Tipo. |
| **TA03.04** | O administrador seleciona uma entrada para visualizar e o sistema exibe todas as informações detalhadas da entrada. |
| **TA03.05** | O administrador edita uma entrada existente, altera os dados permitidos e clica em Salvar. O sistema exibe a mensagem: Entrada atualizada com sucesso! |
| **TA03.06** | O administrador exclui uma entrada no mesmo dia de cadastro (até 23h59) e o sistema exibe a mensagem: Entrada excluída com sucesso! |
| **TA03.07** | O administrador tenta excluir uma entrada após o prazo permitido e o sistema exibe a mensagem: Não é possível excluir esta entrada após o prazo permitido. |


### User Story US04 - Manter Saída


| **Descrição** | O sistema deve permitir o gerenciamento de saídas financeiras, possibilitando ao administrador registrar, visualizar, alterar, listar e excluir saídas. Cada saída possui os seguintes atributos: Data, Valor Total, Descrição, Forma de Pagamento e Tipo da Saída. O sistema deve garantir o controle adequado dessas informações para apoiar a gestão financeira da empresa. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF03          | Manter Saída |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 5 PF                                | 
| **Analista**              | Felipe                               | 
| **Desenvolvedor**         | Elder                               | 
| **Revisor**               | Felipe                              | 
| **Testador**              | Pedro                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA04.01** | O administrador informa os dados da saída (Data, Valor Total, Descrição, Forma de Pagamento e Tipo) corretamente e clica em Salvar. O sistema exibe a mensagem: Saída cadastrada com sucesso! |
| **TA04.02** | O administrador informa dados inválidos ou incompletos ao cadastrar uma saída e clica em Salvar. O sistema exibe a mensagem: Informações inválidas, tente novamente! |
| **TA04.03** | O administrador acessa a listagem de saídas e visualiza todas as saídas cadastradas, podendo aplicar filtros por Data, Forma de Pagamento e Tipo. |
| **TA04.04** | O administrador seleciona uma saída para visualizar e o sistema exibe todas as informações detalhadas da saída. |
| **TA04.05** | O administrador edita uma saída existente, altera os dados permitidos e clica em Salvar. O sistema exibe a mensagem: Saída atualizada com sucesso! |
| **TA04.06** | O administrador exclui uma saída no mesmo dia de cadastro (até 23h59) e o sistema exibe a mensagem: Saída excluída com sucesso! |
| **TA04.07** | O administrador tenta excluir uma saída após o prazo permitido e o sistema exibe a mensagem: Não é possível excluir esta saída após o prazo permitido. |

### User Story US05 - Manter Venda


| **Descrição** | O sistema deve permitir o gerenciamento de vendas, possibilitando ao administrador realizar a inclusão de vendas associadas a clientes, além de alterar, listar, visualizar e excluir registros. O sistema deve calcular automaticamente o valor total com base nos itens, frete e descontos, e aplicar a regra restritiva de exclusão apenas no dia da operação. |

| **Requisitos envolvidos** |                                                     |
| ------------- | :------------------------------------------------------------- |
| RF02          | Manter Venda |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 8 PF                                | 
| **Analista**              | Elder                               | 
| **Desenvolvedor**         | Pedro                               | 
| **Revisor**               | Felipe                              | 
| **Testador**              | Elder                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA05.01** | O administrador informa os dados da venda (Data, Cliente, Itens, Forma de Pagamento, Desconto, Frete e Tipo) e clica em Salvar. O sistema calcula o Valor Total e exibe: Venda realizada com sucesso! |
| **TA05.02** | O administrador altera itens, desconto ou frete de uma venda e o sistema recalcula o Valor Total automaticamente antes de salvar as alterações. |
| **TA05.03** | O administrador acessa a listagem de vendas e aplica filtros por Data, Cliente, Forma de Pagamento ou Tipo, visualizando apenas os resultados correspondentes. |
| **TA05.04** | O administrador seleciona uma venda para visualizar e o sistema exibe detalhadamente todos os dados, incluindo a lista de itens vendidos e o cliente associado. |
| **TA05.05** | O administrador solicita a exclusão de uma venda realizada no mesmo dia (até as 23h59) e o sistema exibe a mensagem: Venda excluída com sucesso! |
| **TA05.06** | O administrador tenta excluir uma venda realizada em data anterior à atual e o sistema exibe a mensagem: Não é possível excluir esta venda após o prazo permitido. |


### User Story US07 - Manter Tipo


| **Descrição** | O sistema deve permitir o gerenciamento de tipos (categorias) utilizados para classificar entradas, saídas, vendas ou compras. Cada tipo possui como atributo o Nome. O sistema deve permitir incluir, alterar, listar, visualizar e excluir tipos, garantindo a organização das movimentações financeiras. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF06          | Manter Tipo |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 4 PF                                | 
| **Analista**              | Elder                               | 
| **Desenvolvedor**         | Pedro                               | 
| **Revisor**               | Felipe                              | 
| **Testador**              | Elder                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA05.01** | O administrador informa o Nome do tipo corretamente na tela de cadastro e clica em Salvar. O sistema exibe: Tipo cadastrado com sucesso! |
| **TA05.02** | O administrador informa dados inválidos ou deixa o Nome em branco e clica em Salvar. O sistema exibe: Informações incorretas, tente novamente! |
| **TA05.03** | O administrador informa dados inválidos, repetidos ou deixa o Nome em branco e clica em Salvar. O sistema exibe: Informações incorretas, tente novamente! |
| **TA05.04** | O administrador seleciona um tipo e visualiza seus detalhes (Nome). |
| **TA05.05** | O administrador altera o Nome de um tipo existente e clica em Salvar. O sistema exibe: Tipo atualizado com sucesso! |
| **TA05.06** | O administrador exclui um tipo e o sistema exibe: Tipo excluído com sucesso!|

### User Story US08 - Manter Cliente


| **Descrição** | O sistema deve permitir o gerenciamento de clientes, possibilitando ao administrador cadastrar, visualizar, alterar, listar e excluir clientes. Cada cliente possui os seguintes atributos: Nome, Telefone e Endereço (Logradouro, Bairro e Número). O sistema deve oferecer facilidades de busca e ordenação para otimizar o atendimento e a gestão da base de contatos. |

| **Requisitos envolvidos** |                                                     |
| ------------- | :------------------------------------------------------------- |
| RF07          | Manter Cliente |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 6 PF                                | 
| **Analista**              | Pedro                               | 
| **Desenvolvedor**         | Elder                               | 
| **Revisor**               | Felipe                              | 
| **Testador**              | Pedro                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA08.01** | O administrador informa os dados do cliente (Nome, Telefone e Endereço completo) corretamente e clica em Salvar. O sistema exibe a mensagem: Cliente cadastrado com sucesso! |
| **TA08.02** | O administrador deixa campos obrigatórios em branco ou informa dados inválidos e clica em Salvar. O sistema exibe a mensagem: Informações incorretas, tente novamente! |
| **TA08.03** | O administrador acessa a listagem de clientes e visualiza todos os registros, podendo utilizar o filtro alfabético para ordenação. |
| **TA08.04** | O administrador utiliza o campo de pesquisa na listagem de clientes e o sistema retorna apenas os resultados que condizem com o termo pesquisado. |
| **TA08.05** | O administrador seleciona um cliente para visualizar e o sistema exibe detalhadamente o Nome, Telefone e o Endereço (Logradouro, Bairro e Número). |
| **TA08.06** | O administrador edita os dados de um cliente existente (Nome, Telefone ou Endereço) e clica em Salvar. O sistema exibe a mensagem: Dados do cliente atualizados com sucesso! |
| **TA08.07** | O administrador solicita a exclusão de um cliente e, após confirmação, o sistema exibe a mensagem: Cliente excluído com sucesso! |


### User Story US10 - Manter Relatório


| **Descrição** | O sistema deve permitir a visualização de relatórios que apresentam dados consolidados por setor do sistema. O administrador poderá visualizar relatórios gerais e acessar relatórios específicos com informações detalhadas, auxiliando na análise e tomada de decisão. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF10          | Manter Relatório |

| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 5 PF                                | 
| **Analista**              | Elder                               | 
| **Desenvolvedor**         | Felipe                               | 
| **Revisor**               | Pedro                              | 
| **Testador**              | Elder                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA05.01** | O administrador acessa a área de relatórios e visualiza os relatórios disponíveis por setor do sistema. |
| **TA05.02** | O administrador seleciona um setor específico e o sistema exibe todos os relatórios daquele setor. |
| **TA05.02** | O administrador seleciona um relatório específico e o sistema exibe suas informações detalhadas corretamente. |
