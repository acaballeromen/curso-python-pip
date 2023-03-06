import matplotlib.pyplot as plt    # steps to use the chart with matplotlib

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()    # steps to use the chart with matplotlib
    ax.pie(values, labels = labels) #steps to use the chart with matplotlib
    plt.savefig("pie.png")    # estamos dando la instruccion de que en vez de que muestre la grafica (plt.show) lo guarde como una imagen
    plt.close()