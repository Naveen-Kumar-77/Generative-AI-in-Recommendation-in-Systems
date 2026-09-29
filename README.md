# Generative AI in Recommendation Systems

A Django-based web application for exploring how generative AI techniques such as GANs, VAEs, and hybrid models can improve recommendation systems, especially for synthetic data generation, cold-start handling, and diversity enhancement.

## Features

- User registration and login
- Admin login and user management
- Recommendation system concept interface powered by generative AI
- PDF export of generated outputs
- Django templates and SQLite database setup

## Tech Stack

- Python
- Django
- SQLite
- Google Gemini API
- xhtml2pdf
- HTML/CSS

## Project Structure

```text
RecommendationSystems/
├── Recommendation_Systems/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── admins/
├── users/
├── templates/
├── static/
├── media/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Naveen-Kumar-77/Generative-AI-in-Recommendation-in-Systems.git
cd Generative-AI-in-Recommendation-in-Systems
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

- Windows:

```bash
venv\Scripts\activate
```

- Linux/macOS:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Set your Gemini API key:

```bash
set GOOGLE_API_KEY=your_api_key_here
```

or

```bash
$env:GOOGLE_API_KEY="your_api_key_here"
```

6. Run the project:

```bash
python manage.py runserver
```

7. Open the app in a browser:

```text
http://localhost:8000/
```

## Usage

- Navigate to the home page
- Register a user
- Login as a user
- Open the Generative AI recommender section
- Submit a recommendation task and view the generated output

## Notes

- This project uses the Google Generative AI SDK and requires a valid API key.
- The app is designed for academic/demo usage and can be extended for production deployment.

## License

This project is for educational and academic use.
