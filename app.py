import streamlit as st
from modules.travel_planner import generate_travel_plan
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️"
)

st.title("✈️ AI Travel Planner")

st.write("Plan your trip easily with AI Travel Planner.")
st.info("Enter your travel details to generate a travel plan.")


destination = st.text_input(
    "Enter Travel Destination"
)

budget = st.selectbox(
    "Select Budget",
    ["Low", "Medium", "High"]
)

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

if st.button("Generate Travel Plan"):

    if destination == "":

        st.warning("Please enter a destination.")

    else:

        st.success("Travel Plan Generated")

        st.write(f"📍 Destination: {destination}")
        st.write(f"💰 Budget: {budget}")
        st.write(f"📅 Duration: {days} Days")

        travel_plan = generate_travel_plan(
            destination,
            budget,
            days
        )

        st.subheader("AI Travel Plan")

        st.write(travel_plan)

        