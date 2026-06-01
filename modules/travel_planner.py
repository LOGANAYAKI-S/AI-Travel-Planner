from groq import Groq

client = Groq(api_key="Your_Grog_API_Key")

def generate_travel_plan(destination, budget, days):

    prompt = f"""
    Create a travel itinerary.

    Destination: {destination}
    Budget: {budget}
    Days: {days}

    Give a day-by-day travel plan.
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