from flask import Flask, request, jsonify, render_template
import subprocess
import base64
import os

app = Flask(__name__, template_folder='templates')

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to receive image data and call AI model
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get image data and name from POST request
        data = request.get_json()
        
        # Validate input data
        if 'image' not in data or 'name' not in data:
            return jsonify({'error': 'Invalid request format'}), 400
        
        data_url = data['image']
        name = data['name']
        
        # Extract base64 image data
        base64_str = data_url.split(',')[1]
        image_data = base64.b64decode(base64_str)
        
        # Call ai_model.py with image data
        process = subprocess.Popen(
            ['python', 'D:/dbms/ai_model.py'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=image_data)
        
        if stderr:
            return jsonify({'error': stderr.decode()}), 500
        
        # Parse predictions from ai_model.py output
        predictions = stdout.decode().strip().split('==, ')
        if len(predictions) != 4:
            return jsonify({'error': 'Invalid predictions format'}), 500

        age, gender, race, expression = [p.strip('==') for p in predictions]
        
        # Return predictions as JSON response
        return jsonify({
            'name': name,
            'age': age,
            'gender': gender,
            'race': race,
            'expression': expression
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
