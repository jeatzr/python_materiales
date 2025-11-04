# 📘 **Práctica 2.1: Limpieza y exploración de datos de Airbnb con Pandas**

## 🎯 Objetivos

- Aprender a cargar, explorar y limpiar un dataset real.
- Corregir valores nulos, duplicados y errores de formato.
- Preparar los datos para su uso posterior en una API.

---

### 1. Preparación del entorno

Asegúrate de tener **pandas** instalado y carga las librerías necesarias:

```python
import pandas as pd
import numpy as np
```

El cuaderno Jupyter lo realizaremos en **Google Colab** o en el local en el entorno **Jupyter Lab** (este último habría que instalarlo por ejemplo con la distrubución **[Anaconda](https://www.anaconda.com/download)**). Se recomienda usar Colab para no tener que instalar nada.

Usa el fichero propocionado por el profesor `airbnb.csv`. Si usas Colab Has de subirlo a tu Google Drive y conectar Drive desde Colab. Si

---

## 2. Cargar y explorar el dataset

Usa los métodos usados en clase para explorar el dataset.
Tipos de datos. Número de filas y columnas, primeras y últimos registros...

💡 _Objetivo:_ entender qué datos hay y en qué formato vienen (texto, número, fecha...).

---

## 3. Cambiar los nombres de las columnas a notación `snake_case`si fuese necesario

## 4. Detectar y tratar valores nulos

```python
# Número de valores nulos por columna
df.isna().sum()

# Ejemplo: rellenar valores nulos de 'reviews_per_month' con 0
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
```

💬 También puedes eliminar filas si tienen demasiados nulos:

```python
df = df.dropna(subset=["name", "host_name"])
```

---

## 4 Eliminar duplicados

Podemos eliminar valores duplicados

```python
df = df.drop_duplicates()
```

💡 _Pista:_ prueba a comparar el tamaño antes y después con `df.shape`.

---

## 5. Limpiar textos y normalizar valores

Normaliza columnas como `neighbourhood`, `room_type` o `city`:

```python
df["neighbourhood"] = df["neighbourhood"].str.strip().str.lower()
df["room_type"] = df["room_type"].str.strip().str.lower()
```

---

## 6. Limpiar precios

A veces el precio viene con símbolos o comas. Convierte la columna `price` a número:

```python
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
```

## 7. Comprobar si existen categorías repetidas pero escritas de modo distinto, no normalizadas en columnas `neighbourhood`, `room_type` o `city`. Corrige los errores

## Finalmente exportar el fichero en formato HTML.

Esta característica esta por defecto en Jupyter Lab en local pero en colab no viene, si bien podemos usar este cuaderno utilitario para realizar la conversión.

[Utilidad Colab para descargar cuaderno Jupyter en HTML](https://colab.research.google.com/github/Mostafa-MR/Convert_ipynb_to_HTML_in_Colab/blob/main/Convert_ipynb_to_HTML_in_Colab.ipynb#scrollTo=4FhcP565-JpA)
