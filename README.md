# internship_task
Here is the implementation of the model that takes meeting transcripts as inputs and generates the output that contains topics and their corresponding keynotes
To run the project clone the repository and run the following command in the terminal " python manage.py runserver"
please note:
        * in the Django application (mywebapp) we had 2 backend files
                                      1. backend_gpt (which uses gpt)
                                      2. backend_spacy ( which uses spacy)
        * first I used spacy "en_core_web_sm" model along with some NLP techniques such as tokenization POS NER etc but the results were not great so i deployed gpt model in the Django
        * We can also run the backend_spacy file to see the result obtained by that approach (make sure to install "en_core_web_sm")
        * I also did not use .env file to hide my api keys because you have to give your openai api key to test the model 

    

