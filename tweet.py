import os
import tweepy

from tweetcapture import TweetCapture
import asyncio

from constants import TWITTER_USER_ID
from llm import ClarifaiPrompter, ClarifaiTranslator
from upload import ClarifaiUploader

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

def clean_llm_output(raw_text: str) -> str:
    try:
        cleaned = raw_text.split('\"')
        if len(cleaned) <= 1:
            cleaned = raw_text.replace("\n\n", "")
        else:
            cleaned = cleaned[1]

        cleaned = cleaned.replace("\"", "")
        cleaned = cleaned.replace("Example:", "")
        cleaned = cleaned.replace("Here's a possible tweet:", "")
        cleaned = cleaned.replace("Tweet:", "")
    except:
        raise Exception("Raw output: %s, cleaned:%s" % (raw_text, str(cleaned)))
    return cleaned

def build_tweet_url(tweet_id:str) -> str:
    return "https://twitter.com/%s/status/%s" %(TWITTER_USER_ID, tweet_id)

def main(generate_only=False, tweet_only=False):
    """
    For each prompt, generate all language variants and upload.
    """
    prompter = ClarifaiPrompter()
    while True:
        output = prompter.predict()
        tweet = clean_llm_output(output)
        if len(tweet) < 280:
            break
    
    # initialize client only once.
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    ## https://github.com/xacnio/tweetcapture/blob/main/tweetcapture/examples/tweet_screenshot.py    
    tc = TweetCapture()

    translator = ClarifaiTranslator()
    for mid, mvid in translator.models.items():
        try:
            translated_tweet = translator.predict(tweet, model_id=mid, model_version_id=mvid)
        except:
            translated_tweet = tweet #default back to English.
        if generate_only:
            print(f"{translated_tweet=}")
            continue

        response = client.create_tweet(
            text=translated_tweet
        )
        tweet_id = response.data['id']
        print(f"Tweet ID: {tweet_id}")

        if tweet_only:
            exit()

        tweet_url = build_tweet_url(tweet_id)
        image_path = f"{tweet_id}.png"
        
        asyncio.run(tc.screenshot(tweet_url, image_path, mode=3, night_mode=0))
        ClarifaiUploader().upload(image_file_location=image_path)


if __name__ == "__main__":
    main(generate_only=False, tweet_only=False)