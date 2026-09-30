import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# ============================================================
# 1. BAR CHART - MONTHLY SALES
# ============================================================

print("\n========== 1. BAR CHART ==========")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 170, 140, 200, 230]

fig1 = go.Figure()

fig1.add_trace(
    go.Bar(
        x=months,
        y=sales,
        name="Sales"
    )
)

fig1.update_layout(
    title="Monthly Sales",
    xaxis_title="Month",
    yaxis_title="Sales (₹ Thousands)"
)

fig1.show()


# ============================================================
# 2. LINE CHART - MONTHLY SALES
# ============================================================

print("\n========== 2. LINE CHART ==========")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=months,
        y=sales,
        mode="lines+markers",
        name="Sales"
    )
)

fig2.update_layout(
    title="Monthly Sales Trend",
    xaxis_title="Month",
    yaxis_title="Sales (₹ Thousands)"
)

fig2.show()


# ============================================================
# 3. PIE CHART - DEPARTMENT-WISE EMPLOYEE DISTRIBUTION
# ============================================================

print("\n========== 3. PIE CHART ==========")

departments = [
    "Engineering",
    "Sales",
    "Marketing",
    "HR",
    "Operations"
]

employees = [40, 25, 15, 10, 10]

fig3 = go.Figure(
    data=[
        go.Pie(
            labels=departments,
            values=employees,
            hole=0
        )
    ]
)

fig3.update_layout(
    title="Department-wise Employee Distribution"
)

fig3.show()


# ============================================================
# 4. SCATTER PLOT - HOURS STUDIED VS EXAM MARKS
# ============================================================

print("\n========== 4. SCATTER PLOT ==========")

hours_studied = [
    1, 2, 2.5, 3, 3.5,
    4, 4.5, 5, 5.5, 6,
    6.5, 7, 7.5, 8, 9
]

exam_marks = [
    42, 48, 51, 55, 60,
    64, 68, 72, 75, 79,
    82, 85, 88, 92, 96
]

fig4 = go.Figure()

fig4.add_trace(
    go.Scatter(
        x=hours_studied,
        y=exam_marks,
        mode="markers",
        name="Students"
    )
)

fig4.update_layout(
    title="Hours Studied vs Exam Marks",
    xaxis_title="Hours Studied",
    yaxis_title="Exam Marks"
)

fig4.show()


# ============================================================
# 5. HISTOGRAM - 500 RANDOM VALUES
# ============================================================

print("\n========== 5. HISTOGRAM ==========")

random_values = np.random.normal(
    loc=50,
    scale=10,
    size=500
)

fig5 = go.Figure()

fig5.add_trace(
    go.Histogram(
        x=random_values,
        name="Random Values"
    )
)

fig5.update_layout(
    title="Distribution of 500 Random Values",
    xaxis_title="Value",
    yaxis_title="Frequency"
)

fig5.show()


# ============================================================
# 6. BOX PLOT - SALARY DISTRIBUTION
# ============================================================

print("\n========== 6. BOX PLOT ==========")

salary = [
    35000, 42000, 48000, 52000, 55000,
    58000, 60000, 62000, 65000, 68000,
    70000, 72000, 75000, 78000, 80000,
    82000, 85000, 88000, 90000, 95000,
    98000, 100000, 105000, 110000, 115000,
    120000, 125000, 130000, 140000, 150000
]

fig6 = go.Figure()

fig6.add_trace(
    go.Box(
        y=salary,
        name="Employee Salary",
        boxpoints="all"
    )
)

fig6.update_layout(
    title="Employee Salary Distribution",
    xaxis_title="Employee Salary",
    yaxis_title="Salary (₹)"
)

fig6.show()


# ============================================================
# 7. MULTIPLE CATEGORIES - PRODUCT SALES
# ============================================================

print("\n========== 7. MULTIPLE CATEGORIES ==========")

laptop_sales = [100, 120, 140, 130, 160, 180]
mobile_sales = [200, 220, 250, 240, 280, 300]
tablet_sales = [80, 90, 100, 95, 120, 140]

fig7 = go.Figure()

fig7.add_trace(
    go.Scatter(
        x=months,
        y=laptop_sales,
        mode="lines+markers",
        name="Laptop"
    )
)

fig7.add_trace(
    go.Scatter(
        x=months,
        y=mobile_sales,
        mode="lines+markers",
        name="Mobile"
    )
)

fig7.add_trace(
    go.Scatter(
        x=months,
        y=tablet_sales,
        mode="lines+markers",
        name="Tablet"
    )
)

fig7.update_layout(
    title="Product Sales Comparison",
    xaxis_title="Month",
    yaxis_title="Sales (Units)"
)

fig7.show()


# ============================================================
# 8. STUDENT PERFORMANCE
# ============================================================

print("\n========== 8. STUDENT PERFORMANCE ==========")

students = [
    "Rahul", "Priya", "Amit", "Sneha", "Rohan",
    "Neha", "Karan", "Pooja", "Vikas", "Anita"
]

python_marks = [85, 78, 92, 88, 75, 90, 82, 95, 80, 87]

