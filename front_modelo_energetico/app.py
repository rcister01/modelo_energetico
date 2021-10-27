from numpy.core.fromnumeric import size
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from wordcloud import WordCloud
from matplotlib import rcParams
import plotly.figure_factory as ff

header = st.container()
explanation = st.container()
eda = st.container()
screenshots = st.container()
conclusions = st.container()

st.set_option('deprecation.showPyplotGlobalUse', False)

with header:
    st.markdown("<h1>Proyecto sobre Consumo Energético</h1>",unsafe_allow_html=True)

with explanation:
    st.markdown("<h2>Objetivo</h2>",unsafe_allow_html=True)
    st.markdown("Construir un modelo estadístico para predecir y analizar los consumos de energía de un edificio.",unsafe_allow_html=True)

    st.markdown("<h2>Estrategia</h2>",unsafe_allow_html=True)
    st.markdown("Desarrollo de un modelo basado en una gran cantidad de simulaciones almacenadas.", unsafe_allow_html=True)

with eda:
    st.markdown("<h2>Análisis de la Data</h2>", unsafe_allow_html=True)



    # Set data
    df = pd.DataFrame({
        'group': ['S1','S2',],
        'N° Ocupantes': [5, 3],
        'Relación Area-Vidrio': [5, 4],
        'Diferencia T°': [3, 1],
        'Espesor Pared': [3, 5],
        'Caudal de Aire': [2, 3],
        'Espesor Techo': [3, 5],
        'Cantidad Dispositivos': [2, 2],
    })

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
    plt.ylim(0, 5)

    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

    # Ind1
    values = df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles,
            values,
            linewidth=1,
            linestyle='solid',
            label="Consumo Edificio 1")
    ax.fill(angles, values, 'b', alpha=0.1)

    #Ind2
    values = df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles,
            values,
            linewidth=1,
            linestyle='solid',
            label="Consumo Edificio 2")
    ax.fill(angles, values, 'r', alpha=0.1)





    st.markdown("<h3>Consumos por Estación del Año</h3>", unsafe_allow_html=True)

    # Add histogram data
    x1 = np.random.randn(200) - 5
    x2 = np.random.randn(200) - 3
    x3 = np.random.randn(200) + 1
    x4 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3, x4]

    group_labels = ['Primavera', 'Otoño', 'Invierno', 'Verano']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.25, .25, .25, .25])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)


    # Show the graph
    st.markdown("<h3>Influencia de las variables sobre el Consumo</h3>",
                unsafe_allow_html=True)
    st.pyplot()


    time_range_x = [28,14,7,4,2,1]
    time_range_y = [0.96,0.94,0.91,0.901,0.89,0.88]


    # Basic stacked area chart.
    st.markdown("<h3>Scoring (R2) con distintos rangos de días</h3>",
                unsafe_allow_html=True)
    plt.plot(time_range_x, time_range_y)
    plt.xlabel("Rango (días) de periodo")
    plt.ylabel("R*2")


    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.markdown("<h3>Matriz de Correlación de las features</h3>",
                unsafe_allow_html=True)
    st.image(
        "https://github.com/rcister01/modelo_energetico/blob/master/images/Captura_Corr.JPG?raw=true",
        width=750)

    st.image(
        "https://github.com/rcister01/modelo_energetico/blob/master/images/Captura_Corr_Zoom.JPG?raw=true",
        width=750)

with screenshots:
    st.markdown("<h2>Capturas del código</h2>", unsafe_allow_html=True)
    with st.expander("Ver loop para separar las horas en distintas filas"):
        st.image(
            "https://github.com/rcister01/modelo_energetico/blob/master/images/Captura_Loop.JPG?raw=true"
        )

    with st.expander("Ver un pipeline típico"):
        st.image(
            "https://github.com/rcister01/modelo_energetico/blob/master/images/Captura_Pipeline.JPG?raw=true"
        )

    with st.expander("Ver función generadora de redes neuronales"):
        st.image(
            "https://github.com/rcister01/modelo_energetico/blob/master/images/Captura_Generador_RN.JPG?raw=true"
        )


CSS = """

header{color: #white;
}

h1 {color: #3D2C8D;
    font-size: 4.rem;
    font-family: Arial;
    line-height: 1.2;
    adding-bottom: 10px;
    text-align: center;

}

h2 {color: #3D2C8D;
    font-size: 1.5rem;
    font-family: 'Arial';
    line-height: 0.75;
}

h3 {
font-family: Arial;
font-size: 1.2rem;
color: #3D2C8D;
line-height: 0.75;
}

h4 {color: #3D2C8D;
    font-family: 'Arial';
    font-size: 1.1rem;
}

image{
  position: relative;
  margin: 10px 80px 15px 120px
}


.stApp {

  font-family: 'Raleway', sans-serif;
  font-size: 13px;
  line-height: 24px;
  font-weight: 400;
  letter-spacing: 0.06em;
  background-color: #f1f9f0;
  overflow-y: scroll;
  overflow-x: hidden!important;
  -webkit-font-smoothing: antialiased;
  background-image: url("https://raw.githubusercontent.com/rcister01/modelo_energetico/54cccf208d3d3cb4b022b0072dafbc1fe987d6f9/Dise%C3%B1o%20sin%20t%C3%ADtulo.png");
  background-size: cover;

}

}

hr {
  border: dotted #ffc7c7 2.5px;
  border-bottom: none;
  /*otra forma puede ser
  border-style: none;
  border-top-style: dotted;*/
  /*ahora esot background-color: #ffc7c7;
  NO que sirve, para ponerle color a la linea:*/
  width: 12%;
  margin: 10px auto;
  font-size: 0.9rem;
}
.top{
  background-color: #defcf9;
  padding-top: 50px;
  text-align: left;
  line-height:2;
  border-bottom: 10px;
  border-radius: 5%;
  padding-bottom: 50px;
}


"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
