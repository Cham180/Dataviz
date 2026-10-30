import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Social Media Impact",
    page_icon="📊",
    layout="wide"
)

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("Social_media_impact_on_life(1).csv")
    return df

df = load_data()

st.title("Impact des réseaux sociaux sur la vie des étudiants")
st.markdown(
    "Analyse exploratoire des habitudes numériques, du sommeil, "
    "de la santé mentale et des performances académiques."
)

st.caption(
    "Objectif : étudier les associations entre les habitudes "
    "d'utilisation des réseaux sociaux et différentes dimensions de la vie étudiante."
)

# Barre latérale : filtres
st.sidebar.header("Filtres")

ages = sorted(df["Age"].dropna().unique())
selected_ages = st.sidebar.multiselect(
    "Âge",
    ages,
    default=ages
)

genders = sorted(df["Gender"].dropna().unique())
selected_genders = st.sidebar.multiselect(
    "Genre",
    genders,
    default=genders
)

levels = sorted(df["Academic_Level"].dropna().unique())
selected_levels = st.sidebar.multiselect(
    "Niveau d'études",
    levels,
    default=levels
)

platforms = sorted(df["Primary_Platform"].dropna().unique())
selected_platforms = st.sidebar.multiselect(
    "Plateforme principale",
    platforms,
    default=platforms
)

min_hours = float(df["Daily_Usage_Hours"].min())
max_hours = float(df["Daily_Usage_Hours"].max())

usage_range = st.sidebar.slider(
    "Utilisation quotidienne (heures)",
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours)
)

# Application des filtres
filtered = df[
    df["Age"].isin(selected_ages)
    & df["Gender"].isin(selected_genders)
    & df["Academic_Level"].isin(selected_levels)
    & df["Primary_Platform"].isin(selected_platforms)
    & df["Daily_Usage_Hours"].between(
        usage_range[0], usage_range[1]
    )
].copy()

if filtered.empty:
    st.warning("Aucune observation ne correspond aux filtres sélectionnés.")
    st.stop()

# Indicateurs clés
st.subheader("Vue d'ensemble")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Étudiants", f"{len(filtered):,}".replace(",", " "))
c2.metric(
    "Utilisation quotidienne moyenne",
    f"{filtered['Daily_Usage_Hours'].mean():.2f} h"
)
c3.metric(
    "Sommeil moyen",
    f"{filtered['Sleep_Duration_Hours'].mean():.2f} h"
)
c4.metric(
    "GPA moyen",
    f"{filtered['Academic_Performance_GPA'].mean():.2f}"
)

st.caption(
    "Les indicateurs sont calculés sur les observations filtrées. "
    "Les moyennes ignorent les valeurs manquantes de chaque variable."
)

# Onglets
tab1, tab2, tab3, tab4 = st.tabs([
    "Données",
    "Utilisation",
    "Sommeil et performances",
    "Corrélations et synthèse"
])

