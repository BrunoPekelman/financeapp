from src.transformacoes_fatura import carregar_faturas, tratar_faturas, montar_rows
from src.transformacoes_extrato import (
    carregar_extratos,
    tratar_extratos,
    montar_rows_extratos,
)

from src.turso_etl import (
    enviar_rows,
    SQL_INSERT_FATURAS,
    SQL_INSERT_EXTRATOS,
)


def main():

    # ETL das faturas
    df_faturas = carregar_faturas("faturas/*.csv")
    df_faturas = tratar_faturas(df_faturas)

    rows_faturas = montar_rows(df_faturas)

    enviar_rows(rows_faturas, SQL_INSERT_FATURAS, "Enviando faturas")


    # ETL dos extratos
    df_extratos = carregar_extratos("extratos/*.csv")
    df_extratos = tratar_extratos(df_extratos)

    rows_extratos = montar_rows_extratos(df_extratos)

    enviar_rows(rows_extratos, SQL_INSERT_EXTRATOS, "Enviando extratos")


if __name__ == "__main__":
    main()