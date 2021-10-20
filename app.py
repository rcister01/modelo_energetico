import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import squarify
from wordcloud import WordCloud
from matplotlib import rcParams

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()





with header:
    
    st.markdown("<h1>Eficiencia de un Modelo energético:</h1>",unsafe_allow_html=True)
    #st.markdown("<h2>Análisis de la eficiencia energética</h2>",unsafe_allow_html=True)
    st.markdown("<h3>Estudio de la eficiencia computacional en el desarrollo de un modelo aplicado a la medicion del consumo energético </h3>", unsafe_allow_html=True)
    add_selectbox = st.sidebar.selectbox(
    "Modelos",
    ("Q/datetime", "Q as product", "Finally"))

    add_selectbox = st.selectbox(
    "Indice",
    ("Data Exploration", "Machine Learning", "Nueral Network "))


with dataset:
    st.markdown("<h2>Unstestading the data...</h2>",unsafe_allow_html=True)


    #X = pd.read_csv("./raw_data/X.csv", index_col = 0)
    #X = X.head()
    #st.write(X)

    #Xs = df.shape
    #st.write(Xs)


    #y = pd.read_csv("./raw_data/y.csv", index_col = 0)
    #y = y.head()
    #st.write(y)

    #ys = df.shape
    #st.write(ys)





with features:
    st.markdown("<h3>Unstestading the data...</h3>",unsafe_allow_html=True)




with model_training:
    st.subheader("Model Training")
    st.markdown("<hr>SDG Rgressor</hr>",unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("R2 - monthly", "90%","Processing time : + 30", delta_color="inverse")
    col2.metric(label="R2 - biweekly", value="88%",  delta=-30 , delta_color="inverse")
    col3.metric("R2 - daily", "86%", "Processing time : - 45",)

    st.markdown("<h4>NN</h4>",unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("R2 - monthly", "90%", "gg")
    col2.metric("R2 - biweekly", "88%", "8hh")
    col3.metric("R2 - daily", "86%", "fgsg")




    names = [ 'Data original', 'Reducida', '2', '1']
    size = [1200,100,30,3]
    my_circle = plt.Circle( (0,0), 0.7, color='white')

    plt.rcParams['text.color'] = '406343'
    plt.style.context(None)
    plt.style.use('ggplot')
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = 'Tahoma'
    plt.pie(size, labels=names)
    p = plt.gcf()
    p.gca().add_artist(my_circle)


    st.pyplot(p)
    st.set_option('deprecation.showPyplotGlobalUse', False)



    
            # Set data
    df = pd.DataFrame({
    'group': ['S1','S2',],
    'N° Ocupantes': [5,3],
    'Ratio Area Vidrio': [5,4],
    'Delta Temp': [3,1],
    'Espesor Pared': [3,5],
    'Caudal de Aire': [2,3],
    'Espesor Techo' :[3,5],
    'Cantidad Dispositivos' :[2,2],
    
    
    })

    # number of variable
    categories=list(df)[1:]
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
    plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,5)


    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

    # Ind1
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Consumo Edificio 1")
    ax.fill(angles, values, 'b', alpha=0.1)

     #Ind2
    values=df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Consumo Edificio 2")
    ax.fill(angles, values, 'r', alpha=0.1)

    # Ind3
    
    #values=df.loc[2].drop('group').values.flatten().tolist()
    #values += values[:1]
    #ax.plot(angles, values, linewidth=1, linestyle='solid', label="T temperatura")
    #ax.fill(angles, values, 'r', alpha=0.1)


    plt.title('Influencia del las variables más significativas en el consumo')


    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))


    # Show the graph
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)




    time_range_x = [28,14,7,4,2,1]
    time_range_y = [0.96,0.94,0.91,0.901,0.89,0.88]


    # Basic stacked area chart.
    plt.plot(time_range_x, time_range_y)
    plt.xlabel("Days range")
    plt.ylabel("R*2")
    
   
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

 



    squarify.plot(sizes=[60,2,35,5], label=["Time-series", "group B", "group C", "group D"], color=["red","green","blue", "grey"], alpha=.4 )
    plt.axis('off')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

















CSS = """

header{color: #white;
}

h1 {color: #3D2C8D;
    font-size: 4.rem;
    font-family: Arial, Papyrus, fantasy;
    line-height: 1.2;
    adding-bottom: 10px;
    text-align: center;

}

h2 {color: #3D2C8D;
    font-size: 1.2rem;
    font-family: 'Arial';
    line-height: 0.75;
}



h3{
font-family: Arial, Papyrus, fantasy;
/font-size: 0.5rem;/
color: #3D2C8D;
line-height: 1.5;
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
  color: white;
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
