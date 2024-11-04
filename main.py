
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv
import tweepy
import os

from twitter_agent.state import State
from twitter_agent.tools import retweet_tweet,like_tweet,reply_to_tweet,post_tweet

load_dotenv()

# Twitter API credentials
bearer_token = os.getenv("bearer_token")
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)






# Initialize the StateGraph
graph_builder = StateGraph(State)

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)



tools = [
    post_tweet,
    retweet_tweet,
    reply_to_tweet,
    like_tweet,
]
llm_with_tools=llm.bind_tools(tools)

# Define the function to invoke LLM with tools
def llm_invoke(state: State):
    
    response = llm_with_tools.invoke(state["messages"])  # Pass the messages directly
    return {"messages": [response]}


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Agent:", value["messages"][-1].content)


# add nodes
graph_builder.add_node("llm_invoke", llm_invoke)
tool_node = ToolNode(tools=[post_tweet, retweet_tweet, reply_to_tweet, like_tweet])
graph_builder.add_node("tools", tool_node)


# add edges
graph_builder.add_conditional_edges(
    "llm_invoke",   
    tools_condition
)


graph_builder.add_edge("tools", "llm_invoke")
graph_builder.set_entry_point("llm_invoke")


# Compile the graph
graph = graph_builder.compile()



while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break