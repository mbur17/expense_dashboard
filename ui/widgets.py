import streamlit as st

from services.categories import add_category


def add_category_widget() -> None:
    with st.sidebar.expander('Добавить категорию'):
        name = st.text_input('Новая категория', key='new_category_name')
        if st.button('Добавить категорию', key='add_category_button'):
            try:
                add_category(name)
            except ValueError as e:
                st.error(str(e))
            else:
                st.success('Категория добавлена!')
