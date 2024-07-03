import nltk
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Sample corpus of text for the chatbot to learn from
corpus = [
    'Hello, how are you?',
    'I am doing great, thank you!',
    'Sure, I can help you with that.',
    'Sorry, I do not understand your question.',
    'Goodbye! Have a nice day!',
]
# Function to perform text preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    return text
# Function to generate response to user input
def generate_response(user_input, corpus):
    corpus.append(user_input)  # Add user input to the corpus
    tfidf_vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    # Calculate similarity between user input and corpus
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    idx = np.argmax(similarities)  # Find index of most similar response
    return corpus[idx]
# Main function to run the chatbot
def main():
    print("Chatbot: Hello! I am your AI chatbot. You can start chatting with me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        preprocessed_input = preprocess_text(user_input)
        response = generate_response(preprocessed_input, corpus)
        print("Chatbot:", response)
# Initialize NLTK tokenizer
nltk.download('punkt')
# Run the chatbot
if __name__ == "__main__":
    main()
