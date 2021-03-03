import dash 
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go 
import pandas as pd
import dash_html_components as html
# ipl_data1->sales
ipl_data1 = pd.read_csv("https://raw.githubusercontent.com/pikachu28/ipl-saga/main/Datasets/Clean_Data.csv")

app = dash.Dash(__name__,)
server = app.server
app.layout = html.Div([

html.Div([
        html.Br(), html.Br(),
        html.H1("IPL Data Analysis")],
        style={'margin-left': '5%','color':'#808000','width': '50%', 'display': 'inline-block'
 
    }),
html.Div([
    html.Br(), html.Br(),
    html.H4('Prepared by: Anjali Singh')],
    style={'color':'#17202A','width': '30%', 'display': 'inline-block', 'float': 'right'
    }),

html.Div([
    html.Label('Select a Team:'),
    dcc.Dropdown(id='team',
    multi=False,
    clearable=True,
    value='ABC',
    placeholder='Select Team',
    options=[{'label':c, 'value': c}
            for c in (ipl_data1['IPL 4 Franchise'].unique())])],
    style={'width':'10%', 'margin-left':'20%'}),

html.Div([
    html.Label('Select a Team:'),
    dcc.Dropdown(id='team2',
    multi=False,
    clearable=True,
    value='ABC',
    placeholder='Select Team',
    options=[{'label':c, 'value': c}
            for c in (ipl_data1['IPL 4 Franchise'].unique())])],
    style={'width':'10%', 'margin-left':'20%'}),

html.Div([
    html.Label('Select a Column:'),
    dcc.Dropdown(id='col1',
    multi=False,
    clearable=True,
    value='columns',
    placeholder='Graph1',
    options=[{'label':c, 'value': c}
            for c in ["50 runs made", "Strike rate", "matches", "Balls faced", "Batting avg", "Is batsman","runs scored", "innings played","Nationality(1=Overseas)","4s","6s", "highest score", "Is star batsman", "Is batsman","100 runs made","Catches per match","Catches taken","Number of balls bowled","Number of balls bowled", "runs given", "Is star bowler","Retained"]])],
    style={'width':'10%', 'margin-left':'80%', 'margin-top':'-8%'}),
html.Div([
    html.Label('Select a Column:'),
    dcc.Dropdown(id='col2',
    multi=False,
    clearable=True,
    value='columns',
    placeholder='Graph1',
    options=[{'label':c, 'value': c}
            for c in ["50 runs made", "Strike rate", "matches", "Balls faced", "Batting avg", "Is batsman","runs scored", "innings played","Nationality(1=Overseas)","4s","6s","highest score", "Is star batsman", "Is batsman","100 runs made","Catches per match","Catches taken","Number of balls bowled","Number of balls bowled", "runs given", "Is star bowler","Retained"]])],
    style={'width':'10%', 'margin-left':'80%'}),


html.Div([
    html.Br(),
    dcc.Graph(id='bar_line_1',
                config={'displayModeBar':False}),
            ],style={'margin-left': '1.4%','width': '50%', 'display': 'inline-block'}),
# Create line chart (One team comparison to others)
html.Div([
    html.Br(),
    dcc.Graph(id='line_line_5',
              config={'displayModeBar': False}),
 
        ],style={'margin-left': '1.4%','width': '50%', 'display': 'inline-block', 'margin-bottom':'3%'}),
html.Div([
    html.Br(),
    dcc.Graph(id='pie_1',
              config={'displayModeBar': 'hover'}),
 
        ],style={'margin-left': '1.4%', 'width': '50%', 'display': 'inline-block'}),

# html.Div([
#     html.Br(),
#     dcc.Graph(id='pie_2',
#               config={'displayModeBar': 'hover'}),
 
#         ],style={'margin-left': '1.4%', 'width': '50%', 'display': 'inline-block'}),
# Create bubble chart (Compare several columns)
# html.Div([
#     html.Br(),
#     dcc.Graph(id='bubble_2',
#               config={'displayModeBar': 'hover'}),
 
#         ],style={'margin-left': '1.4%', 'width': '50%', 'display': 'inline-block'}),
    html.Div([
    html.Br(),
    dcc.Graph(id='bar_bar_3',
              config={'displayModeBar': False}),
 
        ],style={'margin-left': '1.4%','width': '50%', 'display': 'inline-block'})
])

