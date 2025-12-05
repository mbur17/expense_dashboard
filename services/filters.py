from dataclasses import dataclass
from datetime import date
from typing import List

import pandas as pd


@dataclass
class ExpenseFilter:
    date_from: date
    date_to: date
    categories: List[str]
    min_amount: float = 0.0


def filter_expenses(df: pd.DataFrame, f: ExpenseFilter) -> pd.DataFrame:
    if df.empty:
        return df
    mask = (
        df['date'].dt.date >= f.date_from
    ) & (
        df['date'].dt.date <= f.date_to
    )
    if f.categories:
        mask &= df['category'].isin(f.categories)
    if f.min_amount > 0:
        mask &= df['amount'] >= f.min_amount
    return df[mask]
