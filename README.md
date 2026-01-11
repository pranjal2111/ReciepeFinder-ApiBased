 🍽️ RecipeFinder Website

RecipeFinder is a web application that allows users to search for recipes based on ingredients using an external API. Built with Django, it provides a simple interface to explore and discover new dishes.

---

 📦 Project Structure

```
RecipeFinder-ApiBased/
├── app/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   └── receipes.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── receipe/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---
 🚀 Features

- Search for recipes using ingredients
- Fetch recipe data via external API
- Display results in a clean HTML interface
- Django-based backend with SQLite database

---

 🛠️ Installation

1. Clone the repository
   git clone https://github.com/pranjal2111/RecipeFinder-ApiBased.git
   cd RecipeFinder-ApiBased
   ```

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate
   On Windows: venv\Scripts\activate
   ```

4. Install dependencies
   pip install -r requirements.txt
   ```

5. Run migrations
   python manage.py migrate
   ```

6. Start the development server
   python manage.py runserver
   ```

---

 🌐 Usage

- Navigate to `http://127.0.0.1:8000/` in your browser.
- Enter ingredients to search for recipes.
- View results and explore recipe details.

---

 📁 Templates

- index.html: Homepage with search form
- receipes.html: Displays fetched recipes

---

 🙋‍♂️ Author

Pranjal Vejani  
GitHub: pranjal2111 
```

Would you like help writing the `requirements.txt` or adding API integration details next?
