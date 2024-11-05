from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import ToolNode, tools_condition
from agent.twitter_actions import post_tweet, retweet_tweet, reply_to_tweet, like_tweet
from models.schemas import State
from config import google_api_key



llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key
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
    
    response = llm_with_tools.invoke(state["messages"])  
    return {"messages": [response]}


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Agent:", value["messages"][-1].content)

graph_builder = StateGraph(State)

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