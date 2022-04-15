import ast
from datetime import datetime

import pandas as pd
import time

import streamlit as st

from altair import Chart, X, Y, Axis, SortField
import altair as alt
import ast
from datetime import datetime

import pandas as pd
import time

import streamlit as st

from altair import Chart, X, Y, Axis, SortField
import altair as alt


@st.cache
def load_data(path):
    df = pd.read_excel(path,engine='openpyxl')
    return df


#
# df_news = load_data(path=r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\news\ОБЛЕГЧЕННЫЕ_НОВОСТИ.xlsx")
# df_anon = load_data(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\anon\ОБЛЕГЧЕННЫЕ_АНОНИМЫ.xlsx")
# df_public = load_data(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\anon_n_channels\ОБЛЕГЧЕННЫЕ ПУБЛИЧНЫЕ КАНАЛЫ.xlsx")
#
# df_news_for_lines = load_data(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\нормализованная дата для лайн чартов\сгруппированные_нормализованные_новости.xlsx")
# df_anon_for_lines = load_data(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\нормализованная дата для лайн чартов\сгруппированные_нормализованные_анонимы.xlsx")
# df_public_for_lines = load_   data(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\нормализованная дата для лайн чартов\сгруппированные_нормализованные_публичные.xlsx")
#
# df_news_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_новости.xlsx')
# df_anon_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_анонимы.xlsx')
# df_public_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_публичные.xlsx')

df_news_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_новости_norm_nav.xlsx')
df_anon_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_анонимы_norm_nav.xlsx')
df_public_for_lines = load_data('./нормализованная дата для лайн чартов/сгруппированные_нормализованные_публичные_norm_nav.xlsx')




df_news = load_data(path= './облегченные/ОБЛЕГЧЕННЫЕ_НОВОСТИ.xlsx')
df_anon = load_data(path= './облегченные/ОБЛЕГЧЕННЫЕ_АНОНИМЫ.xlsx')
df_public = load_data(path= './облегченные/ОБЛЕГЧЕННЫЕ ПУБЛИЧНЫЕ КАНАЛЫ.xlsx')


# ЗАГОЛОВОК
st.title('Гид по информационным потокам Телеграма')
st.markdown('#### Формируем сбалансированную картину мира')
st.markdown(' ')

# ВСТУПЛЕНИЕ
#text1 = ''.join(open('текст для телеги.txt', encoding='utf-8').readlines()).split('#')[1]
# st.markdown(text1)

st.markdown('''В начале 2021 года ежемесячная аудитория Telegram превысила 500 млн пользователей. Помимо высокого уровня приватности юзеров привлекает контроль над своим медиапотреблением – телеграм-каналы позволяют обойти рекомендательные алгоритмы и цензуру соцсетей. Однако разобраться в обилии авторов может быть непросто. Данная работа – попытка сделать краткий гид по общественно-политическим и новостным каналам.''')
st.markdown('''Карта ниже иллюстрирует связи между каналами из нашей выборки. Чем ближе они находятся друг к другу, тем больше взаимных упоминаний и репостов они делают. Размер узлов соответствует количеству подписчиков. Цветом выделены кластеры, представители которых связаны между собой сильнее, чем с другими. *Интерактивная версия доступна по [ссылке](https://kbondar17.github.io/telega_2/)* ''')

st.image('https://sun9-42.userapi.com/impg/WFmv3t6uHuj0x2ouLeD5U-GY7Jqw5YcncyIfAA/HE3iObwn4SQ.jpg?size=1024x578&quality=96&sign=9005ce333dea36b091c413faa1ffb685&type=album',
         width=800)

