import pandas as pd
import folium
from folium.plugins import HeatMap
import streamlit as st

# Caminho para o arquivo CSV na pasta 'api_telemetry'
file_path = 'D:/DADOS/Desktop/project/api_telemetry/pressao_corte.csv'

# Carregar os dados
data = pd.read_csv(file_path, delimiter=';')

# Função principal que será executada pelo Streamlit
def main():
    st.title('Mapa Pressão do Corte de Base Georreferenciado')

    # Mostrar prévia dos dados
    st.write("Prévia dos Dados:", data[['LAT', 'LON', 'VALUE']].head())

    # Criar o mapa centrado nas médias de LAT e LON
    m = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=11)

    # Gerar os dados para o mapa de calor
    heat_data = [[row['LAT'], row['LON'], row['VALUE']] for index, row in data.iterrows()]

    # Adicionar o mapa de calor ao mapa
    HeatMap(heat_data).add_to(m)

    # Usar o componente folium_static para renderizar o mapa no Streamlit
    from streamlit_folium import folium_static
    folium_static(m)

if __name__ == "__main__":
    main()
    