from flask import Flask, request, jsonify, render_template
import subprocess
import base64
import os
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

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
        
        # Save image to 'static/uploads/image.jpg'
        upload_dir = os.path.join(app.root_path, 'static', 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        image_path = os.path.join(upload_dir, 'image.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_data)
        
        # Call ai_model.py with image data
        process = subprocess.Popen(
            ['python', 'D:/dbms/ai_model.py', image_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        
       
        
        # Capture the predictions from ai_model.py output
        result_string = stdout.decode().strip()
        print("Captured result:", result_string)  # Print for debugging
        
        # Return the result string directly as JSON response
        return jsonify({
            'result': result_string
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