@app.callback(Output('bar_line_1','figure'),
                [Input('team', 'value'),
                Input('col1', 'value')])

def update_graph(team, col1):
    data1=ipl_data1.groupby(['Team', 'IPL 4 Franchise'])[col1].sum().reset_index()
    data2=ipl_data1.groupby(['Team', 'IPL 4 Franchise'])['Player cost USD'].mean().reset_index()
    return{
        'data': [go.Bar(x=data1[data1['IPL 4 Franchise'] == team]['Team'],
                        y=data1[data1['IPL 4 Franchise'] == team][col1],
                        text=data1[data1['IPL 4 Franchise'] == team][col1],
                        name='matches played',
                        texttemplate='%{text:.2s}',
                        textposition='auto',
                        marker=dict(
                            color=data1[data1['IPL 4 Franchise'] == team][col1],
                            colorscale='phase',
                            showscale=False),
                        yaxis='y1',
 
                        hoverinfo='text',
                        hovertext=
                        '<b>Team Name</b>: ' + data1[data1['IPL 4 Franchise'] == team]['IPL 4 Franchise'].astype(str) + '<br>'+
                        '<b>Column </b>: ' + [f'{x:,.0f}' for x in data1[data1['IPL 4 Franchise'] == team][col1]] + '<br>'+
                        '<b>Country</b>: ' + data1[data1['IPL 4 Franchise'] == team]['Team'].astype(str) + '<br>'
 
 
                        ),
                         go.Scatter(
                            x=data2[data2['IPL 4 Franchise'] == team]['Team'],
                            y=data2[data2['IPL 4 Franchise'] == team]['Player cost USD'],
                            name='Player cost USD',
                            text=data2[data2['IPL 4 Franchise'] == team]['Player cost USD'],
                            mode='markers + lines',
                            marker=dict(color='#bd3786'),
                            yaxis='y2',
                            hoverinfo='text',
                            hovertext=
                            '<b>Team Name</b>: ' + data2[data2['IPL 4 Franchise'] == team]['IPL 4 Franchise'].astype(str) + '<br>'+
                            '<b>Player cost</b>: $' + [f'{x:,.0f}' for x in data2[data2['IPL 4 Franchise'] == team]['Player cost USD']] + '<br>'+
                            '<b>Country</b>: ' + data2[data2['IPL 4 Franchise'] == team]['Team'].astype(str) + '<br>'
                            )],
            'layout': go.Layout(
             width=780,
             height=520,
             title={
                'text':  (col1) + ' and Average player cost : ' + (team),
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={'family': 'Oswald',
                        'color': 'rgb(230, 34, 144)',
                        'size': 25},
 
             hovermode='x',
                            xaxis=dict(title='<b>Country</b>',
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='rgb(17, 37, 239)'
                        )
 
                ),
 
             yaxis=dict(title='<b>'+ col1 + '</b>',
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                           family='Arial',
                           size=12,
                           color='rgb(17, 37, 239)'
                        )
 
                ),
             yaxis2=dict(title='<b>Avg. Player Cost($)</b>', overlaying='y', side='right',
                         color='rgb(230, 34, 144)',
                         showline=True,
                         showgrid=False,
                         showticklabels=True,
                         linecolor='rgb(104, 204, 104)',
                         linewidth=2,
                         ticks='outside',
                         tickfont=dict(
                           family='Arial',
                           size=12,
                           color='rgb(17, 37, 239)'
                         )
 
                 ),
 
             legend=dict(title='',
                         x=0.25,
                         y=1.08,
                         orientation='h',
                         bgcolor='rgba(255, 255, 255, 0)',
                         traceorder="normal",
                         font=dict(
                              family="sans-serif",
                              size=12,
                              color='#000000')),
 
                         legend_title_font_color="green",
                         uniformtext_minsize=12,
                         uniformtext_mode='hide',
 
                 )
 
    }
