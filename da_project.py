# -*- coding: utf-8 -*-
"""DA_Project(Draft-1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VyuYp_k4YkdKaZ0nyk_LFzf_4EINK9AP

# __1. Import packages and load data__
"""
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np

path = "Airbnb_Open_Data.csv"
df = pd.read_csv(path)


# create the missingno plot
missing_values_count, ax = plt.subplots(figsize=(12, 12))
msno.bar(df, ax=ax, figsize=(12, 5), sort='ascending')

# extract the bars and their heights
bars = ax.containers[0]
heights = [bar.get_height() for bar in bars]

# create a custom color scale
# create a custom color scale
colors = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1',
          '#6baed6', '#4292c6', '#2171b5', '#084594']
n_colors = len(colors)
color_scale = [colors[int((n_colors-1)*h/max(heights))] for h in heights]

# convert to plotly figure
missing_values_count = go.Figure(go.Bar(
    x=[rect.get_x() + rect.get_width() / 2 for rect in bars],
    y=heights,
    marker_color=color_scale,
    marker_line_width=0
))

# update the layout
missing_values_count.update_layout(
    title='Missing Values Count',
    xaxis_title='',
    yaxis_title='Count',
    width=1200,
    height=700,
    margin=dict(l=0, r=0, t=50, b=0),
    font=dict(family='Arial', size=16, color='#737373'),
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    xaxis=dict(showgrid=True, gridwidth=1,
               gridcolor='white', tickfont=dict(size=14)),
    yaxis=dict(showgrid=True, gridwidth=1,
               gridcolor='white', tickfont=dict(size=14))
)

# show the plot
# fig.show()


def check_missing_value(column: 'str'):
    print(
        f'Percentage of Missing data in \033[1m"{column}"\033[0m is \033[1m{round(df[column].isna().sum()/df[column].shape[0] * 100, 2)} %\033[0m')


for x in df.columns:
    check_missing_value(x)


def check_unique_value(column: 'str'):
    print(f'The \033[1m"{column}"\033[0m has \033[1m{df[column].nunique()}\033[0m unique values out of \033[1m{df[column].shape[0]}\033[0m values')


for x in df.columns:
    check_unique_value(x)

df.drop(['host name', 'license', 'country code',
        'country', 'house_rules'], axis=1, inplace=True)

df.shape


def remove_dollar_sign(value):
    if pd.isna(value):
        return np.NaN
    else:
        x = value.replace("$", "").replace(",", "").replace(" ", "")
        return x


df["price"] = df["price"].apply(lambda x: remove_dollar_sign(x))
df["service fee"] = df["service fee"].apply(lambda x: remove_dollar_sign(x))

df['neighbourhood group'] = df['neighbourhood group'].replace(
    'brookln', 'Brooklyn')
df['neighbourhood group'] = df['neighbourhood group'].replace(
    'manhatan', 'Manhattan')

df['Construction year'] = df['Construction year'].dropna().astype('Int64')

df['instant_bookable'] = df['instant_bookable'].dropna().astype('bool')

min_night_neg_val = df[df['minimum nights'] < 0].count()
min_night_neg_val/df.shape[0] * 100

ava_365_neg_val = df[df['availability 365'] < 0].count()
ava_365_neg_val/df.shape[0] * 100

df['minimum nights'] = abs(df['minimum nights'])
df['availability 365'] = abs(df['availability 365'])

host = df['NAME'].value_counts(ascending=False)
top10 = host.head(10)

top_10_most_given_names_for_accommodation = px.bar(x=top10, y=top10.index, orientation='h', color=top10.values,
                                                   color_continuous_scale=px.colors.sequential.Reds[::-1],
                                                   title='Top 10 most given names for accommodation')

# update the layout
top_10_most_given_names_for_accommodation.update_layout(
    title=dict(font=dict(family='Times New Roman', size=30, color="white")),
    xaxis_title='Count',
    yaxis_title='Names',
    font=dict(family='Arial', size=18, color="white"),
    height=700,
    width=1200,
    margin=dict(l=100, r=100, t=100, b=100),
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    xaxis=dict(showgrid=True, gridwidth=1,
               gridcolor='white', tickfont=dict(size=14)),
    yaxis=dict(showgrid=True, gridwidth=1,
               gridcolor='white', tickfont=dict(size=14))
)


