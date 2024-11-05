
from typing import Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages



class State(TypedDict):
    messages: Annotated[list, add_messages] 

class TwitterActionRequest(TypedDict, total=False):
    """Schema for Twitter action requests, with optional fields to handle various actions."""
    tweet_content: Optional[str]  # For posting a tweet
    tweet_id: Optional[str]       # For retweeting, replying, or liking
    reply_content: Optional[str] 


class TwitterActionResponse(TypedDict):
    """Schema for Twitter action responses."""
    message: str    


class ErrorResponse(TypedDict):
    """Schema for an error response."""
    error: str    

