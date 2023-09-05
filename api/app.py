from flask import Flask, render_template, request
import googletrans

app = Flask(__name__,template_folder='templates')

class TranslatorApp:

    def __init__(self):
        self.translator = googletrans.Translator()

    def _getting_key(self, val):
        for key, value in googletrans.LANGUAGES.items():
            if val == value:
                return key
        return "key doesn't exist"

@app.route('/', methods=['GET', 'POST'])
def translate():
    app_instance = TranslatorApp()

    if request.method == 'POST':
        option = request.form['language']

        text = request.form['text']
        translated = app_instance.translator.translate(text, dest=app_instance._getting_key(option))
        return render_template('result.html', translation=translated.text)

    return render_template('index.html', languages=tuple(googletrans.LANGUAGES.values()))

if __name__ == '__main__':
    app.run(debug=True)
