# -*- coding: utf8 -*-
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_gif_component as gif
import tab
from dash import html
from dash import dash_table as dt
from dash import dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]  # Size adaptation for phone version
                )
app.title = 'Изучение основных элементов программирования'

if __name__ == "__main__":
    app.layout = dbc.Container([

        dbc.Row([
            dbc.Col(html.Div(
                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink("Главная страница", href="main")),
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("", header=True),
                                dbc.DropdownMenuItem("Сортировки", href="sortings")
                            ],
                            nav=True,
                            in_navbar=True,
                            label="",
                        ),
                    ],
                    brand="Basics of programming",
                    brand_href="#",
                    color="#45527a",
                    dark=True,
                    style={'box-shadow': '5px 5px 5px #818db3', 'border-radius': '10px'}
                ), className=''
            ))
        ]),
        dbc.Row([
            dbc.Col(html.Div([
                dcc.Markdown('''
            # Добро пожаловать на сайт Basics Of Programming!
             Здесь вы с легкостью сможете изучить самые основные вещи связанные с программированием.



            ''')
            ], className='text-left',
                style={'marginTop': 10, 'border': 'solid', 'border-radius': '20px', 'border-width': '2px',
                       'border-color': '#45527a', 'padding': '6px 0px 0px 8px', 'font-size': '18px'})
            )
        ]),
        dbc.Row([
            dbc.Col(html.Div([
                html.H2('Основные виды сортировок и примеры их реализации'),
                html.P('Алгоритм сортировки — это алгоритм для упорядочивания элементов в массиве.')
            ], className='text-center',
                style={'marginTop': 10, 'marginBottom': 10, 'font-size': '18px'}
            )),
        ]),
        dbc.Row([
            dbc.Col(html.Div([
                dcc.Markdown('''

                ## Зачем они нужны ?
                В первую очередь, для поиска и представления данных. Некоторые задачи с неотсортированными данными решить очень трудно, 
                а некоторые просто невозможно. Пример: орфографический словарь, в нем слова отсортированы по алфавиту. 
                Если бы это было не так, то попробуйте найти в нем нужное слово. 
                Телефонная книга, где абоненты отсортированы по алфавиту. Даже если сортировка не обязательна и не сильно нужна, 
                все равно бывает удобнее работать с отсортированными данными.
                ''')
            ], className='text-center',
                style={'marginTop': 20, 'font-size': '20px', 'border': 'solid', 'border-width': '2px',
                       'border-radius': '20px', 'background-color': '#ffffffab'})),

        ]),
        dbc.Row([  # Bubble Sort Markdown
            dbc.Col(html.Div([
                dcc.Markdown('''
            ## Сортировка пузырьком или Bubble Sort

           >
           > Сортировка пузырьком — один из самых известных алгоритмов сортировки. Здесь нужно последовательно сравнивать значения соседних элементов
           > и менять числа местами, если предыдущее оказывается больше последующего. 
           > Таким образом элементы с большими значениями оказываются в конце списка, а с меньшими остаются в начале
           >
           * Достоинство метода: не требуется дополнительных массивов
           * Недостаток: время алгоритма пропорционально квадрату количества элементов (самый медленный способ сортировки)
            ''')
            ], className='text-left',
                style={'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10,
                       'font-family': 'Arial', 'width': '15cm'})
            ),
            dbc.Col(html.Div([
                html.H5(' Сортировка пузырьком'),
                gif.GifPlayer(
                    gif='assets/bubbleSort.gif',
                    still='',
                    autoplay=True
                )
            ], style={'marginLeft': 10, 'marginRight': 10, 'marginTop': 50, 'marginBottom': 50,
                      'border': 'dashed'})),
        ]),
        dbc.Row([
            dbc.Col(html.Div([
                dbc.Tabs(
                    [
                        dbc.Tab(tab.tab1_content, label="Python", tab_id="tab-1"),
                        dbc.Tab(tab.tab2_content, label="Java", tab_id="tab-2"),
                        dbc.Tab(tab.tab3_content, label="C++", tab_id="tab-3"),
                    ],
                    id="tabs",
                    active_tab="tab-1",
                ),
                html.Div(id="content")
            ], className='',
                style={'width': '15cm'})),
            dbc.Col(html.Div([
                dcc.Markdown('''
                ## Сортировка вставкой

                Сортировка вставкой - это алгоритм сортировки, который помещает несортированный элемент в подходящее место на каждой итерации.
                Сортировка вставкой работает так же, как мы сортируем карты в вашей руке в карточной игре.
                Мы предполагаем, что первая карта уже отсортирована, затем мы выбираем несортированную карту. Если несортированная карта больше, чем карта в руке, она кладется справа, в противном случае - слева. Таким же образом берутся и другие несортированные карты и кладутся на свое место.

                В отличие от пузырьковой сортировки и сортировки посредством выбора, количество сравнений в сортировке вставками зависит от изначальной упорядоченности списка. 
                Если список уже отсортирован, количество сравнений равно n - 1; 
                в противном случае его производительность является величиной порядка n2
                Вообще говоря, в худших случаях сортировка вставками настолько же плоха, как и пузырьковая сортировка и сортировка посредством выбора, а в среднем она лишь немного лучше. Тем не менее, у сортировки вставками есть два преимущества. 
                * Во-первых, ее поведение естественно. Другими словами, она работает меньше всего, когда массив уже упорядочен, и больше всего, когда массив отсортирован в обратном порядке. Поэтому сортировка вставками — идеальный алгоритм для почти упорядоченных списков. 
                * Второе преимущество заключается в том, что данный алгоритм не меняет порядок одинаковых ключей. Это значит, что если список отсортирован по двум ключам, то после сортировки вставками он останется упорядоченным по обоим.

                 Несмотря на то, что количество сравнений при определенных наборах данных может быть довольно низким, при каждой вставке элемента на свое место массив необходимо сдвигать. Вследствие этого количество перемещений может быть значительным.
            ''')
            ], className='text-right',
                style={'width': '18cm', 'marginTop': '50px'}))
        ]),
        # dbc.Row([
        #     dbc.Col(html.Div(
        #         [
        #             dbc.Card(
        #                 dbc.CardBody(
        #                     [
        #                         html.H2("Сортировка как основа программирования", className="card-title"),
        #                         html.P("Сортировка - это алгоритм для упорядочивания элементов в массиве. "
        #                                 "В случае, когда элемент в массиве имеет несколько полей, "
        #                                 "поле, служащее критерием порядка, называется ключом сортировки",
        #                                 className="card-subtitle"),
        #
        #                         # dbc.CardLink("Card link", href="#"),
        #                         # dbc.CardLink("External link", href="https://google.com"),
        #                     ]
        #                 ),
        #                 style={"width": "50rem"},
        #             )
        #
        #         ]))
        # ]),
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5('Сортировка вставками'),
                    gif.GifPlayer(
                        gif='assets/insertionSort.gif',
                        still='',
                        autoplay=True
                    )
                ], style={'border': 'dashed', 'width': '15cm', 'marginTop': '50px'})),
            dbc.Col(html.Div([
                dbc.Tabs(
                    [
                        dbc.Tab(tab.tab4_content, label="Python", tab_id="tab-4", tab_style={'margin-left': 'auto'}),
                        dbc.Tab(tab.tab5_content, label="Java", tab_id="tab-5"),
                        dbc.Tab(tab.tab6_content, label="C++", tab_id="tab-6"),
                    ],
                    id="tabs2",
                    active_tab="tab-4",
                ),
                html.Div(id="content2")
            ], className='',
                style={'width': '18cm', 'border-radius': '10px'}))
        ]),

        dbc.Row([
            dbc.Col(html.Div([
                dcc.Markdown('''
            ## Сортировка слиянием
            Сортировка слиянием – алгоритм, который сортирует такие структуры данных, где доступ к элементам осуществляется последовательно. Эта сортировка происходит следующим образом:
            массив разбивается на две примерно равные части, затем каждая из них сортируется. После этого два отсортированных подмассива сливаются в один. Для этого сравниваются два первых элемента в каждом из них и в зависимости от порядка сортировки ставятся в нужной последовательности. Если же один подмассив закончился, то оставшиеся элементы второго записываются после последнего элемента первого.
            #### Плюсы
            * Список большого размера, объединенный этой сортировкой.
            * Также используется в связанном списке.
            * Внешняя сортировка
            * Экономия времени O(NlogN)
            ''')
            ], style={'width': '15cm','marginTop':'20px'})),
            dbc.Col(
                html.Div([
                    html.H5('Сортировка слиянием'),
                    gif.GifPlayer(
                        gif='assets/mergeSort.gif',
                        still='',
                        autoplay=True
                    )
                ], style={'border': 'dashed', 'width': '15cm', 'marginTop': '20px','marginLeft':'50px'})),
            dbc.Col(html.Div([
                ##            dbc.Tabs(
                ##                [
                ##                    dbc.Tab(tab.tab4_content, label="Python", tab_id="tab-4", tab_style={'margin-left': 'auto'}),
                ##                    dbc.Tab(tab.tab5_content, label="Java", tab_id="tab-5"),
                ##                    dbc.Tab(tab.tab6_content, label="C++", tab_id="tab-6"),
                ##                ],
                ##                id="tabs3",
                ##                active_tab="tab-4",
                ##            ),
                html.Div(id="content32")
            ], className='',
                style={'width': '15cm', 'border-radius': '10px'}))]
        ),

        dbc.Row([
            dbc.Col(html.Div([
                           dbc.Tabs(
                               [
                                   dbc.Tab(tab.tab7_content, label="Python", tab_id="tab-7", tab_style={}),
                                   dbc.Tab(tab.tab8_content, label="Java", tab_id="tab-8"),
                                   dbc.Tab(tab.tab9_content, label="C++", tab_id="tab-9"),
                               ],
                               id="tabs3",
                               active_tab="tab-7",
                           ),
                html.Div(id="content3")
            ], className='',
                style={'width': '34cm', 'border-radius': '10px'}))]
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dcc.Markdown('''
                
                ## Существуют и другие виды сортировок
                
                ''')
            ], className='text-center', style = {'marginTop':'80px', 'marginBottom':'80px'}))
        ),
])

        # Datatable
        ##    dbc.Row([dbc.Col(html.Div(
        ##        [
        ##            dt.DataTable
        ##                (
        ##                id='input_data_table',
        ##                columns=[
        ##                    {'id':'n1', 'name': '1'},
        ##                    {'id':'n2', 'name': '2'},
        ##                    {'id':'n3', 'name': '3'},
        ##                    {'id':'n4', 'name': '4'},
        ##                    {'id':'n5', 'name': '5'},
        ##                    {'id':'n6', 'name': '6'},
        ##                    {'id':'n7', 'name': '7'},
        ##                    {'id':'n8', 'name': '8'},
        ##                    {'id':'n9', 'name': '9'},
        ##                ],
        ##                data=[
        ##                    {
        ##                        'n1': '0',
        ##                        'n2': '0',
        ##                        'n3': '0',
        ##                        'n4': '0',
        ##                        'n5': '0',
        ##                        'n6': '0',
        ##                        'n7': '0',
        ##                        'n8': '0',
        ##                        'n9': '0',
        ##                    }
        ##                ],
        ##                page_action='none',
        ##                style_table={'width': '11cm', 'overflowY': 'auto','borderRadius':'10px'},
        ##                style_cell={'textAlign': 'center'},
        ##                style_header={
        ##                    'backgroundColor': 'rgb(190, 209, 230)',
        ##                    'color': 'white'
        ##                },
        ##                style_data={
        ##                    'backgroundColor': 'rgb(190, 209, 230)',
        ##                    'color': 'white'
        ##                },
        ##                editable=True,
        ##            )
        ##        ],
        ##        style={
        ##            'margin':'1cm',
        ##            'display':'flex',
        ##            'flex-direction':'row',
        ##            'justify-content':'center',
        ##        },
        ##        className='text-center'))]),
        ##    dbc.Row([ # Buttons
        ##        dbc.Col(html.Div(
        ##            [
        ##                dbc.Button("1", color='primary', className="me-1", style={}),
        ##                dbc.Button("2", color="secondary", className="me-1"),
        ##                dbc.Button("3", color="success", className="me-1"),
        ##                dbc.Button("4", color="warning", className="me-1"),
        ##                dbc.Button("5", color="danger", className="me-1"),
        ##                dbc.Button("6", color="info", className="me-1"),
        ##                dbc.Button("7", color="light", className="me-1"),
        ##                dbc.Button("8", color="dark", className="me-1"),
        ##                dbc.Button("9", color="dark"),
        ##
        ##            ],className='text-center'
        ##
        ##        ))
        ##    ]),
        ##    dbc.Row([
        ##        dbc.Col(html.Div(
        ##            [
        ##                dbc.Button("0", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b1'),
        ##                dbc.Button("1", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b2'),
        ##                dbc.Button("2", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b3'),
        ##                dbc.Button("3", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b4'),
        ##                dbc.Button("4", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b5'),
        ##                dbc.Button("5", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b6'),
        ##                dbc.Button("6", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b7'),
        ##                dbc.Button("7", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b8'),
        ##                dbc.Button("8", disabled=True, outline=True, className="me-1", style={'border-color': 'white'}, id='b9'),
        ##
        ##            ], className='text-center'
        ##
        ##        ))
        ##    ]),
        ##


    app.run_server()