# Creating line chart for comparison
@app.callback(Output('line_line_5', 'figure'),
                        [Input('team', 'value'),
                        Input('team2', 'value')])

def update_graph(team, team2):
    # data for line
    data3 = ipl_data1.groupby(['IPL 4 Franchise', 'matches'])['50 runs made'].mean().reset_index()

    return{
        'data': [go.Scatter(x=data3[(data3['IPL 4 Franchise'] == team)]['50 runs made'],
                            y=data3[(data3['IPL 4 Franchise'] == team)]['matches'],
                        text=data3[(data3['IPL 4 Franchise'] == team)]['matches'],
                        name=team,
                        mode='markers+lines',
                        hoverinfo='text',
                        hovertext=
                        '<b>Team</b>: ' + data3[(data3['IPL 4 Franchise'] == team)]['IPL 4 Franchise'].astype(str) + '<br>'+
                        # '<b>Country</b>: ' + data3[ (data3['IPL 4 Franchise'] == team)]['Team'].astype(str) + '<br>'+
                        '<b>matches played</b>: ' + [f'{x:,.0f}' for x in data3[(data3['IPL 4 Franchise'] == team)]['matches']] + '<br>'
                            ),
                    go.Scatter(x=data3[(data3['IPL 4 Franchise'] == team2)]['50 runs made'],
                            y=data3[(data3['IPL 4 Franchise'] == team2)]['matches'],
                        text=data3[(data3['IPL 4 Franchise'] == team2)]['matches'],
                        name=team2,
                        mode='markers+lines',
                        hoverinfo='text',
                        hovertext=
                        '<b>Team</b>: ' + data3[(data3['IPL 4 Franchise'] == team2)]['IPL 4 Franchise'].astype(str) + '<br>'+
                        # '<b>Country</b>: ' + data3[ (data3['IPL 4 Franchise'] == team)]['Team'].astype(str) + '<br>'+
                        '<b>matches played</b>: ' + [f'{x:,.0f}' for x in data3[(data3['IPL 4 Franchise'] == team2)]['matches']] + '<br>'
                            )],

        'layout': go.Layout(
             width=780,
             height=520,
             title={
                'text': 'Teams comparsion : ' + (team) + ' V/S ' + (team2),
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={'family': 'Oswald',
                        'color': 'rgb(230, 34, 144)',
                        'size': 25},
 
             hovermode='x',
                         xaxis=dict(title='<b>50 runs made</b>',
                        tick0=0,
                        dtick=1,
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='rgb(17, 37, 239)'
                        )
 
                ),
             yaxis=dict(title='<b>Matches played</b>',
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                           family='Arial',
                           size=12,
                           color='rgb(17, 37, 239)'
                        )
 
                ),
 
        legend=dict(title='',
                         x=0.25,
                         y=1.08,
                         orientation='h',
                         bgcolor='rgba(255, 255, 255, 0)',
                         traceorder="normal",
                         font=dict(
                              family="sans-serif",
                              size=12,
                              color='#000000')),
 
                         legend_title_font_color="green",
                         uniformtext_minsize=12,
                         uniformtext_mode='hide',
 
                 )
    }

