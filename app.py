import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah']

pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('IPL Win Predictor')
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the Batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling team', sorted(teams))

selected_city = st.selectbox('Select the City', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs')
with col5:
    wickets = st.number_input('Wickets')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = runs_left/balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city':[selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
                             'wickets': [wickets], 'total_runs_x': [score], 'crr': [crr], 'rrr': [rrr]})
    # st.table(input_df)

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header('Probablity of winning IPL')
    st.subheader(batting_team + ' - ' + str(round(win*100)) + '%')
    st.subheader(bowling_team + ' - ' + str(round(loss*100)) + '%')