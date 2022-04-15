import  pandas as pd
from datetime import  datetime
from altair import Chart
import altair as alt
import streamlit as st


def draw_bar_chart(df):
    st.markdown('#### Выбери источник:')
    st.markdown('\n')
    selected_name = st.selectbox("", df['name'].unique())  # выбрали имя

    grouped_test_df = df.groupby(['name','main_topic_named']).count().reset_index()[['name','main_topic_named','index']] # сгрупировали
    df_one_name = grouped_test_df[grouped_test_df['name'] == selected_name] # выбрали выбранное имя
    df_one_name = df_one_name[~df_one_name['main_topic_named'].isin(['нет темы','Другое_14'])]
    #st.write(df_one_name)
    selection = alt.selection_multi(fields=['main_topic_named'], bind='legend')

    st.write(Chart(df_one_name).mark_bar().encode(y=alt.Y('index:Q', title='Количество публикаций'),x=alt.X('main_topic_named:O',title='Темы',axis=alt.Axis(labels=False)) # вииииз
                       ,color = alt.Color('main_topic_named',legend=alt.Legend( title=None, labelFontSize = 13) ), tooltip = 'main_topic_named',
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2))).properties(width=700,height=400).add_selection(selection))

