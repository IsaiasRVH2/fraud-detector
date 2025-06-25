# FraudDetector: Sistema Inteligente para Detección de Fraudes en Transacciones
 ## Objetivo
 Desarrollar un sistema de detección de fraudes en transacciones financieras usando Machine Learning, integrando buenas prácticas de MLOps para facilitar su entrenamiento, mantenimiento y despliegue continuo.

 ## Tareas
 1. Procesar y analizar datos transaccionales con características numéricas y categóricas.
 2. Entrenar modelos robustos que manejen clases desbalanceadas.
 3. Evaluar y comparar modelos con métricas apropiadas (AUC-ROC, F1-Score).
 4. Integrar interpretabilidad del modelo SHAP o LIME.
 5. Desplegar el modelo como API REST.
 6. Aplicar principios de MLOps (versionado, pruebas, despliegue continuo, monitoreo).

## Arquitectura del Proyecto
```graphql
fraud-detector/
│
├── data/                  # Datos crudos y procesados
├── notebooks/             # Exploración inicial y experimentos
├── src/
│   ├── data/              # Carga y preprocesamiento
│   ├── features/          # Feature engineering
│   ├── models/            # Entrenamiento, evaluación
│   ├── serving/           # API REST con FastAPI
│   └── pipelines/         # Orquestación ML (ej. MLflow, DVC)
│
├── tests/                 # Unit tests y pruebas de integración
├── .dvc/                  # Configuración de versionado de datos
├── mlruns/                # Experimentos de MLflow
├── Dockerfile             # Imagen reproducible
├── requirements.txt
├── README.md
└── config.yaml            # Configuración centralizada
```

## Tecnologías
| Área | Herraminetas / Frameworks |
|-------|--------------------------|
|Análisis/Modelado |pandas, scikit-learn, XGBoost, imalanced-learn|
|Interpretabilidad|SHAP, LIME|
|Experimentación|MLflow|
|Visionado|Git, DVC|
|Despliegue|FastAPI, Docker|
|CI/CD| GitHub Actions|
|Visualización| Streamlit o Gradio|

## Temas que cubre
- Aprendizaje supervisado (clasificación)
- Manejo de clases desbalanceadas
- Interpretabilidad de modelos
- Validación cruzada estratificada
- MLOps
- Despliegue de modelos

## Fases del proyecto
1. Definición y recolección de datos
   - Uso del dataset público de tarjetas de credito de Kaggle ([Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)).
2. EDA + Preprocesamiento
   - Análisis de clases, distribución de variables.
   - Normalización, codificación, eliminación de outliers si aplica.
3. Modelado
   - Entrenamiento con modelos base: Logistic Regression, Random Forest, etc.
   - Mejoras con XGBoost/LightGBM.
   - Técnicas de balanceo: SMOTE, RandomUnderSampler.
4. Evaluación
   - AUC, F1, precision/recall, confusion matrix.
   - Validación cruzada estratificada.
5. Interpretabilidad
   - SHAP para análisis por muestra y global.
   - LIME para explicaciones locales.
6. Pipeline reproducible
   - Automatizar flujo con MLflow + DVC.
   - Guardar artefactos, modelos, métricas.
7. Despliegue
   - API REST en FastAPI.
   - Dockerización del proyecto.
8. MLOps y mantenimiento
   - Versionado (Git + DVC).
   - Logging de predicciones.
   - Plan de monitoreo.
