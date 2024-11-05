from models.schemas import TwitterActionRequest, TwitterActionResponse, ErrorResponse

def post_tweet(request: TwitterActionRequest) -> TwitterActionResponse:
    """Post a tweet to Twitter"""
    try:
        tweet_content = request.get("tweet_content")
        if tweet_content is None:
            return {"error": "Tweet content is required"}
        # client.create_tweet(text=tweet_content)  # Post the tweet
        return {"message": "Tweet posted successfully!"}
    except Exception as e:
        return {"error": f"Error posting tweet: {str(e)}"}

def retweet_tweet(request: TwitterActionRequest) -> TwitterActionResponse:
    """Retweet a tweet on Twitter"""
    try:
        tweet_id = request.get("tweet_id")
        if tweet_id is None:
            return {"error": "Tweet ID is required for retweeting"}
        # Add logic to retweet the tweet
        return {"message": "Tweet retweeted successfully!"}
    except Exception as e:
        return {"error": f"Error retweeting tweet: {str(e)}"}

def reply_to_tweet(request: TwitterActionRequest) -> TwitterActionResponse:
    """Reply to a tweet on Twitter"""
    try:
        tweet_id = request.get("tweet_id")
        reply_content = request.get("reply_content")
        if tweet_id is None or reply_content is None:
            return {"error": "Tweet ID and reply content are required for replying"}
        # Add logic to reply to the tweet
        return {"message": "Tweet replied to successfully!"}
    except Exception as e:
        return {"error": f"Error replying to tweet: {str(e)}"}

def like_tweet(request: TwitterActionRequest) -> TwitterActionResponse:
    """Like a tweet on Twitter"""
    try:
        tweet_id = request.get("tweet_id")
        if tweet_id is None:
            return {"error": "Tweet ID is required for liking"}
        # Add logic to like the tweet
        return {"message": "Tweet liked successfully!"}
    except Exception as e:
        return {"error": f"Error liking tweet: {str(e)}"}
