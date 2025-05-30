# Custom Named Entity Medical Text Analyzer

A web-based application for extracting and highlighting key medical entities—such as diseases, pathogens, and medications—from raw clinical text using a custom-trained Named Entity Recognition (NER) model in Python. Built with Flask and SpaCy, this project demonstrates modern NLP techniques applied to the healthcare domain.

---

## 🚀 Features

- **Custom Medical NER:** Accurately identifies pathogens, conditions, and medicines from unstructured medical text.
- **Interactive Web Interface:** Easy-to-use web app built with Flask.
- **Domain-Specific Training:** NER model trained on a medical text corpus for improved accuracy vs. generic models.
- **Visual Entity Highlighting:** Extracted entities are color-coded in the UI for instant comprehension.
- **Upload & Analyze:** Paste text or upload files for analysis.
- **API Ready:** Exposes endpoints for integration with other healthcare applications.
- **English Language (International Ready):** All code and UI in English—easy to localize for Poland/EU.

---

## 🎯 Use Cases

- Automating clinical documentation and EHR annotation
- Supporting biomedical research and academic projects
- Accelerating information extraction for healthcare analytics
- Demonstrating AI/ML skills for job applications

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **NLP/ML:** SpaCy (custom model training)
- **Frontend:** HTML5, Bootstrap
- **Visualization:** Custom highlighting, Chart.js (optional for stats)
- **Deployment:** Compatible with Heroku, Render, etc.

---

## 🏁 Getting Started

1. **Clone this repository**
git clone https://github.com/Alibalio/medical-ner-analyzer.git
cd medical-ner-analyzer


2. **Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt


4. **Download SpaCy model and train or load the custom NER model**
python -m spacy download en_core_web_sm

Place your custom model in the /model directory if available


5. **Run the Flask server**

python app.py



6. **Access the web app**
- Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📊 Screenshots

*Add screenshots of your app interface here (input form, entity highlight results, charts, etc.)*

---

## 📦 API Usage

The analyzer also provides a simple API for programmatic access.

- **POST** `/analyze`
 - **Input:** Raw text (`text` field)
 - **Output:** JSON with extracted entities

Example:
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text":"Patient has malaria and was prescribed paracetamol."}'

📝 Project Structure

medical-ner-analyzer/
│
├── app.py               # Main Flask application
├── model/               # Custom NER model
├── static/
├── templates/           # Jinja2 HTML templates
├── requirements.txt
├── README.md
└── ...

🤝 Contributing

Pull requests and suggestions are welcome!
For significant changes, please open an issue first to discuss your ideas.

📬 Contact
Author: Alibalio

Email: davidalibalio5@email.com

LinkedIn: linkedin.com/in/yourprofile
