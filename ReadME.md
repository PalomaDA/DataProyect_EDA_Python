# Análisis Exploratorio de Datos (EDA): Factores de Suscripción Bancaria

## Descripción del Proyecto

Este proyecto realiza un **análisis exploratorio de datos (EDA)** completo para identificar los factores clave que influyen en la decisión de los clientes de suscribirse a un producto bancario (depósito a plazo). 

El análisis utiliza datos de campañas de marketing bancario, combinando información demográfica, económica y de interacción con el cliente para descubrir patrones y generar insights accionables.

### Objetivos

- Identificar los principales factores que influyen en la suscripción de clientes
- Analizar el impacto de variables demográficas, económicas y de campaña
- Generar recomendaciones estratégicas basadas en datos
- Crear visualizaciones que comuniquen hallazgos clave

---

## Estructura del Proyecto

```
DataProyect_EDA_Python/
│
├── files/
│   ├── input/                          # Datos originales
│   │   ├── bank-additional.csv         # Datos de campaña y cliente
│   │   └── customer-details.xlsx       # Datos de ingresos y actividad web
│   │
│   └── output/                         # Datos procesados
│       ├── df_bank_ap.csv              # Bank data después de análisis inicial
│       ├── df_bank_clean.csv           # Bank data limpio
│       ├── df_customer_ap.csv          # Customer data después de análisis inicial
│       └── df_customer_clean.csv       # Customer data limpio
│
├── scr/                                # Funciones auxiliares reutilizables
│   ├── explore_utils.py                # Utilidades para exploración de datos
│   └── formatting_utils.py             # Utilidades para formateo de datos
│
├── 01-analisis_inicial.ipynb           # Notebook 1: Carga y análisis inicial
├── 02-limpieza.ipynb                   # Notebook 2: Limpieza y transformación
├── 03-EDA.ipynb                        # Notebook 3: Análisis exploratorio
├── INFORME_FINAL.md                    # Informe ejecutivo con hallazgos
├── presentación-resultados.pdf         # Presentación de resultados
├── requirements.txt                    # Dependencias del proyecto
└── ReadME.md                           # Este archivo
```

---

## Flujo de Trabajo

El proyecto sigue un flujo de trabajo estructurado en **3 etapas**, cada una documentada en un notebook independiente:

###  **Análisis Inicial** (`01-analisis_inicial.ipynb`)

**Objetivo**: Cargar los datos, realizar un primer análisis y entender su estructura.

**Procesos**:
- Carga de archivos CSV y Excel desde `files/input/`
- Análisis exploratorio básico (dimensiones, tipos de datos, valores únicos)
- Identificación de valores nulos y duplicados
- Formateo de nombres de columnas usando `column_names_formatting()`
- Análisis de nulos con `null_analysis()`
- Exportación de datos procesados a `files/output/`

**Salidas**:
- `df_bank_ap.csv`
- `df_customer_ap.csv`

---

### **Limpieza de Datos** (`02-limpieza.ipynb`)

**Objetivo**: Limpiar y transformar los datos para el análisis.

**Procesos**:
- **Gestión de valores nulos**:
  - Imputación de `EURIBOR3M` usando KNNImputer (correlación con indicadores económicos)
  - Imputación de `AGE` por mediana dentro de grupos sociodemográficos
- **Transformación de variables**:
  - Conversión de `PDAYS` (999 = no contactado) en dos variables:
    - `WAS_CONTACTED`: variable categórica (yes/no)
    - `DAYS_SINCE_CONTACT`: variable numérica limpia
- **Normalización**:
  - Agrupación de niveles educativos básicos en categoría "basic"
- **Creación de variables derivadas**:
  - `AGE_CAT`: categorización por grupos de edad
  - Variables temporales (`YEAR`, `MONTH`, `DAY_OF_WEEK`)
- Exportación de datos limpios a `files/output/`

**Salidas**:
- `df_bank_clean.csv`
- `df_customer_clean.csv`

---

### **Análisis Exploratorio (EDA)** (`03-EDA.ipynb`)

**Objetivo**: Realizar el análisis exploratorio completo y generar insights.

**Procesos**:
- **Análisis univariado**: Distribuciones de variables individuales
- **Análisis bivariado**: Relación de cada variable con la suscripción
- **Análisis de correlaciones**: Identificación de relaciones entre variables
- **Segmentación**: Análisis por cohortes (año de alta, edad, ocupación)
- **Análisis temporal**: Tendencias por año, mes y día de la semana
- **Análisis macroeconómico**: Impacto de indicadores económicos
- **Visualizaciones**: Gráficos de barras, boxplots, heatmaps, etc.

**Hallazgos Clave**:
- **Relación previa**: Factor más determinante (65% conversión vs 9.2%)
- **Cohorte 2014**: Tasa de conversión del 23% (5x superior a otras)
- **Canal móvil**: 3x más efectivo que teléfono fijo (14% vs 5%)
- **Contexto económico**: Mayor suscripción con Euribor bajo

