import streamlit as st 
import datetime

st.set_page_config(page_title='Wanderlust Ventures', layout="wide")

name = "Wanderlust Ventures 🌍✈️"
tag = "Journey Beyond Boundaries!"
st.markdown(f"<h1 style='text-align: center;'>{name}</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'><em>{tag}<em></h3>", unsafe_allow_html=True)

tab1, tab2 , tab3 = st.tabs(['Request Memo', 'Who are you ?', 'Your personalized Iternary'])

with tab1:
    st.title('User Details')
    st.subheader("**We kindly request your participation in completing this form. Following your submission, your travel AI buddy will promptly create a comprehensive quote in the next slide.**")

    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)
        # Create the form
    with st.form(key='user_entry_form'):
        name = st.text_input(' Full Name')
        destination = st.text_input('What city are you traveling to?')
        noofpeople = st.text_input("How many people will be traveling?")
        d = st.date_input(
            "Select your vacation period.",
            (jan_1, datetime.date(next_year, 1, 7)),
            jan_1,
            dec_31,
            format="MM.DD.YYYY",
        )
        budget = st.text_input("Expected Budget (per person)")
        option = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone"),
            index=None,
            placeholder="Select contact method...",
            )
        other = st.text_input("Is there additional information you would like us to know?")
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        st.write(f'Hey {name}, Good Choice on dream desitnation- {destination}. Hope you will have a great time there.')

    
    with tab2:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image("mountain.jpg", caption='Elevate Your Journey')
            submit= st.button("Mountain Person? **Click here**")
            if submit:
                st.write(f"hey {name}")
            
            
        with col2:
            st.image("beach.jpg", caption= "Where Every Wave is an Invitation")
            submit = st.button("Beach Person? **Click here**")
            
        with col3:
            st.image("rdtp.jpg", caption="Hit the Road, Discover the Soul.")
            submit= st.button("RoadTrip? **Click here**")