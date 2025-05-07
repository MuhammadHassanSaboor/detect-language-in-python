from langdetect import detect , DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return f"The Detected Language is: {language}"
    
    except LangDetectException:
        return "Could not detect a language"
    
    
text_input = input("Enter a text:  ")
print(detect_language(text_input))