import  pandas as pd
from datetime import  datetime
import altair as alt
import streamlit as st
#from who_is_who_copy import dual_who_is_who_dict

def test_chart_2(df,selected_group='Навальный',selected_year=2020):

    years_or_months = '%B'  # это значит месяц - подается в настройки чарта, если выбран один год
    num_of_ticks = 6  # количество тиков на Х
    if selected_year == 2020:
#        df = df[df['date'] > datetime(2020, 1, 1)]
        df = df[(df['date'] > datetime(2020, 1, 1)) & (df['date'] < datetime(2020, 12, 31))]

    elif selected_year == 2019:
        df = df[(df['date'] > datetime(2019, 1, 1)) & (df['date'] < datetime(2020, 1, 1))]

    elif selected_year == 2021:
        df = df[(df['date'] > datetime(2021, 1, 1))]


    else:
        years_or_months = '%Y'  # значит год, подается в настройки чарта
        num_of_ticks = 4  # кол-во тиков
        df = df[df['date'] > datetime(2017, 1, 1)]


    df = df[df['main_topic_named'] == selected_group]

    selection = alt.selection_multi(fields=['type'], bind='legend')

    test_chart_kremlin = alt.Chart(df).mark_line(interpolate='basis').encode(

        alt.X('date', axis=alt.Axis(title='Дата', format=(years_or_months), tickCount=num_of_ticks)),
        alt.Y('NORM_NORM_INDEX:Q',axis=alt.Axis(title='Публикации',labels = True)),

        #alt.Y('norm_index:Q', scale=alt.Scale(domain=(0, 2), clamp=True)),
        # color='type'

    color= alt.Color('type',scale = alt.Scale(range = ['#165fb8','#b81639'])), tooltip='type',
        opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).properties(width=700, height=450).add_selection(selection)

    st.altair_chart(test_chart_kremlin)

