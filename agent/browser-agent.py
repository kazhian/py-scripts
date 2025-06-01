# Mermaid diagram for the agent-browser interaction
# ```mermaid
# flowchart TD
#     A[Python Code] --> |Instantiates| B[Agent]
#     B --> |Asks_Steps| C[LLM]
#     C --> |Generates_Query| B
#     B --> |using| D[Browser-Use Library]
#     D --> |Launches| E[Chrome Browser]
#     E --> |Extractes_Data| B
#     B --> |"Parsed_Data"| A

## Before you run this code, make sure you have the necessary environment set up.
# create a file named .env in the root directory with the following content
#   OPENAI_API_KEY=your_openai_api_key_here

# Make sure you have below packages installed: 
# pip install browser-use
# playwright install chromium --with-deps --no-shell

from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

async def main():
    try:
        agent = Agent(
            task="Goto Github.com and getthe list of repositories from the profile kazhian",
            llm=llm,
        )
        result = await agent.run()
        print(f'--- printing the result---')
        print(result.extracted_content())
        print(f'--- Printing END ---')
    except Exception as e:
        print(f"Error: {str(e)}")

asyncio.run(main())
