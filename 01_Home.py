import pandas as pd
import streamlit as st
import datetime

# Main page
def main():
    # Page config
    st.set_page_config (
        page_title='Energy and Engagement Visualizer',
        layout='wide'
    )
    def load_user_input_data():
        try:
            data = pd.read_csv('user_data.csv')
        except FileNotFoundError:
            data = pd.DataFrame(columns=['Date', 'Time', 'Activity', 'Energy', 'Engagement', 'Elapsed', 'Flow'])
        return data
    # Instantiate dataframe
    if 'data' not in st.session_state:
        st.session_state.data = load_user_input_data()

    # Main body
    st.title('Energy and Engagement Visualizer')
    st.header('Data Input', divider='gray')

    # Activity submission form
    with st.form('data_input', clear_on_submit=True):
        
        # Entry parameters
        st.write('Please enter activity information.')
        activity = st.text_input('Activity name')
        date = st.date_input('Date')
        time = st.time_input('Time')
        energy = st.slider('Enter energy level', 0, 5)
        engagement = st.slider('Enter engagement level', 0, 5)
        elapsed = st.number_input('Enter elapsed time')
        flow = st.checkbox('Flow?')

        # Re-format datetime variables
        new_date = date.strftime('%Y/%m/%d')
        new_time = time.strftime('%I:%M %p')
        
        # Submission
        submitted = st.form_submit_button("Submit")
        if submitted:
            if not activity:
                st.error('Please enter an activity name.', icon='🚨')
            elif ((st.session_state.data['Date'] == new_date) & (st.session_state.data['Time'] == new_time)).any():
                st.error('Please enter a date/time that does not overlap with another activity.', icon='🚨')
            else:
                data_entry = {'Date': new_date, 'Time': new_time, 'Activity': activity, 'Energy': energy, 'Engagement': engagement, 'Elapsed': elapsed, 'Flow': flow}
                st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([data_entry])], ignore_index=True)
    
    # Display activity log
    st.write('##')
    st.write('##')
    st.header('Activity Log:', divider='gray')
    
    grouped_dataframe = st.session_state.data.sort_values(by=['Time']).groupby('Date')
    for date, group in grouped_dataframe:
        st.subheader(date)
        with st.expander('Expand/collapse', expanded=True):
            for index, row in group.iterrows():
                st.subheader(f"[{row['Time']}] - {row['Activity']}")
                st.write(f"- Energy Level: {row['Energy']}\n- Engagement: {row['Engagement']}\n- Time Spent: {row['Elapsed']} hr(s)\n- Flow? {row['Flow']}")
                if st.button(f"Delete Entry {index}"):
                    delete_entry_by_index(index)
                st.divider()
    
    # Complete log
    st.write('##')
    st.write('##')
    st.header("Complete dataframe", divider='gray')
    st.write(st.session_state.data)
    if st.session_state.data is not None:
        st.session_state.data.to_csv('user_data.csv', index=False)

if __name__ == "__main__":
    main()