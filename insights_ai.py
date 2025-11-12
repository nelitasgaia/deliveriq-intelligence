from typing import List
import pandas as pd

def generate_insights(df: pd.DataFrame) -> List[str]:
    insights = []
    if df.empty:
        return ["Nenhum dado no filtro atual. Ajuste os filtros para ver insights."]

    tempo_medio = df["tempo_entrega_min"].mean()
    atraso_pct = 100 * df["atraso"].mean()
    nota_media = df["nota_cliente"].mean()

    insights.append(
        f"Tempo médio de entrega: {tempo_medio:.1f} min | Atrasos: {atraso_pct:.1f}% | Nota média: {nota_media:.2f}."
    )

    atraso_por_bairro = df.groupby("bairro")["atraso"].mean().sort_values(ascending=False)
    top_bairro = atraso_por_bairro.index[0]
    top_bairro_atraso = 100 * atraso_por_bairro.iloc[0]
    if top_bairro_atraso > 20:
        insights.append(
            f"O bairro {top_bairro} concentra {top_bairro_atraso:.1f}% de atrasos. "
            f"Avalie alocar +1 entregador no pico local ou ajustar janelas de preparo."
        )

    notas_por_entregador = df.groupby("entregador")["nota_cliente"].mean().sort_values()
    low_ent = notas_por_entregador.index[0]
    low_ent_nota = notas_por_entregador.iloc[0]
    if low_ent_nota < 4.0:
        insights.append(
            f"O entregador {low_ent} apresenta menor nota média ({low_ent_nota:.1f}). "
            f"Recomenda-se feedback rápido e revisão de rotas/treinamento."
        )

    if tempo_medio > 38:
        insights.append(
            "Tempo médio acima do ideal. Simulação: reduzir preparo em 3 min pode diminuir o tempo total em ~8–12%."
        )
    elif tempo_medio < 30:
        insights.append(
            "Tempo médio eficiente. Priorize manter o padrão em horários de pico e replicar boas práticas em áreas críticas."
        )

    corr = df[["atraso", "nota_cliente"]].corr().iloc[0,1]
    if corr < -0.2:
        insights.append(
            "Atraso tem correlação negativa com a satisfação. Atue primeiro nos bairros com maior atraso para ganhos rápidos de NPS."
        )

    return insights
