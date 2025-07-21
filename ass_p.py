import streamlit as st
st.header('BMI calculator')

weight = st.number_input('enter your weight in KGs')
height = st.number_input('enter your height in feet')


bmi_btn =st.button('show BMI')


if bmi_btn:

    bmi = weight/((height/3.28)**2)

    if bmi<16:
        st.error('Extremely Underweight!')
    elif bmi>=16 and bmi<18.5:
        st.warning('Underweight')
    elif bmi>=18.5 and bmi<25:
        st.success('Healthy guy , keep it up')
    elif bmi>=25 and bmi<30:
        st.info('Overweight')
    elif bmi>=30:
        st.error('Extremely Overweight')