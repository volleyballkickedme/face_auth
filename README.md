# FastAPI Face Recognition Backend

This repository contains a FastAPI backend for face recognition. It processes uploaded images, compares them against a database of known faces, and returns whether a match is found.

---

## **Features**
- Upload an image via an API endpoint.
- Compares uploaded faces against a database of known faces.
- Returns a JSON response indicating if a match is found.

---

## **Requirements**
- Python 3.9 or later
- Docker (optional for containerized setup)

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/fastapi-face-recognition-backend.git
cd fastapi-face-recognition-backend
```

---

### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate
```

---

### **3. Install Dependencies**
Install the Python dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### **4. Prepare the Database**
Add images of known faces to the `database/` directory. Supported formats:
- `.jpg`
- `.jpeg`
- `.png`

---

### **5. Run the Application**
Run the FastAPI application:
```bash
uvicorn app.backend:app --host 0.0.0.0 --port 8000 --reload
```

Access the API documentation at:
```
http://127.0.0.1:8000/docs
```

---

## **Using Docker**

### **1. Build the Docker Image**
Build the Docker image for the backend:
```bash
docker build -t face-recognition-backend .
```

---

### **2. Run the Docker Container**
Run the container:
```bash
docker run -it --rm -p 8000:8000 face-recognition-backend
```

Access the API documentation at:
```
http://127.0.0.1:8000/docs
```

---

## **API Endpoint**

### **POST /process-image**

- **Description**: Upload an image to check for matches in the database.
- **Request**:
  - Form-data:
    - `file`: The image file to process.
- **Response**:
  - **Success**: JSON response indicating a match.
    ```json
    {
      "message": "Match found: Person 0 in database."
    }
    ```
  - **Error**: JSON response with an error message.
    ```json
    {
      "message": "Image contains 2 faces. Only one face is allowed."
    }
    ```

---

## **Notes**
1. The `user_inputs/` folder is ignored in the repository and used for testing only.
2. For any issues or improvements, create an issue or pull request.

---