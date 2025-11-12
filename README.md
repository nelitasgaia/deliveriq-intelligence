# 📦 DeliverIQ — Delivery Intelligence

**DeliverIQ** é um painel inteligente (Streamlit) que analisa dados de entregas simuladas e gera **insights automáticos** para otimização operacional (tempo de entrega, atrasos, satisfação por região e por entregador).  
O objetivo é demonstrar **análise de dados aplicada**, **IA prática (simulada)** e **comunicação clara de métricas de negócio**.

## ✨ Principais recursos
- KPIs: **tempo médio**, **% de atraso**, **nota média**, **pedidos/dia**
- Gráficos interativos por **bairro** e **entregador** (Plotly)
- **Filtros dinâmicos** (datas, bairro, entregador)
- **Recomendações inteligentes** (módulo `insights_ai.py`, sem depender de API externa)
- Dados **simulados** com comportamento realista para estudo e portfólio

## 🧱 Estrutura
```
deliveriq-intelligence/
├── data/
│   └── deliveries.csv
├── app.py
├── insights_ai.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar localmente
1. Crie e ative um ambiente virtual (opcional)
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode o dashboard:
   ```bash
   streamlit run app.py
   ```
4. O app abrirá no navegador (geralmente em `http://localhost:8501`).

## 🧠 Sobre o módulo de "IA"
Para simplificar o uso, os **insights são gerados por heurísticas** (regras simples) em `insights_ai.py`.  
Caso deseje integrar uma IA real (OpenAI/Gemini), basta adaptar a função `generate_insights` para chamar a API e enriquecer as recomendações.

## 📌 Observações
- Este é um projeto educacional com **dados simulados**.
- Pode ser publicado no GitHub e evoluído com novas fontes de dados, alertas, e integrações (ex.: n8n para automações).

---

**Autor(a):** Nélita Gaia — Projeto de portfólio para análise de dados aplicada a operações de delivery.
