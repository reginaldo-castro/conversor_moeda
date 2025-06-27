# 💱 Conversor de Moedas com Django

Este é um projeto de conversor de moedas em tempo real utilizando **Django**, com integração a uma API de câmbio e suporte a **cache** para reduzir chamadas externas. A aplicação está containerizada com **Docker** e orquestrada via **docker-compose**.

---

## 🚀 Funcionalidades

- Conversão entre múltiplas moedas (USD, EUR, GBP, JPY, BRL, etc)
- Integração com [ExchangeRate API](https://www.exchangerate-api.com/)
- Cache automático das taxas de câmbio por 12 horas
- Interface simples com formulário HTML
- Deploy local via Docker

---

## 🛠 Tecnologias Utilizadas

- Python 3.12
- Django 4.2
- HTML + CSS (estático)
- Docker
- docker-compose
- ExchangeRate API
- Cache com `LocMemCache` (pode ser adaptado para Redis)

---

## 🐳 Como Executar com Docker

### 1. Clone o repositório

```
    git clone https://github.com/reginaldo-castro/conversor_moeda.git
    cd conversor_moeda
```

### 2. Crie o arquivo .env (opcional)
## .env
``` 
DEBUG=True
ALLOWED_HOSTS=*
SECRET_KEY=
ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=currenypassword
DB_HOST=db
DB_PORT=5432
```
3. Construa e suba os containers
 ```
    docker-compose up --build
    Acesse em: http://localhost:8000
```

📂 Estrutura do Projeto
    
    ├── converter/
    │   ├── templates/converter/convert.html
    │   └── views.py
    ├── currency/
    │   ├── settings.py
    │   └── urls.py
    ├── manage.py
    ├── Dockerfile
    ├── infra/
        ├── docker-compose.yml
        └── run.sh
    ├── requirements.txt
    |── static/css/style.css
    └── README.md
