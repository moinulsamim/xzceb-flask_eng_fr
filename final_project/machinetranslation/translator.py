"""importing modules"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#authenticate
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
lt.set_service_url(url)


def english_to_french(english_text):
    """Translate from English to French"""
    translation = lt.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Translate from French to English"""
    translation = lt.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
