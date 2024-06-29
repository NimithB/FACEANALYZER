from deepface import DeepFace
import sys

def process_image(image_path):
    try:
        print(f"Analyzing image: {image_path}")
        
        # Analyze image using DeepFace
        result = DeepFace.analyze(img_path=image_path, actions=['age', 'gender', 'race', 'emotion'])
        print("Analysis result:", result)
        
        # Access the first dictionary in the list
        result = result[0]

        # Extract predictions
        age = result['age']
        gender = max(result['gender'], key=result['gender'].get)
        race = max(result['race'], key=result['race'].get)
        expression = max(result['emotion'], key=result['emotion'].get)
        
        predictions = {
            'age': age,
            'gender': gender,
            'race': race,
            'expression': expression
        }
        
        return predictions
    
    except Exception as e:
        print("Error analyzing image:", str(e))
        return {'error': str(e)}

if __name__ == '__main__':
    # Specify the path to the image you want to analyze
    image_path = r'D:\dbms\image.jpg'
    
    
    predictions = process_image(image_path)
    
    if 'error' in predictions:
        print(predictions['error'])
    else:
        # Print predictions
        print(f"Age: {predictions['age']}")
        print(f"Gender: {predictions['gender']}")
        print(f"Race: {predictions['race']}")
        print(f"Expression: {predictions['expression']}")


