from flask import Flask, request, render_template
import spacy
from spacy import displacy
import random

# Load the trained NER model
nlp = spacy.load("model-best")

app = Flask(__name__)

# Function to generate random color
def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method == 'POST':
        # Check if a file is uploaded
        file = request.files.get('file')
        text = request.form.get('text', '')

        if file and file.filename:  # File input takes precedence
            # Read and decode the uploaded file
            readable_file = file.read().decode('utf-8', errors='ignore')
            processed_text = readable_file
        elif text:  # If no file, check for text input
            processed_text = text
        else:
            return render_template('index.html', error="No input provided. Please upload a file or enter text.")

        # Process the text through the NER model
        doc = nlp(processed_text)

        # Generate a random color for each entity type
        entity_colors = {}
        for ent in doc.ents:
            if ent.label_ not in entity_colors:
                entity_colors[ent.label_] = random_color()

        # Prepare the options for displacy with random colors
        options = {
            "colors": entity_colors
        }

        # Render the entities using displacy with page=True to output full HTML
        html = displacy.render(doc, style='ent', options=options, page=True, jupyter=False)

        # Return the template with the rendered HTML
        return render_template('index.html', html=html, text=processed_text)

if __name__ == '__main__':
    app.run(debug=False)
