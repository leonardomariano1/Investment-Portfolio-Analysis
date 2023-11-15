# Investment Portfolio Analysis

This project involves organizing and analyzing investment data to assess the adherence of accounts to an investment policy. The data is stored in PostgreSQL, and the goal is to calculate Euclidean Distance as a metric for portfolio adherence.

## Table of Contents
- [Streamlit Dashboard](#streamlit-dashboard)
- [Database Schema](#database-schema)
- [Data Source](#data-source)
- [Data Transformation](#data-transformation)
- [Calculation of Euclidean Distance](#calculation-of-euclidean-distance)
- [Results](#results)
- [Visualization](#visualization)
- [Usage](#usage)

## Streamlit Dashboard

In addition to the data analysis and transformation, this project includes a user-friendly Streamlit dashboard for interactive exploration of the investment portfolio. The dashboard provides key insights and visualizations, making it easier for stakeholders to understand the data.

## Streamlit Dashboard Features

1. **Custom Styling with CSS**: The dashboard features custom styling with CSS to enhance the visual appeal and create a cohesive design. The main content area is padded for better readability.

2. **Title and Description**: The dashboard opens with a clear title, "Investment Portfolio Analysis," and a sidebar that credits the developer.

3. **Filtering Data**: Users can dynamically filter the data based on account suitability using a select box in the sidebar. The default selection is set to 'Agressivo.'

4. **Top 10 Position Values by Asset**: A horizontal bar chart showcases the top 10 position values by asset, providing a quick overview of the most significant investments.

5. **Class Distribution Pie Chart**: A pie chart visually represents the distribution of asset classes, with distinct colors for each class (Equity, Fixed Income, Cash).

6. **Asset Classes with the Most Disrespected Policy**: A table displays the average Euclidean Distance for each asset class, helping identify classes where the actual allocation deviates significantly from the ideal allocation.

7. **Correlation Heatmap**: A heatmap reveals the correlation between numeric columns, aiding in understanding relationships between different variables in the dataset.

8. **Dataset Summary**: The sidebar includes a summary of the dataset, providing key statistics for quick reference.

## Usage Instructions

1. **Access the Dashboard**: To access the Streamlit dashboard, visit [https://investment-portfolio-analysis.streamlit.app/](https://investment-portfolio-analysis.streamlit.app/).

2. **Filter Data**: Use the select box in the sidebar to filter data based on account suitability.

3. **Explore Visualizations**: Interact with visualizations, such as the top 10 position values, class distribution pie chart, and correlation heatmap.

4. **Gain Insights**: Leverage the dashboard to gain insights into the investment portfolio, identify trends, and explore correlations.

Feel free to explore and analyze the data interactively using the Streamlit dashboard!


## Database Schema
![Database Schema](Untitled%20(1).png)

### Tables
1. **accounts**
   - account_code (Primary Key)
   - account_suitability

2. **assets**
   - asset_id (Primary Key)
   - asset_name
   - asset_cnpj
   - class_name

3. **positions**
   - position_id (Primary Key)
   - account_code (Foreign Key references accounts.account_code)
   - asset_id (Foreign Key references assets.asset_id)
   - position_value

4. **classes**
   - class_id (Primary Key)
   - class_name

5. **allocation_policies**
   - policy_id (Primary Key)
   - class_id (Foreign Key references classes.class_id)
   - account_suitability (Foreign Key references accounts.account_suitability)
   - percentage

6. **combined_data**
   - account_code (Foreign Key references accounts.account_code)
   - account_suitability (Foreign Key references accounts.account_suitability)
   - position_id (Foreign Key references positions.position_id)
   - asset_id (Foreign Key references assets.asset_id)
   - position_value
   - asset_name
   - asset_cnpj
   - class_name
   - class_id (Foreign Key references classes.class_id)
   - policy_id (Foreign Key references allocation_policies.policy_id)
   - percentage
   - euclidean_distance

7. **euclidean_distance_results**
   - account_code (Primary Key, Foreign Key references accounts.account_code)
   - euclidean_distance

## Data Source

The data for this project is sourced from the PostgreSQL tables: `accounts`, `assets`, `positions`, `classes`, `allocation_policies`, `combined_data`, and `euclidean_distance_results`.

## Data Transformation

### 1. Normalization
The data underwent normalization to adhere to the Third Normal Form (3NF) principles, ensuring efficient data storage and reducing redundancy.

### 2. Query Execution
SQL queries were executed to join and transform the data, creating the `combined_data` table. The query brought together information from `accounts`, `assets`, `positions`, `classes`, and `allocation_policies`.

### 3. Euclidean Distance Calculation
The Euclidean Distance, a metric for portfolio adherence, was calculated for each account based on the percentage distribution in the `combined_data` table.

## Calculation of Euclidean Distance

The Euclidean Distance was calculated using the following formula:

\[ \text{Euclidean Distance} = \sqrt{\sum_{i=1}^{n} (X_i - Y_i)^2} \]

Where:
- \(X_i\) is the ideal percentage allocation based on the investment policy.
- \(Y_i\) is the actual percentage allocation from the `combined_data` table.

The calculation provides a measure of how closely the actual portfolio allocation aligns with the ideal allocation.

## Results

The results of the Euclidean Distance calculations are stored in the `euclidean_distance_results` table, providing insights into the adherence of each account to the investment policy.

## Visualization

The database schema and relationships can be visualized using the dbdiagram.io tool. The schema includes tables such as `accounts`, `assets`, `positions`, `classes`, `allocation_policies`, `combined_data`, and `euclidean_distance`.

## Usage

1. **Data Import**: Ensure that the PostgreSQL database contains the necessary tables with the provided schema.
2. **SQL Script Execution**: Run the SQL scripts to transform the data, calculate Euclidean Distance, and store the results.
3. **Visualization**: Utilize dbdiagram.io to visualize the database schema.
4. **Analysis**: Explore the `euclidean_distance_results` table for insights into account adherence to the investment policy.
