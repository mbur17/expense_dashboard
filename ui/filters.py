from datetime import date
from typing import List

import streamlit as st

from services.filters import ExpenseFilter


def render_filters(df, all_categories: List[str]) -> ExpenseFilter:
    st.sidebar.header('Фильтры')
    if df.empty:
        today = date.today()
        return ExpenseFilter(
            date_from=today,
            date_to=today,
            categories=all_categories,
            min_amount=0.0,
        )
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date_from, date_to = st.sidebar.date_input(
        'Период',
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    if not all_categories:
        all_categories = sorted(df['category'].dropna().unique().tolist())
    selected_categories = st.sidebar.multiselect(
        'Категории',
        options=all_categories,
        default=all_categories,
    )
    min_amount = st.sidebar.number_input(
        'Минимальная сумма расхода',
        min_value=0.0,
        value=0.0,
        step=100.0,
    )
    return ExpenseFilter(
        date_from=date_from,
        date_to=date_to,
        categories=selected_categories,
        min_amount=min_amount,
    )
