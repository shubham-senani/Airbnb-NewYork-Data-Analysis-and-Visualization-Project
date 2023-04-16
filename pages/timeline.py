from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navbar
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/timeline', title="Data Analysis and Visualization",
                   description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={"position": "fixed", "width": "100%"}),

    html.Div([
        html.H1("January 22, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Dataset selection: The team meets to decide on the dataset to be used for the Airbnb data analysis. After reviewing multiple options, the team selects the NYC Airbnb dataset, which includes information about accommodations, hosts, prices, and reviews", style={
               "color": "#d46565"})

    ], style={"padding-top": "80px", "margin-inline": "50px"}),

    html.Div([
        html.H1("January 23 - 25, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Data cleaning and preprocessing: The team starts cleaning and preprocessing the Airbnb dataset. This involves removing irrelevant columns, handling missing values, and standardizing data formats.", style={
               "color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("January 26 - 28, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Exploratory data analysis: The team conducts exploratory data analysis (EDA) to gain insights into the dataset. They create various visualizations, including Graph-1: Top 10 most given names for accommodation, Graph-2: Airbnb host verification, Graph-3: Percentage of NYC Airbnb accommodation by room type, and Graph-4: Distribution of NYC Airbnb accommodation.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("January 29 - 31, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Further data analysis: The team continues with data analysis, creating additional visualizations, including Graph-5: Construction years of Airbnb accommodations, Graph-6: Cancellation policy strictness by percentage, Graph-7: Relationship between Minimum of nights and number of Reviews, and Graph-8: The availability in 365 days.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("February 1 - 5, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Website development: The team starts developing a website for visualizations of the graphs. They design the website layout, create interactive visualizations using data visualization libraries such as Matplotlib and Seaborn, and implement the website using web development technologies such as HTML, CSS, and JavaScript.", style={
               "color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("February 6 - 12, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Review and refinement: The team reviews and refines the data analysis, visualizations, and the website. They make necessary adjustments and improvements based on feedback from team members and stakeholders.", style={
               "color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("February 13 - 18, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Finalization: The team finalizes the data analysis, visualizations, and the website. They ensure that all the visualizations are accurate and visually appealing, and that the website is user-friendly and functional.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("February 19 - 23, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Team meetings and coordination: The team holds regular meetings to discuss progress, resolve any issues, and coordinate efforts for the final presentation.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("February 24 - March 31, 2023:",
                style={"color": "rgb(139 54 54)"}),
        html.P("Presentation preparation: The team prepares for the final presentation, which includes summarizing the findings, creating a presentation deck, and rehearsing the presentation.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

    html.Div([
        html.H1("April 1 - 2, 2023:", style={"color": "rgb(139 54 54)"}),
        html.P("Final presentation: The team presents their Airbnb data analysis and visualizations to stakeholders, showcasing the insights and findings from the analysis, as well as demonstrating the website with interactive visualizations.",
               style={"color": "#d46565"})

    ], style={"padding-top": "80px", "margin": "50px"}),

], style={"padding": "0px", "margin": "0px", "width": "100vw", "background": "linear-gradient(180deg, rgba(238,157,154,1) 10%, rgba(250,250,250,1) 38%)"})
