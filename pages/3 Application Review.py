import streamlit as st


def uat_page():
    st.header('User Acceptance Testing')

    st.write(
        'Please answer the following questions about the music genre classifications system:')

    q1 = 'Was the system easy to use?'
    q2 = 'Did the system accurately classify songs into the correct genres?'
    q3 = 'Did you encounter any bugs or technical issues while using the system?'
    q4 = 'Should the system add new genres for prediction?'
    q5 = 'Did the system provide helpful error messages when necessary?'
    q6 = 'Were the loading times for the system acceptable?'

    answers = {}
    answers[q1] = st.radio('Question 1: ' + q1, ['Yes', 'No'])
    answers[q2] = st.radio('Question 2: ' + q2, ['Yes', 'No'])
    answers[q3] = st.radio('Question 3: ' + q3, ['Yes', 'No'])
    answers[q4] = st.radio('Question 4: ' + q4, ['Yes', 'No'])
    answers[q5] = st.radio('Question 5: ' + q5, ['Yes', 'No'])
    answers[q6] = st.radio('Question 6: ' + q6, ['Yes', 'No'])

    st.write('Thank you for completing the User Acceptance Testing!')
    st.write('Your answers:', answers)


if __name__ == '__main__':
    uat_page()
