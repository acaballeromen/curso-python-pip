import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{name}.png")    # estamos dando la instruccion de que en vez de que muestre la grafica (plt.show) lo guarde como una imagen
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.savefig("pie.png")    # estamos dando la instruccion de que en vez de que muestre la grafica (plt.show) lo guarde como una imagen
  plt.close()
  
if __name__ == "__main__":
  labels = ["a", "b", "c"]
  values = [10, 40, 800]
# generate_bar_chart(labels, values)
# generate_pie_chart(labels, values)