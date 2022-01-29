def apresentarGraficoDeLinha():
    # importing modules
    import csv
    import matplotlib.pyplot as plt
    # data import csv --> Upload the data in GitHub
    x = []
    y = []

    with open('sample-line.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    #definindo tamando do grafico
    plt.figure(figsize=(6, 5))
    plt.plot(x, y, label='Loaded from file!')
    #axis X
    plt.xlabel('Game Number')
    #axis y
    plt.ylabel('Game Length')
    #titulo do gráfico
    plt.title('Relação entre Game Number e Game Length')
    plt.legend()
    #salvar em png
    plt.savefig('graph_linha.png')
    plt.show()




#modificar plt.show() para plt.close() para somente salvar o arquivo do gráfico.
    #95%