# show the plot
# fig.show()

airbnb_host_verification = go.Figure(go.Bar(
    x=df['host_identity_verified'].value_counts().index,
    y=df['host_identity_verified'].value_counts().values,
    marker_color=['#3182bd', '#9ecae1'],  # set custom colors for the bars
))

# add annotations to the plot
airbnb_host_verification.add_annotation(
    x=0, y=51000,
    text='51,200',
    font=dict(size=16, color="white"),
    showarrow=False
)

airbnb_host_verification.add_annotation(
    x=1, y=51110,
    text='51,110',
    font=dict(size=16, color="white"),
    showarrow=False
)

# update the layout
airbnb_host_verification.update_layout(
    title=dict(text='Airbnb host verification',
               font=dict(size=24, color="white")),
    xaxis=dict(title='', tickfont=dict(
        size=16, color="white"), showgrid=False),
    yaxis=dict(title='Count', tickfont=dict(size=16, color="white"),
               color="white", gridcolor='white'),
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    width=1200,
    height=700,
    margin=dict(l=0, r=0, t=100, b=0),
)

# show the plot
# fig.show()

# pip install ipywidgets

neighborhood_counts = df['neighbourhood group'].value_counts().reset_index()
neighborhood_counts.columns = ['Neighborhood Group', 'Count']

# create the bar chart
count_of_nyc_airbnb_accommodation_by_neighborhood_group = px.bar(
    neighborhood_counts,
    x='Neighborhood Group',
    y='Count',
    color='Neighborhood Group',
    color_discrete_sequence=px.colors.sequential.Reds[::-1],
    title='Count of NYC Airbnb accommodation by neighborhood group'
)

# create the pie chart
percentage_of_nyc_airbnb_accommodation_by_neighborhood_group = px.pie(
    neighborhood_counts,
    values='Count',
    names='Neighborhood Group',
    title='Percentage of NYC Airbnb accommodation by neighborhood group',
    color_discrete_sequence=px.colors.sequential.Reds[::-1]
)

# update the layout
count_of_nyc_airbnb_accommodation_by_neighborhood_group.update_layout(
    xaxis_title='Neighborhood Group',
    yaxis_title='Count',
    showlegend=False,
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    width=1200,
    height=700,
    margin=dict(l=20, r=20, t=100, b=20),
    # Update x-axis title font color to white
    xaxis_title_font=dict(color='white'),
    yaxis_title_font=dict(color='white'),
    title=dict(
        font=dict(
            color='white'
        )
    ),
    xaxis=dict(
        tickfont=dict(
            color='white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white'
        )
    )
)


percentage_of_nyc_airbnb_accommodation_by_neighborhood_group.update_layout(
    showlegend=False,
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    width=1200,
    height=700,
    margin=dict(l=20, r=20, t=100, b=20),
    title=dict(
        font=dict(
            color='white'
        )
    ),
    xaxis=dict(
        tickfont=dict(
            color='white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white'
        )
    )
)

# display the figures
# fig1.show()
# fig2.show()


room_order = df.groupby('room type')['id'].count(
).sort_values(ascending=False).index
piedata2 = df.groupby('room type')['id'].count()

ny_airbnb_accommodation_by_room_type = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]], subplot_titles=(
    'Count of NY Airbnb accommodation by room type', 'Percentage of NYC Airbnb accommodation by room type'))

ny_airbnb_accommodation_by_room_type.add_trace(
    go.Bar(x=df['room type'], y=df['id'],
           marker_color='cornflowerblue', name='Room type count'),
    row=1, col=1
)
ny_airbnb_accommodation_by_room_type.update_yaxes(type="log")

ny_airbnb_accommodation_by_room_type.add_trace(
    go.Pie(labels=piedata2.index, values=piedata2.values,
           name='Room type percentage'),
    row=1, col=2
)

