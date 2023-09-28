from string import Template

## For the LLM Prompting
USER_ID = 'meta'
APP_ID = 'Llama-2'
MODEL_ID = 'llama2-70b-chat'
MODEL_VERSION_ID = 'acba9c1995f8462390d7cb77d482810b'

TRANSLATE_USER_ID = 'facebook'
TRANSLATE_APP_ID = 'translation'
TRANSLATE_MODEL_IDS = {
    'translation-english-to-urdu-text': '2bfef71f85274a70ab89dfb6132c424f', 
    'translation-english-to-zulu-text': '757c23362ff040438a7ec196fa54f065', 
    'translation-english-to-chinese-text': '50818c1b93f7463eb9151c174dbb19f7', 
    'translation-english-to-yoruba-text': '4c978c790b5d4d5e8d8296c04984b05c', 
    'translation-english-to-yiddish-text': 'bdfa1dc41f3841d586210cdbcf84b8bb', 
    'translation-english-to-xhosa-text': '2dc47a1f8e0b470d8ef0b6a9a24753a2', 
    'translation-english-to-wolof-text': 'cd397a947abb4ab99ae7a0c711645847', 
    'translation-english-to-vietnamese-text': '8f14dcd00b1144cfa69c84397e9fd787', 
    'translation-english-to-uzbek-text': '828a08ac80144111921cdd9d2037cf7d', 
    'translation-english-to-ukrainian-text': 'fb68450a852549a1949d3aa73ef5cc56', 
    'translation-english-to-turkish-text': '33856f0ac9004c40afc8195d7bd98037', 
    'translation-english-to-tswana-text': '30f9202b88904311b5d8110ef4b070d0', 
    'translation-english-to-tagalog-text': 'd84c83b0c8784f13bc264f91bb30ed2d', 
    'translation-english-to-thai-text': '4d3727215968444eaa8da1527a7f8549', 
    'translation-english-to-tamil-text': '389105a3050b4e91968ca47bf69df233', 
    'translation-english-to-swahili-text': '8546b58d366e4f2f9af7e0bdbd73763f', 
    'translation-english-to-swedish-text': 'a22b2e78171b40019ff0331959f96bfc', 
    'translation-english-to-sundanese-text': '662967d3c4ed4a079bd78c8a7620ab2c', 
    'translation-english-to-swati-text': '633267976caf4670b3d252d7f9ca59f9', 
    'translation-english-to-serbian-text': '858a37b21bc345e897a5dfa74a5409f2', 
    'translation-english-to-albanian-text': '76154f03c0174e17bb4d12ac4ae480ca', 
    'translation-english-to-somali-text': 'f698617020c5407ca057e92dbf7e5145', 
    'translation-english-to-slovenian-text': '18788a856d56438f8f76d7b347b59209', 
    'translation-english-to-slovak-text': '7ed067ae3e964f63a1efa9b46aff349a', 
    'translation-english-to-sinhala-sinhalese-text': 'cf1a80870bb54ce7af8997ac8138fc09', 
    'translation-english-to-sindhi-text': 'd79029f39f6948d9873696de6ac4e36b', 
    'translation-english-to-russian-text': 'e56b09a88a3545b08e69e626e76c46d1', 
    'translation-english-to-romanian-moldavian-text': 'ebc62f2c18b74a71ac265bdd3387ffbd', 
    'translation-english-to-portuguese-text': '3d7ec8bc51ca4572a52a18f00b868573', 
    'translation-english-to-pushto-pashto-text': '4dbfd9b01a7a40bca309c314fb8ba4b2', 
    'translation-english-to-polish-text': '084ad252dc144a3b945cc2be0b86c07f', 
    'translation-english-to-panjabi-punjabi-text': 'cb6bae72a8ec4cb5b634e488a2cc2e47', 
    'translation-english-to-oriya-text': 'b6d35185d5cf46298c4a4b55bcfb5c71', 
    'translation-english-to-occitan-text': '4300cb7024294fe4abf8c6bd036ebe91', 
    'translation-english-to-northern-sotho-text': 'd801f455d242440ca375b04274bf8ea8', 
    'translation-english-to-norwegian-text': '554dc84c56534184bbaa9926466603de', 
    'translation-english-to-dutch-flemish-text': '4d7f0073d6ce442ea949f6c0395e287d', 
    'translation-english-to-nepali-text': '069be59c008d40eba0e195c843cb678d', 
    'translation-english-to-burmese-text': 'f696b7405c924b5b9d3f1f5930541ec5', 
    'translation-english-to-malay-text': '3b7793c56c45400babfcf41282acb51f', 
    'translation-english-to-marathi-text': '1494942870bc471c86cc7315f953592e', 
    'translation-english-to-mongolian-text': 'd661a68d35f34e82b0d36b2f5ffbcd41', 
    'translation-english-to-malayalam-text': '97e7bd80cc68471f89410f0bfcc1e420', 
    'translation-english-to-macedonian-text': '0a767eef523243aaa5bb2d8cc868455a', 
    'translation-english-to-malagasy-text': '65503adbaefb451694872126f76c5e9b', 
    'translation-english-to-latvian-text': 'a92138a8a2544c09a94853bbfa59a7df', 
    'translation-english-to-lithuanian-text': '1ed7ee87287c498ab4ec6a8436fb7701', 
    'translation-english-to-lao-text': '76038b393245473aa6d470a304571691', 
    'translation-english-to-lingala-text': '563d2b68450c4a5cac801aa8a96028d8', 
    'translation-english-to-ganda-text': 'e02d3b078989421480aa484ec77d6343', 
    'translation-english-to-luxembourgish-text': '683ed6351bc94520b1711b96f1e3c41c', 
    'translation-english-to-korean-text': '990d38daa90c4235b9cd65f0c76b06a0', 
    'translation-english-to-kannada-text': '6f15df3cf1994badaed5089ddcf0e3c1', 
    'translation-english-to-central-khmer-text': '43ccde5bb0ff4ea786dd77a8e53d1fb7', 
    'translation-english-to-kazakh-text': '2539fa3e17cd4646973c5cc871ccc99c', 
    'translation-english-to-georgian-text': 'a5e6eb45f343433ea1a3542f4f76aef7', 
    'translation-english-to-javanese-text': '90684ab948a143839f7e969a43552786', 
    'translation-english-to-japanese-text': '16bf635764804873860faf9344e29ee1', 
    'translation-english-to-italian-text': 'cb973e72b8df47819d05da7348126c88', 
    'translation-english-to-icelandic-text': 'bcdb4afaa4df4283a7d6027edac00451', 
    'translation-english-to-iloko-text': '90dacae5b83b4e74bccc089e698f6b82', 
    'translation-english-to-igbo-text': '63c1023dad0f4916a7df67f674c0b44c', 
    'translation-english-to-indonesian-text': '05f3ca1af28f4203a011620836e1718a', 
    'translation-english-to-armenian-text': '05b730c72b0244dcb72b51a62686c41a', 
    'translation-english-to-hungarian-text': '152aea75542642f59dd3c7756c242fab', 
    'translation-english-to-haitian-haitian-text': '34639c9ac0e8481e879b79e6a7cce5b4', 
    'translation-english-to-croatian-text': 'e258633c76894362b68e91ae3ce3dc7e', 
    'translation-english-to-hindi-text': 'b8187ffcd6284bec92f7bd32b4909a4f', 
    'translation-english-to-hebrew-text': '119f085fcc45443f82acfff3364ffaf1', 
    'translation-english-to-hausa-text': 'd0a4ee80e0e24614a310ed090ae8206a', 
    'translation-english-to-gujarati-text': '39f783c03e974fc38a640550dce40a09', 
    'translation-english-to-galician-text': 'a4cacb436d78423ab0d1481a5dd28cf6', 
    'translation-english-to-gaelic-scottish-text': '43c67663f793427690c01b4d0cf792cc', 
    'translation-english-to-irish-text': '8ff93d29afdf403dadbf3a6b11eebf6b', 
    'translation-english-to-western-frisian-text': '95686e6b959c4e2fa01fa90e15e41a8a', 
    'translation-english-to-french-text': 'c65a4a51c2b646fca5f0e4bf1ff200d7', 
    'translation-english-to-finnish-text': '5b8003d16d5b4b6398b16f0eff126666', 
    'translation-english-to-fulah-text': '47ca8b77bfd642b288c8a926cda34c44', 
    'translation-english-to-persian-text': 'fe1800614d0041c986e41d142d0af83e', 
    'translation-english-to-estonian-text': 'b73a8df37f6747c9badd9c1b412d8343', 
    'translation-english-to-spanish-text': '0fc872ec19724e1f964dd260945ed861', 
    'translation-english-to-greeek-text': '346245ae191a445092e456adb31ac68c', 
    'translation-english-to-german-text': '109b92ac34a348a68903d9a9f2be7fd6', 
    'translation-english-to-danish-text': '159154fcc704459980c6afd0646cb83a', 
    'translation-english-to-welsh-text': '0a6cd6a28fc643829998a6e666440813', 
    'translation-english-to-czech-text': 'd38f3d2e42f443e1b3737b7d7528a4b0', 
    'translation-english-to-cebuano-text': '4e8ec14738c64029a03fdc8fce78d9ef', 
    'translation-english-to-catalan-valencian-text': 'bd19937e39dd4558912d912060e31f84', 
    'translation-english-to-bosnian-text': '485068ac0bb040b488c305bdf6d22aa6', 
    'translation-english-to-breton-text': '7ca6a46e6acc412399e567c72435e359', 
    'translation-english-to-bengali-text': '2c5a8bc71d9743f293ed645355a69f63', 
    'translation-english-to-bulgarian-text': '8eb0d9841c91431caf8fe5d8661eb97c', 
    'translation-english-to-belarusian-text': 'ca9b28ed8bd84bb0b139cb8677936683', 
    'translation-english-to-bashkir-text': 'af4690bf9fa74d1e9cfd0db812c43361', 
    'translation-english-to-azerbaijani-text': '0740808356854838a09943362652f2d4', 
    'translation-english-to-asturian-text': 'df9733df5e594b6797748892ba1f6be0', 
    'translation-english-to-arabic-text': '510688015a764cd38923476acabe7c3c', 
    'translation-english-to-amharic-text': '49c38513c1484aacbd02ca55a6b562e4', 
    'translation-english-to-afrikaans-text': '1f609170ee3c47f89beb899b29e142ad'
}

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
