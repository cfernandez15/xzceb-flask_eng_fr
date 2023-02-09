import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']
version = '2019-04-30'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2019-04-30',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

print(englishToFrench('Yes'))
print(frenchToEnglish('Oui'))