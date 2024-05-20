## Análisis de Precios de Vehículos Usados en EE.UU.

Este proyecto tiene como objetivo realizar un análisis exhaustivo de un conjunto de datos de vehículos usados en EE.UU., identificando y visualizando factores que influyen en los precios de venta. Utilizando diversas herramientas y bibliotecas de Python, el proyecto aborda la limpieza de datos, la imputación de valores ausentes, la creación de nuevas características y la visualización interactiva de los resultados. A continuación, se detalla el flujo de trabajo y los pasos principales realizados en este proyecto.

# Objetivos del Proyecto:
1. Limpieza y Preparación de Datos:

Carga de Datos: Lectura del conjunto de datos de vehículos desde un archivo CSV.
Imputación de Valores Ausentes: Relleno de valores ausentes en columnas críticas (is_4wd, paint_color, model_year, cylinders, odometer) utilizando técnicas como el reemplazo con valores definidos, medianas o promedios calculados a partir de grupos.

2. Creación de Nuevas Características:

Cálculo de Edad del Vehículo al Momento de la Publicación: Determinación de la antigüedad de los vehículos al momento de su publicación en función del año del modelo y la fecha de publicación.
Extracción de la Marca del Vehículo: Obtención de la marca del vehículo a partir de la columna model.

3. Análisis y Visualización:

Histogramas Interactivos: Visualización de la relación entre el precio promedio y el kilometraje (odometer), diferenciados por marcas.
Gráficos de Dispersión: Análisis de la influencia de la condición del vehículo y el año del modelo en el precio, con una representación visual que también incorpora el kilometraje.

# Bibliotecas Utilizadas:

pandas: Manipulación y análisis de datos.
plotly.express: Visualización interactiva.
streamlit: Creación de aplicaciones web interactivas para el análisis de datos.

### Utilidad del Proyecto:

Este proyecto es útil para varios fines:

1. Compradores y Vendedores de Vehículos Usados:
Proporciona una herramienta visual interactiva para comprender cómo diferentes factores (como el kilometraje, el año del modelo y la condición del vehículo) afectan el precio de los vehículos usados.
Ayuda a los compradores a tomar decisiones informadas sobre qué vehículos ofrecen una mejor relación calidad-precio.
Asiste a los vendedores a fijar precios competitivos basados en análisis de mercado.

2. Investigadores y Analistas de Mercado:
Ofrece un conjunto de datos limpio y procesado listo para realizar análisis más profundos y desarrollar modelos predictivos.

3. Desarrolladores de Software y Científicos de Datos:
Proporciona un ejemplo práctico de cómo aplicar técnicas de limpieza de datos, creación de características y visualización interactiva utilizando Python y sus bibliotecas.
Sirve como base para desarrollar aplicaciones más complejas y personalizadas para análisis de datos en otras áreas.
