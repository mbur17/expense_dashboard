import streamlit as st

from services.analytics import get_category_stats, get_monthly_stats
from services.data_service import get_expenses_df
from services.categories import get_categories
from services.filters import filter_expenses
from ui.charts import category_donut
from ui.filters import render_filters
from ui.forms import add_expense_form
from ui.tables import expenses_table, categories_table, monthly_table
from ui.widgets import add_category_widget


st.set_page_config(
    page_title='Куда ушло?',
    page_icon='💸',
    layout='wide',
)

st.markdown(
    """
        # 💸 Куда ушло?

        **Следи за расходами, находи привычки, которые стоят слишком дорого,
        и смотри картину по категориям и месяцам.**
    """
)


df = get_expenses_df()

categories = get_categories()

add_category_widget()

add_expense_form(categories)

df = get_expenses_df()
categories = get_categories()

expense_filter = render_filters(df, categories)
filtered_df = filter_expenses(df, expense_filter)

st.subheader('Данные о расходах')
expenses_table(filtered_df)

st.subheader('Расходы по категориям')
by_category = get_category_stats(filtered_df)
if not by_category.empty:
    categories_table(by_category)
    category_donut(by_category)
else:
    st.info('Нет данных для агрегации по категориям (проверь фильтры).')

st.subheader('Расходы по месяцам')
monthly = get_monthly_stats(filtered_df)
if not monthly.empty:
    monthly_table(monthly)
    st.bar_chart(monthly.set_index('month')['amount'])
else:
    st.info('Нет данных для агрегации по месяцам (проверь фильтры).')
