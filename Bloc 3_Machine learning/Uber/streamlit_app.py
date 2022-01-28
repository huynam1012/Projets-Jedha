import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
from PIL import Image

st.set_page_config(layout="wide")

# prepare the sidebar options
daysofweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = [i for i in range(0, 24)]

date_select = st.sidebar.date_input(
    label = 'Select the date:',
    value = datetime.date(2014, 4, 1),
    min_value = datetime.date(2014, 4, 1),
    max_value = datetime.date(2014, 9, 30)
)

# transform the datetime.date object to retrieve dayofweek, month and dayofmonth
dayofweek = date_select.strftime("%A")
month = date_select.strftime("%B")
dayofmonth = date_select.strftime("%d")

# create a slider to select the hour of the day we want to visualize
hour_select = st.sidebar.select_slider(
    label = 'Select the hour of the day (0h-23h):',
    options = hours
)

# create a checkbox to choose whether or not to display the DBSCAN outliers on the scattermapbox
show_outliers_Db = st.sidebar.checkbox(
    label = 'Show outliers DBSCAN',
    value = False
)

# load the data based on the inputs
dir1 = f"data/DBSCAN_month_day_hour_manhattan/{month}/{dayofweek}.csv"
data1 = pd.read_csv(dir1, index_col=0, parse_dates=[0])
data1.rename(columns = {col:col.lower() for col in data1.columns}, inplace = True)

dir2 = f"data/Kmean_month_day_hour/{month}/{dayofweek}.csv"
data2 = pd.read_csv(dir2, index_col=0, parse_dates=[0])
data2.rename(columns = {col:col.lower() for col in data2.columns}, inplace = True)

# create the masks from the selected features
hour_mask1 = data1['hour'] == hour_select
day_mask1 = data1['dayofweek'] == dayofweek
month_mask1 = data1['month'] == month
outlier_mask1 = data1['db_clusters'] != -1

hour_mask2 = data2['hour'] == hour_select
day_mask2 = data2['dayofweek'] == dayofweek
month_mask2 = data2['month'] == month


# build the plots to be displayed

# plot the clustered data with or without the outliers
if show_outliers_Db:
    mask1 = hour_mask1 & day_mask1 & month_mask1
    plot_db = px.scatter_mapbox(data1.loc[mask1], lat = "lat",  lon = "lon", color = 'db_clusters',
                                mapbox_style='carto-positron', width=700, height=400, zoom = 9.2)
else:
    mask1 = hour_mask1 & day_mask1 & month_mask1 & outlier_mask1
    plot_db = px.scatter_mapbox(data1.loc[mask1], lat = "lat", lon = "lon", color = 'db_clusters',
                                mapbox_style='carto-positron', width=700, height=400, zoom = 9.2)


plot_db.update_layout(margin={'l':15, 'r':10, 'b':10, 't':40}, coloraxis_colorbar=dict(title="DBSCAN-clusters"))

# plot the unclustered data with transparancy
mask2 = hour_mask2 & day_mask2 & month_mask2
plot_k_mean = px.scatter_mapbox(data2.loc[mask2], lat = 'lat', lon = 'lon', mapbox_style='carto-positron', 
                                color = 'db_clusters', width=700, height=400, zoom = 9.2)

plot_k_mean.update_layout(margin={'l':15, 'r':10, 'b':10, 't':40}, coloraxis_colorbar=dict(title="K-Mean-clusters"))



# plot the histogram of uber pickups for the selected date
hour_counts = data1.groupby(by = 'hour', as_index=False)['hour'].count()
colors = ['blue'] * hour_counts.shape[0]
colors[hour_select] = 'red'
x = hour_counts.index
y = hour_counts['hour']

barchart = go.Figure(
    data = [
        go.Bar(
            x = x,
            y = y,
            marker_color = colors,
            text = y,
            textposition = 'auto',
        )
    ]
)

barchart.update_layout(
    height = 500,
    xaxis = dict(
        title = 'Hour of the day',
        titlefont_size = 16,
        tickfont_size = 16,
        type = 'category'
    ),
    yaxis = dict(
        title='Number of pick-ups',
        titlefont_size = 16,
        tickfont_size = 16
    )
)

# build the webpage
header = st.container()
description = st.expander(label = 'Project description', expanded = False)
clustering = st.container()
bars = st.container()



with header:
    st.title("Uber pick-ups in New-York city")
    st.text(f"Selected date and time: {dayofweek}, {dayofmonth} {month} between {hour_select}:00h and {hour_select + 1}:00h ")

with description:
        st.markdown("The goals of Uber pick-ups project is to find out where are the hot-zones that drivers should be in.<br> \
                    Available data are selected per **day** and **time** from **May** to **September 2014**.<br> \
                    **K-mean** algorithm with <ins>5 clusters</ins> was performed on latitude and longitude data for each hour of each day.<br> \
                    **DBSCAN** algorithm with an <ins>epsilon = 0.5, min_sample = 8 and the manhattan metric</ins> was performed on latitude and longitude data for each hour of each day.<br> \
                    <br> On the left, the **sidebar** can be used to select the date and time that you want to display. <br> \
                    The DBSCAN outliers can be showed by ticking the `show outliers DBSCAN` box.", unsafe_allow_html=True)
                    

with clustering:
    all_data, clustered_data = st.columns(2)

    all_data.header("K-mean method")
    all_data.text("Plot of all the data.")
    all_data.plotly_chart(plot_k_mean, use_container_width=True)

    clustered_data.header("DBSCAN method")
    if show_outliers_Db:
        clustered_data.text("Plot of the data with the outliers.")
    else:
        clustered_data.text("Plot of the data without the outliers.")
    clustered_data.plotly_chart(plot_db, use_container_width=True)


with bars:
    st.header("Barchart of Uber pickups")
    st.text("Number of pickups per hour for the given date")
    st.plotly_chart(barchart, use_container_width=True)


