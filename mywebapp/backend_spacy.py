import spacy

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

def extract_topics_from_transcription(transcription_text):
    # Process the meeting transcription using spaCy
    doc = nlp(transcription_text)

    # List to store identified topics and their content
    topics = {}

    # Iterate through each sentence in the transcription
    for sentence in doc.sents:
        # If the sentence contains a verb (action word) and a noun (subject), consider it as a potential topic
        if any(token.pos_ == "VERB" for token in sentence) and any(token.pos_ == "NOUN" for token in sentence):
            topic = " ".join(token.text for token in sentence if not token.is_stop)
            if topic not in topics:
                topics[topic] = [sentence.text]
            else:
                topics[topic].append(sentence.text)

    return topics

def generate_keynotes(topics):
    # Generate concise keynotes for each topic
    keynotes = {}
    for topic, content_list in topics.items():
        keynote_sentences = content_list[:3]  # Select the first three sentences for each topic
        # Combine the sentences and ensure the keynote ends with a period
        keynote = " ".join(keynote_sentences).rstrip(".") + "."
        keynotes[topic] = keynote

    return keynotes

def display_keynotes(keynotes):
    # Display the identified topics and their keynotes
    for topic, keynote in keynotes.items():
        if topic.strip():  # Skip topics with empty spaces
            print(f"Topic: {topic}")
            print(f"Keynote: {keynote}\n")

if __name__ == "__main__":
    # Example usage with a sample meeting transcription
    meeting_transcription = """
    Good morning, everyone. Today, we are here to discuss the project progress and any challenges we might be facing.
    The marketing team has been doing a great job in promoting the product, and we've seen a significant increase in sales.
    However, the development team has encountered some issues with the latest update, which has led to negative customer feedback.
    We need to address these issues promptly to maintain customer satisfaction.
    Additionally, we need to plan for the upcoming product launch event. We should focus on inviting key industry influencers to the event.
    """

    topics = extract_topics_from_transcription(meeting_transcription)
    keynotes = generate_keynotes(topics)

    # Display the identified topics and their keynotes
    display_keynotes(keynotes)
