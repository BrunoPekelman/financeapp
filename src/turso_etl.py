# src/turso_etl.py

import libsql
from tqdm import tqdm
from src.config import TURSO_DATABASE_URL, TURSO_AUTH_TOKEN

SQL_INSERT = """
INSERT OR IGNORE INTO faturas
(data, estabelecimento, valor, categoria, parcela, parcelas_total, hash)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

def conectar():
    return libsql.connect(
        "hello.db",
        sync_url=TURSO_DATABASE_URL,
        auth_token=TURSO_AUTH_TOKEN
    )

def enviar_para_turso(rows: list[list]) -> None:
    conn = conectar()

    for r in tqdm(rows, desc="Enviando para Turso"):
        conn.execute(SQL_INSERT, r)

    conn.commit()
    print(f"{len(rows)} linhas processadas.")