import os
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Configuration
n_rows = 1600
output_dir = r"C:\Users\suman\Downloads\shadowfox"
output_file = os.path.join(output_dir, "tableau_sales_export_dirty.csv")

# Create directories if they don't exist
os.makedirs(output_dir, exist_ok=True)

# 1. Base clean lists
categories = ['Technology', 'Office Supplies', 'Furniture']
sub_categories = {
    'Technology': ['Laptops', 'Phones', 'Accessories'],
    'Office Supplies': ['Binders', 'Paper', 'Storage'],
    'Furniture': ['Chairs', 'Tables', 'Bookcases']
}
regions = ['North', 'South', 'East', 'West']

# Generate transactional data
txn_ids = []
dates = []
cats = []
subcats = []
regs = []
gross_sales_list = []
discounts = []
net_sales_list = []
mfg_costs_list = []
freight_costs_list = []
cogs_list = []
reported_profits = []

start_date = pd.to_datetime('2022-07-01')
end_date = pd.to_datetime('2025-06-30')
date_range = (end_date - start_date).days

for i in range(n_rows):
    # ID
    txn_ids.append(f"TXN-{2022 + (i % 4)}-{10000 + i}")
    
    # Date
    random_days = np.random.randint(0, date_range)
    date_val = start_date + pd.to_timedelta(random_days, unit='D')
    dates.append(date_val.strftime('%Y-%m-%d'))
    
    # Category / Subcategory
    cat = np.random.choice(categories)
    subcat = np.random.choice(sub_categories[cat])
    cats.append(cat)
    subcats.append(subcat)
    
    # Region
    regs.append(np.random.choice(regions))
    
    # Financial Base Calculations
    # Higher sales for Technology, lower for Office Supplies
    if cat == 'Technology':
        base_gross = np.random.uniform(500, 5000)
    elif cat == 'Furniture':
        base_gross = np.random.uniform(200, 3000)
    else:
        base_gross = np.random.uniform(10, 800)
        
    discount = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], p=[0.5, 0.2, 0.15, 0.1, 0.05])
    net_sales = base_gross * (1 - discount)
    
    # Mfg cost is 40-70% of gross
    mfg_cost = base_gross * np.random.uniform(0.40, 0.70)
    # Freight cost is 5-15% of gross
    freight_cost = base_gross * np.random.uniform(0.05, 0.15)
    # COGS = Mfg Cost + some standard overhead (e.g. 5% of gross)
    cogs = mfg_cost + (base_gross * 0.05)
    # Profit = Net Sales - COGS - Freight
    profit = net_sales - cogs - freight_cost
    
    gross_sales_list.append(base_gross)
    discounts.append(f"{int(discount*100)}%")
    net_sales_list.append(net_sales)
    mfg_costs_list.append(mfg_cost)
    freight_costs_list.append(freight_cost)
    cogs_list.append(cogs)
    reported_profits.append(profit)

# Convert to DataFrame
df = pd.DataFrame({
    'Transaction_ID': txn_ids,
    'Date': dates,
    'Product_Category': cats,
    'Sub_Category': subcats,
    'Region': regs,
    'Gross_Sales': gross_sales_list,
    'Discount_Rate': discounts,
    'Net_Sales': net_sales_list,
    'Manufacturing_Cost': mfg_costs_list,
    'Freight_Cost': freight_costs_list,
    'COGS': cogs_list,
    'Reported_Profit': reported_profits
})

# 2. INJECT NOISE AND FAULTY DATA
# A. Duplicates (around 30 duplicates)
dup_indices = np.random.choice(range(n_rows), size=30, replace=False)
dup_rows = df.iloc[dup_indices].copy()
# Shift dates or keep exactly same
df = pd.concat([df, dup_rows], ignore_index=True)

# Update row count
curr_rows = df.shape[0]

# B. Missing/NaN values (scattered across columns)
for _ in range(40):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Transaction_ID'] = None

for _ in range(50):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Date'] = np.random.choice([None, '', 'NaN', 'N/A', 'TBD'])

for _ in range(45):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Product_Category'] = np.random.choice([None, 'NULL', ''])

for _ in range(40):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Gross_Sales'] = np.random.choice([None, 'NaN', 'N/A'])
    
for _ in range(30):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Manufacturing_Cost'] = np.random.choice([None, 'NULL'])

for _ in range(30):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'Freight_Cost'] = np.random.choice([None, 'TBD'])

for _ in range(50):
    idx = np.random.randint(0, curr_rows)
    df.at[idx, 'COGS'] = np.random.choice([None, 'NaN'])

