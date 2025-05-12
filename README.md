# FACEANALYZER

**FACEANALYZER** is a web-based application designed to analyze facial expressions using AI-driven models. Built with Python and Flask, it allows users to upload images, detects faces, and classifies emotions, storing the results in a MySQL database for further analysis.

## 🧠 Features

* **Facial Expression Detection**: Utilizes AI models to identify and classify emotions from facial images.
* **Image Upload Interface**: User-friendly web interface to upload and analyze images.
* **Result Storage**: Stores analysis results in a MySQL database for record-keeping and further processing.
* **Real-time Feedback**: Provides immediate analysis results upon image submission.

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS (Jinja2 templates)
* **Backend**: Python (Flask)
* **Database**: MySQL
* **AI/ML**: Custom-trained models for facial expression recognition

## 🚀 Getting Started

### Prerequisites

* Python 3.7 or higher
* pip (Python package manager)
* MySQL Server([Hugging Face][1])

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/NimithB/FACEANALYZER.git
   cd FACEANALYZER
   ```
2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**([GitHub][2])

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the database**

   * Ensure MySQL server is running.
   * Create a database named `expression`.
   * Update the `database.py` file with your MySQL credentials:([GitHub][3])

     ```python
     config = {
         'host': '127.0.0.1',
         'user': 'your_username',
         'password': 'your_password',
         'database': 'expression',
         'port': 3306,
         'charset': 'utf8mb4',
         'collation': 'utf8mb4_unicode_ci',
         'autocommit': True
     }
     ```
5. **Run the application**

   ```bash
   python app.py
   ```
6. **Access the application**([PyPI][4])
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```plaintext
FACEANALYZER/
├── __pycache__/            # Compiled Python files
├── static/uploads/         # Uploaded images
├── templates/              # HTML templates
│   └── index.html
├── .gitignore              # Git ignore file
├── ai_model.py             # AI model for facial expression analysis
├── app.py                  # Main Flask application
├── database.py             # Database connection and setup
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```



## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any inquiries or feedback, please contact [nimithbe@gmail.com](mailto:nimithbe@gmail.com).



[1]: https://huggingface.co/NimithB/Noofpeopledetect?utm_source=chatgpt.com "NimithB/Noofpeopledetect - Hugging Face"
[2]: https://github.com/NimithB/FACEANALYZER?utm_source=chatgpt.com "NimithB/FACEANALYZER - GitHub"
[3]: https://github.com/NimithB/FACEANALYZER/blob/master/database.py?utm_source=chatgpt.com "FACEANALYZER/database.py at master · NimithB/FACEANALYZER - GitHub"
[4]: https://pypi.org/project/FaceAnalyzer/?utm_source=chatgpt.com "FaceAnalyzer - PyPI"
