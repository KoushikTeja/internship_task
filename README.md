
# Internship Task - Meeting Transcription -> Topic and keynote Extraction
This project aims to extract topics and generate corresponding keynotes from meeting transcripts. To run the project, follow the steps below:

Setup
Clone the repository to your local machine.
Install the required dependencies by running: pip install -r requirements.txt.

## Running the Django Application
Open the terminal and navigate to the project's root directory.
Run the following command to start the Django server: python manage.py runserver.
### Using the GPT-based Backend (Recommended)
The Django application uses the GPT-based backend (backend_gpt) to process meeting transcripts and generate topics with corresponding keynotes. This approach leverages the power of OpenAI's GPT model to provide more accurate and meaningful results.

### Alternate Approach: Using spaCy (backend_spacy)
first I used spacy "en_core_web_sm" model along with some NLP techniques such as tokenization POS NER etc but the results did not impress me  so I deployed gpt model in the Django
If we are interested in comparing the results obtained using the spaCy-based approach, we can run the backend_spacy file. However, please ensure that you have installed the "en_core_web_sm" model using pip install en_core_web_sm.

***Important Note
please note that I didnot use a .env file to hide the API keys because If I do that you need to provide your own API key to run the model***

Feel free to explore and test the project by providing meeting transcripts as inputs to the application. The system will extract the topics discussed during the meeting and generate concise keynotes for each topic.

## This is the input transcript given for testing:
  ***Good morning, everyone. Today, we are here to discuss the project's progress and any challenges we might be facing.
    The marketing team has been doing a great job in promoting the product, and we've seen a significant increase in sales.
    However, the development team has encountered some issues with the latest update, which has led to negative customer feedback.
    We need to address these issues promptly to maintain customer satisfaction.
    Additionally, we need to plan for the upcoming product launch event. We should focus on inviting key industry influencers to the event.***





