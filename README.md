# Investment Portfolio Analysis

This project involves organizing and analyzing investment data to assess the adherence of accounts to an investment policy. The data is stored in PostgreSQL, and the goal is to calculate Euclidean Distance as a metric for portfolio adherence.

## Table of Contents
- [Database Schema](#database-schema)
- [Data Source](#data-source)
- [Data Transformation](#data-transformation)
- [Calculation of Euclidean Distance](#calculation-of-euclidean-distance)
- [Results](#results)
- [Visualization](#visualization)
- [Usage](#usage)

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