#
#
#
# def test_chart(df,selected_group,selected_year):
#     # один график, одна тема, одна страна, две позиции
#     # на графике - одна тема и трии линии - кремлин, оппозиция и нейтральные.
#
#
#     grouped_df_with_dates = df.groupby(['name', 'date', 'main_topic_named']).count().reset_index()[
#         ['name', 'date', 'main_topic_named', 'index']]
#
#     def fun(x):
#         try:
#             return dual_who_is_who_dict[x]
#         except:
#             return 'нейтральный'
#
#     grouped_df_with_dates['type'] = grouped_df_with_dates['name'].apply(lambda x: fun(x))
#     st.markdown('grouped_df_with_dates')
#     st.dataframe(grouped_df_with_dates)
#
#     st.markdown('total_index_per_month')
#
#     # хочу понять общее количество публикаций по отдельным спикерам
#     total_index_per_month = grouped_df_with_dates.groupby(['name','date'])['index'].agg(['sum']).reset_index()
#     st.dataframe(total_index_per_month)
#
#     #grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['main_topic_named'].isin(selected_group)]
#
#     years_or_months = '%B'  # это значит месяц - подается в настройки чарта, если выбран один год
#     num_of_ticks = 6  # количество тиков на Х
#     if selected_year == 2020:
#         grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['date'] > datetime(2020, 1, 1)]
#     elif selected_year == 2019:
#         grouped_df_with_dates = grouped_df_with_dates[(grouped_df_with_dates['date'] > datetime(2019, 1, 1)) & (grouped_df_with_dates['date'] < datetime(2020, 1, 1))]
#     else:
#         years_or_months = '%Y'  # значит год, подается в настройки чарта
#         num_of_ticks = 4  # кол-во тиков
#         grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['date'] > datetime(2017, 1, 1)]
#
#     # test_df = pd.DataFrame(
#     #
#     #     {'name': ['name1', 'name2', 'name3'],
#     #      'index': [1, 2, 3],
#     #      'type': ['kr', 'kr', 'op']
#     #      }
#     # )
#     #
#     # test_df = test_df.groupby(['type'])['index'].agg(['sum'])
#
#     grouped_by_type = grouped_df_with_dates.groupby(['date','type'])['index'].agg(['sum']).reset_index()
#     grouped_by_type.rename(columns = {'sum':'index'},inplace = True)
#
#  #   st.dataframe(grouped_by_type)
#
#     # НОРМАЛИЗОВАННЫЙ ГРАФИК КРЕМЛЯ
#
#     # процент публикаций в месяц. попробуем
#
#
#     normalized_data = grouped_by_type.copy()
#     normalized_data['max'] = normalized_data['index'].max()
#     normalized_data['norm_index'] = normalized_data['index'] / normalized_data['max']
#   #  st.dataframe(normalized_data)
#     source = normalized_data
#
#     selection = alt.selection_multi(fields=['type'], bind='legend')
#     # ok chart
#     test_chart_kremlin = alt.Chart(source).mark_line(interpolate='basis').encode(
#
#         alt.X('date', axis=alt.Axis(title='Date', format=(years_or_months), tickCount=num_of_ticks)),
#         alt.Y('norm_index:Q', scale=alt.Scale(domain=(0, 1), clamp=True)),
#
#         color='type', tooltip='type',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=600, height=600).add_selection(selection)
#
# #    st.dataframe(test_data_kremlin_2020)
#     st.write(test_chart_kremlin)
#
#
#
#
#
# def draw_line_for_channels(df,selected_group,selected_year,selected_who):
#     grouped_df_with_dates = df.groupby(['name', 'date', 'main_topic_named']).count().reset_index()[
#         ['name', 'date', 'main_topic_named', 'index']]
#
#     grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['main_topic_named'].isin(selected_group)]
#
#     grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['name'].isin(selected_who)]
#
#
#     grouped_df_with_dates = grouped_df_with_dates.groupby(
#         ['name','date', 'main_topic_named']).index.sum().reset_index()
#
#     years_or_months = '%B'  # это значит месяц - подается в настройки чарта, если выбран один год
#     num_of_ticks = 6  # количество тиков на Х
#
#     if selected_year == 2020:
#         grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['date'] > datetime(2020, 1, 1)]
#     elif selected_year == 2019:
#         grouped_df_with_dates = grouped_df_with_dates[(grouped_df_with_dates['date'] > datetime(2019, 1, 1)) & (grouped_df_with_dates['date'] < datetime(2020, 1, 1))]
#     else:
#         years_or_months = '%Y'  # значит год, подается в настройки чарта
#         num_of_ticks = 4  # кол-во тиков
#         grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['date'] > datetime(2017, 1, 1)]
#
#     # НОРМАЛИЗОВАННЫЙ ГРАФИК КРЕМЛЯ
#     test_data_kremlin_2020 = grouped_df_with_dates.copy()
#     test_data_kremlin_2020['max'] = test_data_kremlin_2020['index'].max()
#     test_data_kremlin_2020['norm_index'] = test_data_kremlin_2020['index'] / test_data_kremlin_2020['max']
#     test_max_index = test_data_kremlin_2020['max'].max()
#
#     source = test_data_kremlin_2020
#     # st.dataframe(source)
#
#     selection = alt.selection_multi(fields=['name'], bind='legend')
#     # ok chart
#     test_chart_kremlin = alt.Chart(source).mark_line(interpolate='basis').encode(
#
#         alt.X('date', axis=alt.Axis(title='Date', format=(years_or_months), tickCount=num_of_ticks)),
#         alt.Y('norm_index:Q', scale=alt.Scale(domain=(0, 1), clamp=True)),
#
#         color='name', tooltip='name',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=600, height=600).add_selection(selection)
#
#     st.dataframe(test_data_kremlin_2020)
#     st.write(test_chart_kremlin)
#
# def draw_line_for_smi(df,selected_group = 'Навальный',selected_year = 2020):
#
#     #st.markdown(selected_group)
#     grouped_df_with_dates = df.groupby(['name', 'date', 'main_topic_named']).count().reset_index()[
#         ['name', 'date', 'main_topic_named', 'index']]
#     st.dataframe(grouped_df_with_dates)
#     kremlin_news = ['RT на русском', 'Подъём', 'РИА Новости', 'ТАСС']
#     free_news = ['Baza', '«Открытые медиа». Эксклюзивы', 'МБХ медиа', 'Медуза — LIVE']
#     grouped_df_with_dates['type'] = grouped_df_with_dates['name'].apply(lambda x: 'kremlin' if x in kremlin_news else 'free')
#     # отфильтровали только те которые мы выбрали выше
#     grouped_df_with_dates = grouped_df_with_dates[grouped_df_with_dates['main_topic_named'].isin(  list(selected_group))]
#
#     # df кремля
#     data_kremlin = grouped_df_with_dates[grouped_df_with_dates['type'] == 'kremlin'].groupby(
#         ['type', 'date', 'main_topic_named']).index.sum().reset_index()
#
#     # выбираем дату
#     years_or_months = '%B'  # это значит месяц - подается в настройки чарта, если выбран один год
#     num_of_ticks = 6  # количество тиков на Х
#     if selected_year == 2020:
#         data_kremlin_2020 = data_kremlin[data_kremlin['date'] > datetime(2020, 1, 1)]
#     elif selected_year == 2019:
#         data_kremlin_2020 = data_kremlin[(data_kremlin['date'] > datetime(2019, 1, 1)) & (data_kremlin['date'] < datetime(2020, 1, 1))]
#     else:
#         years_or_months = '%Y'  # значит год, подается в настройки чарта
#         num_of_ticks = 4  # кол-во тиков
#         data_kremlin_2020 = data_kremlin[data_kremlin['date'] > datetime(2017, 1, 1)]
#
#     # НОРМАЛИЗОВАННЫЙ ГРАФИК КРЕМЛЯ
#     test_data_kremlin_2020 = data_kremlin_2020.copy()
#     test_data_kremlin_2020['max'] = test_data_kremlin_2020['index'].max()
#     test_data_kremlin_2020['norm_index'] = test_data_kremlin_2020['index'] / test_data_kremlin_2020['max']
#     test_max_index = test_data_kremlin_2020['max'].max()
#
#     #  st.dataframe(test_data_kremlin_2020)
#
#     source = test_data_kremlin_2020
#     # st.dataframe(source)
#
#     selection = alt.selection_multi(fields=['main_topic_named'], bind='legend')
#     # ok chart
#     test_chart_kremlin = alt.Chart(source).mark_line(interpolate='basis').encode(
#
#         alt.X('date', axis=alt.Axis(title='Date', format=(years_or_months), tickCount=num_of_ticks)),
#         alt.Y('norm_index:Q', scale=alt.Scale(domain=(0, 1), clamp=True)),
#
#         color='main_topic_named', tooltip='main_topic_named',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=350, height=350).add_selection(selection)
#
#     data_oppisition = grouped_df_with_dates[grouped_df_with_dates['type'] == 'free'].groupby(
#         ['type', 'date', 'main_topic_named']).index.sum().reset_index()
#     # выбираем дату
#     years_or_months = '%B'  # это значит месяц - подается в настройки чарта, если выбран один год
#     num_of_ticks = 6  # количество тиков на Х
#     if selected_year == 2020:
#         data_oppisition_2020 = data_oppisition[data_oppisition['date'] > datetime(2020, 1, 1)]
#     elif selected_year == 2019:
#         data_oppisition_2020 = data_oppisition[
#             (data_oppisition['date'] > datetime(2019, 1, 1)) & (data_oppisition['date'] < datetime(2020, 1, 1))]
#     else:
#         years_or_months = '%Y'
#         num_of_ticks = 4
#         data_oppisition_2020 = data_oppisition[data_oppisition['date'] > datetime(2017, 1, 1)]
#
#     # НОРМАЛИЗОВАННЫЙ ГРАФИК ОППОЗИЦИИ
#
#     test_data_opposotion_2020 = data_oppisition_2020.copy()
#     test_data_opposotion_2020['max'] = test_data_opposotion_2020['index'].max()
#
#     test_data_opposotion_2020['norm_index'] = test_data_opposotion_2020['index'] / test_data_opposotion_2020['max']
#     # st.dataframe(test_data_kremlin_2020)
#
#     source = test_data_opposotion_2020
#
#     selection = alt.selection_multi(fields=['main_topic_named'], bind='legend')
#     # ok chart
#     test_chart_opposition = alt.Chart(source).mark_line(interpolate='basis').encode(
#         alt.X('date', axis=alt.Axis(title='Date', format=(years_or_months), tickCount=num_of_ticks)),
#         alt.Y('norm_index:Q', scale=alt.Scale(domain=(0, 1), clamp=True)),
#
#         color='main_topic_named', tooltip='main_topic_named',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=350, height=350).add_selection(selection)
#
#     concat_test_charts = alt.hconcat(test_chart_kremlin, test_chart_opposition)
#     st.write(concat_test_charts)
#     # data_oppisition_2020 = data_oppisition[data_oppisition['date'] > datetime(2020,1,1)]
#     #        data_oppisition_2020['main_topic'] = data_oppisition_2020['main_topic'].apply(str)
#
#     # st.dataframe(data_oppisition_2020)
#
#     data_kremlin_2020_max_index = data_kremlin_2020['index'].max()
#     data_oppisition_2020_max_index = data_oppisition_2020['index'].max()
#     max_index = max([data_kremlin_2020_max_index, data_oppisition_2020_max_index])
#
#     source = data_kremlin_2020
#
#     selection = alt.selection_multi(fields=['main_topic_named'], bind='legend')
#     # ok chart
#     chart1 = alt.Chart(source).mark_line(interpolate='basis').encode(
#         alt.X('date:T', ),
#         alt.Y('index:Q', scale=alt.Scale(domain=(1, max_index), clamp=True)),
#
#         color='main_topic_named', tooltip='main_topic_named',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=350, height=350).add_selection(selection)
#
#     # второй ok chart
#     source2 = data_oppisition_2020
#
#     chart2 = alt.Chart(source2).mark_line(interpolate='basis').encode(
#         alt.X('date:T'),
#         alt.Y('index:Q', scale=alt.Scale(domain=(1, max_index), clamp=True)),
#         color='main_topic_named', tooltip='main_topic_named',
#         opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
#     ).properties(width=350, height=350).add_selection(selection)
#
#     # ПОКАЗАТЬ ЧАРТЫ
#     kremlin_n_free_chart = alt.hconcat(chart1, chart2)
#
#     st.write(kremlin_n_free_chart)