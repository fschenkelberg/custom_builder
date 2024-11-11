# Text Embeddings
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# File path where embeddings are stored
embedding_file = 'embeddings.npy'

def get_document_embedding(text):
    """
    Convert a given text to an embedding using Sentence-BERT.
    """
    embedding = model.encode(text)
    return embedding

def save_embeddings(embeddings, file_path):
    """
    Save the embeddings to the specified file.
    If the file exists, append the embeddings.
    If not, create the file and save the embeddings.
    """
    if os.path.exists(file_path):
        # Load existing embeddings and append new ones
        existing_embeddings = np.load(file_path)
        updated_embeddings = np.vstack([existing_embeddings, embeddings])
        np.save(file_path, updated_embeddings)
    else:
        # File doesn't exist, create a new file and save embeddings
        np.save(file_path, embeddings)

def load_embeddings(file_path):
    """
    Load the embeddings from the specified file.
    Returns None if the file doesn't exist.
    """
    if os.path.exists(file_path):
        return np.load(file_path)
    else:
        return None

# Example usage
texts = ["This is a test sentence.", "Another example sentence for embedding."]

# Try to load existing embeddings
existing_embeddings = load_embeddings(embedding_file)

# Create a list of new embeddings
new_embeddings = np.array([get_document_embedding(text) for text in texts])

if existing_embeddings is not None:
    # Append new embeddings to existing ones
    save_embeddings(new_embeddings, embedding_file)
else:
    # No existing embeddings, create the file with the new embeddings
    save_embeddings(new_embeddings, embedding_file)

# Now the embeddings are either saved as new or appended
print(f"Updated embeddings saved to: {embedding_file}")
