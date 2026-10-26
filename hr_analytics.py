from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
DB_PATH = ROOT / "hr_analytics.db"

def load_csvs():
    employees = pd.read_csv(DATA / "employees.csv")
    attendance = pd.read_csv(DATA / "attendance_monthly.csv")
    payroll = pd.read_csv(DATA / "payroll_monthly.csv")
    attrition = pd.read_csv(DATA / "attrition.csv")
    employees["HireDate"] = pd.to_datetime(employees["HireDate"], errors="coerce")
    attendance["MonthStart"] = pd.to_datetime(attendance["MonthStart"], errors="coerce")
    payroll["PayMonth"] = pd.to_datetime(payroll["PayMonth"], errors="coerce")
    attrition["ExitDate"] = pd.to_datetime(attrition["ExitDate"], errors="coerce")
    return employees, attendance, payroll, attrition

def create_database(employees, attendance, payroll, attrition):
    with sqlite3.connect(DB_PATH) as conn:
        employees.to_sql("Employees", conn, if_exists="replace", index=False)
        attendance.to_sql("AttendanceMonthly", conn, if_exists="replace", index=False)
        payroll.to_sql("PayrollMonthly", conn, if_exists="replace", index=False)
        attrition.to_sql("Attrition", conn, if_exists="replace", index=False)

def save_chart(fig, filename):
    REPORTS.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(REPORTS / filename, dpi=160, bbox_inches="tight")
    plt.close(fig)

def build_reports(employees, attendance, payroll, attrition):
    REPORTS.mkdir(exist_ok=True)
    active = employees[employees["EmploymentStatus"] == "Active"].copy()
    headcount = active.groupby("Department")["EmployeeID"].nunique().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    headcount.plot(kind="barh", ax=ax)
    ax.set_title("Active Headcount by Department")
    ax.set_xlabel("Employees")
    ax.set_ylabel("Department")
    save_chart(fig, "headcount_by_department.png")

    attendance_summary = attendance.groupby("MonthStart", as_index=False).agg(
        PresentDays=("PresentDays", "sum"),
        WorkingDays=("WorkingDays", "sum")
    )
    attendance_summary["AttendanceRatePct"] = (
        100 * attendance_summary["PresentDays"] /
        attendance_summary["WorkingDays"].replace(0, pd.NA)
    )
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(attendance_summary["MonthStart"], attendance_summary["AttendanceRatePct"], marker="o")
    ax.set_title("Monthly Attendance Rate")
    ax.set_ylabel("Attendance (%)")
    ax.set_xlabel("Month")
    ax.tick_params(axis="x", rotation=35)
    save_chart(fig, "monthly_attendance_rate.png")

    payroll_summary = payroll.groupby("PayMonth", as_index=False)["NetPayINR"].sum()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(payroll_summary["PayMonth"], payroll_summary["NetPayINR"], marker="o")
    ax.set_title("Monthly Net Payroll")
    ax.set_ylabel("Net payroll (INR)")
    ax.set_xlabel("Month")
    ax.tick_params(axis="x", rotation=35)
    save_chart(fig, "monthly_net_payroll.png")

    exits = attrition.groupby("Department")["EmployeeID"].nunique().sort_values()
    fig, ax = plt.subplots(figsize=(9, 5))
    exits.plot(kind="barh", ax=ax)
    ax.set_title("Synthetic Exits by Department")
    ax.set_xlabel("Exit count")
    ax.set_ylabel("Department")
    save_chart(fig, "attrition_by_department.png")

    active_count = int(active["EmployeeID"].nunique())
    total_count = int(employees["EmployeeID"].nunique())
    exit_count = int(attrition["EmployeeID"].nunique())
    attendance_pct = float(100 * attendance["PresentDays"].sum() / attendance["WorkingDays"].sum())
    gross_payroll = float(payroll["GrossPayINR"].sum())
    net_payroll = float(payroll["NetPayINR"].sum())
    metrics = pd.DataFrame([
        ("Total employees in sample", total_count),
        ("Active employees", active_count),
        ("Synthetic exits", exit_count),
        ("Synthetic exit share (%)", round(100 * exit_count / total_count, 2) if total_count else 0),
        ("Overall attendance rate (%)", round(attendance_pct, 2)),
        ("Annual gross payroll (INR)", round(gross_payroll, 2)),
        ("Annual net payroll (INR)", round(net_payroll, 2)),
    ], columns=["Metric", "Value"])
    metrics.to_csv(REPORTS / "hr_summary_metrics.csv", index=False)
    md_lines = ["| Metric | Value |", "|---|---:|"]
    for _, row in metrics.iterrows():
        md_lines.append(f"| {row['Metric']} | {row['Value']} |")
    (REPORTS / "hr_summary_metrics.md").write_text("\\n".join(md_lines) + "\\n", encoding="utf-8")

def main():
    employees, attendance, payroll, attrition = load_csvs()
    create_database(employees, attendance, payroll, attrition)
    build_reports(employees, attendance, payroll, attrition)
    print("HR Analytics project completed successfully.")
    print(f"Employees: {len(employees):,}")
    print(f"Attendance monthly rows: {len(attendance):,}")
    print(f"Payroll monthly rows: {len(payroll):,}")
    print(f"Attrition records: {len(attrition):,}")
    print(f"SQLite database: {DB_PATH}")
    print(f"Charts and metrics saved in: {REPORTS}")

if __name__ == "__main__":
    main()
