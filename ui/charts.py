import plotly.express as px
import streamlit as st


def category_donut(by_category):
    if by_category.empty:
        st.info('Нет данных для диаграммы по категориям.')
        return
    fig = px.pie(
        by_category,
        names='category',
        values='amount',
        hole=0.45,
    )
    fig.update_traces(
        textposition='inside',
        textinfo='percent',
    )
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        legend_title_text='Категории',
        height=360,
    )
    st.plotly_chart(fig, use_container_width=True)
