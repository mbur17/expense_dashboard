from typing import List

import streamlit as st

from .data_service import get_expenses_df

SESSION_KEY = 'categories'


def _init_categories_if_needed() -> None:
    """Инициализируем список категорий, если он ещё не создан."""

    if SESSION_KEY not in st.session_state:
        df = get_expenses_df()
        if df.empty:
            st.session_state[SESSION_KEY] = []
        else:
            cats = (
                df['category']
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )
            st.session_state[SESSION_KEY] = sorted(cats)


def get_categories() -> List[str]:
    _init_categories_if_needed()
    return st.session_state[SESSION_KEY]


def add_category(name: str) -> None:
    _init_categories_if_needed()
    name = (name or '').strip()
    if not name:
        raise ValueError('Название категории не может быть пустым.')
    cats: List[str] = st.session_state[SESSION_KEY]
    if name in cats:
        raise ValueError('Такая категория уже существует.')
    cats.append(name)
    cats.sort()
    st.session_state[SESSION_KEY] = cats
