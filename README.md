# ⚾ MLB Rookies Stats 2020-2025

Dashboard interactivo de análisis de estadísticas de novatos de la MLB (2020-2025), construido con Python, pandas y Streamlit. Los datos fueron extraídos de [Baseball-Reference](https://www.baseball-reference.com/).

🔗 **[Ver Dashboard en vivo](https://mlb-rookies-analysis-jjkgcvcfxgqta6m94pfrj6.streamlit.app/)**

---

## 📊 ¿Qué hace este proyecto?

- Calcula el **WAR (Wins Above Replacement) acumulado por equipo**, en tres vistas: bateadores, pitchers y combinado
- Muestra los **Top 10 novatos** en distintas categorías:
  - Bateadores: WAR, Home Runs, AVG, RBI, Hits, OPS
  - Pitchers: WAR, Strikeouts, ERA, WHIP, Innings Pitched, Saves
- Gráficas **interactivas** (Plotly): al hacer clic en la barra de un equipo, se despliega el listado de jugadores de ese equipo con scroll
- **Selector de idioma** Español / English integrado en el dashboard

---

## 🛠️ Tecnologías utilizadas

- **Python** — pandas para limpieza y análisis de datos
- **Streamlit** — construcción del dashboard interactivo
- **Plotly** — gráficas interactivas con eventos de clic
- **Jupyter Notebook** — exploración y limpieza inicial de datos
- **Streamlit Community Cloud** — despliegue gratuito

---

## 📁 Estructura del proyecto

```
mlb-rookies-analysis/
├── data/
│   ├── bateadores_limpio.csv
│   └── pitchers_limpio.csv
├── notebooks/
│   └── exploracion.ipynb       # Limpieza y exploración inicial de datos
├── app.py                      # Dashboard de Streamlit
├── requirements.txt
└── README.md
```

---

## ⚠️ Limitaciones conocidas de los datos

Este proyecto usa datos descargados directamente de Baseball-Reference, que tienen algunas limitaciones importantes a tener en cuenta al interpretar los resultados:

- **Jugadores que jugaron para más de un equipo en una misma temporada:** Baseball-Reference no siempre desglosa las estadísticas por equipo individual en el formato de descarga usado para este proyecto. En estos casos, el jugador aparece asociado a un solo equipo (generalmente el último o el de mayor participación), aunque parte de su producción (incluyendo WAR) haya ocurrido con otro equipo durante la misma temporada. Esto puede generar pequeñas distorsiones en el cálculo de **WAR acumulado por equipo**, favoreciendo ligeramente al equipo donde quedó registrado el jugador.
- **Filtros de calificación (qualifiers):** para evitar que estadísticas de promedio (AVG, OPS, ERA, WHIP) se vean infladas por muestras muy pequeñas, se aplicaron mínimos de turnos al bate (AB ≥ 100) e innings lanzados (IP ≥ 100) antes de calcular los tops. Esto significa que jugadores con pocas apariciones, aunque tengan números llamativos, no aparecen en esos rankings específicos.

Estas limitaciones no afectan las categorías de totales acumulados (Home Runs, Hits, RBI, Strikeouts, Saves, Innings Pitched), que se calculan sobre el 100% de los datos disponibles.

---

## 🚀 Cómo correrlo localmente

```bash
# Clonar el repositorio
git clone https://github.com/Cromerleon/mlb-rookies-analysis.git
cd mlb-rookies-analysis

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Correr la app
streamlit run app.py
```

---

## 👤 Autor

**Cromerleon**
GitHub: [@Cromerleon](https://github.com/Cromerleon)