# @app.callback(Output('bubble_2','figure'),
#                 [Input('team', 'value')])
# def update_graph(team):
#     data4 = ipl_data1.groupby(['IPL 4 Franchise'])[['Player cost USD','Batting avg','Bowling average']].sum().reset_index()
#     size = data4[(data4['IPL 4 Franchise'] == team)]['Player cost USD']
#     return {
#         'data' : [go.Scatter(x=data4[data4['IPL 4 Franchise'] == team]['Batting avg'],
#                              y=data4[data4['IPL 4 Franchise'] == team]['Bowling average'],
#                             #  text=data4[data4['IPL 4 Franchise'] == team]['Bowling average'],
#                             #  mode='markers',
#                             #  name='team',
#                             #  hoverinfo='text',
#                             #  hovertext=
#                             #  '<b>Batting avg</b>'+data4[data4['IPL 4 Franchise'] == team]['Batting avg'] + '<br>'+
#                             #  '<b>bowling avg</b>'+data4[data4['IPL 4 Franchise'] == team]['Bowling average'] + '<br>',
#                              marker=dict(
            #                     size=size,
            #                     color=data4[(data4['IPL 4 Franchise'] == team)]['Player cost USD'],
            #                     colorscale='mrybm',
            #                     showscale=False
            #                  ),
                            
            #                 )],
            # 'layout': go.Layout(
            #  width=780,
            #  height=520,
            #  title={
            #     'text': 'Bubble chart: ' + (team),
            #     'y': 0.93,
            #     'x': 0.43,
            #     'xanchor': 'center',
            #     'yanchor': 'top'},
            #  titlefont={'family': 'Oswald',
            #             'color': 'rgb(230, 34, 144)',
            #             'size': 25},
 
            #  hovermode='closest',
 
            #  xaxis=dict(title='<b>Batting Avg</b>',
 
            #             color='rgb(230, 34, 144)',
            #             showline=True,
            #             showgrid=True,
            #             showticklabels=True,
            #             linecolor='rgb(104, 204, 104)',
            #             linewidth=2,
            #             ticks='outside',
            #             tickfont=dict(
            #                 family='Arial',
            #                 size=12,
            #                 color='rgb(17, 37, 239)'
    #                     )
 
    #             ),
    #             yaxis=dict(title='<b>Bowling Avg</b>',
    #                     color='rgb(230, 34, 144)',
    #                     showline=True,
    #                     showgrid=True,
    #                     showticklabels=True,
    #                     linecolor='rgb(104, 204, 104)',
    #                     linewidth=2,
    #                     ticks='outside',
    #                     tickfont=dict(
    #                        family='Arial',
    #                        size=12,
    #                        color='rgb(17, 37, 239)'
    #                     )
 
    #             ),
    #               legend=dict(title='',
    #                      x=0.25,
    #                      y=1.08,
    #                      orientation='h',
    #                      bgcolor='rgba(255, 255, 255, 0)',
    #                      traceorder="normal",
    #                      font=dict(
    #                         family="sans-serif",
    #                         size=12,
    #                         color='#000000')),

    #     )
    # }


@app.callback(Output('bar_bar_3', 'figure'),
                        [Input('col1', 'value'),
                        Input('col2', 'value')])

def update_graph(col1, col2):
    data5 = ipl_data1.groupby(['IPL 4 Franchise'])[col1].sum().reset_index()
    data6 = ipl_data1.groupby(['IPL 4 Franchise'])[col2].sum().reset_index()
    return{
        'data' : [go.Bar(x = data5['IPL 4 Franchise'],
                         y = data5[col1],
                         text = data5[col1],
                         name = 'Sum of '+(col1),
                         texttemplate = '%{text: .2s}',
                         textposition = 'auto',
                         marker = dict(color='rgb(214, 137, 16)'),
                         yaxis='y1',
                         offsetgroup=1,
                         hoverinfo='text',
                         hovertext=
                         '<b>Team</b>: ' + data5['IPL 4 Franchise'].astype(str) + '<br>'+
                        '<b>Left y-axis</b>: $' + [f'{x:,.0f}' for x in data5[col1]] + '<br>'
                         ),
                  go.Bar(
                      x=data6['IPL 4 Franchise'],
                      y=data6[col2],
                      name='Sum of '+(col2),
                      text=data6[col2],
                      texttemplate='%{text:.2s}',
                      textposition='auto',
                      marker=dict(color='rgb(112, 123, 124)'),
                      yaxis='y2',
                      offsetgroup=2,
                      hoverinfo='text',
                      hovertext=
                      '<b>Team</b>: ' + data6['IPL 4 Franchise'].astype(str) + '<br>'+
                       '<b>Right y-axis</b>: ' + [f'{x:,.0f}' for x in data6[col2]] + '<br>'
                  )],
                  'layout': go.Layout(
             width=780,
             height=520,
             title={
                'text': 'Total number of ' + (col1) + ' v/s ' + (col2) + ' for every team',
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={'family': 'Oswald',
                        'color': 'rgb(230, 34, 144)',
                        'size': 25},
 
             hovermode='x',
 
             xaxis=dict(title='<b>Team Name</b>',
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='rgb(17, 37, 239)'
                        )
                    ),
 
             yaxis=dict(title='<b>Total ' + col1 + ' in each team </b>',
                        color='rgb(230, 34, 144)',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='rgb(104, 204, 104)',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                           family='Arial',
                           size=12,
                           color='rgb(17, 37, 239)'
                        )
 
                ),
             yaxis2=dict(title='<b>Total ' + col2 + ' in each team </b>', overlaying='y', side='right',
                         color='rgb(230, 34, 144)',
                         showline=True,
                         showgrid=False,
                         showticklabels=True,
                         linecolor='rgb(104, 204, 104)',
                         linewidth=2,
                         ticks='outside',
                         tickfont=dict(
                           family='Arial',
                           size=12,
                           color='rgb(17, 37, 239)'
                         )
                           ),
 
             legend=dict(title='',
                         x=0.25,
                         y=1.08,
                         orientation='h',
                         bgcolor='rgba(255, 255, 255, 0)',
                         traceorder="normal",
                         font=dict(
                              family="sans-serif",
                              size=12,
                              color='#000000')),
 
                         legend_title_font_color="green",
                         uniformtext_minsize=12,
                         uniformtext_mode='hide',
 
                 )
    }