---

## Funciones Auxiliares

El proyecto incluye funciones reutilizables en el directorio `scr/` para mantener el código limpio y modular:

### `scr/explore_utils.py`

#### `null_analysis(df)`
Genera un resumen completo de valores nulos en el dataframe.

**Parámetros**:
- `df` (DataFrame): Dataframe a analizar

**Retorna**:
- DataFrame con columnas:
  - `COLUMN_NAME`: Nombre de la columna
  - `NON_NULL_COUNT`: Cantidad de valores no nulos
  - `NULL_COUNT`: Cantidad de valores nulos
  - `NULL_PERCENT`: Porcentaje de valores nulos
  - `DTYPE`: Tipo de dato

**Uso**:
```python
from scr.explore_utils import null_analysis
null_summary = null_analysis(df)
```

---

#### `column_type_dataframe(df, col_type)`
Filtra el dataframe para mostrar solo las columnas de un tipo específico.

**Parámetros**:
- `df` (DataFrame): Dataframe original
- `col_type` (str): Tipo de dato deseado ('object', 'float64', 'int64', etc.)

**Retorna**:
- Tupla con:
  - DataFrame filtrado con solo las columnas del tipo especificado
  - Lista de nombres de columnas de ese tipo

**Uso**:
```python
from scr.explore_utils import column_type_dataframe
df_numeric, numeric_cols = column_type_dataframe(df, 'float64')
```

---

### `scr/formatting_utils.py`

#### `column_names_formatting(df)`
Formatea los nombres de columnas del dataframe a un estándar consistente.

**Formato aplicado**:
- Convierte a mayúsculas
- Elimina guiones bajos (_)
- Elimina puntos (.)
- Elimina espacios al inicio y final

**Parámetros**:
- `df` (DataFrame): Dataframe a formatear

**Retorna**:
- DataFrame con nombres de columnas formateados

**Uso**:
```python
from scr.formatting_utils import column_names_formatting
df = column_names_formatting(df)
```

---

##  Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

1. **Clonar el repositorio** (si aplica):
```bash
git clone <url-repositorio>
cd DataProyect_EDA_Python
```

2. **Instalar las dependencias**:
```bash
pip install -r requirements.txt
```

O instalar individualmente:
```bash
pip install pandas openpyxl numpy matplotlib seaborn scikit-learn ipykernel pytest coverage
```

### Dependencias del Proyecto

- **pandas**: Manipulación y análisis de datos
- **openpyxl**: Lectura de archivos Excel
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **seaborn**: Visualizaciones estadísticas avanzadas
- **scikit-learn**: Imputación de valores nulos (KNNImputer)
- **ipykernel**: Ejecución de notebooks Jupyter
- **pytest**: Framework de testing
- **coverage**: Medición de cobertura de tests

---

## Uso del Proyecto

### Ejecutar el Análisis Completo

1. **Ejecutar los notebooks en orden**:
   - `01-analisis_inicial.ipynb`
   - `02-limpieza.ipynb`
   - `03-EDA.ipynb`

2. **Revisar el informe final**:
   - Abrir `INFORME_FINAL.md` para ver los hallazgos y recomendaciones

### Ejecutar Solo una Parte

Puedes ejecutar cualquier notebook de forma independiente, siempre que los archivos de entrada necesarios estén disponibles en `files/output/`.

---

## Resultados Principales

Los hallazgos detallados se encuentran en [`INFORME_FINAL.md`](INFORME_FINAL.md), pero aquí un resumen ejecutivo:

| Factor | Impacto | Tasa de Conversión |
|--------|---------|-------------------|
|  Éxito en campaña previa | **MUY ALTO** | 65% |
|  Cohorte 2014 | **ALTO** | 23% |
|  Canal móvil | **MEDIO-ALTO** | 14% |
|  Duración > 5 min | **ALTO** | Correlación positiva fuerte |
|  Euribor bajo | **MEDIO** | Correlación negativa |

### Recomendaciones Estratégicas

1. **Priorizar retargeting** de clientes con historial positivo
2. **Analizar y replicar** la estrategia de captación de 2014
3. **Concentrar recursos** en el canal móvil
4. **Optimizar timing** de campañas según contexto macroeconómico


## Notas Adicionales

- Los datos procesados se guardan automáticamente en `files/output/`
- Las funciones auxiliares están documentadas con docstrings
- El código sigue las mejores prácticas de Python (PEP 8)
- Los notebooks incluyen markdown explicativo para facilitar la comprensión

---

**¡Gracias por revisar este proyecto!**

Para más detalles sobre los hallazgos, consulta [`INFORME_FINAL.md`](INFORME_FINAL.md) o la [presentación de resultados](presentación-resultados.pdf).