with tab1:
    st.subheader("Présentation du jeu de données")

    a, b, c = st.columns(3)
    a.metric("Nombre de lignes initial", len(df))
    b.metric("Nombre de variables", df.shape[1])
    c.metric(
        "Cellules manquantes",
        int(df.isna().sum().sum())
    )

    st.markdown("**Aperçu des données filtrées**")
    st.dataframe(filtered.head(100), use_container_width=True)

    missing = pd.DataFrame({
        "Variable": df.columns,
        "Valeurs manquantes": df.isna().sum().values,
        "Pourcentage (%)": (
            df.isna().mean().values * 100
        ).round(2)
    }).sort_values("Valeurs manquantes", ascending=False)

    st.markdown("**Valeurs manquantes dans la base complète**")
    st.dataframe(missing, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Habitudes d'utilisation")

    left, right = st.columns(2)

    with left:
        fig = px.histogram(
            filtered,
            x="Daily_Usage_Hours",
            nbins=20,
            title="Distribution du temps quotidien d'utilisation",
            labels={
                "Daily_Usage_Hours": "Heures par jour",
                "count": "Nombre d'étudiants"
            }
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        platform_counts = (
            filtered["Primary_Platform"]
            .value_counts()
            .rename_axis("Plateforme")
            .reset_index(name="Nombre")
        )
        fig = px.bar(
            platform_counts,
            x="Plateforme",
            y="Nombre",
            title="Plateformes principales",
            labels={"Plateforme": "Plateforme"}
        )
        st.plotly_chart(fig, use_container_width=True)

    impact_counts = (
        filtered["Overall_Impact"]
        .value_counts()
        .rename_axis("Impact déclaré")
        .reset_index(name="Nombre")
    )
    fig = px.bar(
        impact_counts,
        x="Impact déclaré",
        y="Nombre",
        title="Répartition de l'impact global déclaré"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Sommeil, santé mentale et performances")

    left, right = st.columns(2)

    with left:
        scatter_data = filtered.dropna(
            subset=["Daily_Usage_Hours", "Academic_Performance_GPA"]
        )
        fig = px.scatter(
            scatter_data,
            x="Daily_Usage_Hours",
            y="Academic_Performance_GPA",
            trendline="ols",
            title="Temps d'utilisation et GPA",
            labels={
                "Daily_Usage_Hours": "Heures d'utilisation par jour",
                "Academic_Performance_GPA": "GPA"
            },
            hover_data=["Age", "Primary_Platform"]
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            f"Observations disponibles pour ce graphique : {len(scatter_data)}."
        )

    with right:
        sleep_data = filtered.dropna(
            subset=["Late_Night_Usage", "Sleep_Duration_Hours"]
        ).copy()
        sleep_data["Late_Night_Usage"] = (
            sleep_data["Late_Night_Usage"].map(
                {True: "Oui", False: "Non"}
            ).fillna(sleep_data["Late_Night_Usage"].astype(str))
        )
        fig = px.box(
            sleep_data,
            x="Late_Night_Usage",
            y="Sleep_Duration_Hours",
            title="Durée de sommeil et utilisation tardive",
            labels={
                "Late_Night_Usage": "Utilisation tardive",
                "Sleep_Duration_Hours": "Heures de sommeil"
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            f"Observations disponibles pour ce graphique : {len(sleep_data)}."
        )

    stress_data = filtered.dropna(
        subset=["Daily_Usage_Hours", "Perceived_Stress_Score"]
    ).copy()

    if not stress_data.empty:
        stress_data["Catégorie d'utilisation"] = pd.cut(
            stress_data["Daily_Usage_Hours"],
            bins=[-float("inf"), 2, 5, float("inf")],
            labels=["Moins de 2 h", "De 2 à 5 h", "Plus de 5 h"],
            right=False
        )

        stress_summary = (
            stress_data.groupby(
                "Catégorie d'utilisation",
                observed=False
            )["Perceived_Stress_Score"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            stress_summary,
            x="Catégorie d'utilisation",
            y="Perceived_Stress_Score",
            title="Stress moyen selon la durée d'utilisation",
            labels={
                "Catégorie d'utilisation": "Durée quotidienne",
                "Perceived_Stress_Score": "Score moyen de stress"
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            "Les catégories sont définies pour cette analyse. "
            "Le graphique présente des moyennes descriptives."
        )

    mental_data = filtered.dropna(
        subset=["Daily_Usage_Hours", "Mental_Health_Index"]
    )
    fig = px.scatter(
        mental_data,
        x="Daily_Usage_Hours",
        y="Mental_Health_Index",
        title="Temps d'utilisation et indice de santé mentale",
        labels={
            "Daily_Usage_Hours": "Heures d'utilisation par jour",
            "Mental_Health_Index": "Indice de santé mentale"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Matrice de corrélation")

    numeric_cols = [
        "Daily_Usage_Hours",
        "Weekend_Extra_Hours",
        "Sleep_Duration_Hours",
        "Sleep_Quality_Score",
        "Perceived_Stress_Score",
        "Mental_Health_Index",
        "Academic_Performance_GPA"
    ]

    corr = filtered[numeric_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Corrélations entre variables quantitatives"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Corrélations avec le temps quotidien d'utilisation**")
    usage_corr = (
        corr["Daily_Usage_Hours"]
        .drop("Daily_Usage_Hours")
        .dropna()
        .sort_values()
    )
    st.dataframe(
        usage_corr.rename("Corrélation").to_frame(),
        use_container_width=True
    )

    st.info(
        "Une corrélation mesure une association linéaire entre deux variables. "
        "Elle ne démontre pas une relation de cause à effet."
    )

with st.expander("Consulter les statistiques descriptives"):
    st.dataframe(
        filtered.describe(include="all").transpose(),
        use_container_width=True
    )
