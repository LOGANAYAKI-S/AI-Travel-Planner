import streamlit as st
from modules.travel_planner import generate_travel_plan
from pdf_generator import create_pdf

st.set_page_config(
page_title="AI Travel Planner",
page_icon="✈️",
layout="wide"
)

st.markdown("""

<style>

.main {
    background-color: #F5F9FF;
}

h1 {
    color: #0066CC;
    text-align: center;
}

.stButton > button {
    background-color: #0099FF;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 250px;
    font-size: 18px;
}

.stDownloadButton > button {
    background-color: #28A745;
    color: white;
    border-radius: 12px;
}

</style>

""", unsafe_allow_html=True)

st.title("🌍✈️ Smart AI Travel Planner")

st.markdown(
"### Plan your dream trip with AI assistance"
)

st.info("Enter your travel details to generate a travel plan.")

st.subheader("🌍 Trip Details")

col1, col2 = st.columns(2)

with col1:
    start_location = st.text_input(
    "📍 Starting Location"
    )

with col2:
    destination = st.text_input(
    "🌍 Travel Destination"
    )

col3, col4 = st.columns(2)

with col3:
    budget = st.selectbox(
    "💰 Select Budget",
    ["Low", "Medium", "High"]
    )

with col4:
    travel_type = st.selectbox(
    "👤 Travel Type",
    [
    "Solo",
    "Family",
    "Friends",
    "Couple",
    "Business"
    ]
    )

col5, col6 = st.columns(2)

with col5:
    transport = st.selectbox(
    "🚗 Preferred Transport",
    [
    "Car",
    "Bus",
    "Train",
    "Flight"
    ]
    )

with col6:
    days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=30,
    value=3
    )

if st.button("🚀 Generate Travel Plan"):


    if destination == "":

        st.warning("Please enter a destination.")

    else:

        st.success("✅ Travel Plan Generated Successfully")

        st.write(f"📍 Starting Location: {start_location}")
        st.write(f"📍 Destination: {destination}")
        st.write(f"💰 Budget: {budget}")
        st.write(f"👤 Travel Type: {travel_type}")
        st.write(f"🚗 Transport: {transport}")
        st.write(f"📅 Duration: {days} Days")

        travel_plan = generate_travel_plan(
            start_location,
            destination,
            budget,
            days,
            travel_type
        )

        pdf_file = create_pdf(travel_plan)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download Travel Plan PDF",
                data=file,
                file_name="travel_plan.pdf",
                mime="application/pdf"
            )

        st.subheader("🗺️ Your Personalized Travel Plan")

        st.markdown(travel_plan)