# st.markdown('''Заметно, что главное разделение идет по политическим пристрастиям. Голубые - сплошь оппозиционеры. Любопытны "подкластеры" - **Алексей авальный** и **Михаил Ходорковский**, окруженные созданными ими информационными ресурсами.
# Главное оппозиционное СМИ ожидаемо "**Медуза**". На границе двух миров - **Алексей Венедиктов**.
# За ним (сразу после светской тусовки в виде **Ксении Собчак** и **Сергея Минаева**) **госсми** и их видные деятели - **Маргарита Симоньян** и **Владимир Соловьев**.
# Далее на восток - царство анонимных каналов. \n\n
# В поле ниже можно выбрать конкретный канал и посмотреть, какие темы он освещает. Например, **Baza** пишет почти исключительно про криминал,
#  **"Открытые медиа"** следит за протестами, а **"Незыгарь"** одержим перестановками во власти.
# ''')

st.markdown('''Кажется, взаимоотношения в телеграме хорошо отражают политические реалии. Любопытны "подкластеры" - **Алексей Навальный** и **Михаил Ходорковский**, окруженные созданными ими информационными ресурсами.
Главное оппозиционное СМИ ожидаемо "**Медуза**". Мостик на границе двух миров - **Алексей Венедиктов**. 
За ним (сразу после светской тусовки в виде **Ксении Собчак** и **Сергея Минаева**) **госсми** и их видные деятели - **Маргарита Симоньян** и **Владимир Соловьев**. 
Далее на восток - царство анонимных каналов, в котором центробежными силами выступают "**Караульный**" (ведущий агрегатор) и родоначальник жанра "инсайд из телеграма"
 "**Незыгарь**". Внизу – каналы, сошедшиеся на почве нелюбви к власти, но держащиеся вдали от видных оппозиционеров. \n\n
В поле ниже можно выбрать конкретный канал и посмотреть, какие темы он освещает. Например, **Baza** пишет почти исключительно про криминал,
 **"Открытые медиа"** следят за протестами, а **"Незыгарь"** одержим перестановками во власти - "Дабл Ять" и "КСТАТИ".
'''
)

# st.image('https://sun9-38.userapi.com/impg/en5lmi6Zsn5aM1AZb70UaRGsjgJj-_FzbWUJdw/GwIL-mCr7qA.jpg?size=1023x587&quality=96&sign=77e8ae4743e80d13aa7390351e604eeb&type=album',
#          use_column_width=True)




# КАК ЭТО УСТРОЕНО
# st.markdown('')
# optionals = st.beta_expander("Подробнее о том, как это работает", False)
# st.markdown('')

#text2 = ''.join(open('текст для телеги.txt', encoding='utf-8').readlines()).split('#')[2]
#optionals.markdown(text2)


#ПОКАЗАТЬ БАРЧАРТ с темами
from bar_chart import draw_bar_chart
st.markdown('')# пустая строка
st.markdown('#### Выбери тип источника:')
selected_type_of_source = st.selectbox('', ['СМИ', 'анонимные каналы', 'личные каналы'])

if selected_type_of_source == 'СМИ':
    draw_bar_chart(df_news)
elif selected_type_of_source == 'анонимные каналы':
    draw_bar_chart(df_anon)
elif selected_type_of_source == 'личные каналы':
    draw_bar_chart(df_public)



st.markdown('Теперь понаблюдаем, как распределение тем меняется во времени в зависимости от типа источника. Для простоты визуализации разделим источники на две группы – "провластные" и "независимые".')

with st.expander('Показать какой канал в какой группе'):
    st.markdown('**Провластные**')
    st.markdown(
', '.join(['Baronova','Ekvinokurova','Ortega','Skabeeva','ГЕЙ НА ПЕРЕДЕРЖКЕ','Максим Кононенко','Маргарита Симоньян','СОЛОВЬЁВ',
            '338', 'Акитилоп', 'Байки из Спасской Башни', 'Дабл Ять', 'Бойлерная', 'ВЧК-ОГПУ',
            'Байки из Спасской Башни', 'Закулисный шептун', 'Караульный', 'Катарсис','Кремлёвская прачка', 'Кремлёвский безБашенник',  'КСТАТИ', 'Мастер пера',
            'Медиатехнолог', 'Мейстер', 'Методичка', 'Политбюро 2.0', 'Политджойстик/Politjoystic', 'ПолитФорум', 'Полный П', 'ПОСТПРАВДА','НЕЗЫГАРЬ','Мысли-НеМысли',
            'Мышь в овощном',   'НЕШУЛЬМАН', 'Новая Искренность','Старая площадь'
]))

    st.markdown('**Независимые**')
    st.markdown(
    ', '.join(['Leonid Volkov','PLUSHEV/ПЛЮЩЕВ','aavst','Смирнов','Ковалёв Алексей как река Енисей',
                    'Павел Чиков','Колезев', 'Команда Навального','Михаил Ходорковский','Навальный','Таня Ф',
    'Baza','«Открытые медиа». Эксклюзивы', 'МБХ медиа',  'Медуза','Генерал СВР','СерпомПо','Шулика','Сталингулаг', 'Екатерина Шульман','Антискрепа']))




