-- Insert data into accounts table
INSERT INTO accounts (account_code, account_suitability)
SELECT DISTINCT account_code, account_suitability FROM fake_position;

-- Insert data into assets table
INSERT INTO assets (asset_name, asset_cnpj, class_name)
SELECT DISTINCT asset_name, asset_cnpj, class_name FROM fake_position;

-- Insert data into positions table
INSERT INTO positions (account_code, asset_id, position_value)
SELECT DISTINCT account_code, asset_id, position_value FROM fake_position
JOIN assets ON fake_position.asset_name = assets.asset_name;

-- Insert data into classes table
INSERT INTO classes (class_name)
SELECT DISTINCT class_name FROM assets;

-- Insert data into allocation_policies table
INSERT INTO allocation_policies (class_id, account_suitability, percentage)
SELECT
    c.class_id,
    fap.account_suitability,
    CASE
        WHEN fap.Classe = 'Renda Fixa Pós-Fixada' THEN fap."Moderado Conservador"
        WHEN fap.Classe = 'Renda Fixa Inflação' THEN fap.Moderado
        WHEN fap.Classe = 'Renda Fixa Pré-Fixada' THEN fap.Moderado Agressivo
        WHEN fap.Classe = 'Renda Variável' THEN fap.Agressivo
        WHEN fap.Classe = 'Multimercado' THEN fap.Conservador
        WHEN fap.Classe = 'Alternativos' THEN 0
        WHEN fap.Classe = 'Internacional' THEN fap.Agressivo
        WHEN fap.Classe = 'Saldo em Conta' THEN 0
        ELSE 0
    END AS percentage
FROM fake_allocation_policies fap
JOIN classes c ON fap.Classe = c.class_name;