math_marks = [80, 85, 89, 82, 78, 88, 84, 91, 76, 90]

data_science_marks = [
    88, 82, 94, 90, 80,
    92, 86, 96, 84, 89
]

fig8 = go.Figure()

fig8.add_trace(
    go.Bar(
        x=students,
        y=python_marks,
        name="Python"
    )
)

fig8.add_trace(
    go.Bar(
        x=students,
        y=math_marks,
        name="Mathematics"
    )
)

fig8.add_trace(
    go.Bar(
        x=students,
        y=data_science_marks,
        name="Data Science"
    )
)

fig8.update_layout(
    title="Student Performance Comparison",
    xaxis_title="Student",
    yaxis_title="Marks",
    barmode="group"
)

fig8.show()


# ============================================================
# 9. 3D SCATTER PLOT
# ============================================================

print("\n========== 9. 3D SCATTER PLOT ==========")

np.random.seed(10)

age = np.random.randint(22, 51, 30)

experience = np.random.randint(1, 21, 30)

salary_3d = (
    30000
    + experience * 5000
    + np.random.randint(-5000, 10000, 30)
)

fig9 = go.Figure()

fig9.add_trace(
    go.Scatter3d(
        x=age,
        y=experience,
        z=salary_3d,
        mode="markers",
        marker=dict(
            size=6
        ),
        name="Employees"
    )
)

fig9.update_layout(
    title="Age, Experience and Salary Analysis",
    scene=dict(
        xaxis_title="Age",
        yaxis_title="Experience (Years)",
        zaxis_title="Salary (₹)"
    )
)

fig9.show()


# ============================================================
# 10. CUSTOM GRAPH - WEBSITE VISITORS
# ============================================================

print("\n========== 10. CUSTOM GRAPH ==========")

website_visitors = [
    1200, 1350, 1500, 1450,
    1700, 1900
]

fig10 = go.Figure()

fig10.add_trace(
    go.Scatter(
        x=months,
        y=website_visitors,
        mode="lines+markers",
        name="Visitors"
    )
)

fig10.update_layout(
    title="Monthly Website Visitors",
    xaxis_title="Month",
    yaxis_title="Number of Visitors"
)

fig10.show()


# ============================================================
# 11. NUMPY + PLOTLY
# ============================================================

print("\n========== 11. NUMPY + PLOTLY ==========")

random_numbers = np.random.randint(
    1,
    101,
    100
)

print("100 Random Numbers:")
print(random_numbers)

fig11 = go.Figure()

fig11.add_trace(
    go.Scatter(
        x=np.arange(1, 101),
        y=random_numbers,
        mode="lines+markers",
        name="Random Numbers"
    )
)

fig11.update_layout(
    title="100 Random Numbers Generated Using NumPy",
    xaxis_title="Number Index",
    yaxis_title="Random Value"
)

fig11.show()


# ============================================================
# 12. DASHBOARD THINKING CHALLENGE
# ============================================================

print("\n========== 12. DASHBOARD THINKING CHALLENGE ==========")

dashboard_months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun"
]

revenue = [
    500000, 550000, 580000,
    620000, 680000, 750000
]

expenses = [
    350000, 370000, 390000,
    410000, 440000, 470000
]

employee_count = [
    80, 82, 85, 88, 92, 95
]

customer_count = [
    1200, 1350, 1500,
    1700, 1950, 2200
]


# Dashboard Chart 1 - Revenue
fig12_1 = go.Figure()

fig12_1.add_trace(
    go.Scatter(
        x=dashboard_months,
        y=revenue,
        mode="lines+markers",
        name="Revenue"
    )
)

fig12_1.update_layout(
    title="Company Revenue",
    xaxis_title="Month",
    yaxis_title="Revenue (₹)"
)

fig12_1.show()


# Dashboard Chart 2 - Expenses
fig12_2 = go.Figure()

fig12_2.add_trace(
    go.Bar(
        x=dashboard_months,
        y=expenses,
        name="Expenses"
    )
)

fig12_2.update_layout(
    title="Company Expenses",
    xaxis_title="Month",
    yaxis_title="Expenses (₹)"
)

fig12_2.show()


# Dashboard Chart 3 - Employees
fig12_3 = go.Figure()

fig12_3.add_trace(
    go.Scatter(
        x=dashboard_months,
        y=employee_count,
        mode="lines+markers",
        name="Employees"
    )
)

fig12_3.update_layout(
    title="Employee Growth",
    xaxis_title="Month",
    yaxis_title="Number of Employees"
)

fig12_3.show()


# Dashboard Chart 4 - Customers
fig12_4 = go.Figure()

fig12_4.add_trace(
    go.Scatter(
        x=dashboard_months,
        y=customer_count,
        mode="lines+markers",
        name="Customers"
    )
)

fig12_4.update_layout(
    title="Customer Growth",
    xaxis_title="Month",
    yaxis_title="Number of Customers"
)

fig12_4.show()


print("\n========== ALL 12 TASKS COMPLETED ==========")