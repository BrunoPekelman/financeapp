# src/transformacoes.py

import glob
import hashlib
import pandas as pd
from src.categorias import categorizar

def carregar_faturas(caminho: str = "faturas/*.csv") -> pd.DataFrame:
    arquivos = glob.glob(caminho)
    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta faturas/")

    df = pd.concat([pd.read_csv(arq, sep=";") for arq in arquivos], ignore_index=True)
    return df

def tratar_faturas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "Portador" in df.columns:
        df = df.drop(columns=["Portador"])

    df["Estabelecimento"] = df["Estabelecimento"].astype(str).str.lower()

    df["Valor"] = (
        df["Valor"]
        .astype(str)
        .str.replace("R$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
        .astype(float)
    )

    df = df[df["Valor"] >= 0]

    df[["parcela", "parcelas_total"]] = df["Parcela"].astype(str).str.extract(r"(\d+)\s*de\s*(\d+)")
    df["parcela"] = df["parcela"].fillna(1).astype(int)
    df["parcelas_total"] = df["parcelas_total"].fillna(1).astype(int)

    if "Parcela" in df.columns:
        df = df.drop(columns=["Parcela"])

    df["categoria"] = df["Estabelecimento"].apply(categorizar)

    df["hash"] = (
        df["Estabelecimento"].astype(str)
        + "|"
        + df["Valor"].astype(str)
        + "|"
        + df["Data"].astype(str)
        + "|"
        + df["parcela"].astype(str)
        + "|"
        + df["parcelas_total"].astype(str)
    ).apply(lambda x: hashlib.md5(x.encode("utf-8")).hexdigest())

    return df

def montar_rows(df: pd.DataFrame) -> list[list]:
    return df[
        ["Data", "Estabelecimento", "Valor", "categoria", "parcela", "parcelas_total", "hash"]
    ].values.tolist()

if __name__ == "__main__":

    df = carregar_faturas("faturas/*.csv")
    df = tratar_faturas(df)

    print("\nPreview do DataFrame tratado:\n")
    print(df.head(20))

    print("\nTotal de linhas:", len(df))