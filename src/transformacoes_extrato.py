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


def classificar(desc):

    d = desc.lower()

    if "pix" in d:
        return "PIX"

    if "ted" in d:
        return "TED"

    if "cartao" in d or "cartão" in d:
        return "Cartão"

    if "boleto" in d:
        return "Boleto"

    if "transferência" in d:
        return "TED"
    
    if "salário" in d:
        return "Salário XP"
    
    if "rendimento automático" in d:
        return "Rendimento automático"
    
    if "pagamento para banco xp s a" in d:
        return "Fatura cartão"

    return "Outros"


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

    df["Meio"] = df["Descricao"].apply(classificar)

    def classificar_tipo(row):
        descricao = str(row["Descricao"]).lower()
        valor = row["Valor"]

        if "transferência enviada para conta investimento" in descricao:
            return "Investimentos"
        
        if "transferência enviada para a conta investimento" in descricao:
            return "Investimentos"

        if valor > 0:
            return "Recebimento"

        return "Gasto"

    df["Tipo"] = df.apply(classificar_tipo, axis=1)

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
        ["Data", "Descricao", "Valor", "Meio", "Tipo", "hash"]
    ].values.tolist()

    return rows

if __name__ == "__main__":

    df = carregar_extratos("extratos/*.csv")
    df = tratar_extratos(df)

    print("\nPreview do DataFrame tratado:\n")
    print(df.head(20))

    print("\nTotal de linhas:", len(df))

