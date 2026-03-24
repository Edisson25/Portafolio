import pandas as pd
df = pd.read_csv('/home/el_gris/laboratorio#3/CSV_Laboratorio_3_AD-B.csv')
print(df)
df_null =df['City'].isnull().sum()
print(df_null)
df_duplicado = df['City'].duplicated().sum()
print(df_duplicado)
df_conteo = df['City'].value_counts()
print(df_conteo)
df.dropna(subset=['City'],inplace=True)
print(df)
limpiar_duplicados = df['City'].drop_duplicates()
print(limpiar_duplicados)
df['City'] = df['City'].str.lower()
print(df)
df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
print(df)
df.dropna(subset=['Category'],inplace=True)
print(df)
df['Category'] = df['Category'].str.lower()
print(df)
df['Category'] = df['Category'].str.strip().str.lower().replace(
    {
        'cat-c': 'category c',
        'cat c': 'category c'
    }
)
print(df["Category"].unique())
print(df)
df.to_csv('output.csv',index=False)