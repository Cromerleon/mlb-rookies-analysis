import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="MLB Rookies Stats 2020-2025", page_icon="⚾", layout="wide")

# ==========================================
# DICCIONARIO DE TRADUCCIONES
# ==========================================
TRANSLATIONS = {
    "es": {
        "main_title": "⚾ Estadisticas de Novatos en MLB 2020-2025 ⚾",
        "main_description": "Análisis de estadísticas de novatos en la MLB desde 2020 hasta 2025 extraído de Baseball-Reference.",
        "tab_war": "📊 WAR por Equipo",
        "tab_batters": "💥 Top Bateadores",
        "tab_pitchers": "⚾ Top Pitchers",

        "war_header": "📊 WAR por Equipo",
        "war_description": "Visualización del WAR (Wins Above Replacement) acumulado por equipo para novatos en la MLB desde 2020 hasta 2025.",
        "view_selector": "Selecciona la vista:",
        "view_combined": "Combinado",
        "view_batters": "Bateadores",
        "view_pitchers": "Pitchers",

        "chart_combined_title": "WAR Acumulado por Equipo (Bateadores vs Pitchers)",
        "chart_batters_title": "WAR Acumulado por Equipo (Bateadores)",
        "chart_pitchers_title": "WAR Acumulado por Equipo (Pitchers)",
        "xaxis_team": "Equipo",
        "yaxis_war": "WAR Acumulado",

        "batters_of_team": "Bateadores de {team}",
        "pitchers_of_team": "Pitchers de {team}",
        "click_hint_combined": "👆 Haz clic en una barra para ver el detalle de bateadores o pitchers de ese equipo",
        "click_hint_batters": "👆 Haz clic en una barra para ver el detalle de bateadores de ese equipo",
        "click_hint_pitchers": "👆 Haz clic en una barra para ver el detalle de pitchers de ese equipo",

        "col_name": "Nombre",
        "col_war": "WAR",

        "batters_header": "💥 Top 10 Bateadores",
        "batters_description": "Visualización de los 10 mejores bateadores novatos en la MLB desde 2020 hasta 2025 en diferentes categorías.",
        "top_war_batters": "Top 10 Bateadores por WAR",
        "top_hr": "Top 10 Bateadores por Home Runs",
        "top_avg": "Top 10 Bateadores por AVG",
        "top_rbi": "Top 10 Bateadores por RBI",
        "top_hits": "Top 10 Bateadores por Hits",
        "top_ops": "Top 10 Bateadores por OPS",

        "pitchers_header": "⚾ Top 10 Pitchers",
        "pitchers_description": "Visualización de los 10 mejores pitchers novatos en la MLB desde 2020 hasta 2025 en diferentes categorías.",
        "top_war_pitchers": "Top 10 Pitchers por WAR",
        "top_so": "Top 10 Pitchers por Strikeouts",
        "top_era": "Top 10 Pitchers por ERA",
        "top_whip": "Top 10 Pitchers por WHIP",
        "top_ip": "Top 10 Pitchers por IP",
        "top_sv": "Top 10 Pitchers por Saves",

        "col_hr": "HR",
        "col_avg": "AVG",
        "col_rbi": "RBI",
        "col_hits": "Hits",
        "col_ops": "OPS",
        "col_so": "SO",
        "col_era": "ERA",
        "col_whip": "WHIP",
        "col_ip": "IP",
        "col_sv": "SV",

        "language_label": "🌐 Idioma / Language",
    },
    "en": {
        "main_title": "⚾ MLB Rookies Stats 2020-2025 ⚾",
        "main_description": "Analysis of MLB rookie statistics from 2020 to 2025, sourced from Baseball-Reference.",
        "tab_war": "📊 WAR by Team",
        "tab_batters": "💥 Top Batters",
        "tab_pitchers": "⚾ Top Pitchers",

        "war_header": "📊 WAR by Team",
        "war_description": "Visualization of accumulated WAR (Wins Above Replacement) by team for MLB rookies from 2020 to 2025.",
        "view_selector": "Select view:",
        "view_combined": "Combined",
        "view_batters": "Batters",
        "view_pitchers": "Pitchers",

        "chart_combined_title": "Accumulated WAR by Team (Batters vs Pitchers)",
        "chart_batters_title": "Accumulated WAR by Team (Batters)",
        "chart_pitchers_title": "Accumulated WAR by Team (Pitchers)",
        "xaxis_team": "Team",
        "yaxis_war": "Accumulated WAR",

        "batters_of_team": "Batters of {team}",
        "pitchers_of_team": "Pitchers of {team}",
        "click_hint_combined": "👆 Click on a bar to see the batter or pitcher detail for that team",
        "click_hint_batters": "👆 Click on a bar to see the batter detail for that team",
        "click_hint_pitchers": "👆 Click on a bar to see the pitcher detail for that team",

        "col_name": "Name",
        "col_war": "WAR",

        "batters_header": "💥 Top 10 Batters",
        "batters_description": "Visualization of the top 10 MLB rookie batters from 2020 to 2025 across different categories.",
        "top_war_batters": "Top 10 Batters by WAR",
        "top_hr": "Top 10 Batters by Home Runs",
        "top_avg": "Top 10 Batters by AVG",
        "top_rbi": "Top 10 Batters by RBI",
        "top_hits": "Top 10 Batters by Hits",
        "top_ops": "Top 10 Batters by OPS",

        "pitchers_header": "⚾ Top 10 Pitchers",
        "pitchers_description": "Visualization of the top 10 MLB rookie pitchers from 2020 to 2025 across different categories.",
        "top_war_pitchers": "Top 10 Pitchers by WAR",
        "top_so": "Top 10 Pitchers by Strikeouts",
        "top_era": "Top 10 Pitchers by ERA",
        "top_whip": "Top 10 Pitchers by WHIP",
        "top_ip": "Top 10 Pitchers by IP",
        "top_sv": "Top 10 Pitchers by Saves",

        "col_hr": "HR",
        "col_avg": "AVG",
        "col_rbi": "RBI",
        "col_hits": "Hits",
        "col_ops": "OPS",
        "col_so": "SO",
        "col_era": "ERA",
        "col_whip": "WHIP",
        "col_ip": "IP",
        "col_sv": "SV",

        "language_label": "🌐 Language / Idioma",
    },
}

