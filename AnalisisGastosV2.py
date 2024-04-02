import pandas as pd
import streamlit as st
import plotly.express as px
from st_aggrid import AgGrid
from io import BytesIO
import base64
import time
from CategoryMapping import CategoryMapping

# Upload the CSV file
uploaded_file = st.file_uploader("Upload your Revolut Statement CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Started Date', 'Completed Date'])
else:
    st.warning("Please upload a CSV file to proceed.")
    st.stop()

category_mapper = CategoryMapping()

df['Category'] = df['Description'].apply(category_mapper.get_category)

# Create a new column 'Month_Name' with the month name
df['Month_Name'] = df['Started Date'].dt.strftime('%b')

# Delete "Depositing Savings" and "Withdrawing Savings" from the dataframe
df = df[~df['Category'].isin(["Depositing savings", "Withdrawing savings"])]

# Calculate the monthly total for each category
monthly_totals = df.groupby(['Category', 'Month_Name'])['Amount'].sum().reset_index()

# Calculate the monthly average for each category
monthly_average = monthly_totals.groupby('Category')['Amount'].mean().reset_index()
monthly_average.columns = ['Category', 'Monthly Average']
monthly_average['Monthly Average'] = monthly_average['Monthly Average'].round(2)

# Define the desired month order
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

## Streamlit app
st.title('Expense Analysis')

# ## Table with the information for each Category with the columns "Category" "Amount"
# category_table = df.groupby('Category')['Amount'].sum().reset_index()
# category_table['Amount'] = category_table['Amount'].round(2)
# category_table = category_table.merge(monthly_average, on='Category', how='left')
# st.markdown("## Amount by Category")
# AgGrid(category_table, sortable=True, filter=False)

def get_category_table(df):
    category_table = df.groupby('Category')['Amount'].sum().reset_index()
    category_table['Amount'] = category_table['Amount'].round(2)
    category_table = category_table.merge(monthly_average, on='Category', how='left')
    return category_table

# Generate the category table
category_table = get_category_table(df)

# Introduce a delay
time.sleep(2)

# Display the category table
st.markdown("## Amount by Category")
AgGrid(category_table, sortable=True, filter=False)

def get_category_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in: dataframe
    out: href string
    """
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()
    output.seek(0)
    xlsx_data = output.getvalue()
    b64 = base64.b64encode(xlsx_data).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="CategoryTable.xlsx">Download Category Table in an .xlsx file</a>'
    return href

# this will display a download link for the above dataframe
st.markdown(get_category_table_download_link(category_table), unsafe_allow_html=True)

## Multiselect dropdown for category
selected_categories = st.multiselect('Select categories', sorted(df['Category'].unique()))

# Filter data by selected categories
filtered_data = df[df['Category'].isin(selected_categories)]

## KPI with the sum of the Amount of the selected categories
total_amount = filtered_data['Amount'].sum()
formatted_total_amount = f"£{total_amount:,.2f}"
st.markdown(f"## Total Amount for Selected Categories: **{formatted_total_amount}**")

## Bar chart for selected categories by month and year
category_amount = filtered_data.groupby(['Month_Name', pd.Grouper(key='Started Date', freq='Y')])['Amount'].sum().reset_index()

# Create a new column 'Month_Order' with the desired month order
category_amount['Month_Order'] = pd.Categorical(category_amount['Month_Name'], categories=month_order, ordered=True)

# Sort the data by 'Started Date' and 'Month_Order'
category_amount = category_amount.sort_values(['Started Date', 'Month_Order'])

# Create the bar chart
fig = px.bar(category_amount, x='Month_Name', y='Amount', color='Started Date', barmode='group', title='Total Amounts by Month and Year')

# Create a custom legend with years as integers
legend_labels = {str(year): str(year) for year in category_amount['Started Date'].dt.year.unique().astype(str)}
fig.update_layout(legend=dict(title='Year', title_font_size=14, font=dict(family="Courier", size=12, color="black")))
fig.for_each_trace(lambda t: t.update(legendgroup=str(t.name), name=legend_labels[str(pd.to_datetime(t.name).year)]))

# Display the chart in Streamlit
st.plotly_chart(fig)

## For the pie chart: Group data by 'Description' and calculate the sum of 'Amount'
description_amount = filtered_data.groupby('Description')['Amount'].sum().reset_index()

# Create two dataframes: one for positive values and one for negative values
positive_values = description_amount[description_amount['Amount'] > 0]
negative_values = description_amount[description_amount['Amount'] < 0]

# Create the pie chart for positive values
fig_pie_positive = px.pie(positive_values, values='Amount', names='Description', title='Money In')
fig_pie_positive.update_layout(autosize=False, width=400, height=400)

# Create the pie chart for negative values
fig_pie_negative = px.pie(negative_values, values=negative_values['Amount'].abs(), names='Description', title='Money Out')
fig_pie_negative.update_layout(autosize=False, width=400, height=400)

# Display the charts in Streamlit side by side
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_pie_positive)
with col2:
    st.plotly_chart(fig_pie_negative)


## Create a table with the details of the selected categories
st.markdown("## Detail for Selected Categories")
table = filtered_data[['Category', 'Description', 'Amount', 'Started Date']].copy()
table['Started Date'] = table['Started Date'].dt.strftime('%d-%b-%Y')

# Use the ag-grid library to create an interactive table
AgGrid(table, sortable=True, filter=True)

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in: dataframe
    out: href string
    """
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()
    output.seek(0)
    xlsx_data = output.getvalue()
    b64 = base64.b64encode(xlsx_data).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="AllData.xlsx">Download All Data in an .xlsx file</a>'
    return href

# this will display a download link for the above dataframe
st.markdown(get_table_download_link(df), unsafe_allow_html=True)