import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# List of supported languages from deep_translator
supported_languages = {
    "af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "ar": "Arabic", "hy": "Armenian", 
    "az": "Azerbaijani", "eu": "Basque", "be": "Belarusian", "bn": "Bengali", "bg": "Bulgarian", 
    "ca": "Catalan", "ceb": "Cebuano", "ny": "Chichewa", "zh-cn": "Chinese (Simplified)", 
    "zh-tw": "Chinese (Traditional)", "hr": "Croatian", "cs": "Czech", "da": "Danish", 
    "nl": "Dutch", "en": "English", "et": "Estonian", "tl": "Filipino", "fi": "Finnish", 
    "fr": "French", "de": "German", "el": "Greek", "gu": "Gujarati", "ht": "Haitian Creole", 
    "he": "Hebrew", "hi": "Hindi", "hu": "Hungarian", "is": "Icelandic", "id": "Indonesian", 
    "ga": "Irish", "it": "Italian", "ja": "Japanese", "kn": "Kannada", "kk": "Kazakh", 
    "ko": "Korean", "ku": "Kurdish", "lo": "Lao", "lv": "Latvian", "lt": "Lithuanian", 
    "mk": "Macedonian", "ms": "Malay", "ml": "Malayalam", "mt": "Maltese", "mi": "Maori", 
    "mr": "Marathi", "mn": "Mongolian", "ne": "Nepali", "no": "Norwegian", "fa": "Persian", 
    "pl": "Polish", "pt": "Portuguese", "pa": "Punjabi", "ro": "Romanian", "ru": "Russian", 
    "sr": "Serbian", "si": "Sinhala", "sk": "Slovak", "sl": "Slovenian", "es": "Spanish", 
    "sw": "Swahili", "sv": "Swedish", "ta": "Tamil", "te": "Telugu", "th": "Thai", 
    "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "uz": "Uzbek", "vi": "Vietnamese", 
    "cy": "Welsh", "xh": "Xhosa", "yi": "Yiddish", "zu": "Zulu"
}

# Function to translate text
def translate_text():
    try:
        # Get input text
        text_to_translate = input_text.get("1.0", tk.END).strip()
        source_lang = source_language.get()
        target_lang = target_language.get()

        # Validate input
        if not text_to_translate:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        # Validate language selection
        if source_lang not in supported_languages.values() or target_lang not in supported_languages.values():
            messagebox.showerror("Language Error", "The selected languages are not supported.")
            return

        # Get language codes
        source_code = list(supported_languages.keys())[list(supported_languages.values()).index(source_lang)]
        target_code = list(supported_languages.keys())[list(supported_languages.values()).index(target_lang)]

        # Translate
        translator = GoogleTranslator(source=source_code, target=target_code)
        translated_text = translator.translate(text_to_translate)

        # Display translated text
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to clear input and output fields
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Enhanced Multi-Language Translator")
root.geometry("700x550")
root.configure(bg="#f0f8ff")  # Light blue background

# Title
title_label = tk.Label(root, text="Enhanced Language Translator", font=("Helvetica", 24), bg="#f0f8ff", fg="#333333")
title_label.pack(pady=20)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

# Input Label
input_label = tk.Label(input_frame, text="Enter Text:", font=("Helvetica", 14), bg="#f0f8ff")
input_label.grid(row=0, column=0, padx=10, pady=10)

# Text Box for Input
input_text = tk.Text(input_frame, height=6, width=60, font=("Helvetica", 12))
input_text.grid(row=0, column=1, padx=10, pady=10)

# Source Language Dropdown
source_label = tk.Label(input_frame, text="From Language:", font=("Helvetica", 14), bg="#f0f8ff")
source_label.grid(row=1, column=0, padx=10, pady=10)

source_language = ttk.Combobox(input_frame, values=list(supported_languages.values()), font=("Helvetica", 12))
source_language.grid(row=1, column=1, padx=10, pady=10)
source_language.current(0)  # Default to English

# Target Language Dropdown
target_label = tk.Label(input_frame, text="To Language:", font=("Helvetica", 14), bg="#f0f8ff")
target_label.grid(row=2, column=0, padx=10, pady=10)

target_language = ttk.Combobox(input_frame, values=list(supported_languages.values()), font=("Helvetica", 12))
target_language.grid(row=2, column=1, padx=10, pady=10)
target_language.current(1)  # Default to Gujarati

# Output Frame
output_frame = tk.Frame(root, bg="#f0f8ff")
output_frame.pack(pady=20)

# Output Label
output_label = tk.Label(output_frame, text="Translated Text:", font=("Helvetica", 14), bg="#f0f8ff")
output_label.grid(row=0, column=0, padx=10, pady=10)

# Text Box for Output
output_text = tk.Text(output_frame, height=6, width=60, font=("Helvetica", 12))
output_text.grid(row=0, column=1, padx=10, pady=10)

# Buttons
translate_button = tk.Button(output_frame, text="Translate", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=translate_text)
translate_button.grid(row=1, column=0, padx=20, pady=20)

clear_button = tk.Button(output_frame, text="Clear", font=("Helvetica", 14), bg="#f44336", fg="white", command=clear_text)
clear_button.grid(row=1, column=1, padx=20, pady=20)

# Run the GUI
root.mainloop()
