import streamlit as st
import pandas as pd
import plotly.express as px
from insights_ai import generate_insights

st.set_page_config(page_title="DeliverIQ • Intelligence", page_icon="📦", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/deliveries.csv", parse_dates=["data"])

df = load_data()

st.markdown("# 📦 DeliverIQ — Delivery Intelligence Dashboard")
st.caption("Análise de operações de delivery com insights automáticos (dados simulados).")

col1, col2, col3 = st.columns(3)
bairros = ["Todos"] + sorted(df["bairro"].unique().tolist())
entregadores = ["Todos"] + sorted(df["entregador"].unique().tolist())
dates = df["data"].dt.date
date_min, date_max = dates.min(), dates.max()

with col1:
    f_bairro = st.selectbox("Bairro", bairros, index=0)
with col2:
    f_entregador = st.selectbox("Entregador", entregadores, index=0)
with col3:
    f_date = st.date_input("Período", value=(date_min, date_max), min_value=date_min, max_value=date_max)

mask = (df["data"].dt.date >= f_date[0]) & (df["data"].dt.date <= f_date[1])
if f_bairro != "Todos":
    mask &= (df["bairro"] == f_bairro)
if f_entregador != "Todos":
    mask &= (df["entregador"] == f_entregador)

df_f = df.loc[mask].copy()

colA, colB, colC, colD = st.columns(4)
total = len(df_f)
tempo_medio = df_f["tempo_entrega_min"].mean() if total else 0
atraso_pct = 100 * df_f["atraso"].mean() if total else 0
nota_media = df_f["nota_cliente"].mean() if total else 0

colA.metric("Pedidos (período)", f"{total}")
colB.metric("Tempo médio (min)", f"{tempo_medio:.1f}")
colC.metric("Atrasos (%)", f"{atraso_pct:.1f}")
colD.metric("Nota média", f"{nota_media:.2f}")

st.divider()

if not df_f.empty:
    c1, c2 = st.columns(2)
    with c1:
        g1 = df_f.groupby("bairro")["tempo_entrega_min"].mean().reset_index().sort_values("tempo_entrega_min", ascending=False)
        fig1 = px.bar(g1, x="bairro", y="tempo_entrega_min", title="Tempo médio por bairro (min)")
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        g2 = df_f.groupby("bairro")["atraso"].mean().mul(100).reset_index().sort_values("atraso", ascending=False)
        fig2 = px.bar(g2, x="bairro", y="atraso", title="Atraso por bairro (%)")
        st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        g3 = df_f.groupby("entregador")["nota_cliente"].mean().reset_index().sort_values("nota_cliente")
        fig3 = px.bar(g3, x="entregador", y="nota_cliente", title="Nota média por entregador")
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        by_day = df_f.groupby("data").size().reset_index(name="pedidos")
        fig4 = px.line(by_day, x="data", y="pedidos", title="Pedidos por dia")
        st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.subheader("💡 Recomendações automáticas")
for ins in generate_insights(df_f):
    st.write(f"- {ins}")

st.caption("Projeto educacional. Dados simulados para demonstração.")
