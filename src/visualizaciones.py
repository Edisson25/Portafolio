import seaborn as sns
import matplotlib.pyplot as plt
def plot_productos_mejores_valorados(df,product_name,rating_count):
    plt.figure(figsize=(9,8))
    sns.barplot(data=df,x='product_name',y='rating_count')
    plt.xlabel("Nombre del Producto")
    plt.ylabel("Valoracion del Producto")
    plt.show()