# Create pie chart 1
@app.callback(Output('pie_1', 'figure'),
              [Input('team', 'value')])
def display_content(team):
    retained = ipl_data1.loc[ipl_data1['Retained'] == 0].count()[0]
    notRetained = ipl_data1.loc[ipl_data1['Retained'] == 1].count()[0]
 
    return {
        'data': [go.Pie(labels=['retained', 'notRetained'],
                        values=[retained, notRetained],
                        hoverinfo='label+value+percent',
                        textinfo='label+value',
                        textposition='auto',
                        textfont=dict(size=13),
                        insidetextorientation='radial',
                        rotation=70,
 
                        )],
 
        'layout': go.Layout(
            width=780,
            height=520,
            hovermode='closest',
            title={
                'text': 'Retained or not',
                'y': 0.93,
                'x': 0.43,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={'family': 'Oswald',
                   'color': 'rgb(230, 34, 144)',
                   'size': 25},
            legend={
                'orientation': 'h',
                'bgcolor': 'rgba(255,255,255,0)',
                'xanchor': 'center', 'x': 0.5, 'y': -0.05},
            ),
 
 
        }

# Create pie chart 2
# @app.callback(Output('pie_2', 'figure'),
#               [Input('team', 'value')])
# def display_content(team):
#     data7 = ipl_data1.groupby(['IPL 4 Franchise', 'matches'])['50 runs made'].mean().reset_index()
#     data8 = data7[data7['IPL 4 Franchise']==team]['50 runs made']
#     retained = data8.loc[data8['Retained'] == 0].count()[0]
#     notRetained = data8.loc[data8['Retained'] == 1].count()[0]
 
#     return {
#         'data': [go.Pie(labels=['retained', 'notRetained'],
#                         values=[retained, notRetained],
#                         hoverinfo='label+value+percent',
#                         textinfo='label+value',
#                         textposition='auto',
        #                 textfont=dict(size=13),
        #                 insidetextorientation='radial',
        #                 rotation=70,
 
        #                 )],
 
        # 'layout': go.Layout(
        #     width=780,
        #     height=520,
        #     hovermode='closest',
        #     title={
        #         'text': 'Status of each product',
        #         'y': 0.93,
        #         'x': 0.43,
        #         'xanchor': 'center',
        #         'yanchor': 'top'},
        #     titlefont={'family': 'Oswald',
        #            'color': 'rgb(230, 34, 144)',
        #            'size': 25},
        #     legend={
        #         'orientation': 'h',
        #         'bgcolor': 'rgba(255,255,255,0)',
        #         'xanchor': 'center', 'x': 0.5, 'y': -0.05},
        #     ),
 
 
        # }



if __name__ == '__main__':
    app.run_server(debug=True)
