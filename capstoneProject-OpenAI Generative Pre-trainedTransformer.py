# Required Libraries
import openai
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ========== 1. EXPLORATORY DATA ANALYSIS AND VISUALIZATION ==========

def run_eda_visualization(csv_path):
    """
    Perform EDA and generate basic plots using seaborn and matplotlib.
    """
    df = pd.read_csv(csv_path)

    # --- Basic EDA ---
    print("\n--- Head of Dataset ---")
    print(df.head())

    print("\n--- Info ---")
    print(df.info())

    print("\n--- Describe ---")
    print(df.describe())

    print("\n--- Null Values ---")
    print(df.isnull().sum())

    print("\n--- Unique Values ---")
    print(df.nunique())

    # --- Visualization (customize columns as needed) ---
    num_col = df.select_dtypes(include='number').columns[0]
    cat_col = df.select_dtypes(include='object').columns[0]

    # Histogram
    plt.figure(figsize=(6, 4))
    sns.histplot(df[num_col], kde=True)
    plt.title(f'Distribution of {num_col}')
    plt.show()

    # Boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=cat_col, y=num_col, data=df)
    plt.title(f'Boxplot of {num_col} by {cat_col}')
    plt.xticks(rotation=45)
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

# ========== 2. RESUME GENERATION FROM PARAGRAPH ==========

def generate_resume(paragraph, api_key):
    """
    Generate a resume from a given paragraph using OpenAI GPT-3.
    """
    openai.api_key = api_key

    prompt = f"Generate a professional resume in bullet points from the following paragraph:\n\n{paragraph}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    print("\n--- Generated Resume ---")
    print(response['choices'][0]['text'].strip())

# ========== 3. INTERVIEW QUESTION GENERATION ==========

def generate_interview_questions():
    """
    Print a fixed set of Python interview questions.
    """
    questions = [
        "Explain the difference between a list and a tuple in Python.",
        "What are Python decorators and how do you use them?",
        "How does Python handle memory management?",
        "What is a generator in Python? Provide an example.",
        "Explain the concept of list comprehension.",
        "How does exception handling work in Python?",
        "What are Python's key data types?",
        "What is the difference between 'is' and '=='?",
        "How does the GIL (Global Interpreter Lock) affect threading?",
        "Write a Python function to check if a string is a palindrome."
    ]

    print("\n--- Python Interview Questions ---")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")

# ========== 4. MEETING NOTE SUMMARIZER ==========

def summarize_meeting_notes(notes, api_key):
    """
    Summarize meeting notes using OpenAI GPT-3.
    """
    openai.api_key = api_key

    prompt = f"Summarize the following meeting notes:\n{notes}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )

    print("\n--- Meeting Summary ---")
    print(response['choices'][0]['text'].strip())

# ========== MAIN SCRIPT EXECUTION ==========

if __name__ == "__main__":
    # === 1. EDA and Visualization ===
    # Replace with the path to your CSV file
    dataset_path = 'your_dataset.csv'
    run_eda_visualization(dataset_path)

    # === 2. Resume Generator ===
    resume_paragraph = """
    I am a computer science student skilled in Python, machine learning, and web development.
    I have interned at two startups and worked on AI-based chatbots. I'm also experienced in Flask and ReactJS.
    """
    your_api_key = "sk-..."  # Replace with your OpenAI API key
    generate_resume(resume_paragraph, your_api_key)

    # === 3. Interview Questions ===
    generate_interview_questions()

    # === 4. Meeting Notes Summary ===
    meeting_text = """
    Max: Profits up 50%
    Ruby: New servers are online
    Kyle: Need more time to fix software
    Walker: Happy to help
    Parkman: Beta testing almost done
    """
    summarize_meeting_notes(meeting_text, your_api_key)
