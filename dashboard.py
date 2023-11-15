import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# GitHub raw file URL
github_raw_url = 'https://raw.githubusercontent.com/leonardomariano1/Investment-Portfolio-Analysis/main/combined_data.csv'

# Read data from GitHub
df_data = pd.read_csv(github_raw_url)

# Set page configuration
st.set_page_config(
    page_title='Investment Portfolio Analysis',
    layout='wide'
)

# Custom styling with CSS
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom right, #2d4059, #4098d7);
            color: white;
        }
        .sidebar .sidebar-content a {
            color: #f2a365;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title('Investment Portfolio Analysis')
st.sidebar.markdown('Desenvolvido por [Leonardo M. Santos](https://github.com/leonardomariano1/Investment-Portfolio-Analysis/tree/main)')
# Filter data based on user input
selected_suitability = st.sidebar.selectbox('Select Account Suitability:', df_data['account_suitability'].unique(), index=1)
filtered_data = df_data[df_data['account_suitability'] == selected_suitability]

# Show a horizontal bar chart of position values with a color scale
st.subheader('Top 10 Position Values by Asset')
top_10_position_values = filtered_data.nlargest(10, 'position_value')
fig_position_values = px.bar(
    top_10_position_values,
    y='position_value',
    x='asset_name',
    title='Top 10 Position Values by Asset',
    labels={'position_value': 'Position Value (Numeric)'},
    color='position_value',
    color_continuous_scale='blues',
)
fig_position_values.update_layout(
    xaxis_title='Asset Name',
    yaxis_title='Position Value (Numeric)',
    coloraxis_colorbar_title='Position Value',
    height=800,  # Adjust the figure height as needed
)
st.plotly_chart(fig_position_values, use_container_width=True)

# Show a pie chart of class distribution
st.subheader('Class Distribution')
fig_pie = px.pie(
    filtered_data,
    names='class_name',
    title='Class Distribution',
    color='class_name',
    color_discrete_map={'Equity': '#2a9d8f', 'Fixed Income': '#e76f51', 'Cash': '#264653'},
)
st.plotly_chart(fig_pie, use_container_width=True)

# Calculate average Euclidean Distance for each asset class
avg_distance_by_class = filtered_data.groupby('class_name')['euclidean_distance'].mean().reset_index()
avg_distance_by_class = avg_distance_by_class.sort_values(by='euclidean_distance', ascending=False)

# Show the asset classes with the most disrespected policy
st.subheader('Asset Classes with the Most Disrespected Policy:')
st.write(avg_distance_by_class)

# Correlation heatmap (excluding non-numeric columns)
st.subheader('Correlation Heatmap')
numeric_columns = filtered_data.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = filtered_data[numeric_columns].corr()
fig_corr = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='blues',
))
st.plotly_chart(fig_corr, use_container_width=True)

# Display a summary of the dataset at the end
st.sidebar.subheader('Dataset Summary:')
st.sidebar.write(df_data.describe())
