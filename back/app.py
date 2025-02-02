from flask import Flask, request, jsonify
import cohere
from datetime import datetime
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
mongo_uri = os.getenv("MONGO_URI")
mongo_uri = os.getenv("FRONTED_URL")
co = cohere.Client(cohere_api_key)



# MongoDB Setup
client = MongoClient(mongo_uri)
db = client["codeGenerator"]  
collection = db["snippets"] 

class CodeSnippet:
    def __init__(self, task, code_snippet, timestamp):
        self.task = task
        self.code_snippet = code_snippet
        self.timestamp = timestamp

# Function to generate a code snippet using Cohere ai
def generate_code_snippet(task):
    prompt = f"Write a Python function to {task}"
    response = co.generate(
        model="command-xlarge-nightly",  # Use a valid model name
        prompt=prompt,
        max_tokens=150
    )
    return response.generations[0].text.strip()



#  Flask app init
app = Flask(__name__)
CORS(app, origins=["https://aicode.sangammundhe.site"])


#  route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route('/generate_code', methods=['POST'])
def generate_code():
    task = request.json.get('task', '')
    
    if not task:
        return jsonify({"error": "Task is required"}), 400
    
    code_snippet = generate_code_snippet(task)
    timestamp = datetime.now()
    snippet_data = {
        "task": task,
        "code_snippet": code_snippet,
        "timestamp": timestamp
    }
    collection.insert_one(snippet_data)

    return jsonify({
        'task': task,
        'code_snippet': code_snippet,
        'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/get-tasks', methods=['GET'])
def get_all_tasks():
    tasks = collection.find()
    task_list = []
    for task in tasks:
        task_list.append({
            'task_id': str(task['_id']),
            'task': task['task'],
            'code_snippet': task['code_snippet'],
            'timestamp': task['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
        })
    return jsonify(task_list)




# # Run the app
# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    # Use host="0.0.0.0" to make sure the app is publicly available
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
