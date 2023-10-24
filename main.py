import pandas as pd
import streamlit as st

# Main page
def main():
    # Page config
    st.set_page_config (
        page_title='Energy and Engagement Visualizer',
        layout='wide'
    )

    # Instantiate dataframe
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=['Date', 'Activity', 'Energy', 'Engagement', 'Time'])

    # Main body
    st.title('Energy and Engagement Visualizer')
    st.header('Data Input')

    # Activity submission form
    with st.form('data_input', clear_on_submit=True):
        
        # Entry parameters
        st.write('Please enter activity information.')
        activity = st.text_input('Activity name')
        date = st.date_input('Date')
        energy = st.slider('Enter energy level', 0, 5)
        engagement = st.slider('Enter engagement level', 0, 5)
        time = st.number_input('Enter elapsed time')

        # Submission
        submitted = st.form_submit_button("Submit")
        if submitted and activity:
            data_entry = {'Date': str(date), 'Activity': activity, 'Energy': energy, 'Engagement': engagement, 'Time': time}
            st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([data_entry])], ignore_index=True)
    
    # Display activity log
    st.header('Activity Log:')
    
    grouped_dataframe = st.session_state.data.groupby('Date')
    for date, group in grouped_dataframe:
        with st.expander(str(date), expanded=True):
            for index, row in group.iterrows():
                st.subheader(row['Activity'])
                st.write(f"- Energy Level: {row['Energy']}\n- Engagement: {row['Engagement']}\n- Time Spent: {row['Time']} hr(s)")
                st.divider()
    
    # Complete log
    st.header("Complete dataframe")
    st.write(st.session_state.data)

if __name__ == "__main__":
    main()