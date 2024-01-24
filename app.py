
import os
from flask import Flask, jsonify, render_template
# from openai import OpenAIAPI
from flask_cors import CORS  # Import CORS
from plagariasm import check_plagiarism
import ai 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    
# Example Usage:
    aiDecision =  ai.openAi("Jonh","Wick","Rabbit","Kishor","Pema")
    directory_path = r'C:\Users\Asus\Downloads\Plagiarism-checker-Python-master\Plagiarism-checker-Python-master\Bootcamp\converted-text'
    file_extension = '.txt'
    student_files = [os.path.join(directory_path, doc) for doc in os.listdir(directory_path) if os.path.splitext(doc)[1] == file_extension]

    plagiarism_results = check_plagiarism(student_files)
  
    # Print plagiarism results
    # Print plagiarism results
    # Print plagiarism results
    plagiarism_detected = False

    for result, sim_score in plagiarism_results.items():
        if sim_score >0.8:
            print('Plagiarism detected between', result[0], 'and', result[1], 'with similarity score:', sim_score)
            print("Plagiarism is detected")
            plagiarism_detected = True

    if not plagiarism_detected:
        print('Not detected')
        plagiarism_detected = False
    # Your Python logic to generate or retrieve data
    data = {'detected' : plagiarism_detected,
            'simScore' : sim_score,
            "aiDecisions" : aiDecision
            };
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



