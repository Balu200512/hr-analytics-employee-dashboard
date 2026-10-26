-- HR Analytics & Employee Dashboard schema (SQLite compatible)
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID TEXT PRIMARY KEY,
    EmployeeName TEXT NOT NULL,
    Department TEXT NOT NULL,
    JobLevel TEXT NOT NULL,
    Location TEXT NOT NULL,
    EmploymentType TEXT NOT NULL,
    HireDate TEXT NOT NULL,
    Gender TEXT,
    AnnualSalaryINR REAL NOT NULL,
    ManagerID TEXT,
    EmploymentStatus TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS AttendanceMonthly (
    EmployeeID TEXT NOT NULL,
    MonthStart TEXT NOT NULL,
    WorkingDays INTEGER NOT NULL,
    PresentDays INTEGER NOT NULL,
    LeaveDays INTEGER NOT NULL,
    AbsentDays INTEGER NOT NULL,
    PRIMARY KEY (EmployeeID, MonthStart),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE IF NOT EXISTS PayrollMonthly (
    EmployeeID TEXT NOT NULL,
    PayMonth TEXT NOT NULL,
    GrossPayINR REAL NOT NULL,
    DeductionsINR REAL NOT NULL,
    NetPayINR REAL NOT NULL,
    PRIMARY KEY (EmployeeID, PayMonth),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Attrition (
    EmployeeID TEXT PRIMARY KEY,
    Department TEXT NOT NULL,
    JobLevel TEXT NOT NULL,
    HireDate TEXT NOT NULL,
    ExitDate TEXT NOT NULL,
    ExitReason TEXT NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
