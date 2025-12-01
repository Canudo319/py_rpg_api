from sqlite3 import Connection
from db.database_util import get_db


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS conta_bancaria (
            conta_bancaria_id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            agencia TEXT NOT NULL,
            banco TEXT NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            conta_bancaria_id INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(usuario_id),
            FOREIGN KEY(conta_bancaria_id) REFERENCES conta_bancaria(conta_bancaria_id)
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS receitas (
            receita_id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor DECIMAL(6,3) NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS formas_pagamento (
            forma_pagamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            descricao TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS compras (
            compra_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            receita_id INTEGER NOT NULL,
            valor_total DECIMAL(6,3) NOT NULL,
            forma_pagamento_id INTEGER NOT NULL,
            FOREIGN KEY(cliente_id) REFERENCES clientes(cliente_id),
            FOREIGN KEY(receita_id) REFERENCES receitas(receita_id),
            FOREIGN KEY(forma_pagamento_id) REFERENCES formas_pagamento(forma_pagamento_id)
        )
    """)


if(__name__ == "__main__"):
    init_db()
    print("Migration Realizada com sucesso!")