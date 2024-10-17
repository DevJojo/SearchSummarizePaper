import requests
from transformers import pipeline
import smtplib
from email.mime.text import MIMEText

# Function to search for research papers using CrossRef API
def search_papers(query, rows=5):
    url = "https://api.crossref.org/works"
    params = {
        'query': query,
        'filter': 'type:journal-article',
        'rows': rows
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['message']['items']
    else:
        print("Failed to fetch papers.")
        return []

# Function to summarize the text using Hugging Face transformers
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Function to send the summary to your email
def send_email(summary, recipient_email):
    msg = MIMEText(summary)
    msg['Subject'] = 'Marine Research Paper Summary'
    msg['From'] = 'your_email@example.com'
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail('your_email@example.com', recipient_email, msg.as_string())

# Main function to combine search, summarization, and email
def main():
    # Search for marine and ocean research papers
    query = "clinic AND Oncology"
    papers = search_papers(query, rows=4)  # Fetch top 3 papers as an example

    if not papers:
        print("No papers found.")
        return

    # Process each paper
    summaries = []
    for paper in papers:
        title = paper['title'][0]
        paper_url = paper['URL']

        # Placeholder for the paper abstract (you can replace this with actual paper content if available)
        abstract = paper.get('abstract', f"Abstract not available. Check the paper here: {paper_url}")
        
        # Summarize the abstract or full text if available
        summary = summarize_text(abstract)
        summaries.append(f"Title: {title}\nSummary: {summary}\nLink: {paper_url}\n\n")

    # Combine all summaries into a single message
    email_content = "\n".join(summaries)
    
    print(email_content)

    # Send the summaries to your email
    #recipient_email = "recipient_email@example.com"  # Replace with the target email address
    #send_email(email_content, recipient_email)

    #print(f"Summaries sent to {recipient_email}")

# Call the main function
if __name__ == "__main__":
    main()
