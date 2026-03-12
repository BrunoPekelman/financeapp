# main.py

from src.transformacoes_fatura import carregar_faturas, tratar_faturas, montar_rows
from src.turso_etl import enviar_para_turso

def main():
    df = carregar_faturas("faturas/*.csv")
    df = tratar_faturas(df)
    rows = montar_rows(df)
    enviar_para_turso(rows)

if __name__ == "__main__":
    main()