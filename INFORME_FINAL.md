# INFORME FINAL DE RESULTADOS: ANÁLISIS DE FACTORES DE SUSCRIPCIÓN

## 1. RESUMEN EJECUTIVO Y RECOMENDACIONES CLAVE

El análisis exploratorio revela que **la relación histórica con el cliente y el contexto macroeconómico son los factores más potentes para predecir la suscripción**. Los esfuerzos futuros de marketing deben centrarse en la activación de cohortes de alto valor y en el cultivo de las relaciones existentes, en lugar de depender únicamente de la estacionalidad o las campañas a clientes sin contacto previo.

| Impulsor Clave | Hallazgo Principal | Recomendación Estratégica |
|----------------|-------------------|---------------------------|
| **Relación Previa** | Los clientes con éxito previo en campañas se suscriben un **65%** de las veces. | Priorizar sistemáticamente el retargeting y la fidelización de clientes con historial positivo. |
| **Segmentación** | La cohorte de clientes dados de alta en **2014** es 3 a 5 veces más propensa a suscribirse (tasa de conversión del **23%**). | Analizar el perfil de los clientes de 2014 y replicar la estrategia de captación utilizada en ese periodo. |
| **Factores Operacionales** | El canal móvil es casi tres veces más efectivo que el fijo (**14% vs 5%**). | Concentrar los recursos de contacto en el canal móvil. Usar la duración de la llamada (más de 5 minutos) como indicador de interés inmediato. |
| **Contexto Económico** | La suscripción se correlaciona negativamente con el Euribor y positivamente con la incertidumbre laboral. | Posicionar el producto como un "refugio seguro" o activo defensivo durante periodos de tipos de interés bajos y variaciones de empleo negativas. |

---

## 2. METODOLOGÍA Y PROCESO DE DATOS

El análisis se realizó sobre un conjunto de datos unificado de **42,752 registros**, obtenidos de la fusión de `bank-additional` (información de campaña y cliente) y `customer-details` (ingresos y actividad web).

Se ejecutó un riguroso proceso de limpieza de datos, incluyendo:

### Gestión de Nulos

- **`EURIBOR3M`** (21.53% de nulos): Se imputó utilizando el método `KNNImputer` debido a su fuerte correlación (cercana a 0.95-0.97) con indicadores económicos como `EMPVARRATE` y `NREMPLOYED`.
- **`AGE`** (11.91% de nulos): Se imputó mediante la mediana dentro de subgrupos sociodemográficos para preservar la coherencia del perfil.

### Ingeniería de Variables

- Se transformó la variable `PDAYS` (donde 999 era un nulo estructural) en dos variables: 
  - `WAS_CONTACTED` (categórica: si hubo contacto previo)
  - `DAYS_SINCE_CONTACT` (numérica limpia)

### Normalización

- Se agruparon los subniveles de educación obligatoria en la categoría "basic".

---

## 3. HALLAZGOS DETALLADOS POR CATEGORÍA

### A. Impacto de la Relación Previa (Predictor Principal)

**La calidad de la interacción y el historial del cliente son el factor más determinante para la suscripción**, multiplicando la probabilidad de éxito por un factor de hasta seis.

| Categoría | Tasa de Suscripción (Aprox.) |
|-----------|------------------------------|
| Éxito Previo (`POUTCOME = SUCCESS`) | **65%** |
| Contactado Previamente (`WAS_CONTACTED = yes`) | **64.1%** |
| Sin Contacto Previo (`WAS_CONTACTED = no`) | **9.2%** |

![alt text](/files/output/images/image-1.png)
![alt text](/files/output/images/image.png)

> Se observa una barra de conversión de **64.1%** para el segmento 'yes' de `WAS_CONTACTED`, contrastando fuertemente con la barra de **9.2%** para el segmento 'no', indicando que la existencia de una relación previa y continuada es la máxima prioridad.

---

### B. Segmentación y Factores Demográficos

El análisis demográfico muestra una **mayor receptividad en los extremos del ciclo vital** y un **impacto significativo del año de alta como cliente** en el banco.

#### 1. Antigüedad del Cliente (`DTCUSTOMER`)

