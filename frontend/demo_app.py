import streamlit as st
import pandas as pd

# Text elements
st.header("Streamlit Core Features")
st.subheader("Text Elements")
st.text("This is a simple text element")

# Data display
st.subheader("Data Display")
st.write("Here is a simple table -")

df = pd.DataFrame({
    "Date": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "Amount": [250, 134, 340]
})

# st.table({"Column 1": [1,2,3], "Column 2": [4,5,6]})
st.table(df)

# Charts
st.subheader("Charts")
st.line_chart([1,2,6,9,12,3,4])

# User Input
st.subheader("User Input")
value = st.slider("Select a value", 0, 100)
st.write(f"Selected value: {value}")

st.title("Interactive Widgets Example")

# Checkbox
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked!")

# Select box
option = st.selectbox("Category", ["Rent", "Food", "Shopping"], label_visibility="collapsed")
st.write(f"You selected: {option}")

# Multiselect
options = st.multiselect("Select multiple numbers", [1,2,3,4])
st.write(f"You selected: {options}")

expense_dt = st.date_input("Expense date: ")
if expense_dt:
    st.write(f"Fetching expenses for {expense_dt}")

st.title("Expense Management System")
# st.number_input("Enter your name")