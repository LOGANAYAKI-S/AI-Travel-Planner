import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
def generate_travel_plan(start_location, destination, budget, days, travel_type):

    prompt = f"""
Create a travel itinerary.

Starting Location: {start_location}
Destination: {destination}
Budget: {budget}
Days: {days}
Travel Type: {travel_type}

Generate a detailed day-by-day travel plan.

Include:
- Places to visit
- Activities
- Food recommendations
- Travel tips

After the itinerary, suggest 3 suitable hotels based on the selected budget.

Also provide a packing checklist for the trip.

Also suggest 5 famous local foods that travelers should try at the destination.

Also provide an estimated trip cost.

Include:
- Hotel Cost
- Food Cost
- Transport Cost
- Activity Cost
- Total Estimated Cost

Show the cost in Indian Rupees (₹).
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
