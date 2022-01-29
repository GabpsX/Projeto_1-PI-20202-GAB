def apresentarGragicodeBarras():
    #importando modulos
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    #tamanho do grafico
    plt.figure(figsize=(10, 6))
    #lendo planilha
    df = pd.read_csv("wealth-per-country.csv")
    Country = df['Country'].values
    x = np.arange(len(Country))
    w = 0.3
    plt.bar(x - w, df['Median_Wealth'].values, width=w, label='Median_Wealth')
    
    plt.bar(x, df['Mean_Wealth'].values, width=w, label='Mean_Wealth')
    plt.bar(x + w, df['Population'].values, width=w, label='Population')
          
    #plt.plot(x, df[''].values, lw=2, label=
    #variavel x, com nomes dos paises:
    plt.xticks(x, Country)
    plt.ylim([0, 30])
    plt.tight_layout()

    #rotulo do grafico
    plt.xlabel('Countries')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
    #salvando imagem do grafico em png
    plt.savefig("graph_barras.png", bbox_inches="tight")
    #executando
    plt.show()
  
  
#modificar plt.show() para plt.close() para somente salvar o arquivo do gráfico.
    #100%