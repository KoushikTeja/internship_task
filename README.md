
Internship Task - Meeting Transcription Topic Extraction
This project aims to extract topics and generate corresponding keynotes from meeting transcripts. To run the project, follow the steps below:

Setup
Clone the repository to your local machine.
Install the required dependencies by running: pip install -r requirements.txt.

Running the Django Application
Open the terminal and navigate to the project's root directory.
Run the following command to start the Django server: python manage.py runserver.
Using the GPT-based Backend (Recommended)
The Django application uses the GPT-based backend (backend_gpt) to process meeting transcripts and generate topics with corresponding keynotes. This approach leverages the power of OpenAI's GPT model to provide more accurate and meaningful results.

Alternate Approach: Using spaCy (backend_spacy)
If you are interested in comparing the results obtained using the spaCy-based approach, you can run the backend_spacy file. However, please ensure that you have installed the "en_core_web_sm" model using pip install en_core_web_sm.

Important Note
Please note that to use the GPT-based approach, you need to provide your own OpenAI API key in the .env file. This is essential to authenticate and access the GPT model.

Feel free to explore and test the project by providing meeting transcripts as inputs to the application. The system will extract the topics discussed during the meeting and generate concise keynotes for each topic.

Thank you for your interest in this project! If you have any questions or need further assistance, please don't hesitate to reach out. Happy topic extraction!
