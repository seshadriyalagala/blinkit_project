# Blinkit Data Analytics Dashboard

## Project Overview

The **Blinkit Data Analytics Dashboard** is a data analytics project designed to explore business performance through interactive dashboards and structured data analysis.

The project focuses on analyzing product and inventory data, customer behavior, orders, delivery performance, customer feedback, marketing performance, and investment information. The objective is to transform raw data into meaningful insights that can support data-driven business decisions.

## Project Objectives

* Analyze overall business and order performance.
* Understand customer behavior and customer segments.
* Monitor product availability and inventory levels.
* Evaluate delivery partner performance and delivery earnings.
* Analyze customer feedback and satisfaction.
* Measure marketing campaign performance.
* Explore Blinkit's investment and funding information.
* Build interactive dashboards for exploring business insights.

## Tools and Technologies

* **Python:** Data cleaning and preprocessing.
* **Pandas:** Data manipulation and analysis.
* **SQL Server:** Database storage and querying.
* **Power BI:** Interactive dashboards and data visualization.
* **DAX:** Measures and calculated columns.
* **Excel and CSV:** Data sources and dataset preparation.
* **Git and GitHub:** Version control and project sharing.

## Dataset Description

The project uses multiple datasets covering different business areas:

| Dataset                                           | Description                                   |
| ------------------------------------------------- | --------------------------------------------- |
| `blinkit_customers.csv`                           | Customer information and customer analysis    |
| `blinkit_orders.csv`                              | Order information and business performance    |
| `blinkit_order_items.csv`                         | Individual items associated with orders       |
| `blinkit_products.csv`                            | Product information and pricing               |
| `blinkit_inventory.csv`                           | Product inventory and stock information       |
| `blinkit_inventoryNew.csv`                        | Additional inventory dataset                  |
| `blinkit_delivery_performance.csv`                | Delivery performance information              |
| `Blinkit_Delivery_salary.xlsx`                    | Delivery partner earnings and salary analysis |
| `blinkit_customer_feedback.csv`                   | Customer feedback and satisfaction            |
| `blinkit_marketing_performance.csv`               | Marketing campaigns and performance           |
| `Blinkit_Complete_Investment_Data_2015_2026.xlsx` | Investment and funding information            |

<img width="1695" height="712" alt="Screenshot 2026-10-02 134645" src="https://github.com/user-attachments/assets/e0f64d8a-9bc2-41f0-8e57-8662bffd685c" />


## Dashboard Modules

# Dashboard Pages Explanation

The Blinkit Data Analytics Dashboard contains multiple interactive report pages, each designed to analyze a specific area of business performance.

### 1. Overview Dashboard

Provides a high-level summary of business performance through KPI cards, charts, and visual indicators. It helps users quickly understand overall performance and explore key business metrics.
<img width="1317" height="735" alt="Screenshot 2026-10-02 134215" src="https://github.com/user-attachments/assets/a5646164-1dff-4295-acf0-b12729d48a44" />

### 2. Products Analysis

Focuses on product information, pricing, categories, and inventory-related metrics. It helps analyze product distribution, compare prices, and understand stock availability.
<img width="1337" height="737" alt="Screenshot 2026-10-02 134358" src="https://github.com/user-attachments/assets/01343199-1e3e-447e-beba-9451a7adb4a4" />

### 3. Customer Analysis

Explores customer information, customer segments, and purchasing behavior. It helps identify customer groups and understand patterns in customer activity.
<img width="1338" height="742" alt="Screenshot 2026-10-02 134423" src="https://github.com/user-attachments/assets/8e5749ca-2d9c-4933-81c7-5c772514c08c" />

### 4. Delivery Partner Analysis

Examines delivery partner performance and earnings. It helps evaluate delivery-related metrics and understand operational performance.
<img width="1307" height="737" alt="image" src="https://github.com/user-attachments/assets/e01efe7d-9713-4254-a6b5-d6eb2c418425" />

### 5. Investment Analysis

Presents investment and funding information, including funding rounds, investors, transaction values, and year-wise trends. It helps explore the available investment records from 2015 to 2026.
<img width="1325" height="742" alt="Screenshot 2026-10-02 134445" src="https://github.com/user-attachments/assets/363f3489-5677-4096-91de-043da6631e25" />

### 6. Marketing Performance

Analyzes marketing campaign data and performance metrics. It helps users explore campaign results and compare marketing performance across available categories.
<img width="1315" height="738" alt="Screenshot 2026-10-02 134251" src="https://github.com/user-attachments/assets/973106bf-4387-445c-b442-22d1bf668a20" />

## Power BI Navigation Buttons

The dashboard uses interactive page navigation buttons to help users move between different analytical sections without manually selecting report tabs.

### Navigation Features