# ==========================================
# SELECTOR DE IDIOMA (botones tipo toggle EN/ES)
# ==========================================
if "lang" not in st.session_state:
    st.session_state.lang = "es"

col_espacio, col_es, col_en = st.columns([10, 1, 1])
with col_es:
    if st.button("ES", type="primary" if st.session_state.lang == "es" else "secondary", use_container_width=True):
        st.session_state.lang = "es"
        st.rerun()
with col_en:
    if st.button("EN", type="primary" if st.session_state.lang == "en" else "secondary", use_container_width=True):
        st.session_state.lang = "en"
        st.rerun()

lang = st.session_state.lang
t = TRANSLATIONS[lang]

# ==========================================
# TÍTULO Y DESCRIPCIÓN
# ==========================================
st.title(t["main_title"])
st.write(t["main_description"])

df_batters = pd.read_csv("data/bateadores_limpio.csv")
df_pitchers = pd.read_csv("data/pitchers_limpio.csv")

tab1, tab2, tab3 = st.tabs([t["tab_war"], t["tab_batters"], t["tab_pitchers"]])

# ==========================================
# TAB 1: WAR POR EQUIPO
# ==========================================
with tab1:
    st.header(t["war_header"])
    st.write(t["war_description"])

    war_batters_team = df_batters.groupby("Tm")["WAR"].sum().sort_values(ascending=False)
    war_pitchers_team = df_pitchers.groupby("Tm")["WAR"].sum().sort_values(ascending=False)

    view = st.radio(
        t["view_selector"],
        (t["view_combined"], t["view_batters"], t["view_pitchers"]),
        horizontal=True,
    )

    if view == t["view_combined"]:
        comparative = pd.DataFrame({'Bateadores': war_batters_team, 'Pitchers': war_pitchers_team}).fillna(0)
        totals = comparative.sum(axis=1)
        comparative = comparative.loc[totals.sort_values(ascending=False).index]
        totals = comparative.sum(axis=1)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=comparative.index,
            y=comparative['Bateadores'],
            name=t["view_batters"],
            marker_color='tomato',
            text=comparative["Bateadores"].round(1),
            textposition='inside'
        ))
        fig.add_trace(go.Bar(
            x=comparative.index,
            y=comparative['Pitchers'],
            name=t["view_pitchers"],
            marker_color='lightblue',
            text=comparative["Pitchers"].round(1),
            textposition='inside'
        ))

        fig.update_layout(
            barmode='stack',
            title=t["chart_combined_title"],
            xaxis_title=t["xaxis_team"],
            yaxis_title=t["yaxis_war"],
            height=600,
            xaxis=dict(fixedrange=True),
            yaxis=dict(fixedrange=True)
        )

        for equipo, total in totals.items():
            fig.add_annotation(
                x=equipo,
                y=total,
                text=f'{total:.1f}',
                showarrow=False,
                yshift=10,
                font=dict(size=11, color='white')
            )

        evento = st.plotly_chart(
            fig, use_container_width=True, on_select="rerun", key="grafico_war",
            config={'displayModeBar': False, 'scrollZoom': False}
        )

        if evento and evento['selection']['points']:
            punto = evento['selection']['points'][0]
            equipo_seleccionado = punto['x']
            tipo_seleccionado = punto['curve_number']  # 0 = Bateadores, 1 = Pitchers

            if tipo_seleccionado == 0:
                st.subheader(t["batters_of_team"].format(team=equipo_seleccionado))
                bateadores_equipo = df_batters[df_batters['Tm'] == equipo_seleccionado][['Name', 'WAR']].sort_values('WAR', ascending=False)
                bateadores_equipo = bateadores_equipo.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
                st.dataframe(bateadores_equipo, hide_index=True, height=300)
            else:
                st.subheader(t["pitchers_of_team"].format(team=equipo_seleccionado))
                pitchers_equipo = df_pitchers[df_pitchers['Tm'] == equipo_seleccionado][['Name', 'WAR']].sort_values('WAR', ascending=False)
                pitchers_equipo = pitchers_equipo.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
                st.dataframe(pitchers_equipo, hide_index=True, height=300)
        else:
            st.info(t["click_hint_combined"])

    elif view == t["view_batters"]:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=war_batters_team.index,
            y=war_batters_team.values,
            marker_color='tomato',
            text=war_batters_team.round(1),
            textposition='outside'
        ))

        fig.update_layout(
            title=t["chart_batters_title"],
            xaxis_title=t["xaxis_team"],
            yaxis_title=t["yaxis_war"],
            height=600,
            xaxis=dict(fixedrange=True),
            yaxis=dict(fixedrange=True)
        )

        evento = st.plotly_chart(
            fig, use_container_width=True, on_select="rerun", key="grafico_bateadores",
            config={'displayModeBar': False, 'scrollZoom': False}
        )

        if evento and evento['selection']['points']:
            equipo_seleccionado = evento['selection']['points'][0]['x']
            st.subheader(t["batters_of_team"].format(team=equipo_seleccionado))
            bateadores_equipo = df_batters[df_batters['Tm'] == equipo_seleccionado][['Name', 'WAR']].sort_values('WAR', ascending=False)
            bateadores_equipo = bateadores_equipo.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
            st.dataframe(bateadores_equipo, hide_index=True, height=300)
        else:
            st.info(t["click_hint_batters"])

    else:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=war_pitchers_team.index,
            y=war_pitchers_team.values,
            marker_color='lightblue',
            text=war_pitchers_team.round(1),
            textposition='outside'
        ))

        fig.update_layout(
            title=t["chart_pitchers_title"],
            xaxis_title=t["xaxis_team"],
            yaxis_title=t["yaxis_war"],
            height=600,
            xaxis=dict(fixedrange=True),
            yaxis=dict(fixedrange=True)
        )

        evento = st.plotly_chart(
            fig, use_container_width=True, on_select="rerun", key="grafico_pitchers",
            config={'displayModeBar': False, 'scrollZoom': False}
        )

        if evento and evento['selection']['points']:
            equipo_seleccionado = evento['selection']['points'][0]['x']
            st.subheader(t["pitchers_of_team"].format(team=equipo_seleccionado))
            pitchers_equipo = df_pitchers[df_pitchers['Tm'] == equipo_seleccionado][['Name', 'WAR']].sort_values('WAR', ascending=False)
            pitchers_equipo = pitchers_equipo.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
            st.dataframe(pitchers_equipo, hide_index=True, height=300)
        else:
            st.info(t["click_hint_pitchers"])

