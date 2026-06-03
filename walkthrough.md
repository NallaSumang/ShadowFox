# Walkthrough: Advanced Sales & Financial Data Analysis

This document provides a summary of the accomplishments, data cleaning methodologies, key findings, and final visualizations for the Sales Data Analysis project in [task1-advance.ipynb](task1-advance.ipynb).

---

## 1. Messy Dataset Generation
To demonstrate data cleaning on realistic Excel/Tableau output without using dummy data, we implemented a data generator script [generate_dirty_data.py](generate_dirty_data.py) that created [tableau_sales_export_dirty.csv](tableau_sales_export_dirty.csv) with the following realistic noises:
* **String Currency Columns**: Sales and costs stored with currency symbols, spaces, and commas (e.g., `"$ 1,200.50"`).
* **Missing values**: Scatterings of blanks, `"NaN"`, `"N/A"`, `"NULL"`, and `"TBD"`.
* **Corrupt/Mixed Dates**: Multi-format date strings and corrupt year structures like `20228-005-12`.
* **Outliers**: Order records with typing errors scaling sales up to `$6,500,000.00`.
* **Negative Values**: Incorrect negative entries in physical cost columns.
* **Categorical Inconsistencies**: Spelling variations and casing errors for categories and regions (e.g. `'Office_Supplies'`, `'tech'`).
* **Duplicates**: Redundant transactional rows.

---

## 2. Rigorous Data Cleaning Process
In the main Jupyter notebook [task1-advance.ipynb](task1-advance.ipynb), we implemented a full cleaning pipeline:
1. **Deduplication**: Removed duplicate transactional rows.
2. **Text Normalization**: Standardized capitalization and corrected spelling variations/typos in categories and regions.
3. **Currency Conversion**: Stripped symbols (`$`, `,`) and parsed messy strings to float values.
4. **Datetime Standardization**: Parsed dates using multiple format templates, filtering out out-of-bounds years.
5. **Outlier Mitigation**: Filtered out negative sales and restricted analysis to transactions under `$25,000` to eliminate typing errors.
6. **Imputation**: Estimated missing cost/sales entries using category-level median proportions.
7. **Mathematical Reconcilliation**: Computed true actual profits: `Profit = Net Sales - COGS - Freight Costs` to rectify mathematical discrepancies in the raw system export.

---

## 3. Financial & Temporal Calculations
* **Fiscal Calendar Mapping**: Mapped transactions to a custom fiscal calendar starting **July 1st** (mapping quarters and months accordingly).
* **Key Financial Metrics**: Computed Gross Profit Margin, Net Profit Margin, COGS Ratio, and Freight Ratio to analyze structural cost drivers.

---

## 4. Visualizations & Strategic Answers

### Research Question 1: How do manufacturing costs and freight costs correlate with net sales, and how do they impact the net profit margin across different product categories and regions?

#### Figure 1: Cost Structures vs. Net Sales
We plotted the linear relationships of manufacturing and freight costs against Net Sales. Manufacturing costs scale closely with sales, while freight costs scale linearly but show distinct regional clusters.
![Cost Structures vs. Net Sales](plot1.png)

#### Figure 2: Sales Cost Breakdown & Profit Margin by Category
A stacked percentage bar chart shows the breakdown of revenue into COGS, Freight, and Net Profit across product categories.
* **Office Supplies** yields the highest Net Profit Margin (~34.9%).
* **Technology** has high volume but high COGS (~60%), yielding moderate profit margins (~25.3%).
* **Furniture** suffers from very high manufacturing costs and freight costs, resulting in a thin margin (~9.8%).
![Sales Cost Breakdown](plot2.png)

---

### Research Question 2: How do gross sales and net profit margins vary across different quarters of the fiscal year, and what does this reveal about seasonal trends?

#### Figure 3: Fiscal Seasonality (Sales Volume & Profit Margin)
By mapping transactions to fiscal quarters (FY Q1 starts in July), we identify a strong seasonal surge in **Fiscal Q2 (Oct - Dec)**, matching the holiday period. Both revenue volume and profit margins peak here. In contrast, **Fiscal Q3 (Jan - Mar)** experiences a post-holiday dip in both volume and margins.
![Fiscal Seasonality](plot3.png)

#### Figure 4: Year-over-Year Fiscal Performance comparison (YoY)
A grouped bar chart demonstrates robust year-over-year growth across all product categories from **FY23 to FY25**, led by the **Technology** segment.
![YoY Performance comparison](plot4.png)

---

## 5. Strategic Recommendations
1. **Reduce Furniture Freight costs**: Negotiate consolidated shipping arrangements or adjust minimum purchase limits on heavy items.
2. **Optimize Peak Scheduling**: Build up inventory and support in Q1 to handle the high-volume, high-margin surge in Q2.
3. **Cross-Sell Office Supplies**: Leverage high margin items (~35% profit margin) to buffer thinner margins in other segments.
