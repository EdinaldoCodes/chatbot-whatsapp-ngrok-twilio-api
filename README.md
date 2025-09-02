## Projeto chatbot - WhatsApp (Ngrok + Twilio API)
Este projeto é um chatbot desenvolvido para lojas que atuam na venda de roupas, produtos tecnológicos e outros itens diversos. Ele visa oferecer atendimento automatizado via WhatsApp, utilizando a API do Twilio e integração com Ngrok para facilitar o desenvolvimento local.


### 🔧 Pré-requisitos
- Python 3.6+
- Conta gratuita na [Twilio](https://www.twilio.com/)
- WhatsApp instalado (para ativar o sandbox)
- [Ngrok](https://ngrok.com) para expor o servidor local

### ⚙️ Tecnologias Utilizadas
- Python – linguagem principal do projeto
- Flask – micro-framework para construção da API
- Twilio API – envio e recebimento de mensagens via WhatsApp
- Ngrok – exposição do servidor local para testes externos
- Webhook – comunicação entre o bot e o WhatsApp
- JSON  – armazenamento de informações de clientes e produtos

### 🚀 Como Executar
1. Clone o repositório
2. Crie o ambiente virtual e ative
```shell
python -m venv venv
```
Windows (cmd)
```shell
venv\Scripts\activate
```
Linux/macOS
```shell
source venv/bin/activate
```

4. Instale as dependências
```
pip install flask twilio
```
5. Configure as variáveis de ambiente (Twilio SID, Auth Token, número de telefone)
6. Execute o app.py e Ngrok

```
# Terminal 1
python app.py

# Terminal 2
ngrok http 5000

```
5. Inicie o túnel com Ngrok: ngrok http 5000
6. Configure o webhook no Twilio com a URL gerada pelo Ngrok
No console da Twilio, em **Sandbox do WhatsApp**, cole a URL do ngrok seguida de `/whatsapp`:
```
https://SEU-LINK-NGROK.ngrok.io/whatsapp
```
8. Teste o bot via WhatsApp
- Envie uma mensagem para o número Twilio do sandbox.
- Teste com:
    - `olá` → resposta de boas-vindas
    - `ajuda` → resposta de suporte

### 📄 Licença
Este projeto está sob a licença MIT
