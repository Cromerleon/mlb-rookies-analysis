# ⚾ MLB Rookies Stats 2020-2025

Interactive dashboard for analyzing MLB rookie statistics (2020-2025), built with Python, pandas, and Streamlit. Data sourced from [Baseball-Reference](https://www.baseball-reference.com/).

🔗 **[View Live Dashboard](https://mlb-rookies-analysis-jjkgcvcfxgqta6m94pfrj6.streamlit.app/)**

**[📖 Leer en Español](README_ES.md)**

---

## 📊 What does this project do?

<<<<<<< HEAD
- Calculates **accumulated WAR (Wins Above Replacement) by team** in three views: batters, pitchers, and combined
- Displays **Top 10 rookies** in different categories:
  - Batters: WAR, Home Runs, AVG, RBI, Hits, OPS
=======
**Nota Adicional**

Estos datos son recolectados de los jugadores colocados como novatos en sus respectivos años mediante la regla de eligibilidad de MLB(no por su año de Debut) la cual estipula lo siguiente:
1- Un pelotero pierde su estatus de novato si acumula 130 turnos al bate o 50 entradas lanzadas en las mayores
2- Si pasa más de 45 días en el roster activo durante temporadas anteriores.

Por ejemplo Josh Sborz debuto en MLB en 2019, sin embargo su año de novato fue designado por MLB en 2021.

- Calcula el **WAR (Wins Above Replacement) acumulado por equipo**, en tres vistas: bateadores, pitchers y combinado
- Muestra los **Top 10 novatos** en distintas categorías:
  - Bateadores: WAR, Home Runs, AVG, RBI, Hits, OPS
>>>>>>> 0cff47030078eed02d7a831487c5005f7ffc9b9e
  - Pitchers: WAR, Strikeouts, ERA, WHIP, Innings Pitched, Saves
- **Interactive charts** (Plotly): click on a team's bar to see a detailed list of that team's players with scrolling
- **Language selector** Spanish / English built into the dashboard

---

## 🛠️ Technologies Used

- **Python** — pandas for data cleaning and analysis
- **Streamlit** — interactive dashboard framework
- **Plotly** — interactive charts with click events
- **Jupyter Notebook** — initial data exploration and cleaning
- **Streamlit Community Cloud** — free deployment

---

## 📁 Project Structure

```
mlb-rookies-analysis/
├── data/
│   ├── bateadores_limpio.csv
│   └── pitchers_limpio.csv
├── notebooks/
│   └── exploracion.ipynb       # Initial data cleaning and exploration
├── app.py                      # Streamlit dashboard
├── requirements.txt
├── README.md
└── README_ES.md
```

---

## ⚠️ Known Data Limitations

This project uses data downloaded directly from Baseball-Reference, which has some important limitations to consider when interpreting results:

<<<<<<< HEAD
- **Players who played for multiple teams in the same season:** Baseball-Reference does not always break down statistics by individual team in the download format used for this project. In these cases, the player is associated with a single team (usually the last or the one with the most participation), even though part of their production (including WAR) may have occurred with another team during the same season. This can create minor distortions in the calculation of **accumulated WAR by team**, slightly favoring the team where the player's record was registered.
- **Qualification filters:** to prevent average statistics (AVG, OPS, ERA, WHIP) from being inflated by very small sample sizes, minimums were applied: at least 100 at-bats (AB ≥ 100) and at least 100 innings pitched (IP ≥ 100) before calculating the top rankings. This means that players with few appearances, even if they have impressive numbers, do not appear in those specific rankings.

These limitations do not affect accumulated total categories (Home Runs, Hits, RBI, Strikeouts, Saves, Innings Pitched), which are calculated on 100% of available data.

### Additional Note

This data is collected from players designated as rookies in their respective years according to **MLB's rookie eligibility rule** (not their debut year), which states the following:

1. A player loses rookie status if he accumulates 130 at-bats or 50 innings pitched in the majors.
2. If he spends more than 45 days on the active roster during previous seasons.

For example, Josh Sborz debuted in MLB in 2019, but his rookie year was designated by MLB as 2021.
=======
- **Jugadores que jugaron para más de un equipo en una misma temporada:** Baseball-Reference no siempre desglosa las estadísticas por equipo individual en el formato de descarga usado para este proyecto. En estos casos, el jugador aparece asociado a un solo equipo (generalmente el último o el de mayor participación), aunque parte de su producción (incluyendo WAR) haya ocurrido con otro equipo durante la misma temporada. Esto puede generar pequeñas distorsiones en el cálculo de **WAR acumulado por equipo**, favoreciendo ligeramente al equipo donde quedó registrado el jugador.

- **Filtros de calificación (qualifiers):** para evitar que estadísticas de promedio (AVG, OPS, ERA, WHIP) se vean infladas por muestras muy pequeñas, se aplicaron mínimos de turnos al bate (AB ≥ 100) e innings lanzados (IP ≥ 100) antes de calcular los tops. Esto significa que jugadores con pocas apariciones, aunque tengan números llamativos, no aparecen en esos rankings específicos.


Estas limitaciones no afectan las categorías de totales acumulados (Home Runs, Hits, RBI, Strikeouts, Saves, Innings Pitched), que se calculan sobre el 100% de los datos disponibles.
>>>>>>> 0cff47030078eed02d7a831487c5005f7ffc9b9e

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Cromerleon/mlb-rookies-analysis.git
cd mlb-rookies-analysis

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👤 Author

**Cromerleon**
GitHub: [@Cromerleon](https://github.com/Cromerleon)
