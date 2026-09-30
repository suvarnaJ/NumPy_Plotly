# ============================================================
# E-COMMERCE SALES DATA ANALYSIS
# Using NumPy and Plotly
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# ------------------------------------------------------------
# 1. Create fictional sales data for 12 months
# ------------------------------------------------------------

months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Monthly Revenue
revenue = np.array([
    120000, 135000, 150000, 145000,
    170000, 185000, 200000, 210000,
    195000, 230000, 260000, 300000
])

# Monthly Orders
orders = np.array([
    450, 480, 520, 510,
    580, 620, 670, 700,
    660, 750, 820, 900
])

# Monthly Customers
customers = np.array([
    300, 320, 350, 370,
    410, 450, 480, 520,
    550, 600, 670, 750
])

# Monthly Expenses
expenses = np.array([
    80000, 85000, 90000, 92000,
    100000, 108000, 115000, 120000,
    118000, 130000, 145000, 160000
])


# ------------------------------------------------------------
# 2. Calculate Total Annual Revenue
# ------------------------------------------------------------

total_revenue = np.sum(revenue)

print("Total Annual Revenue: ₹", total_revenue)


# ------------------------------------------------------------
# 3. Calculate Average Monthly Revenue
# ------------------------------------------------------------

average_revenue = np.mean(revenue)

print("Average Monthly Revenue: ₹", round(average_revenue, 2))


# ------------------------------------------------------------
# 4. Find Best-Performing Month
# ------------------------------------------------------------

best_month_index = np.argmax(revenue)

print(
    "Best Performing Month:",
    months[best_month_index],
    "- Revenue: ₹",
    revenue[best_month_index]
)


# ------------------------------------------------------------
# 5. Find Lowest-Performing Month
# ------------------------------------------------------------

lowest_month_index = np.argmin(revenue)

print(
    "Lowest Performing Month:",
    months[lowest_month_index],
    "- Revenue: ₹",
    revenue[lowest_month_index]
)


# ------------------------------------------------------------
# 6. Calculate Month-to-Month Revenue Differences
# ------------------------------------------------------------

revenue_difference = np.diff(revenue)

print("\nMonth-to-Month Revenue Differences:")

for i in range(len(revenue_difference)):
    print(
        months[i],
        "to",
        months[i + 1],
        ": ₹",
        revenue_difference[i]
    )


# ------------------------------------------------------------
# 7. Line Chart - Revenue Trend
# ------------------------------------------------------------

fig1 = px.line(
    x=months,
    y=revenue,
    markers=True,
    title="Monthly Revenue Trend",
    labels={
        "x": "Month",
        "y": "Revenue (₹)"
    }
)

fig1.show()


# ------------------------------------------------------------
# 8. Bar Chart - Monthly Orders
# ------------------------------------------------------------

fig2 = px.bar(
    x=months,
    y=orders,
    title="Monthly Orders",
    labels={
        "x": "Month",
        "y": "Number of Orders"
    }
)

fig2.show()


# ------------------------------------------------------------
# 9. Comparison Graph - Revenue vs Expenses
# ------------------------------------------------------------

fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=months,
        y=revenue,
        mode="lines+markers",
        name="Revenue"
    )
)

fig3.add_trace(
    go.Scatter(
        x=months,
        y=expenses,
        mode="lines+markers",
        name="Expenses"
    )
)

fig3.update_layout(
    title="Revenue vs Expenses",
    xaxis_title="Month",
    yaxis_title="Amount (₹)"
)

fig3.show()


# ------------------------------------------------------------
# 10. Customer Growth Visualization
# ------------------------------------------------------------

fig4 = px.line(
    x=months,
    y=customers,
    markers=True,
    title="Monthly Customer Growth",
    labels={
        "x": "Month",
        "y": "Number of Customers"
    }
)

fig4.show()


# ------------------------------------------------------------
# 11. Calculate and Visualize Monthly Profit
# Profit = Revenue - Expenses
# ------------------------------------------------------------

profit = revenue - expenses

print("\nMonthly Profit:")

for month, monthly_profit in zip(months, profit):
    print(month, ": ₹", monthly_profit)


fig5 = px.bar(
    x=months,
    y=profit,
    title="Monthly Profit",
    labels={
        "x": "Month",
        "y": "Profit (₹)"
    }
)

fig5.show()


# ------------------------------------------------------------
# 12. Final Management Performance Visualization
# Revenue, Expenses and Profit
# ------------------------------------------------------------

fig6 = go.Figure()

fig6.add_trace(
    go.Scatter(
        x=months,
        y=revenue,
        mode="lines+markers",
        name="Revenue"
    )
)

fig6.add_trace(
    go.Scatter(
        x=months,
        y=expenses,
        mode="lines+markers",
        name="Expenses"
    )
)

fig6.add_trace(
    go.Scatter(
        x=months,
        y=profit,
        mode="lines+markers",
        name="Profit"
    )
)

fig6.update_layout(
    title="Overall Company Performance",
    xaxis_title="Month",
    yaxis_title="Amount (₹)",
    hovermode="x unified"
)

fig6.show()


# ------------------------------------------------------------
# Final Summary for Management
# ------------------------------------------------------------

print("\n========== MANAGEMENT SUMMARY ==========")

print(f"Total Annual Revenue : ₹{total_revenue:,}")
print(f"Average Monthly Revenue : ₹{average_revenue:,.2f}")

print(
    f"Best Performing Month : "
    f"{months[best_month_index]} "
    f"(₹{revenue[best_month_index]:,})"
)

print(
    f"Lowest Performing Month : "
    f"{months[lowest_month_index]} "
    f"(₹{revenue[lowest_month_index]:,})"
)

print(f"Total Annual Expenses : ₹{np.sum(expenses):,}")
print(f"Total Annual Profit : ₹{np.sum(profit):,}")

print(
    f"Average Monthly Profit : "
    f"₹{np.mean(profit):,.2f}"
)

print("========================================")