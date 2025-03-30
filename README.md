
# Career Recommender

A Django-based project for career recommendations using machine learning.

## Installation

### 1. Clone the Repository
```sh
git clone (https://github.com/Allan-Saud/Career-Recommendation-System.git)
cd career-recommender
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```

Activate the virtual environment:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add:
```env
HF_token=your_huggingface_token_here
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Run the Server
```sh
python manage.py runserver
```

### 7. Access the Application
Open your browser and visit:
```
http://127.0.0.1:8000/
```

## Project Structure
To successfully run the project, ensure the following directory structure is maintained:
```
career_recommender/
│-- career_recommender/
│-- recommender/
│   │-- __pycache__/
│   │-- migrations/
│   │-- models/
│   │   │-- best_career_recommendation_model.pkl
│   │   │-- label_encoder.pkl
│   │   │-- scaler.pkl
│   │-- templates/recommender/
│   │   │-- index.html
│   │   │-- result.html
│   │-- __init__.py
│   │-- admin.py
│   │-- apps.py
│   │-- forms.py
│   │-- models.py
│   │-- tests.py
│   │-- views.py
│-- db.sqlite3 (optional)
│-- manage.py
│-- requirements.txt
│-- .env (not included in Git)
│-- venv/ (not included in Git)
```

## Notes
- Ensure `.env` is set up correctly before running the project.
- If `.pkl` files are missing, you may need to download or train the model.
- For database persistence, keep `db.sqlite3`, otherwise, create a fresh one using `migrate`.
- The directory structure must match the format above for the project to work correctly.

## Contribution
Feel free to contribute by forking the repository and submitting pull requests!

## License
This project is open-source. Modify and use as needed!

