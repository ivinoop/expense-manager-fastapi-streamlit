import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_month_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    if response.status_code == 200:
        monthly_summary = response.json()
    else:
        st.error("Failed to fetch monthly summary from server.")
        monthly_summary = []

    df = pd.DataFrame(monthly_summary)
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    df_sorted = df.sort_values(by="Month Number", ascending=False)
    df_sorted.set_index("Month Number", inplace=True)

    st.title("Expense Breakdown By Months")

    st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], use_container_width=True)

    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted.sort_index())

# def analytics_month_tab():
#     response = requests.get(f"{API_URL}/monthly_summary/")
#     if response.status_code == 200:
#         monthly_summary = response.json()
#     else:
#         st.error("Failed to fetch monthly summary from server.")
#         monthly_summary = []
#
#     # Guard Clause: Prevent crash if database returns no records
#     if not monthly_summary:
#         st.info("No expense data available for monthly summary.")
#         return
#
#     df = pd.DataFrame(monthly_summary)
#
#     # Rename columns safely
#     df.rename(columns={
#         "expense_month": "Month Number",
#         "month_name": "Month Name",
#         "total": "Total"
#     }, inplace=True)
#
#     # Fallback check in case backend keys don't match
#     if "Month Number" not in df.columns:
#         st.error("Unexpected data format received from server.")
#         return
#
#     df_sorted = df.sort_values(by="Month Number", ascending=False)
#
#     st.title("Expense Breakdown By Months")
#
#     # Render bar chart
#     st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], use_container_width=True)
#
#     # Format numbers for table view
#     df_display = df_sorted.copy()
#     df_display["Total"] = df_display["Total"].map("{:.2f}".format)
#     df_display.set_index("Month Number", inplace=True)

#     st.table(df_display.sort_index())