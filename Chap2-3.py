# C:\Users\ephra\Documents\myScript\Streamlit>C:\Users\ephra\anaconda3\Scripts\activate.bat
# (base) C:\Users\ephra\Documents\myScript\Streamlit>activate py314
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>
# (py314) C:\Users\ephra\Documents\myScript\Streamlit>streamlit run firstScript.py

import streamlit as st
import sympy as sp
import pandas as pd
import numpy as np
import json
import graphviz
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff
from streamlit_bokeh import streamlit_bokeh
from bokeh.plotting import figure
import pydeck as pdk

st.title("My First Streamlit App")

name = st.text_input("請輸入你的名字")

if name:
    st.write(f"Hello, {name}!")

st.title("Animal Selection", anchor="animal-selection")
st.text('''請選擇你喜歡的動物：''')
options = ["狗", "貓", "兔子", "鳥"]
selected_animal = st.selectbox("選擇動物", options)
if selected_animal:
    st.write(f"你選擇了：{selected_animal}")

st.subheader("喜歡的Programming Language")
languages = ["Python", "JavaScript", "Java", "C++", "Go"]
selected_language = st.selectbox("選擇你喜歡的程式語言", languages)
if selected_language:    
    st.write(f"你喜歡的程式語言是：{selected_language}")

python_cides = [
    "print('Hello, World!')",
    "for i in range(5):\n    print(i)",
    "def greet(name):\n    return f'Hello, {name}!'"
]
st.subheader("Python Code Examples")
for code in python_cides:
    st.code(code, language="python") 

st.subheader("SymPy Example")
x = sp.symbols('x')
expression = sp.sin(x) + sp.cos(x)
st.write("Expression:")
st.latex(sp.latex(expression))
derivative = sp.diff(expression, x)
st.write("Derivative:")
st.latex(sp.latex(derivative)) 
st.write("Derivative evaluated at x=0:")
st.latex(sp.latex(derivative.subs(x, 0)))
st.latex(r"\int \sin(x) \, dx = -\cos(x) + C")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
st.subheader("Data Frame")
st.write(df)

dataSeries = {
    "Python": [100, 90, 80],
    "JavaScript": [80, 70, 60],
    "Java": [60, 50, 40],
    "C++": [40, 30, 20],
    "Go": [20, 10, 5]
}

df_series = pd.DataFrame(dataSeries, index=["Alice", "Bob", "Charlie"])
st.subheader("Programming Language Proficiency")
st.write(df_series)

st.subheader("Programming Language Proficiency2")
st.table(df_series)

st.subheader('income statistics')
st.metric(label="Average Income", value="$50,000", delta="$5,000")
st.subheader('Temperature')
c1,c2,c3 = st.columns(3)
c1.metric(label="Current Temperature", value="25°C", delta="-2°C")
c2.metric(label="High Temperature", value="30°C", delta="+3°C")
c3.metric(label="Low Temperature", value="20°C", delta="-1°C")

