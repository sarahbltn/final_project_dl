
# Análisis de Sentimiento

## Descripción del proyecto

Este proyecto consiste en un sistema de análisis de sentimientos aplicado a reseñas de productos, utilizando un modelo preentrenado basado en BERT

El objetivo no es únicamente clasificar reseñas como positivas o negativas, sino también identificar **qué aspectos específicos del producto influyen en la opinión del usuario**, como calidad, precio y envío, generando así un análisis más detallado y útil.

---

## Objetivos

- Clasificar el sentimiento general de reseñas de texto.
- Realizar fine-tuning de BERT para adaptación al problema.
- Implementar análisis por aspectos.
- Evaluar el modelo con métricas como accuracy, precision, recall y F1-score.

---

## Dataset

Se utilizó el dataset de Amazon Reviews, el cual contiene reseñas de productos con etiquetas de sentimiento.

Para el entrenamiento se utilizaron:
- 10000 muestras para entrenamiento  
- 2000 muestras para prueba  

Además, se generó un conjunto de validación a partir del conjunto de entrenamiento para monitorear el desempeño del modelo durante el fine-tuning.

---

## Metodología

### 1. Preprocesamiento
- Unión de título y contenido de la reseña en un solo texto.
- Tokenización utilizando el tokenizer de BERT.
- Padding y truncamiento a longitud fija.

### 2. Modelo
- Modelo base: BERT (`bert-base-uncased`)
- Fine tuning para clasificación binaria (positivo / negativo)

### 3. Entrenamiento
- Optimización con learning rate reducido.
- Regularización con weight decay.
- Early stopping para evitar sobreajuste.
- Selección del mejor modelo basado en F1-score.

### 4. Análisis por aspectos
- Detección de palabras clave asociadas a:
  - Calidad
  - Precio
  - Envío
- Clasificación del sentimiento a nivel de frase para cada aspecto.

---

## Evaluación

El modelo fue evaluado utilizando:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- Matriz de confusión  

---

## Resultados del sistema

El sistema permite obtener:

- Sentimiento general de la reseña  
- Sentimiento por aspecto identificado  
- Nivel de confianza de cada predicción  
- Resumen global de múltiples reseñas de un producto  

---

## Ejemplo de uso

```python
review = "The quality is amazing but shipping was very slow"

analizar_resena(review)