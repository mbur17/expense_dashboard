from datetime import date
from typing import List

import streamlit as st

from services.data_service import add_expense


def add_expense_form(categories: List[str]) -> None:
    """Форма добавления расхода."""

    st.subheader('Добавить новый расход')

    with st.form('add_expense_form', clear_on_submit=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            exp_date: date = st.date_input('Дата', value=date.today())
        with col2:
            if categories:
                category = st.selectbox('Категория', options=categories)
            else:
                st.info('Пока нет ни одной категории. Сначала добавь её.')
                category = ''
        with col3:
            amount = st.number_input(
                'Сумма',
                min_value=0.0,
                step=100.0,
                format='%.2f',
            )
        with col4:
            comment = st.text_input('Комментарий', value='')
        submitted = st.form_submit_button('Добавить расход')
        if submitted:
            try:
                add_expense(exp_date, category, amount, comment)
            except ValueError as e:
                st.error(str(e))
            else:
                st.success('Расход добавлен!')
