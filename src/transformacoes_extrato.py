import glob
import hashlib
import pandas as pd


def carregar_extratos(caminho="extratos/*.csv"):

    arquivos = glob.glob(caminho)

    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta extratos/")

    df = pd.concat([pd.read_csv(arq, sep=";") for arq in arquivos], ignore_index=True)

    if "Hora" in df.columns:
        df = df.drop(columns=["Hora"])

    if "Saldo" in df.columns:
        df = df.drop(columns=["Saldo"])

    return df


def tratar_extratos(df):

    df = df.copy()

    df["Descricao"] = df["Descricao"].astype(str).str.lower()

    df["Valor"] = (
        df["Valor"]
        .astype(str)
        .str.replace("R$", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df["hash"] = (
        df["Data"].astype(str)
        + "|"
        + df["Descricao"].astype(str)
        + "|"
        + df["Valor"].astype(str)
    ).apply(lambda x: hashlib.md5(x.encode()).hexdigest())

    return df


def montar_rows_extratos(df):

    rows = df[
        ["Data", "Descricao", "Valor", "hash"]
    ].values.tolist()

    return rows

if __name__ == "__main__":

    df = carregar_extratos("extratos/*.csv")
    df = tratar_extratos(df)

    print("\nPreview do DataFrame tratado:\n")
    print(df.head(20))

    print("\nTotal de linhas:", len(df))

