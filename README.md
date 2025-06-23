# Casas Bahia Marketplace API Access Token

Este repositório tem como objetivo demonstrar de forma simples e prática como obter um access_token para integrar com a API do Marketplace das Casas Bahia. Essa autenticação é o primeiro passo fundamental para que você possa acessar os dados da plataforma, automatizar operações e construir integrações robustas com os serviços oferecidos.

## Como obter suas credenciais

### 1. Criar uma aplicação no Portal do Desenvolvedor

1. Acesse o [Portal do Desenvolvedor Casas Bahia](https://developer.casasbahia.com.br/)
2. Faça login ou crie uma conta
3. Acesse a seção "Minhas Aplicações"
4. Clique em "Criar Nova Aplicação"
5. Preencha as informações solicitadas:
   - Nome da Aplicação
   - Descrição
   - URL de retorno (callback)
   - Contatos técnicos
6. Após a criação, você receberá:
   - `client_id`
   - `client_secret`
   - Dados adicionais da aplicação


### Estrutura das credenciais

Após a autenticação bem-sucedida, você receberá um token no formato:

```
<client_id>:<access_token>
```

Exemplo:
```
s2939dsa:dada03312
```