ny_airbnb_accommodation_by_room_type.update_layout(
    # title='NY Airbnb Accommodation by Room Type',
    height=700,
    width=1200,
    plot_bgcolor='#000000',
    paper_bgcolor='#000000',
    showlegend=True,
    legend=dict(orientation="h", xanchor="center", yanchor="bottom", x=0.5),
    # yaxis_title="Count",
     title=dict(
        font=dict(
            color='white'
        )
    ),
    xaxis=dict(
        tickfont=dict(
            color='white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white'
        )
    )
)

# fig.show()

# Create a line plot with Plotly

# Assuming 'df' is your DataFrame containing the data
# Set the style to dark background
plt.style.use('dark_background')

# Group by construction year and count the number of listings
df_grouped = df.groupby('Construction year')['id'].count().reset_index()

# Create a Plotly figure
construction_years_of_airbnb_accommodations = go.Figure()

# Add a line trace to the figure
construction_years_of_airbnb_accommodations.add_trace(
    go.Scatter(
        x=df_grouped['Construction year'],
        y=df_grouped['id'],
        mode='lines',
        line=dict(color='yellow'),  # Set line color to yellow
        name='Number of Listings'
    )
)

# Update the figure layout
construction_years_of_airbnb_accommodations.update_layout(
    title='Construction Years of Airbnb Accommodations',  # Set title
    xaxis=dict(
        title='Construction Year',  # Set x-axis title
        gridcolor='red',  # Set x-axis grid color
        showgrid=True,  # Show x-axis grid
        tickfont=dict(color='white'),  # Set x-axis tick font color
    ),
    yaxis=dict(
        title='Number of Listings',  # Set y-axis title
        gridcolor='red',  # Set y-axis grid color
        showgrid=True,  # Show y-axis grid
        tickfont=dict(color='white')  # Set y-axis tick font color
    ),
    paper_bgcolor='black',  # Set plot background color
    plot_bgcolor='black',  # Set plot background color
    font=dict(color='white'),  # Set font color
    showlegend=False,  # Hide legend
    height=700, width=1200
)


policy = df.groupby('cancellation_policy')['id'].count()
labels = policy.index.tolist()
values = policy.values.tolist()

cancellation_policy_strictness_by_percentage = go.Figure(
    data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

cancellation_policy_strictness_by_percentage.update_layout(
    title='Cancellation policy strictness by percentage',
    font=dict(color='white'),
    paper_bgcolor='black',
    plot_bgcolor='black',
    height=700, width=1200
)

cancellation_policy_strictness_by_percentage.update_traces(
    marker=dict(colors=['#08306b', '#2171b5', '#6baed6', '#bdd7e7']),
    textfont=dict(color='white')
)

# fig.show()

df['minimum nights'].mean()

# Remove outliers in the 'min_nights' column
# Calculate IQR
Q1 = df['minimum nights'].quantile(0.25)
Q3 = df['minimum nights'].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

# Remove outliers
df_no_ouliers = df[(df['minimum nights'] > lower_bound) &
                   (df['minimum nights'] < upper_bound)]

relation_between_minimum_of_nights_and_number_of_reviews = px.scatter(df_no_ouliers, x='minimum nights', y='number of reviews',
                                                                      title='Relation between Minimum of nights and number of Reviews',
                                                                      labels={'minimum nights': 'Minimum nights', 'number of reviews': 'Number of reviews'}, height=700, width=1200)
relation_between_minimum_of_nights_and_number_of_reviews.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    xaxis=dict(gridcolor='gray'),
    yaxis=dict(gridcolor='gray')
)


color_scale = px.colors.sequential.Reds[::-1]

distribution_of_availability_365 = px.histogram(df, x='availability 365', nbins=45, range_x=(0, 450),
                                                labels={
                                                    'availability 365': 'Availability 365'},
                                                title='Distribution of Availability 365', height=700, width=1200)

distribution_of_availability_365.update_layout(
    xaxis={'categoryorder': 'array', 'categoryarray': sorted(df['availability 365'].unique())})
distribution_of_availability_365.update_traces(marker_color=color_scale)
distribution_of_availability_365.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='white')
distribution_of_availability_365.update_layout(hovermode='x', bargap=0.2)
distribution_of_availability_365.update_traces(xbins=dict(  # bins used for histogram
    start=0.0,
    #         end=600.0,
    size=50
))

