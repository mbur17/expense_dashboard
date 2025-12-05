import pandas as pd


def get_category_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Агрегация расходов по категориям."""

    if df.empty:
        return df.head(0)
    by_category = (
        df.groupby('category')['amount']
        .sum()
        .reset_index()
        .sort_values('amount', ascending=False)
    )
    return by_category


def get_monthly_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Агрегация расходов по месяцам."""

    if df.empty:
        return df.head(0)
    monthly = (
        df
        .assign(month=df['date'].dt.to_period('M').dt.to_timestamp())
        .groupby('month')['amount']
        .sum()
        .reset_index()
        .sort_values('month')
    )
    monthly['month'] = monthly['month'].astype(str)
    return monthly
