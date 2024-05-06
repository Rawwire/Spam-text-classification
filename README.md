Spam Text Classification


This project demonstrates a simple spam text classification system using a Random Forest Classifier. The classifier is trained on a balanced dataset of spam and ham (non-spam) messages, with a TF-IDF vectorization approach to process the text data. The project utilizes Streamlit to create a user-friendly interface, allowing users to classify text as spam or ham.


Table of Contents
- Project Overview
- Installation and Setup
- Usage
- Contributing
- License


Project Overview
The Spam Text Classification project aims to:

Create a Random Forest classifier to detect spam messages.
Utilize TF-IDF (Term Frequency-Inverse Document Frequency) for text vectorization.
Implement a Streamlit web interface for easy interaction.
Achieve a balanced dataset by sampling the "ham" class to match the "spam" class.


Installation and Setup
To set up this project on your local environment, follow these steps:

1) Clone the repository to your local machine:
     `git clone https://github.com/Rawwire/Spam-text-classification.git`
   
3) Navigate to the project directory:
     `cd Spam-text-classification`

4) Install the required Python packages:
     `pip install -r requirements.txt`


Usage
After installing the project and setting up the environment, you can run the Streamlit app to classify spam text messages:
     `streamlit run main.py`

This command opens a Streamlit web application where you can enter text to be classified. The app predicts whether the input text is spam or ham using a pre-trained Random Forest classifier.

NOTE: Don't forget to change the directory location of os environment and tsv file directory while reading it.

Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1) Fork the repository and create a new branch for your feature or bug fix.
2) Commit your changes and push the branch to your forked repository.
3) Open a Pull Request on the original repository, describing the changes you've made.


License
This project is licensed under the MIT License. For more information, see the LICENSE file in the repository.


This project is created by Raja Pandi S.
#### My LinkedIn : https://www.linkedin.com/in/raja-pandi-s