# fig.show()

distribution_of_accommodation_price = px.histogram(df, x='price', nbins=12, range_x=(0, 1200),
                                                   labels={
                                                       'price': 'Price', 'count': 'Number of listings'},
                                                   title='Distribution of Accommodation price',
                                                   opacity=0.7, color_discrete_sequence=['#636EFA'], height=700, width=1200)
distribution_of_accommodation_price.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='white')
distribution_of_accommodation_price.add_annotation(x=30, y=15, text='Each bin corresponds to $100', font=dict(color='white', size=14),
                                                   showarrow=False, xref='paper', yref='paper')
distribution_of_accommodation_price.update_xaxes(title_font=dict(
    size=16, color='white'), tickfont=dict(size=14, color='white'))
distribution_of_accommodation_price.update_yaxes(title_font=dict(
    size=16, color='white'), tickfont=dict(size=14, color='white'))
distribution_of_accommodation_price.update_layout(bargap=0.2)
# fig.show()

distribution_of_service_fee = px.histogram(df, x='service fee', nbins=10, range_x=(0, 250),
                                           labels={
                                               'service fee': 'Service fee', 'count': 'Number of listings'},
                                           title='Distribution of Service fee',
                                           opacity=0.7, color_discrete_sequence=['#EF553B'], height=700, width=1200)
distribution_of_service_fee.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='white')
distribution_of_service_fee.add_annotation(x=750, y=15, text='Each bin corresponds to $25', font=dict(color='white', size=14),
                                           showarrow=False, xref='paper', yref='paper')
distribution_of_service_fee.update_xaxes(title_font=dict(
    size=16, color='white'), tickfont=dict(size=14, color='white'))
distribution_of_service_fee.update_yaxes(title_font=dict(
    size=16, color='white'), tickfont=dict(size=14, color='white'))
distribution_of_service_fee.update_layout(bargap=0.2)

df['price'] = df['price'].astype('float')

distribution_of_price_by_nyc_borough = px.box(df, x='price', y='neighbourhood group', color='neighbourhood group',
                                              title='Distribution of Price by NYC borough', height=700, width=1200)
distribution_of_price_by_nyc_borough.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='orange')
distribution_of_price_by_nyc_borough.update_yaxes(title='Neighbourhood group')
distribution_of_price_by_nyc_borough.update_xaxes(title='Price')

distribution_of_price_by_host_verification_status = px.box(df, x='price', y='host_identity_verified', color='host_identity_verified',
                                                           title='Distrbution of Price by Host verification status', height=700, width=1200)
distribution_of_price_by_host_verification_status.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='orange')
distribution_of_price_by_host_verification_status.update_yaxes(
    title='Host verification status')
distribution_of_price_by_host_verification_status.update_xaxes(title='Price')
# price_hostverif_fig.show()


relation_between_minimum_of_nights_and_price = px.scatter(df, x='minimum nights', y='price', color='neighbourhood group',
                                                          title='Relation between Minimum of nights and price',
                                                          labels={'min_nights': 'Minimum nights', 'price': 'Price',
                                                                  'neighbourhood group': 'Neighbourhood Group'},
                                                          range_x=[0, 30], range_y=[0, 1500],
                                                          template='plotly_dark', height=700, width=1200)
relation_between_minimum_of_nights_and_price.update_traces(
    marker_size=5, opacity=0.7)
# fig.show()
color_scale = px.colors.sequential.Reds[::-1]
relationship_between_price_and_service_fee = px.scatter(df, x='price', y='service fee', color='neighbourhood group',
                                                        labels={
                                                            'price': 'Price', 'service fee': 'Service fee', 'neighbourhood group': 'Neighbourhood Group'},
                                                        title='Relationship between Price and Service Fee', height=700, width=1200, color_discrete_sequence=color_scale)

relationship_between_price_and_service_fee.update_traces(
    marker=dict(size=3, color='#636EFA', opacity=0.7))
relationship_between_price_and_service_fee.update_layout(
    plot_bgcolor='black', paper_bgcolor='black', font_color='white')
# fig.show()