# LINE CHART
# ОКОШКО С ВЫБОРОМ СТОЧНИКА
st.markdown('#### Выбери тип источника:')
selected_source = st.selectbox('',['анонимные каналы',  'СМИ','личные каналы'])


#global_topics = open(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\my_tools\ALL_TOPICS.txt",'r').readlines()[0].split('|')

# anon_topics = open(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\anon_topics.txt",'r').readlines()[0].split('|')
# topics_for_channels = open(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\public_topics.txt",'r').readlines()[0].split('|')
# topics_for_news = open(r"C:\Users\Kirill\JUPITER NOTEBOOKS\тематическое моделирование\telega\NEW_WAY\news_topics.txt",'r').readlines()[0].split('|')

anon_topics = list(df_anon_for_lines['main_topic_named'].unique())
anon_topics = [e for e in anon_topics if e not in ['нет темы','Другое_14']]

topics_for_channels = list(df_public_for_lines['main_topic_named'].unique())
topics_for_channels = [e for e in topics_for_channels if e not in ['нет темы','Другое_14']]

topics_for_news = list(df_news_for_lines['main_topic_named'].unique())
topics_for_news = [e for e in topics_for_news if e not in ['нет темы','Другое_14']]



# ОКОШКО С ВЫБОРОМ ТЕМЫ
st.markdown('#### Выбери тему:')
if selected_source == 'анонимные каналы':

    selected_group = st.selectbox('',anon_topics)

elif selected_source == 'СМИ':
    selected_group = st.selectbox('',topics_for_news)


elif selected_source == 'личные каналы':
    selected_group = st.selectbox('',topics_for_channels)

st.markdown('#### Выбери год:')

selected_year = st.selectbox('',['с 2017 до сегодня',2019,2020,2021])


from line_chart import test_chart_2 #  draw_line_for_channels, test_chart, 

if selected_group:
    if selected_source == 'СМИ':
                                                # тут невидимые символы
        #st.markdown('ᅠ Прокремлевские  ᅠ ᅠ ᅠ ᅠ ᅠ ᅠ ᅠᅠ ᅠ ᅠ ᅠ ᅠ ᅠᅠᅠ  ᅠ ᅠ ᅠ Независимые')

        test_chart_2(df_news_for_lines,selected_group=selected_group, selected_year=selected_year)

    elif selected_source == 'личные каналы':
        #test_chart(df_public,selected_group=selected_group,selected_year=selected_year)


        test_chart_2(df_public_for_lines, selected_group=selected_group, selected_year=selected_year)


    elif selected_source == 'анонимные каналы':

        test_chart_2(df_anon_for_lines,selected_group=selected_group, selected_year=selected_year)


st.markdown('Любопытно, что, например, обострение на востоке Украины в конце 2020-начале 2021 или ситуация в США явно сильнее интересовали прокремлевские СМИ. Обратная ситуация с протестами в Белоруссии или судебными процессами в РФ – публичные независимые авторы комментировали эту тему гораздо охотнее.')

# wind of changing
st.markdown('В работе использована библиотека Gensim и алгоритм моделирования LDA. Подробнее по [ссылке](https://webdevblog.ru/tematicheskoe-modelirovanie-s-pomoshhju-gensim-python)' )