from deepface import DeepFace

def analyze_image(image_path):
    try:
        # Analyze image using DeepFace
        result = DeepFace.analyze(img_path=image_path, actions=['age', 'gender', 'race', 'emotion'])
        
        # Access the first dictionary in the list
        result = result[0]

        # Extract predictions
        age = result['age']
        gender = max(result['gender'], key=result['gender'].get)
        race = max(result['race'], key=result['race'].get)
        expression = max(result['emotion'], key=result['emotion'].get)
        
        # Store the concatenated result as a single string
        result_string = f"Age: {age}, Gender: {gender}, Race: {race}, Expression: {expression}"
        print("Predictions :", result_string)  # Print for debugging
        
        return result_string
    
    except Exception as e:
        print("Error analyzing image:", str(e))
        return str(e)

if __name__ == '__main__':
    # Specify the path to the image you want to analyze
    image_path = r'D:\dbms\image.jpg'
    
    predictions = analyze_image(image_path)
    print(predictions)  # Print predictions for debugging