# C. Formatting Inconsistencies
# Currency string formatting with symbols, spaces, and commas
for idx in range(curr_rows):
    # Gross Sales formatting (if not null)
    g_val = df.at[idx, 'Gross_Sales']
    if pd.notna(g_val) and g_val not in ['NaN', 'N/A']:
        if np.random.rand() < 0.85: # 85% formatted as string
            df.at[idx, 'Gross_Sales'] = f"$ {float(g_val):,.2f}"
            
    # Net Sales formatting
    n_val = df.at[idx, 'Net_Sales']
    if pd.notna(n_val):
        if np.random.rand() < 0.85:
            df.at[idx, 'Net_Sales'] = f"${float(n_val):,.2f}"
            
    # Manufacturing Cost
    m_val = df.at[idx, 'Manufacturing_Cost']
    if pd.notna(m_val) and m_val not in ['NULL']:
        if np.random.rand() < 0.80:
            df.at[idx, 'Manufacturing_Cost'] = f"${float(m_val):,.2f}"

    # Freight Cost
    f_val = df.at[idx, 'Freight_Cost']
    if pd.notna(f_val) and f_val not in ['TBD']:
        if np.random.rand() < 0.80:
            df.at[idx, 'Freight_Cost'] = f"${float(f_val):,.2f}"

    # COGS
    c_val = df.at[idx, 'COGS']
    if pd.notna(c_val) and c_val not in ['NaN']:
        if np.random.rand() < 0.80:
            df.at[idx, 'COGS'] = f"$ {float(c_val):,.2f}"

    # Reported Profit
    p_val = df.at[idx, 'Reported_Profit']
    if pd.notna(p_val):
        if np.random.rand() < 0.85:
            df.at[idx, 'Reported_Profit'] = f"${float(p_val):,.2f}"

# Date Inconsistency (some MM/DD/YYYY, some DD-MM-YYYY, some corrupt years, some TBD)
for idx in range(curr_rows):
    d_val = df.at[idx, 'Date']
    if pd.notna(d_val) and d_val not in ['', 'NaN', 'N/A', 'TBD']:
        r = np.random.rand()
        dt = pd.to_datetime(d_val)
        if r < 0.15:
            df.at[idx, 'Date'] = dt.strftime('%m/%d/%Y')
        elif r < 0.25:
            df.at[idx, 'Date'] = dt.strftime('%d-%m-%Y')
        elif r < 0.28:
            # Corrupt dates (extra zero or typo)
            df.at[idx, 'Date'] = dt.strftime('202%d-0%m-%d') # e.g. 20228-005-12
        elif r < 0.30:
            # Out of bounds date (future/past)
            df.at[idx, 'Date'] = dt.strftime('1900-%m-%d') if np.random.rand() < 0.5 else dt.strftime('2045-%m-%d')

# D. Text Inconsistency and Typos (Product_Category, Region)
pc_typos = {
    'Technology': ['technology', 'Tech', 'TECHNOLOGY', 'Tehnology'],
    'Office Supplies': ['Office_Supplies', 'office supplies', 'Office Supp.', 'Officesupplies'],
    'Furniture': ['furniture', 'Furnitures', 'Furnitur', 'FURNITURE']
}
reg_typos = {
    'North': ['north', 'N.', 'NORTH'],
    'South': ['south', 'S.', 'SOUTH'],
    'East': ['east', 'E.', 'EAST', 'EST'],
    'West': ['west', 'W.', 'WEST']
}

for idx in range(curr_rows):
    cat_val = df.at[idx, 'Product_Category']
    if pd.notna(cat_val) and cat_val not in ['', 'NULL']:
        if np.random.rand() < 0.15: # 15% typo
            df.at[idx, 'Product_Category'] = np.random.choice(pc_typos[cat_val])
            
    reg_val = df.at[idx, 'Region']
    if pd.notna(reg_val):
        if np.random.rand() < 0.15:
            df.at[idx, 'Region'] = np.random.choice(reg_typos[reg_val])

# E. Out-of-Bounds and Mathematical Errors (Outliers, negatives, math errors)
# Negative Gross Sales
neg_sales_indices = np.random.choice(range(curr_rows), size=15, replace=False)
for idx in neg_sales_indices:
    df.at[idx, 'Gross_Sales'] = "-$ 350.00"

# Outliers
outlier_indices = np.random.choice(range(curr_rows), size=8, replace=False)
for idx in outlier_indices:
    df.at[idx, 'Gross_Sales'] = "$ 6,500,000.00" # Typing error, way too high!
    df.at[idx, 'Net_Sales'] = "$ 6,500,000.00"

# Mathematical mismatch: Reported_Profit != Net_Sales - COGS - Freight
math_error_indices = np.random.choice(range(curr_rows), size=40, replace=False)
for idx in math_error_indices:
    df.at[idx, 'Reported_Profit'] = "$ 99,999.00" # Mismatched profit value

# F. Bad transaction IDs
for idx in range(curr_rows):
    txn_id = df.at[idx, 'Transaction_ID']
    if pd.notna(txn_id):
        r = np.random.rand()
        if r < 0.05:
            df.at[idx, 'Transaction_ID'] = txn_id.lower() # lowercase txn
        elif r < 0.08:
            df.at[idx, 'Transaction_ID'] = txn_id.replace("TXN-", "") # missing prefix

# Export dirty dataset
df.to_csv(output_file, index=False)
print(f"Generated {df.shape[0]} rows of noisy sales data at: {output_file}")
