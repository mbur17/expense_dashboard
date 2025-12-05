from datetime import date

from services.filters import ExpenseFilter, filter_expenses


def test_filter_by_date_range(expenses_df):
    f = ExpenseFilter(
        date_from=date(2025, 10, 2),
        date_to=date(2025, 10, 3),
        categories=['Еда', 'Транспорт', 'Подписки'],
        min_amount=0.0,
    )
    result = filter_expenses(expenses_df, f)

    assert len(result) == 2
    assert set(result['amount'].tolist()) == {200, 50}


def test_filter_by_categories(expenses_df):
    f = ExpenseFilter(
        date_from=date(2025, 10, 1),
        date_to=date(2025, 11, 30),
        categories=['Подписки'],
        min_amount=0.0,
    )
    result = filter_expenses(expenses_df, f)

    assert len(result) == 1
    assert result.iloc[0]['category'] == 'Подписки'


def test_filter_by_min_amount(expenses_df):
    f = ExpenseFilter(
        date_from=date(2025, 10, 1),
        date_to=date(2025, 11, 30),
        categories=['Еда', 'Транспорт', 'Подписки'],
        min_amount=250.0,
    )
    result = filter_expenses(expenses_df, f)

    assert set(result['amount'].tolist()) == {300, 499}


def test_filter_empty_df(empty_df):
    f = ExpenseFilter(
        date_from=date(2025, 1, 1),
        date_to=date(2025, 12, 31),
        categories=['Еда'],
        min_amount=0.0,
    )
    result = filter_expenses(empty_df, f)

    assert result.empty