- Los clientes captados en **2014** presentan una tasa de conversión del **23%**, significativamente superior a la cohorte de 2013 (7.7%) y 2012 (4.6%).
- Este hallazgo convierte el año de alta en una **dimensión clave de segmentación**.

![alt text](/files/output/images/image-2.png)

#### 2. Edad y Ocupación (`AGE_CAT`, `JOB`)

- **Jubilados** (65+ años) y **Estudiantes** (15-24 años) tienen las tasas de conversión más elevadas, oscilando entre el **25%** y el **46%**.
- Los clientes en edad laboral intermedia (30-50 años) muestran tasas de suscripción significativamente menores (8-10%).
- El nivel universitario de educación también se asocia con un buen desempeño, ofreciendo una base muestral sólida para futuras segmentaciones.

![alt text](/files/output/images/image-3.png)

---

### C. Factores Operacionales y Duración

**El cómo se realiza el contacto y su duración son cruciales para el éxito.**

#### 1. Duración de la Interacción (`DURATION`)

- Esta es **la variable más predictiva**. La duración media de la llamada para los suscriptores es de **553 segundos** (más de 9 minutos), comparado con solo **220 segundos** (menos de 4 minutos) para los no suscriptores.
- **Nota**: Se debe usar con cautela en modelos predictivos, ya que se conoce solo después de la interacción.

![alt text](/files/output/images/image-5.png)

#### 2. Canal de Contacto (`CONTACT`)

- El contacto a través de **teléfono móvil** (`cellular`) registra una tasa de éxito del **14%**, lo que representa casi el **triple** de la tasa obtenida por teléfono fijo (alrededor del **5%**).

![alt text](/files/output/images/image-4.png)

---

### D. Indicadores Macroeconómicos (Producto "Refugio")

Existe una **clara correlación inversa entre los principales indicadores económicos y la suscripción**.

#### Tipos de Interés (`EURIBOR3M`)

- Los suscriptores contratan el producto cuando el Euribor medio es de **2.11**, frente al **3.81** de los no suscriptores.

#### Empleo (`EMPVARRATE` y `NREMPLOYED`)

- La suscripción es mayor en contextos de tasas de variación de empleo negativas (`EMPVARRATE` medio de **-1.24**).

Esto sugiere que **el producto se vuelve más atractivo como refugio seguro** para los clientes en momentos de incertidumbre económica o cuando los tipos de interés de referencia son más bajos.

---

### E. Estabilidad Temporal

**El momento específico de la campaña (año, mes o día de la semana) tiene un impacto marginal en la tasa de suscripción.**

- La tasa de conversión se mantiene estable, en un rango estrecho (**10.9%** a **11.7%**), entre 2015 y 2016.
- **No se identificó un "mes estrella"**. Octubre tiene la tasa ligeramente más alta (12.4%) y septiembre la más baja (10.3%), pero la diferencia es marginal (menos de 2 puntos porcentuales).
- El día de la semana (con el jueves ligeramente superior) tampoco condiciona el resultado de la campaña.

---

## 4. CONCLUSIONES Y PRÓXIMOS PASOS

### Conclusiones Principales

1. **La relación previa es el factor más determinante**: Los clientes con éxito previo en campañas tienen una tasa de conversión del 65%, comparado con solo el 9.2% de aquellos sin contacto previo.

2. **El contexto económico importa**: El producto actúa como "refugio seguro" durante períodos de incertidumbre económica (tipos de interés bajos, variación de empleo negativa).

3. **La segmentación por cohorte es crítica**: Los clientes dados de alta en 2014 son significativamente más propensos a suscribirse (23% vs 4-7% de otras cohortes).

4. **La calidad sobre la cantidad**: La duración de la llamada (promedio 553 segundos para conversiones exitosas) y el canal móvil (14% de éxito) son indicadores clave de calidad en el contacto.

### Recomendaciones Estratégicas

> **Acción Inmediata Requerida**
>
> Evitar campañas masivas de "contacto frío" que tienen una tasa de conversión inferior al 10%. Concentrar recursos en:
> 1. **Retargeting de clientes con historial positivo** (65% de conversión)
> 2. **Análisis profundo de la cohorte 2014** para replicar estrategias exitosas
> 3. **Priorización del canal móvil** para contactos
> 4. **Timing de campañas durante contextos macroeconómicos favorables**


