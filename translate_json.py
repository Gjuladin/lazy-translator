import json
import sys
from googletrans import Translator, LANGUAGES
from concurrent.futures import ThreadPoolExecutor
import time

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        if translation and translation.text:
            return translation.text
        else:
            print(f"Warning: No translation returned for '{text}'")
            return text
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text  # Fallback to the original text in case of error

def translate_dict(data, dest_language):
    translated_data = {}
    keys = list(data.keys())
    values = list(data.values())
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda val: translate_value(val[1], dest_language, val[0]), enumerate(values, 1)))
    
    translated_data = dict(zip(keys, results))
    return translated_data

def translate_value(value, dest_language, index):
    if isinstance(value, dict):
        return translate_dict(value, dest_language)
    elif isinstance(value, str):
        translated_value = translate_text(value, dest_language)
        print(f'Translating {index}')
        return translated_value
    elif value == "":
        translated_value = translate_text(" ", dest_language).strip()
        print(f'Translating {index} (empty string)')
        return translated_value
    else:
        return value

def translate_json(input_file, output_file, dest_language):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    translated_data = translate_dict(data, dest_language)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python translate_json.py <input_file> <output_file> <target_language>")
        sys.exit(1)

    input_file = sys.argv[1]  # Path to your input JSON file
    output_file = sys.argv[2]  # Path to your output JSON file
    dest_language = sys.argv[3]  # Target language code (e.g., 'es' for Spanish, 'fr' for French)

    if dest_language not in LANGUAGES:
        print(f"Error: Invalid language code '{dest_language}'")
        sys.exit(1)

    start_time = time.time()
    translate_json(input_file, output_file, dest_language)
    end_time = time.time()
    print(f"\nTranslation completed in {end_time - start_time:.2f} seconds.")
