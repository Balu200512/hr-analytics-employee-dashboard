-- Useful HR analytics queries (SQLite)
-- 1. Headcount by department
SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
WHERE EmploymentStatus = 'Active'
GROUP BY Department
ORDER BY EmployeeCount DESC;

-- 2. Average annual salary by department
SELECT Department, ROUND(AVG(AnnualSalaryINR), 2) AS AverageAnnualSalaryINR
FROM Employees
WHERE EmploymentStatus = 'Active'
GROUP BY Department
ORDER BY AverageAnnualSalaryINR DESC;

-- 3. Monthly attendance rate
SELECT MonthStart,
       ROUND(100.0 * SUM(PresentDays) / NULLIF(SUM(WorkingDays), 0), 2) AS AttendanceRatePct
FROM AttendanceMonthly
GROUP BY MonthStart
ORDER BY MonthStart;

-- 4. Monthly payroll totals
SELECT PayMonth,
       ROUND(SUM(GrossPayINR), 2) AS GrossPayrollINR,
       ROUND(SUM(DeductionsINR), 2) AS DeductionsINR,
       ROUND(SUM(NetPayINR), 2) AS NetPayrollINR
FROM PayrollMonthly
GROUP BY PayMonth
ORDER BY PayMonth;

-- 5. Attrition count by department
SELECT Department, COUNT(*) AS Exits
FROM Attrition
GROUP BY Department
ORDER BY Exits DESC;

-- 6. Overall attrition rate in this synthetic sample (all listed employees)
SELECT ROUND(
    100.0 * SUM(CASE WHEN EmploymentStatus = 'Resigned' THEN 1 ELSE 0 END) / COUNT(*), 2
) AS AttritionRatePct
FROM Employees;
