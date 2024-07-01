from flask import Flask, request, jsonify, render_template
import base64
import os
from ai_model import analyze_image  # Import the function to analyze the image
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')

# MySQL Configuration
config = {
    'host': '127.0.0.1',
    'user': 'nimith',
    'password': '1234567890',
    'database': 'expression',  # Replace with your actual database name
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
    'autocommit': True
}
def insert_analysis_result(name, result_data):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Insert details into 'analysis_results' table
        query = "INSERT INTO analysis_results (name, result_data) VALUES (%s, %s)"
        cursor.execute(query, (name, result_data))

        # Commit the transaction
        connection.commit()

        cursor.close()
        connection.close()

        print(f"Successfully inserted analysis result for {name} into the database")

    except mysql.connector.Error as error:
        print(f"Error inserting analysis result for {name} into the database: {error}")


def fetch_analysis_results():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(dictionary=True)

        # Fetch all rows from 'analysis_results' table
        query = "SELECT id, name, result_data FROM analysis_results"
        cursor.execute(query)

        # Fetch all rows
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    except mysql.connector.Error as error:
        print(f"Error fetching analysis results from the database: {error}")
        return []

    
# Function to insert analysis result into database


# Serve the index.html page
@app.route('/')
def index():
    return render_template('index3.html')

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
        result_string = analyze_image(image_path)
        
        # Insert analysis result into database
        insert_analysis_result(name, result_string)
        
        # Return the result string directly as JSON response
        return jsonify({
            'result': result_string
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/database')
def show_database():
    # Fetch analysis results from database
    results = fetch_analysis_results()
    
    return render_template('database.html', results=results)    

if __name__ == '__main__':
    app.run(debug=True)
