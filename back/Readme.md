# Code Generator API 🚀

A Flask-based API that uses **AI** to generate Python code snippets based on user-provided tasks. The generated code snippets are stored in database

---

## 🔥 Features
✅ Generate Python code snippets using AI  
✅ Store code snippets in database
✅ Retrieve all previously generated tasks  
✅ CORS enabled for frontend integration  

---

## 🛠️ Technologies Used
- **Flask** (Python Web Framework)  
- **Cohere AI API** (For AI-based code generation)  
- **MongoDB Atlas** (Cloud-based NoSQL Database)  
- **Flask-CORS** (To allow frontend access)  

---

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/code-generator-api.git
cd code-generator-api
```


### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Setup Environment Variables**
Create a `.env` file and add your **Cohere API Key** & **MongoDB URI**:
```ini
COHERE_API_KEY=your-cohere-api-key
MONGO_URI=your-mongodb-uri
```

---

## 🎯 API Endpoints

### **✅ Test API**
```http
GET /hello
```
**Response:**
```json
{
  "message": "Hello, World!"
}
```

### **✅ Generate Code Snippet**
```http
POST /generate_code
```
**Request Body (JSON):**
```json
{
  "task": "reverse a string"
}
```
**Response:**
```json
{
  "task": "reverse a string",
  "code_snippet": "def reverse_string(s): return s[::-1]",
  "timestamp": "2024-02-02 12:00:00"
}
```

### **✅ Get All Generated Tasks**
```http
GET /get-tasks
```
**Response Example:**
```json
[
  {
    "task_id": "65d0a2...",
    "task": "reverse a string",
    "code_snippet": "def reverse_string(s): return s[::-1]",
    "timestamp": "2024-02-02 12:00:00"
  }
]
```

---

## 🏃‍♂️ Running the Project
Start the Flask server:
```sh
python app.py
```
The API will run at `http://127.0.0.1:5000`.



---

## 👨‍💻 Author
Developed by **Your Name**  
🔗 GitHub: [Your GitHub](https://github.com/sangam5756)  
🌐 Portfolio: [Your Portfolio](https://sangammundhe.site)  
```

---

### **✅ What This README Includes**
- 📌 **Project Overview**  
- 🔥 **Features**  
- 🛠️ **Technologies Used**  
- 🚀 **Setup & Installation** (Cloning, Virtual Env, Dependencies)  
- 🎯 **API Endpoints** (With examples)  
- 🏃‍♂️ **Running the Project**  
- 📌 **Deployment Instructions**  
- 💡 **Future Improvements**  
- 👨‍💻 **Author Info**  

---