with open("json_data.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

st.subheader("JSON Data")
st.json(json_data)


sales_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    '1 Sales': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
    '2 Sales': [1100, 1400, 2100, 2400, 3100, 3600, 4100, 4600, 5100, 5600, 6100, 6600],
    '3 Sales': [1200, 1300, 2200, 2300, 3200, 3700, 4200, 4700, 5200, 5700, 6200, 6700],
    '4 Sales': [1300, 1200, 2300, 2200, 3300, 3800, 4300, 4800, 5300, 5800, 6300, 6800],
    '5 Sales': [1400, 1100, 2400, 2100, 3400, 3900, 4400, 4900, 5400, 5900, 6400, 6900],
    '6 Sales': [1500, 1000, 2500, 2000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
}   

index = pd.Series(sales_data['Month'])
df_sales = pd.DataFrame(sales_data, index=index)

st.header("Monthly Sales Data")
st.line_chart(df_sales.drop(columns=['Month']))

st.subheader("set x parameter")
st.line_chart(df_sales, x='Month')

st.subheader("set y parameter")
st.line_chart(df_sales.drop(columns=['Month']), y=['1 Sales','3 Sales','5 Sales'])

st.subheader("Bar Chart")
st.bar_chart(df_sales, y=['2 Sales','4 Sales','6 Sales'])

st.subheader("Area Chart")
st.area_chart(df_sales, y=['1 Sales','2 Sales','3 Sales','4 Sales','5 Sales','6 Sales'])

df = pd.DataFrame(np.random.randn(10, 2)/[20,50]+[25.03,121.5], columns=['latitude', 'longitude'])
df.index.name = 'id'
st.subheader("Map")
st.dataframe(df[1:5])

st.map(df)

graph = graphviz.Digraph()

graph.edge('A', 'B')
graph.edge('A', 'C')
graph.edge('B', 'D')
graph.edge('C', 'D')

st.subheader("Graph Visualization")
st.graphviz_chart(graph)

st.subheader("Graph Visualization2")
st.graphviz_chart('''
digraph {
    A -> B
    A -> C
    B -> D
    C -> D
}
''')    

plt.rcParams['font.family'] = 'Microsoft JhengHei'
store1 =[100, 150, 200, 250, 300, 350, 400, 410, 520, 550, 600, 650]
store2 =[110, 140, 210, 240, 310, 360, 410, 460, 510, 660, 620, 660]
store3 =[120, 130, 220, 230, 320, 370, 420, 470, 540, 670, 620, 600]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

fig, ax = plt.subplots()
ax.plot(months, store1, label='Store 1')
ax.plot(months, store2, label='Store 2')
ax.plot(months, store3, label='Store 3')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Monthly Sales Data')
plt.xticks(rotation=90)
ax.legend()
st.subheader("Sales Chart")
st.pyplot(fig)


fig2, ax2 = plt.subplots()
bar_labels = ['Store 1', 'Store 2', 'Store 3']
bar_values = [sum(store1)-3000, sum(store2)+1700, sum(store3)-1300]

ax2.bar(bar_labels, bar_values, color=['blue', 'orange', 'green'], label=bar_labels)
ax2.set_xlabel('Store')
ax2.set_ylabel('Total Sales')
ax2.set_title('Total Sales by Store')
ax2.legend(title='Stores')

st.subheader("Total Sales by Store")
st.pyplot(fig2)

plt.rcParams['font.family'] = 'Microsoft JhengHei'
fig3, ax3 = plt.subplots()
ax3.fill_between(months, store1, color='blue', alpha=0.5, label='Store 1')
ax3.fill_between(months, store2, color='orange', alpha=0.5, label='Store 2')
ax3.fill_between(months, store3, color='green', alpha=0.5, label='Store 3')
ax3.set_xlabel('Month')
ax3.set_ylabel('Sales')
ax3.set_title('Monthly Sales Data') 
plt.xticks(rotation=90)
ax3.legend(loc='upper left')
st.subheader("Area Chart")
st.pyplot(fig3)


rnds = np.random.randint(1,7, size =1000)
df = pd.DataFrame(rnds, columns=['Dice Rolls'])
df.index.name = 'id'
st.subheader("Dice Rolls")
st.write(df.head(10))

fig4, ax4 = plt.subplots()
sns.set_theme(style="whitegrid")
sns.histplot(df['Dice Rolls'], bins=np.arange(0.5, 7.5, 1), kde=False, color='blue', ax=ax4)
ax4.set_xlabel('Dice Value')
ax4.set_ylabel('Frequency')
ax4.set_title('Distribution of Dice Rolls')

st.subheader("Distribution of Dice Rolls")
st.pyplot(fig4)

xa = np.arange(100)

source = pd.DataFrame({
    'x':xa,
    'f(x)': np.sin(xa/10) + np.random.normal(0, 0.1, size=100)
})

source.index.name = 'id'
st.subheader("Source Data")
st.write(source.head(10))

line_chart = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
)
st.subheader("Line Chart with Altair")
st.altair_chart(line_chart, use_container_width=True)

# heatmap
x, y = np.meshgrid(range(-5,5), range(-5,5))
z = x ** 2 + y ** 2

source = pd.DataFrame({
    'x': x.flatten(),
    'y': y.flatten(),
    'z': z.flatten()
})
source.index.name = 'id'
st.subheader("Heatmap Data")
st.write(source.head(10))

heatmap = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)
st.subheader("Heatmap with Altair")
st.altair_chart(heatmap, use_container_width=True)

#plotly chart
x1 = np.random.randn(1000) -2
x2 = np.random.randn(1000)
x3 = np.random.randn(1000) +2
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
bin_size = [.1, .25, .5, .75]
fig5 = ff.create_distplot(hist_data, group_labels, bin_size=bin_size, show_hist=True, show_rug=False)
fig5.update_layout(title='Distribution of Random Data', xaxis_title='Value', yaxis_title='Density')
st.subheader("Distribution of Random Data with Plotly")
st.plotly_chart(fig5, use_container_width=True)


x = np.linspace(-10, 10, 500)

y = 8 * np.sin(x) + 5 * np.cos(x/2) + 3 * np.random.normal(0, 1, size=x.shape)
p = figure(title="Bokeh Line Chart", x_axis_label='x', y_axis_label='f(x)')
p.line(x, y, line_width=2, color='blue', legend_label='f(x)')
p.legend.location = "top_left"
p.background_fill_color = "#f0f0f0"
streamlit_bokeh(p, use_container_width=True, theme="streamlit", key="my_unique_key")



chart_data = pd.DataFrame(
    np.random.rand(1000, 2)/ [50,50] + [39.9, 116.4],
    columns=['lat', 'lon'])

initial_view_state = pdk.ViewState(
    latitude=39.9,
    longitude=116.4,
    zoom=11,
    pitch=50,
)

layer_hexagon = pdk.Layer(
    'HexagonLayer', 
    data=chart_data,
    get_position='[lon, lat]',
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

layer_scatter = pdk.Layer(
    'ScatterplotLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=100,
)

pdk_chart = pdk.Deck(
    layers=[layer_hexagon, layer_scatter],
    initial_view_state=initial_view_state,
    tooltip={"text": "Count: {elevationValue}"},
)

st.pydeck_chart(pdk_chart, use_container_width=True)
