import pandas as pd
import matplotlib.pyplot as plt

# dicionário com os dados do gráfico
dados = {
    "Ryzen 5 5600X": 0.49889,
    "Ryzen 7 5700X": 0.31760,
    "Core i5-12400": 0.35392,
    "Ryzen 5 7600": 0.28898,           
    "Core i5-13400 DDR4": 0.34483,               
    "Ryzen 5 7600X": 0.47242,
    "Ryzen 7 5800X3D": 0.60815,           
    "Core i5-13600K": 0.58621,
    "Core i5-12600K": 0.31459,
    "Ryzen 7 7700": 0.53799,
    "Ryzen 7 7700X": 0.41163,
    "Ryzen 7 7800X3D": 0.40559,
    "Core i7-13700K": 0.50882, 
    "Ryzen 9 5900X": 0.69076, 
    "Ryzen 9 7900X": 0.29202, 
    "Ryzen 9 7900": 0.40342, 
    "Core i7-12700K": 0.71616, 
    "Ryzen 9 7900X3D": 0.54325, 
    "Core i9-13900K": 0.69231, 
    "Ryzen 9 7950X3D": 0.26909, 
    "Ryzen 9 7950X": 0.42, 
    "Core i9-12900K": 0.75263, 
    "Core i9-13900KS": 0.75132, 
    "Ryzen 9 5950X": 0.84242
}


#ordenar os dados
dadosOrdenados = {k: v for k, v in sorted(dados.items(), key=lambda item: item[1])}

#verificar se os dados foram ordenados corretamente
#print(dadosOrdenados)

#criar dataframe
df = pd.DataFrame(list(dadosOrdenados.items()), columns=['Processador', 'CustoBeneficio'])

#construir o gráfico com os dados
plt.figure(figsize=(12, 8))
plt.barh(df['Processador'], df['CustoBeneficio'], color='blue')
plt.xlabel('Custo-Benefício', fontsize=12)
plt.ylabel('Processadores', fontsize=12)
plt.title('Custo X Benefício', fontsize=20)
plt.xticks(fontsize=9)
plt.xlim(0, df['CustoBeneficio'].max() * 1.1)
plt.grid(axis='x')

#mostrar o gráfico
plt.show()
