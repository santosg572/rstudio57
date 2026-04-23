from deep_translator import GoogleTranslator

# Translate from English to Spanish
translated = GoogleTranslator(source='en', target='es').translate("Hello, how are you?")
print(translated)  # Output: Hola, ¿cómo estás?


