import pandas as pd

tabela = pd.read_csv("notas_alunos.csv.csv")
media = (tabela["NOTA_1"] + tabela["NOTA_2"]) / 2
tabela["media"] = media
tabela["situação"] = ""

tabela.loc[tabela["media"] >= 7, "situação"] = "APROVADO"
tabela.loc[tabela["media"] < 7, "situação"] = "REPROVADO"
tabela.loc[tabela["FALTAS"] > 5, "situação"] = "REPROVADO"
print(tabela)

maior_faltas = tabela["FALTAS"].max()
print(f"\nA maior quantidade de faltas foi {maior_faltas}")

media_geral = tabela["media"].median()
print(f"A média geral foi {media_geral}")

maior_media = tabela["media"].max()
print(f"A maior média foi {maior_media}")







