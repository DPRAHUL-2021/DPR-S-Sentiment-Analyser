# DPR'S Sentiment Analyser

This web application provides real-time sentiment analysis for textual inputs using advanced natural language processing techniques. It employs two robust sentiment analysis models—TextBlob and VADER—to analyze and visualize the emotional tone of user-provided text.

## Key Features:
- **Input Text:** Users can input any text for sentiment analysis.
- **Sentiment Analysis Models:**
  - **TextBlob:** Utilizes a simple API for sentiment analysis, categorizing text into negative, neutral, and positive sentiments.
  - **VADER (Valence Aware Dictionary and sEntiment Reasoner):** Employs a lexicon and rule-based sentiment analysis tool that is sensitive to both polarity (positive/negative) and intensity.
- **Visualization:** Presents sentiment proportions (negative, neutral, positive) through intuitive graphical representations.
- **Comparison:** Offers a side-by-side comparison of sentiment analysis results from TextBlob and VADER for deeper insights.
- **User-Friendly Interface:** Interactive UI with clear instructions for seamless user experience.

## Technologies Used:
- **Python:** Core programming language.
- **Streamlit:** Framework for building and deploying interactive web applications with Python.
- **NLTK (Natural Language Toolkit):** Used for text processing and integrating the VADER sentiment analysis tool.
- **TextBlob:** Simplified API for common natural language processing (NLP) tasks, including sentiment analysis.
- **Matplotlib:** Python plotting library for creating visualizations of sentiment analysis results.

## How to Use:
1. **Input Text:** Enter a sentence or paragraph into the provided text area.
2. **Analyze:** Click the "Analyze" button to initiate sentiment analysis.
3. **View Results:** Explore sentiment analysis results for both TextBlob and VADER.
4. **Visualize:** Interpret sentiment proportions visually to understand the distribution of negative, neutral, and positive sentiments.

## Enter The Text
![DPR-S-Sentiment-Analyser](start.png)
## The Analysis
![DPR-S-Sentiment-Analyser](process.png)

This application is designed to provide users with actionable insights into the sentiment conveyed by text, helping them understand and analyze textual data more effectively.
