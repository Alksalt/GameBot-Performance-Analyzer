# Classic Car Sales – Excel Analytics (Intermediate Level)

## Overview
A compact Excel project that walks through the full analytics flow on a public Kaggle data set  
<https://www.kaggle.com/datasets/•••/sales-data-sample>.  
The workbook demonstrates core **intermediate Excel** skills:

* Table-based modelling with structured references  
* Dynamic array formulas (`FILTER`, `SORT`, `QUARTILE.EXC`, `IFS`, etc.)  
* KPI calculation and custom measures (`Profit`, `Cost of Goods Sold`)  
* Client segmentation by quartile  
* Multi-sheet PivotTable dashboards with slicers and a map visual  
* Clear, presentation-ready formatting

---

## Data Source  
`/data/sales_data_sample.csv` – 2 ,837 orders (2003-2005) from a fictitious Classic Car retailer.

---

## Workbook Structure

| Sheet | Purpose | Key Excel features |
|-------|---------|--------------------|
| **sales_data_sample** | Raw data converted to an **Excel Table** (`tblSales`). | Structured refs, data types |
| **customer_categorization** | Quartile-based grouping into *Low*, *Medium*, *High* value customers. | `FILTER`, `QUARTILE.EXC`, spill ranges |
| **Thresholds** | Helper table storing quartile break-points (drives categorisation formulas). | Named range, dynamic links |
| **overall_performance_metrics** | KPI dashboard (Total Sales, Profit, AOV, #Orders, #Products). | Measures via PivotTable, slicers |
| **geographic_values** | Country & city–level sales with a **Map chart** + bar charts. | PivotTable, map visual, slicers |
| **Date_metrics** | Month-by-month analysis, year slicer, bar chart ranking months by sales & profit. | Date grouping, calculated field `Order_DayOfWeek` |
| **Documentation** *(hidden)* | Quick reference of custom formulas & assumptions. | In-cell comments |

---

## Key Calculations

| Column | Formula (Table notation) | Description |
|--------|-------------------------|-------------|
| `CostOfGoodsSold` | `=[@SALES] * 0.68` | Assumed 32 % gross margin. |
| `Profit` | `=[@SALES] - [@CostOfGoodsSold]` | Line-level profit. |
| `Order_DayOfWeek` | `=TEXT([@ORDERDATE],"ddd")` | 3-letter weekday (Mon…Sun). |

See the **Documentation** sheet for the full catalog.

---

## How to Explore
1. Open `project1_intermediate.xlsx`.
2. Use the *Customer* slicer on **overall_performance_metrics** to switch the whole dashboard between client segments.
3. Switch to **Date_metrics** and try selecting different years with the YEAR slicer – the bar chart auto-ranks months.
4. Jump to **geographic_values** and click a country on the map to cross-filter every other visual.

---

## Next Steps
* **Power Query / Power Pivot** version – same dataset, but all transformations done in PQ → Data Model → DAX measures.
* Replace fixed COGS assumption with a per-product `MSRP` vs `PRICEEACH` comparison.
* Add Timeline slicer for finer time navigation.

---

### Author
Oleksandr (Excel / Python enthusiast, aspiring Data Analyst).  
Feel free to open an issue or reach out on LinkedIn for feedback!

