import openai

#OPENAI_API_KEYS
API_KEY_TOPIC_IDENTIFICATION = "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"
API_KEY_KEYNOTE_GENERATION = "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"

def identify_topics_with_gpt(transcription_text):
    conversation = [{"role": "system",
                     "content": f"you are an expert at analyzing the meeting transcript and now your job is to analyse this  transcript: {transcription_text}  and generate the topics discussed along with a short keynote for each individual topic"}]
    conversation.append({"role": "user", "content": transcription_text})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            api_key=API_KEY_TOPIC_IDENTIFICATION
        )
    except openai.error.RateLimitError:
        return {"error": "Sorry, I couldn't identify the topics. Please try again later."}

    summary = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": summary})

    return summary