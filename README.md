# Marketing Niche Discovery & Budget Optimization

## Estructura 

```
marketing-niche-discovery/
│
├── data/
│   ├── marketing_campaign_dataset.csv
│   └── marketing_simulated_niche.csv
│
├── notebooks/
│   ├── 01_data_audit.ipynb         # EDA inicial 
│   └── 02_niche_discovery.ipynb    # EDA final
│
├── scripts/
│   └── data_simulator.py          # El script que inyecta las reglas de negocio
│
└── README.md
```

## El Problema de Negocio
La empresa está experimentando una fuga de capital (alto Costo por Adquisición - CPA) debido a la asignación tradicional del presupuesto de marketing. Se asume erróneamente que los canales con mayor volumen de gasto generan la mayor rentabilidad, ignorando la fatiga de anuncios y la saturación del segmento.

## Objetivo del Proyecto
Identificar "Nichos Ocultos" (cruces específicos de Canal + Segmento de Cliente) que actualmente reciben baja inversión pero presentan un CPA mínimo y una alta tasa de conversión. El objetivo final es proponer una reasignación de presupuesto que incremente el Revenue estimado sin aumentar el gasto global.

## El Pivote: Auditoría de Datos y Simulación Realista
Durante la fase inicial de Análisis Exploratorio (EDA) documentada en 01_data_audit.ipynb, se detectó que el dataset original presentaba una distribución plana y carecía de correlaciones lógicas entre las métricas de marketing (por ejemplo, el CTR no impactaba la tasa de conversión y los costos eran estáticos sin importar el canal).

Realizar un análisis sobre datos sin reglas lógicas de negocio habría resultado en insights ficticios o tautológicos. Para solucionar esto y mantener la integridad del ejercicio analítico:

* Se desarrolló el script data_simulator.py para inyectar reglas de mercado realistas basadas en el Escenario de Descubrimiento de Nicho.

* Se programó fatiga de anuncios (aumento de CPA) para canales saturados y alta conversión para nichos específicos.

* El análisis final y la propuesta de reasignación de presupuesto (02_niche_discovery.ipynb) y el Dashboard en Power BI se basan en este entorno simulado, demostrando cómo identificar y explotar ineficiencias en la inversión publicitaria.

## Stack Tecnológico
Python (Pandas, Numpy): Limpieza, simulación de reglas de negocio y Análisis Exploratorio de Datos (EDA).

Power BI: Modelado de datos, DAX y visualización interactiva para toma de decisiones.

## Hallazgos Clave y Recomendaciones
(En construcción - Se llenará tras finalizar el análisis en Power BI)
