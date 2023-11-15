-- Table 1: Accounts
CREATE TABLE accounts (
    account_code INT PRIMARY KEY,
    account_suitability VARCHAR(255)
);

-- Table 2: Assets
CREATE TABLE assets (
    asset_id SERIAL PRIMARY KEY,
    asset_name VARCHAR(255),
    asset_cnpj VARCHAR(255),
    class_name VARCHAR(255)
);

-- Table 3: Positions
CREATE TABLE positions (
    position_id SERIAL PRIMARY KEY,
    account_code INT,
    asset_id INT,
    position_value NUMERIC,
    FOREIGN KEY (account_code) REFERENCES accounts (account_code),
    FOREIGN KEY (asset_id) REFERENCES assets (asset_id)
);

-- Table 4: Classes
CREATE TABLE classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(255)
);

-- Table 5: Allocation Policies
CREATE TABLE allocation_policies (
    policy_id SERIAL PRIMARY KEY,
    class_id INT,
    account_suitability VARCHAR(255),
    percentage NUMERIC,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
);
