from string import Template

## For the LLM Prompting
USER_ID = 'meta'
APP_ID = 'Llama-2'
MODEL_ID = 'llama2-70b-chat'
MODEL_VERSION_ID = '6c27e86364ba461d98de95cddc559cb3'

GLOBAL_LINK = 'https://www.clarifai.com/blog/clarifai-release-9.8'

PROMPT_TEMPLATE = Template("Prepare a tweet to promote Clarifai's 9.8 Release highlight: $highlight. Only output the raw text of the tweet without any instructions or any preamble. Include the hashtags '$hashtags'. Include the link $link. Limit the tweet to 260 characters.")
PROMOTION_HASHTAG_LINK_TUPLES = [
    ("new Python SDK as a Developer Preview", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model Llama2-70b-chat, a fine-tuned Llama-2 LLM that is optimized for dialogue use cases", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model Claude-Instant-1.2, a fast, versatile, and cost-effective LLM with improved math, coding, reasoning, and safety capabilitie.", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model StarCoder, an LLM excelling in code completion, modification, and explanation, specifically focused on Python", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model Stable Diffusion XL, a text-to-image generation model that excels in producing highly detailed and photorealistic 1024x1024 images", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model RedPajama-INCITE-7B-chat, an LLM that excels in chat-related tasks", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model Whisper, an audio transcription model for converting speech audio to text", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model ElevenLabs Speech Synthesis", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model GCP Chirp ASR, a state-of-the-art, speech-to-text, speech recognition model developed by Google Cloud", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model AssemblyA, a speech recognition model that can quickly turn pre-recorded audio into text, achieving human-level accuracy in just seconds", "#Clarifai #GenerativeAI #Developer"),
    ("new Community model Dolly-v2-12b, a 12 billion parameter causal LLM created by Databricks", "#Clarifai #GenerativeAI #Developer"),
    ("AI Assist on Input-Viewer screen", "#Clarifai #GenerativeAI #Developer"),
    ("Smart Object Search", "#Clarifai #GenerativeAI #Developer"),
    ("Evluation Leaderboard", "#Clarifai #GenerativeAI #Developer"),
    ("Local model upload UI", "#Clarifai #GenerativeAI #Developer"),
    ("Filter inputs by data types", "#Clarifai #GenerativeAI #Developer"),
    ("Hotkeys in annotation tools", "#Clarifai #GenerativeAI #Developer")
]

PROMPTS = [
    PROMPT_TEMPLATE.safe_substitute(
        highlight=tup[0], 
        hashtags=tup[1],
        link=GLOBAL_LINK
    ) for tup in PROMOTION_HASHTAG_LINK_TUPLES
]

## For building the HTML
TWITTER_USER_ID='isaacchung1217'

## For uploading the screenshot to clarifai
UPLOAD_USER_ID = 'Isaac'
UPLOAD_APP_ID = 'tweet-screenshots-98'
