## 1. Instalar o Python

Se você já consegue rodar scripts Python, pode pular esta etapa.

Confira a versão:

```bash
python --version
```

## 2. Criar um Ambiente Virtual

No terminal/prompt:

```bash
python -m venv venv
```

## 3. Ativar o Ambiente Virtual


```bash
venv\Scripts\activate
```

## 4. Instalar as dependencias

```bash
pip install -r requirements.txt
```

## 5. Para rodar o servidor

```bash
python server.py
```

## 6. Para criar a database(SQLite)
```bash
python migration.py
```