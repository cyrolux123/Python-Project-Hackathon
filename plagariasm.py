import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_text(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()

def vectorize(text_list):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(text_list).toarray()


def calculate_similarity(vector1, vector2):
    return cosine_similarity([vector1, vector2])[0][1]

def check_plagiarism(file_paths):
    # Read text from files
    texts = [read_text(file_path) for file_path in file_paths]

    # Vectorize the texts using TF-IDF
    vectors = vectorize(texts)

    plagiarism_results = {}

    # Iterate through each pair of files
    for i, (student_a, vector_a) in enumerate(zip(file_paths, vectors)):
        for student_b, vector_b in zip(file_paths[i+1:], vectors[i+1:]):
            # Calculate similarity score
            sim_score = calculate_similarity(vector_a, vector_b)

            # Pair the files in sorted order
            student_pair = sorted((student_a, student_b))

            # Convert the result to a tuple
            result = (student_pair[0], student_pair[1])

            # Add the result to the dictionary if it does not exist
            if result not in plagiarism_results:
                plagiarism_results[result] = sim_score

    return plagiarism_results


