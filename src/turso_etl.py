# src/turso_etl.py

import libsql
from tqdm import tqdm
from src.config import TURSO_DATABASE_URL, TURSO_AUTH_TOKEN


SQL_INSERT_FATURAS = """
INSERT OR IGNORE INTO faturas
(data, estabelecimento, valor, categoria, parcela, parcelas_total, hash)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""


SQL_INSERT_EXTRATOS = """
INSERT OR IGNORE INTO extratos
(data, descricao, valor, meio, tipo, hash)
VALUES (?, ?, ?, ?, ?, ?)
"""


def conectar():

    conn = libsql.connect(
        "hello.db",
        sync_url=TURSO_DATABASE_URL,
        auth_token=TURSO_AUTH_TOKEN
    )

    return conn


def enviar_rows(rows, sql, descricao):

    conn = conectar()

    for r in tqdm(rows, desc=descricao):

        conn.execute(sql, r)

    conn.commit()

    print(f"{len(rows)} linhas processadas.")