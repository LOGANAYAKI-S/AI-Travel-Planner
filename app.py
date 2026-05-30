import streamlit as st

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️"
)

st.title("✈️ AI Travel Planner")

st.write("Plan your trip easily with AI Travel Planner.")

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

        st.subheader("Suggested Plan")

        st.write(
            f"Explore popular attractions in {destination}. "
            f"Plan your trip for {days} days and manage expenses within your {budget.lower()} budget."
        )