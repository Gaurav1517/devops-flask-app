#  TASK 4: Build a Version-Controlled DevOps Project with Git

> Objective: Manage a DevOps project using Git best practices

---

##  PART 1: Setup the Base Flask Project

###  Step 1.1: Project structure

Create the folder:

```bash
mkdir devops-flask-app
cd devops-flask-app
```

Structure:

```
devops-flask-app/
├── app.py
├── .env
├── requirements.txt
├── README.md
├── .gitignore
```

---

###  Step 1.2: app.py

```python
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, from Python Flask app!</p>"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

---

###  Step 1.3: .env

```env
PORT=5000
```

---

###  Step 1.4: requirements.txt

```txt
Flask==2.1.2
python-dotenv==0.19.2
Werkzeug==2.0.3
```

---

###  Step 1.5: .gitignore

```gitignore
__pycache__/
*.pyc
.env
venv/
*.log
.DS_Store
```

---

### 🔹 Step 1.6: README.md

````markdown
# DevOps Flask App

A simple Python Flask app used to demonstrate DevOps practices with Git, Docker, and GitHub Actions.

## Run the App

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
````

## Git Branches

* `main`: Production
* `dev`: Development
* `feature/*`: Feature branches

## CI/CD

CI/CD is handled using GitHub Actions.

````

---

##  PART 2: Initialize Git and Push to GitHub

###  Step 2.1: Initialize Git repo

```bash
git init
git add .
git commit -m "Initial commit with base Flask app"
````

---

###  Step 2.2: Create GitHub repo

* Go to GitHub
* Create a repo named `devops-flask-app`
* **Do NOT initialize with README**

---

###  Step 2.3: Connect local repo

```bash
git remote add origin https://github.com/Gaurav1517/devops-flask-app.git
git branch -M main
git push -u origin main
```

---

###  Step 2.4: Create branches

```bash
git checkout -b dev
git push -u origin dev
```

---

##  PART 3: Dockerize the Flask App

###  Step 3.1: Create `Dockerfile`

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

###  Step 3.2: Commit Dockerfile

```bash
git add Dockerfile
git commit -m "Add Dockerfile to containerize Flask app"
git push origin dev
```

---

###  Step 3.3: Merge to `dev` via PR

* Go to GitHub
* Open Pull Request: `feature/pre-prod` → `dev`
* Merge it

---

##  PART 4: Add CI/CD via GitHub Actions

###  Step 4.1: Create CI branch

```bash
git checkout -b feature/pre-prod
git push -u origin feature/pre-prod
```

---

###  Step 4.2: Create GitHub Actions workflow

Path: `.github/workflows/main.yaml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: 3.10

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Flask App Test
      run: |
        python app.py &
        sleep 5
        curl --fail http://localhost:3000
```

---

###  Step 4.3: Commit and push CI

```bash
git add .github/workflows/main.yaml
git commit -m "Add GitHub Actions CI/CD workflow"
git push origin feature/pre-prod
```

---

###  Step 4.4: Merge to `dev`

* Go to GitHub
* PR from `feature/pre-prod` → `dev`
* Ensure workflow runs and passes
* Merge

---

##  PART 5: Release Production Version

###  Step 5.1: Merge dev → main

```bash
git checkout main
git merge dev
git push origin main
```

---

###  Step 5.2: Create Git tag

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

##  Final Deliverables

| File/Folder                   | Purpose                     |
| ----------------------------- | --------------------------- |
| `app.py`                      | Flask app                   |
| `.env`                        | Environment config          |
| `requirements.txt`            | Dependencies                |
| `Dockerfile`                  | Docker container definition |
| `.github/workflows/main.yaml` | GitHub Actions pipeline     |
| `.gitignore`                  | Ignore Python & env files   |
| `README.md`                   | Project documentation       |

---
