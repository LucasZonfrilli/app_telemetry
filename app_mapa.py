import pandas as pd
import folium
from folium.plugins import HeatMap
import streamlit as st

# Função principal que será executada pelo Streamlit
def main():
    st.title('Mapa Pressão do Corte de Base Georreferenciado')

    # Carregar o arquivo CSV usando o uploader do Streamlit
    uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

    if uploaded_file is not None:
        # Carregar os dados
        data = pd.read_csv(uploaded_file, delimiter=';')

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
