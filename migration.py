from sqlite3 import Connection
from db.database_util import get_db


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS dices (
            dice_key INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            descricao TEXT NOT NULL,
            valor_faces INTEGER NOT NULL CHECK (valor_faces >= 0)
        );
    """)

    create_dices(conn, "D_6", "d6", 6)
    create_dices(conn, "D_4", "d4", 4)
    create_dices(conn, "D_12", "d12", 12)
    create_dices(conn, "D_20", "d20", 20)


def create_dices(conn: Connection, codigo: str, descricao: str, valor_face: int):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM dices WHERE codigo = ?", (codigo,))
    ok = cursor.fetchone()
    if not ok:
        conn.execute("INSERT INTO dices(codigo, descricao, valor_faces) VALUES(?,?,?)", (codigo, descricao, valor_face,))
        conn.commit()


if(__name__ == "__main__"):
    init_db()
    print("Migration Realizada com sucesso!")