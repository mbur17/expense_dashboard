import streamlit as st

from services.data_service import delete_expenses_by_ids


def expenses_table(df):
    if df.empty:
        st.info('Пока нет расходов.')
        return
    ids = df['id'].copy()
    display_df = df[['date', 'category', 'amount', 'comment']].copy()
    display_df.insert(0, 'selected', False)
    edited = st.data_editor(
        display_df,
        width='stretch',
        hide_index=True,
        column_config={
            'selected': st.column_config.CheckboxColumn(
                'Выбрать', width='small'
            ),
            'date': st.column_config.DateColumn('Дата'),
            'category': st.column_config.TextColumn('Категория'),
            'amount': st.column_config.NumberColumn('Сумма', format='%.2f'),
            'comment': st.column_config.TextColumn('Комментарий'),
        },
        key='expenses_editor',
    )
    selected_mask = edited['selected'].fillna(False)
    selected_ids = ids.loc[selected_mask].tolist()
    if st.button('Удалить выбранные', disabled=not selected_ids):
        delete_expenses_by_ids(selected_ids)
        st.success(f'Удалено: {len(selected_ids)}')
        st.rerun()


def categories_table(by_category):
    st.dataframe(
        by_category,
        use_container_width=True,
        column_config={
            'category': st.column_config.TextColumn('Категория'),
            'amount': st.column_config.NumberColumn('Сумма', format='%.2f'),
        },
    )


def monthly_table(monthly):
    st.dataframe(
        monthly,
        use_container_width=True,
        column_config={
            'month': st.column_config.TextColumn('Месяц'),
            'amount': st.column_config.NumberColumn('Сумма', format='%.2f'),
        },
    )
