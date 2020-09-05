import pandas as pd
import re


def limpa_nome_municipio(nome):
    return re.sub(r'([\d]* [–-] )(.*)', r'\2', nome)


df = pd.read_csv('./arq_municipios_fronteiricos.csv')

municipios = df['Municipio']
municipios_limpos = municipios.apply(limpa_nome_municipio)

df['Municipio'] = municipios_limpos

print(df.head())
