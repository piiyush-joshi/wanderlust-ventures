import streamlit as st 
import datetime
from openai import AzureOpenAI
 
client = AzureOpenAI(
  azure_endpoint = "ENTER_YOUR_ENDPOINT", 
  api_key="ENTER)YOUR_API_KEY",  
  api_version="ENTER_YOUR_API_VERSION"
)

st.set_page_config(page_title='Wanderlust Ventures', layout= "wide")


image_path = 'genai.png'
st.image(image_path, use_column_width=True)
def generate_itinerary(a):
    
    guid= """Do NOT halluicnate. Be Concise. You should generate any PII data of a user.    
    """
    
    prompt1 = f"""Act an expert in generating personas for people.
    You have details of peoples and what are they looking for from {a}. You have to create a persona around travel destinations in one sentence.
    You have to be cautious, as everyone has their own choice.
    follow: {guid}
    """
    
    response = client.chat.completions.create(
        model = "tegpoc4",
        messages=[
            {"role":"system","content":prompt1}
        ],
        temperature=0.4,
        max_tokens= 1000
    )
    persona = response.choices[0].message.content
    print(persona)
    
    guidelines = """Generate a catchy name for the travel as well and don't forget to mention it.Do not hallucinate. Be Concise."""
    
    prompt =f"""Act as an expert travel agent who provides the best itinerary accordingly to all age groups.
            An itinerary should be concise and should include everyday plans for {persona}.
            Analyze the preference and provide only the personalized itinerary related to the user's preferences.
            You should always start your itinerary from the user's home place.
            Follow guidelines: {guidelines}.
    """
    resp = client.chat.completions.create(
        model="ENTER_YOUR_MODEL_NAME",
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=1500
    )
    itinerary = resp.choices[0].message.content
    #print(itinerary)
    return itinerary

tab1, tab2 , tab3 = st.tabs(['Request Memo', 'Travel Preference', 'Your personalized Iternary'])

with tab1:
    title= 'User Details'
    subhead = "We from Wanderlust Ventures kindly request your participation in completing this form. Following your submission, our travel AI buddy will promptly create a comprehensive personalized itinerary for you on the NEXT TAB."
    
    st.markdown(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center;'><em>{subhead}<em></h4>", unsafe_allow_html=True)
    
        # Create the form
    with st.form(key='user_entry_form'):
        name = st.text_input(' Full Name')
        travelfrom = st.text_input("Your location ?")
        destination = st.text_input('What city are you traveling to?')
        noofpeople = st.text_input("How many people will be traveling?")
        noofdays = st.text_input("Enter no of days?")
        budget = st.text_input("Expected Budget (per person)")
        option = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Mobile Number"))
        if option == "Email":
            st.text_input("Please enter your Email.")
        else:
            st.text_input("Please enter your Mobile Number.")
        other = st.text_input("Is there additional information you would like us to know?")
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        st.write(f'Hey {name}, Good Choice on dream desitnation- {destination}. Hope you will have a great time there.')

    
    with tab2:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image("mountain.jpg", caption='Elevate Your Journey.')
            submit= st.button("Mountain Person? **Click here**")
            if submit:
                a = f" {name} has selected his preference as mountains for trekking who's tagline is Elevate Your Journey and {name} is from {travelfrom} & looking for a dream destination i.e. {destination} he/she has a budget of {budget}/person and will be traveling for {noofdays} with {noofpeople} peoples. "
                #print(a)
                with tab3:
                    mountain_itinerary= generate_itinerary(a)
                    st.header("**Personalized Itinerary.**")
                    st.write(mountain_itinerary)
            
        with col2:
            st.image("beach.jpg", caption= "Where Every Wave is an Invitation.")
            submit = st.button("Beach Person? **Click here**")
            if submit:    
                a = f" {name} have selected his preference as beaches and sea whose tagline is Where Every Wave is an Invitation and {name} is from {travelfrom} & looking for a various beaches around in. {destination} he/she has a budget of {budget}/person and will be traveling for {noofdays}  with {noofpeople} peoples."
                #print(a)
                with tab3:
                    mountain_itinerary= generate_itinerary(a)
                    st.header("**Personalized Itinerary.**")
                    st.write(mountain_itinerary)
            
        with col3:
            st.image("rdtp.jpg", caption="Hit the Road, Discover the Soul.")
            submit= st.button("RoadTrip? **Click here**")
            if submit:
                a = f" {name} has selected his preference as roadtrip whose tagline is Hit the Road, Discover the Soul. and {name} is from {travelfrom} & looking for a dream destination i.e. {destination} he/she has a budget of {budget}/person and will be traveling for {noofdays}  with {noofpeople} peoples."
                #print(a)
                with tab3:
                    mountain_itinerary= generate_itinerary(a)
                    st.header("**Personalized Itinerary.**")
                    st.write(mountain_itinerary)
                    
        with col4:
            st.image("culture.jpg", caption = "Journey Through Time, Uncover Cultural Treasures.")
            submit= st.button("History & Culture? **Click here**")
            if submit:
                a = f" {name} has selected his preferences as cultural and historical who's tagline is Embark on a Journey Through Time, Uncover Cultural Treasures and {name} is from {travelfrom} & looking for a dream destination i.e. {destination} he/she has a budget of {budget}/person and will be traveling for {noofdays}  with {noofpeople} peoples."
                #print(a)
                with tab3:
                    mountain_itinerary= generate_itinerary(a)
                    st.header("**Personalized Itinerary.**")
                    st.write(mountain_itinerary)
