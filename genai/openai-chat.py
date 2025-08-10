# create a file named .env in the root directory with the following content
#   OPENAI_API_KEY=your_openai_api_key_here
# This script uses the OpenAI API to interact with a chat model.
# Make sure you have the OpenAI Python package installed:
#   !pip install openai --quiet
#   !pip install openai python-dotenv --quiet

# Import necessary libraries
from openai import OpenAI
import os
from dotenv import load_dotenv
import markdown2

# Load api_key and use in your OpenAI client
load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")
print(f"api_key loaded from config file: {len(my_api_key)} Characters")
client = OpenAI(api_key=my_api_key)

# Takes a prompt and returns the response from the OpenAI API
def get_openai_response(user_input):
    """
    Interacts with the OpenAI API to generate a response for a given user prompt.

    Args:
        user_input (str): the user's message to generate a response for

    Returns:
        str: the response from the OpenAI API
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"An error occurred: {error}"

caption = "$ Ask me something (or 'quit' to end the program): "  

user_prompt = ""
while user_prompt != "quit":
    user_prompt = input(caption)

    if user_prompt != "quit":
        response = markdown2.markdown(get_openai_response(user_prompt))
        if response:
            print(f"OpenAI Response: {response}")
        else:
            print("No response received from OpenAI.")
print("Goodbye!")
