import streamlit as st
import pandas as pd

# Configuración general de la página
st.set_page_config(page_title="Defunciones Argentina 2024", layout="wide")

# Título y portada
st.title("📊 **Defunciones en Argentina (1880 - 2024)**")

st.markdown("""
### **Bienvenido** a la visualización interactiva de defunciones en Argentina
Este dashboard muestra un análisis detallado de las defunciones en Argentina desde el año 1880 hasta 2024. Los gráficos presentados han sido procesados a partir de un conjunto de datos que incluye variables como el año de defunción, la edad y el género de las personas fallecidas.
""")

# Mostrar dataset limpio
df = pd.read_csv("dataset_limpio.csv")
st.subheader("**Dataset Utilizado**")
st.markdown("""
Este es el conjunto de datos procesado, extraidos de Buenos Aires Data, este dataset contiene información sobre las defunciones ocurridas en Argentina en el período de 1880 a 2024.
""")
st.dataframe(df, use_container_width=True)

# Explicación y visualización de gráficos
st.subheader("📈 **Defunciones por Año**")
st.markdown("""
Este gráfico muestra la cantidad de defunciones registradas en cada año desde 1880 hasta 2024. Es evidente que existen picos importantes que podrían estar relacionados con eventos sociales o sanitarios, como crisis económicas o pandemias.

En el gráfico, el eje **X** representa los años, y el eje **Y** muestra el número de defunciones para cada año.
""")
st.image("defunciones_año.png", use_column_width=True)

st.subheader("🎂 **Defunciones por Género**")
st.markdown("""
Este gráfico de barras compara la cantidad de defunciones entre hombres y mujeres en Argentina. Como se puede observar, los registros varían a lo largo de los años, lo que podría estar influenciado por diversos factores sociales y demográficos.

En el gráfico, el eje **X** representa los géneros, y el eje **Y** muestra la cantidad de defunciones por cada género.
""")
st.image("defunciones_genero.png", use_column_width=True)

st.subheader("🚻 **Defunciones por Género y Año**")
st.markdown("""
Este gráfico analiza las defunciones desglosadas por género a lo largo de los años. Permite observar las tendencias temporales y comparar la evolución de las defunciones entre hombres y mujeres.

En el gráfico, el eje **X** representa los años, el eje **Y** la cantidad de defunciones, y las barras están coloreadas según el género.
""")
st.image("defunciones_genero_tiempo.png", use_column_width=True)

# Conclusiones generales
st.subheader("✅ **Conclusiones**")
st.markdown("""
- **Tendencias a lo largo del tiempo**: Las defunciones en Argentina han experimentado fluctuaciones significativas a lo largo de la historia, con picos que podrían correlacionarse con crisis sociales o sanitarias.
- **Distribución por edad**: La mayoría de las defunciones se concentran en personas adultas, lo cual es consistente con las expectativas demográficas.
- **Diferencias de género**: Los gráficos muestran cómo las defunciones están distribuidas entre géneros a lo largo de los años, permitiendo identificar posibles desigualdades en las tasas de mortalidad entre hombres y mujeres.

Estos datos son fundamentales para comprender las dinámicas de salud pública en Argentina y para tomar decisiones informadas en políticas sociales.
""")
