# HR Analytics & Employee Dashboard

A beginner-friendly HR analytics portfolio project using **Python, Pandas, Matplotlib, and SQL**. It analyzes synthetic employee records, monthly attendance, payroll, and attrition, creates a local SQLite database, and generates charts and summary metrics.

> **Privacy and data note:** All names, employee IDs, salary figures, attendance records, and exit reasons are synthetic and generated for demonstration. Do not use this sample to make real employment decisions.

## Repository name
`hr-analytics-employee-dashboard`

## GitHub description
`HR analytics project using Python, Pandas, Matplotlib, and SQL to analyze employee headcount, attendance, payroll, and attrition with automated charts and summary reports.`

## Project objectives
- Summarize employee headcount by department and employment status.
- Analyze monthly attendance rates.
- Track monthly gross and net payroll.
- Explore synthetic exits by department and job level.
- Store data in SQLite and demonstrate analytical SQL queries.
- Automatically generate charts and KPI summary files.

## Technology stack
- Python 3.10+
- Pandas — data loading, cleaning, grouping, and analysis
- Matplotlib — charts and visual reports
- SQLite / SQL — local relational database and queries
- Excel — optional workbook for browsing sample data

## Project structure
```text
hr-analytics-employee-dashboard/
├── data/
│   ├── employees.csv
│   ├── attendance_monthly.csv
│   ├── payroll_monthly.csv
│   └── attrition.csv
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
├── reports/                 # generated when the program runs
├── HR_Analytics_Sample_Data.xlsx
├── hr_analytics.py
├── requirements.txt
└── README.md
```

## Sample data
The generated sample contains:
- 180 employee profiles.
- 2,160 monthly attendance rows (180 employees × 12 months).
- 2,160 monthly payroll rows (180 employees × 12 months).
- A separate attrition table containing synthetic exit records.

### `employees.csv`
EmployeeID, EmployeeName, Department, JobLevel, Location, EmploymentType, HireDate, Gender, AnnualSalaryINR, ManagerID, EmploymentStatus.

### `attendance_monthly.csv`
EmployeeID, MonthStart, WorkingDays, PresentDays, LeaveDays, AbsentDays.

### `payroll_monthly.csv`
EmployeeID, PayMonth, GrossPayINR, DeductionsINR, NetPayINR.

### `attrition.csv`
EmployeeID, Department, JobLevel, HireDate, ExitDate, ExitReason.

## Installation and run (Windows / VS Code)

### 1. Download or clone
Download this repository ZIP from GitHub and extract it, or clone it:

```bash
git clone https://github.com/YOUR_USERNAME/hr-analytics-employee-dashboard.git
cd hr-analytics-employee-dashboard
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment (recommended)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:
```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Run the project
```bash
python hr_analytics.py
```

The script creates `hr_analytics.db` in the project root and generates chart images and summary metrics inside `reports/`.

## Outputs
After running the script, the `reports/` folder contains:
- `headcount_by_department.png`
- `monthly_attendance_rate.png`
- `monthly_net_payroll.png`
- `attrition_by_department.png`
- `hr_summary_metrics.csv`
- `hr_summary_metrics.md`

The local SQLite database `hr_analytics.db` contains the imported Employees, AttendanceMonthly, PayrollMonthly, and Attrition tables.

## SQL examples
Open `sql/analytics_queries.sql` to find example queries for:
- Active headcount by department.
- Average annual salary by department.
- Monthly attendance rate.
- Monthly payroll totals.
- Exits by department.
- Overall synthetic attrition rate.

You can inspect the database using SQLite tools or Python's built-in `sqlite3` module. The Python script rebuilds its tables from the CSV source files each time it runs.

## Metrics definitions
- **Active headcount:** distinct employees whose EmploymentStatus is `Active`.
- **Attendance rate:** sum of PresentDays divided by sum of WorkingDays, multiplied by 100. This is an aggregate rate, not an average of employee-level rates.
- **Net payroll:** sum of monthly NetPayINR values.
- **Synthetic exit share:** synthetic exit records divided by all employee profiles. This is a simple sample-data indicator, not a formal HR attrition rate; formal rates need a defined period and average headcount denominator.

## Data model
- `Employees` is the employee dimension table.
- `AttendanceMonthly` has one row per employee and month.
- `PayrollMonthly` has one row per employee and month.
- `Attrition` contains one record per synthetic exiting employee.

EmployeeID is used to connect attendance, payroll, and attrition records to employee profiles.

## Limitations
- All data is synthetic and has no relationship to real employees.
- Attendance and payroll values are illustrative.
- The example is a local analysis prototype, not a production HR information system.
- It does not include authentication, access controls, or secure handling of actual HR data.
- The included program creates a SQLite database locally; it does not host a web dashboard.

## Future enhancements
- Add a Streamlit dashboard with interactive filters.
- Add monthly and department-level comparisons.
- Add employee tenure and retention cohort analysis.
- Add tests, data quality reports, and configurable input paths.
- Connect to a managed SQL database if needed.
- Add role-based access controls before any use with real HR data.

## Skills demonstrated
Python, Pandas, Matplotlib, SQL, SQLite, data cleaning, KPI reporting, attendance analysis, payroll analysis, attrition analysis, and automated report generation.

## Author
Add your name and GitHub profile here.

## License
No license is included by default. Add a license file if you want to specify reuse permissions.