# ==========================================
# TAB 2: TOP BATEADORES
# ==========================================
with tab2:
    st.header(t["batters_header"])
    st.write(t["batters_description"])

    qualifed_batters = df_batters[df_batters["AB"] >= 100]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(t["top_war_batters"])
        df_show = qualifed_batters.sort_values(by="WAR", ascending=False).head(10)[["Name", "WAR"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_hr"])
        df_show = qualifed_batters.sort_values(by="HR", ascending=False).head(10)[["Name", "HR"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "HR": t["col_hr"]})
        st.dataframe(df_show, hide_index=True)

    with col2:
        st.subheader(t["top_avg"])
        df_show = qualifed_batters.sort_values(by="BA", ascending=False).head(10)[["Name", "BA"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "BA": t["col_avg"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_rbi"])
        df_show = qualifed_batters.sort_values(by="RBI", ascending=False).head(10)[["Name", "RBI"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "RBI": t["col_rbi"]})
        st.dataframe(df_show, hide_index=True)

    with col3:
        st.subheader(t["top_hits"])
        df_show = qualifed_batters.sort_values(by="H", ascending=False).head(10)[["Name", "H"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "H": t["col_hits"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_ops"])
        df_show = qualifed_batters.sort_values(by="OPS", ascending=False).head(10)[["Name", "OPS"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "OPS": t["col_ops"]})
        st.dataframe(df_show, hide_index=True)

# ==========================================
# TAB 3: TOP PITCHERS
# ==========================================
with tab3:
    st.header(t["pitchers_header"])
    st.write(t["pitchers_description"])

    qualifed_pitchers = df_pitchers[df_pitchers["IP"] >= 100]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(t["top_war_pitchers"])
        df_show = qualifed_pitchers.sort_values(by="WAR", ascending=False).head(10)[["Name", "WAR"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "WAR": t["col_war"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_so"])
        df_show = qualifed_pitchers.sort_values(by="SO", ascending=False).head(10)[["Name", "SO"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "SO": t["col_so"]})
        st.dataframe(df_show, hide_index=True)

    with col2:
        st.subheader(t["top_era"])
        df_show = qualifed_pitchers.sort_values(by="ERA", ascending=True).head(10)[["Name", "ERA"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "ERA": t["col_era"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_whip"])
        df_show = qualifed_pitchers.sort_values(by="WHIP", ascending=True).head(10)[["Name", "WHIP"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "WHIP": t["col_whip"]})
        st.dataframe(df_show, hide_index=True)

    with col3:
        st.subheader(t["top_ip"])
        df_show = qualifed_pitchers.sort_values(by="IP", ascending=False).head(10)[["Name", "IP"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "IP": t["col_ip"]})
        st.dataframe(df_show, hide_index=True)

        st.subheader(t["top_sv"])
        df_show = df_pitchers.sort_values(by="SV", ascending=False).head(10)[["Name", "SV"]]
        df_show = df_show.rename(columns={"Name": t["col_name"], "SV": t["col_sv"]})
        st.dataframe(df_show, hide_index=True)
