from analisis import cargar_datos,limpiar_datos,productos_mejores_valorados
from visualizaciones import plot_productos_mejores_valorados
def correr_analisis(file:str,product_name:str,rating_count:str):
    df = cargar_datos(file)
    df = limpiar_datos(df)
    top = productos_mejores_valorados(df,n=10)
    plot_productos_mejores_valorados(top,product_name,rating_count)
    print(top)
if __name__ == '__main__':
    correr_analisis(
        file = ('amazon.csv'),
        product_name = 'product_name',
        rating_count = 'rating_count'
    )