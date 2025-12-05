from datetime import date
from typing import Optional, Iterable
from uuid import uuid4

import pandas as pd
import streamlit as st

from .demo_data import load_demo_expenses

SESSION_KEY = 'expenses'


def _ensure_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Гарантирует наличие нужных колонок и id."""

    for col in ['date', 'category', 'amount', 'comment']:
        if col not in df.columns:
            df[col] = None
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    if 'id' not in df.columns:
        df = df.copy()
        df['id'] = [str(uuid4()) for _ in range(len(df))]
    cols = ['id', 'date', 'category', 'amount', 'comment']
    df = df[cols]
    return df


def get_expenses_df() -> pd.DataFrame:
    if SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = _ensure_schema(load_demo_expenses())
    else:
        st.session_state[SESSION_KEY] = _ensure_schema(
            st.session_state[SESSION_KEY]
        )
    return st.session_state[SESSION_KEY]


def set_expenses_df(df: pd.DataFrame) -> None:
    st.session_state[SESSION_KEY] = _ensure_schema(df)


def add_expense(
    exp_date: date,
    category: str,
    amount: float,
    comment: Optional[str] = '',
) -> None:
    if not category:
        raise ValueError('Категория не может быть пустой')
    if amount <= 0:
        raise ValueError('Сумма должна быть больше 0')
    df = get_expenses_df()
    new_row = pd.DataFrame(
        [{
            'id': str(uuid4()),
            'date': pd.to_datetime(exp_date),
            'category': category,
            'amount': float(amount),
            'comment': comment or '',
        }]
    )
    updated = pd.concat([df, new_row], ignore_index=True)
    set_expenses_df(updated)


def delete_expenses_by_ids(ids: Iterable[str]) -> None:
    ids = set(ids)
    if not ids:
        return
    df = get_expenses_df()
    updated = df[~df['id'].isin(ids)].copy()
    set_expenses_df(updated)
