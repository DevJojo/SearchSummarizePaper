from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input your long text
text = """
Hugging Face is creating a community for AI enthusiasts, researchers, and developers. It is best known for its open-source NLP tools and transformer models. 
These models can be used for various tasks such as text classification, question answering, and summarization. By providing pre-trained models, Hugging Face 
has greatly simplified the process of using state-of-the-art models for real-world applications. Their platform also allows for easy fine-tuning of models on 
custom datasets. NLP research and applications have become more accessible thanks to Hugging Face.
"""

# Get the summary
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("Summary:", summary[0]['summary_text'])
