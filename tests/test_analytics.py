import pandas as pd

from services.analytics import get_category_stats, get_monthly_stats


def test_get_category_stats_sums_and_sorting(expenses_df):
    result = get_category_stats(expenses_df)
    amounts = dict(zip(result['category'], result['amount']))

    assert amounts['Еда'] == 100 + 200 + 300
    assert amounts['Транспорт'] == 50
    assert amounts['Подписки'] == 499
    assert result.iloc[0]['category'] == 'Еда'
    assert result.iloc[0]['amount'] == 600


def test_get_category_stats_empty(empty_df):
    result = get_category_stats(empty_df)

    assert result.empty


def test_get_monthly_stats_groups_by_month(expenses_df):
    result = get_monthly_stats(expenses_df)
    month_keys = pd.to_datetime(result['month']).dt.to_period('M').astype(str)
    month_amounts = dict(zip(month_keys, result['amount']))

    assert month_amounts['2025-10'] == 100 + 200 + 50
    assert month_amounts['2025-11'] == 300 + 499
    assert len(result) == 2
    assert list(result['month']) == sorted(result['month'])


def test_get_monthly_stats_empty(empty_df):
    result = get_monthly_stats(empty_df)

    assert result.empty
