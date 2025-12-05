import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def expenses_df():
    data = [
        {
            'date': '2025-10-01',
            'category': 'Еда',
            'amount': 100,
            'comment': ''
        },
        {
            'date': '2025-10-02',
            'category': 'Еда',
            'amount': 200,
            'comment': ''
        },
        {
            'date': '2025-10-03',
            'category': 'Транспорт',
            'amount': 50,
            'comment': ''
        },
        {
            'date': '2025-11-01',
            'category': 'Еда',
            'amount': 300,
            'comment': ''
        },
        {
            'date': '2025-11-02',
            'category': 'Подписки',
            'amount': 499, 'comment': ''
        },
    ]
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    return df


@pytest.fixture
def empty_df():
    df = pd.DataFrame(columns=['date', 'category', 'amount', 'comment'])
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    return df
