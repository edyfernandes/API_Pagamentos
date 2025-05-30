
# 🧠 API de Integração com PayPal — FastAPI

API simples para criação e captura de pagamentos via **PayPal Sandbox**, utilizando **FastAPI** e **Python**.

---

## 🚀 Tecnologias

- Python
- FastAPI
- Requests
- python-dotenv
- Uvicorn

---

## 🔧 Instalação e Execução

### 1️⃣ Clone o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv .env
```

### 3️⃣ Ative o ambiente virtual

- **Windows**

```bash
.env\Scripts\activate
```

- **Linux/MacOS**

```bash
source .env/bin/activate
```

### 4️⃣ Instale as dependências

```bash
pip install fastapi uvicorn python-dotenv requests
```

### 5️⃣ Crie o arquivo `.env` na raiz do projeto e adicione suas credenciais:

```
PAYPAL_CLIENT_ID=SeuClientID
PAYPAL_CLIENT_SECRET=SeuClientSecret
```

🔗 Pegue essas credenciais no [PayPal Developer](https://developer.paypal.com/) em **Apps & Credentials** → **Sandbox**.

---

## ▶️ Como Rodar

Execute o servidor com:

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa:

- 🧠 Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠️ Endpoints Disponíveis

### ✅ Criar Pagamento

- **POST** `/create-payment`

**Body JSON:**

```json
{
  "amount": 10.00,
  "currency": "USD",
  "description": "Teste de Pagamento"
}
```

**Resposta:**

```json
{
  "order_id": "ID_DO_PEDIDO",
  "approval_url": "URL_para_aprovar_o_pagamento"
}
```

**Ação:** Acesse o link `approval_url` para simular a aprovação no Sandbox.

---

### 💰 Capturar Pagamento

- **POST** `/capture-payment/{order_id}`

**Resposta:**

```json
{
  "status": "COMPLETED",
  "details": { ... }
}
```

---

## 🧠 Como Simular no Sandbox

1. Acesse o link `approval_url` retornado no `/create-payment`.
2. Faça login com uma conta de comprador Sandbox do PayPal (crie em **Developer > Sandbox > Accounts**).
3. Após aprovar, copie o `order_id`.
4. Faça uma requisição no endpoint `/capture-payment/{order_id}` para finalizar a transação.
5. Consulte o dashboard do Sandbox para visualizar a transação:  
   [https://www.sandbox.paypal.com](https://www.sandbox.paypal.com)

---

## 📜 Licença

MIT License — sinta-se livre para usar e modificar!
