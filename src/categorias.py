# src/categorias.py

categorias = {
    "Delivery": ["ifood", "rappi"],
    "Transporte": ["uber", "clickbus", "99"],
    "Mercado": [
        "nutricar", "doog hot dog", "zaffari bordini", "sonda supermercados",
        "smartbreak", "smart break", "pao de acucar-0052", "hiper zaffari sao paul",
        "carrefour", "mambo", "sacolao", "merc zillana", "super nosso", "oxxo"
    ],
    "Restaurante": [
        "bar urca", "mdpsthshdel rey", "lebanese food", "lugar 166",
        "caldo de cana do japa", "bar chopp", "mc donald", "bacio di latte",
        "baciodilatte", "bullguer", "subway", "piadina", "dama", "mb foods",
        "subito rice", "burger king", "come here", "mania de churrasco",
        "ifd*insalata", "viena express sho", "jishin comercio d", "star 176 sp corp",
        "aig comercio de a", "t&l comercio de alimentos", "h r alimentos",
        "zig*carreta churrascad", "fdl comercio de chocola", "expressinho da vila",
        "manteigaria portu", "parrilla sao jose", "mp*pizz", "tarek refeicoes",
        "braz perdizes", "doog", "restaurante", "restauran", "cafe", "dumas parrilla"
    ],
    "Shopping": [
        "loftystyle", "lofty style comercial", "youcom", "lindt sprungli brazil",
        "il93 sp higienopolis", "aramis", "daiso brasil", "lojas americanas",
        "shopping west plaza", "shopping vila olimpia", "bda vila olimpia", "shop", "shopping"
    ],
    "Hotel": ["hotel", "ibispoamoinhosdeventos", "venit hoteis", "airbnb"],
    "Passagem aerea": ["latam", "gol linhas"],
    "Academia": ["gavioes perdizes", "academia"],
    "Lazer": [" bar", "choperia", "clube", "club ", "montecarlopoker"],
    "Carro": ["posto", "shellbox", "sem parar", "centro automotivo", "j b f servicos automot", "carrera vw"],
    "Farmacia": ["drogaria", "drogasil", "pharmacia", "granado"],
    "Compras Online": ["amazon", "apple.", "editora o globo", "mercadolivre", "decolar", "wenov", "applecombill"],
    "Estacionamento": ["ec pinheiros", "estapar", "park", "estacionamento"],
    "Seguro": ["allianz"],
    "Pets": ["petlove"],
    "Cuidados pessoais": ["barbearia", "wesht cabeleireiros", "leo cosmeticos", "sobrancelhas", "sb2k cosmeticos", "dos santos marchiori"],
    "Outros": ["henrique schaumann"],
}

def categorizar(estabelecimento: str) -> str:
    est = str(estabelecimento).lower()

    for categoria, palavras in categorias.items():
        for palavra in palavras:
            if palavra in est:
                return categoria

    return "Outros"