* **Home / Overview:** Navigates to the main dashboard, displaying overall business KPIs and performance insights.
* **Products:** Opens the product and inventory analysis page.
* **Customers:** Navigates to customer behavior and customer segment analysis.
* **Delivery Partners:** Opens the delivery performance and earnings analysis page.
* **Investments:** Displays investment and funding analysis.
* **Marketing:** Navigates to marketing campaign performance analysis.
* **Customer Feedback:** Opens the customer feedback and satisfaction analysis page.

### How Page Navigation Works

Each navigation button is configured in Power BI with an action that directs users to a specific report page.

To configure a navigation button:

1. Select the button in Power BI Desktop.
2. Open the **Format visual** pane.
3. Expand **Action** and turn it on.
4. Set **Type** to `Page navigation`.
5. Select the required page under **Destination**.
6. Repeat the configuration for other navigation buttons.

### User Interaction

In Power BI Desktop editing mode, hold **Ctrl** and click a navigation button to test it. In Power BI Service Reading view, users can normally click the button to navigate between pages.

### Benefits

* Simplifies dashboard navigation.
* Improves the user experience.
* Organizes multiple analytical pages into a single report.
* Makes it easier to explore different business metrics.
* Provides a more professional and interactive dashboard experience.


## Data Analytics Workflow

CSV / Excel Datasets
        │
        ▼
Python + Pandas
(Data Cleaning & Preprocessing)
        │
        ▼
SQLAlchemy
        │
        ▼
SQL Server Database
(Database: blinkit)
        │
        ▼
Power BI
(Data Modeling + DAX)
        │
        ▼
Interactive Dashboard
        │
        ▼
Business Insights


1. **Data Collection:** Gathered datasets covering different Blinkit business areas.
2. **Data Cleaning:** Prepared the data by handling missing values, duplicates, and data inconsistencies where required.
3. **Database Management:** Organized data in SQL Server for querying and analysis.
4. **Data Analysis:** Used SQL queries and Python to explore the datasets.
5. **Data Modeling:** Connected relevant tables and established relationships.
6. **DAX Development:** Created measures and calculated columns for KPIs and analysis.
7. **Dashboard Development:** Built interactive Power BI report pages using charts, cards, slicers, and filters.
8. **Validation:** Reviewed the results and refined the dashboard presentation.

## Key Learning Outcomes

* Practical experience with data cleaning and preprocessing.
* Improved understanding of SQL queries and database management.
* Experience creating data models and relationships.
* Development of DAX measures and calculated columns.
* Creation of interactive Power BI dashboards.
* Experience analyzing business data across multiple domains.
* Improved ability to communicate insights through visualizations.

## Project Status

**Status: Completed**

This project demonstrates an end-to-end data analytics workflow, from preparing datasets and managing data in a database to developing interactive dashboards in Power BI.

## Repository Structure

```text
BLINKIT DATA ANALYTICS PROJECT
│
├── data_sets/
│   ├── blinkit_customers.csv
│   ├── blinkit_orders.csv
│   ├── blinkit_order_items.csv
│   ├── blinkit_products.csv
│   ├── blinkit_inventory.csv
│   ├── blinkit_inventoryNew.csv
│   ├── blinkit_delivery_performance.csv
│   ├── Blinkit_Delivery_salary.xlsx
│   ├── blinkit_customer_feedback.csv
│   ├── blinkit_marketing_performance.csv
│   └── Blinkit_Complete_Investment_Data_2015_2026.xlsx
│
├── Python/
│   ├── pyhton_customers.py
│   ├── pyhton_orders.py
│   ├── python_products.py
│   ├── python_inventory.py
│   ├── pyhton_delivery.py
│   ├── pyhton_delivery_salary.py
│   ├── pyhton_feedback.py
│   ├── python_matkating_performance.py
│   └── python_investment.py
│
├── SQL Server/
│   └── Database: blinkit
│       ├── customers
│       ├── orders
│       ├── order_items
│       ├── products
│       ├── inventory_old
│       ├── inventory_new
│       ├── delivery_performance
│       ├── salarys
│       ├── customer_feedback
│       ├── marketing_performance
│       └── blinkit_investment_data
│
├── Power BI/
│   └── Blinkit Dashboard.pbix
│
├── README.md
└── .gitignore
```

*Note: Update the folder and file names in this structure to match your actual GitHub repository.*

## How to View the Project

1. Clone or download this repository.
2. Open the Power BI `.pbix` file using Power BI Desktop.
3. If prompted, update the data source paths to match your local dataset locations.
4. Refresh the data if the required source files are available.
5. Explore the dashboard pages, visuals, slicers, and filters.

## Future Improvements

* Automate data refresh and data preparation.
* Add more detailed business performance metrics.
* Improve dashboard usability and navigation.
* Expand trend analysis and forecasting where suitable.
* Publish an online dashboard demonstration if supported by the available Power BI account and permissions.

## Disclaimer

This is a portfolio and data analytics project. The datasets and analysis should not be interpreted as official or verified internal Blinkit business records unless their sources have been independently validated.

## Author

**Yalagala Seshadri**

Aspiring Data Analyst

Interested in data analytics, business intelligence, and data visualization.
