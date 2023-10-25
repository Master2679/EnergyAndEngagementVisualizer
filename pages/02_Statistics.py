import pandas as pd
import streamlit as st
import plotly.express as px

# Chart for printing stats by activity type
def ActivityStats(data, dependent):
    df = data
    activities = df['Activity'].str.split(',\s*').explode().unique().tolist()
    variable = [0] * len(activities)
    count = [0] * len(activities)

    for index, row in df.iterrows():
        pos = activities.index(row['Activity'])
        variable[pos] += row[dependent]
        count[pos] += 1
    
    for i in range(len(variable)):
        variable[i] /= count[i]
    
    fig = px.bar(labels=dict(x='Activity', y=dependent))
    fig.add_bar(x=activities, y=variable)
    return fig
    
# Page config
st.set_page_config (
    page_title='Energy and Engagement Visualizer',
    layout='wide'
)

# Instantiate dataframe
st.title('Statistics')
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Activity', 'Energy', 'Engagement', 'Time', 'Flow'])

if st.session_state.data.empty:
    st.write('No statistics to display')

else:
    st.subheader('Average Energy by Activity')
    st.write(ActivityStats(st.session_state.data, 'Energy'))

    st.subheader('Average Engagement by Activity')
    st.write(ActivityStats(st.session_state.data, 'Engagement'))