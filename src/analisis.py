import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = BASE_DIR/'data'/'raw'
DATA_PROCESSED = BASE_DIR/'data'/'processed'
def cargar_datos(file):
    return pd.read_csv(DATA_RAW/file)
def limpiar_datos(df):
    df['rating_count'] = pd.to_numeric(df['rating_count'],errors='coerce')
    df['product_name'] = (df['product_name'].astype(str).str.strip().str.lower())
    df['user_name'] = (df['user_name'].astype(str).str.strip().str.lower())
    df = df.dropna(subset=['rating_count'].copy())
    df = df.drop_duplicates(subset=['product_name'])
    return df
def productos_mejores_valorados(df,n=10,min_reviews=5):
    filtrado = df[df['rating_count']>=min_reviews]
    top = filtrado.sort_values('rating_count',ascending=False).head(n)[['product_name','rating','rating_count']]
    return top
def guardar_datos(df,file):
    df.to_csv(DATA_PROCESSED/file,index=False)
if __name__ == '__main__':
    df = cargar_datos('amazon.csv')
    df = limpiar_datos(df)
    guardar_datos(df,'pp.csv')
    top = productos_mejores_valorados(df)
    print(top)