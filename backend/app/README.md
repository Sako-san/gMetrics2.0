
# Baseball Data API

This project provides a Flask-based API to interact with a SQLite database containing baseball statistics. The application fetches data from **FanGraphs** and **Statcast** using the `pybaseball` library and allows querying the data via RESTful API endpoints.

---

## **Project Structure**

```
project-folder/
│
├── app/                    # Flask app
│   ├── __init__.py         # Initializes the Flask app
│   ├── routes.py           # Defines API routes
│   ├── database.py         # Database connection logic
│   └── static/             # Optional: Static files (CSS, JS)
│   └── templates/          # Optional: HTML templates
│
├── baseball-dump.db        # SQLite database
├── manage.py               # Entry point for running the Flask app
└── requirements.txt        # Python dependencies
```

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone <your-repository-url>
cd project-folder
```

### **2. Create and Activate a Virtual Environment**

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Running the Application**

### **Start the Flask App**
Run the following command from the root of the project:
```bash
python manage.py
```

The app will run in **development mode** by default. Access it in your browser at:
```
http://127.0.0.1:5000
```

---

## **Pausing and Killing the Process**

### **Pause the Application**
To stop the Flask app temporarily, press `CTRL + C` in the terminal where it's running.

### **Kill the Flask Process**
If the app is running in the background, you can find and kill it:

#### **On macOS/Linux:**
1. Find the process:
   ```bash
   ps aux | grep manage.py
   ```
2. Kill the process:
   ```bash
   kill <process-id>
   ```

#### **On Windows:**
1. Find the process:
   ```bash
   tasklist | findstr manage.py
   ```
2. Kill the process:
   ```bash
   taskkill /PID <process-id> /F
   ```

---

## **Available API Endpoints**

### `/` (GET)
- **Description**: Welcome message.

### `/players` (GET)
- **Description**: Fetches a list of distinct player names.

### `/stats/<player_name>` (GET)
- **Description**: Fetches statistics for the specified player.

Example usage:
```
GET http://127.0.0.1:5000/stats/Mike%20Trout
```

---

## **Development Tips**

### **Update Dependencies**
If you add new Python libraries, update `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### **Linting and Formatting**
Use `flake8` or `black` to keep your code clean:
```bash
pip install flake8 black
black .
```

---

## **Future Improvements**
- Add user authentication using Flask-Login.
- Integrate a frontend framework like React or Vue.
- Deploy to production using platforms like Heroku, AWS, or Render.

---

## **License**
This project is open-source and available under the [MIT License](LICENSE).
