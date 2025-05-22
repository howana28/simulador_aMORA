# Simulador de Parcelamento de Entrada de Imóvel - aMORA 🏠

Este é um projeto web simples usando Flask, que calcula:

- O valor da entrada do imóvel
- O valor a ser economizado (15% do valor do imóvel)
- Parcelas mensais base para guardar esse valor
- Correção dessas parcelas pelo IGPM (6% ao ano)
- Correção com juros compostos com taxa anual definida pelo usuário

## 💻 Como usar

### Requisitos

- Python 3.7 ou superior
- Flask (recomendado instalar via `pip install flask`)

### Execução

1. Clone ou baixe o projeto.
2. Navegue até a pasta do projeto no terminal.
3. Instale o Flask (se ainda não tiver):

```bash
pip install flask
```

4. Execute o aplicativo:

```bash
python simulador_amora.py
```

5. Abra seu navegador e acesse:

```
http://127.0.0.1:5000/
```

6. Preencha o formulário e veja o resultado da simulação.

## Estrutura do projeto

```
simulador_amora/
├── simulador_amora.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## Exemplo de entrada

- Valor do imóvel: 500000
- Percentual da entrada: 5
- Duração do contrato (anos): 3
- Taxa de juros anual: 8

