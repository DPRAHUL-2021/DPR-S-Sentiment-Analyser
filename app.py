import streamlit as st
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Function to analyze sentiment using TextBlob

def analyze_textblob_sentiment(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity

    # Map polarity to a scale of 0 to 1
    if polarity > 0:
        positive = polarity
        negative = 0
    elif polarity < 0:
        negative = -polarity
        positive = 0
    else:
        positive = 0
        negative = 0
    neutral = 1 - positive - negative
    return {'negative': negative, 'neutral': neutral, 'positive': positive}


# Function to analyze sentiment using VADER

def analyze_vader_sentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(sentence)

    # Map compound score to a scale of 0 to 1
    if scores['compound'] > 0:
        positive = scores['compound']
        negative = 0
    elif scores['compound'] < 0:
        negative = -scores['compound']
        positive = 0
    else:
        positive = 0
        negative = 0
    neutral = 1 - positive - negative
    return {'negative': negative, 'neutral': neutral, 'positive': positive}


# Function to plot sentiment proportions side by side

def plot_sentiment_proportions_side_by_side(title1, sentiment_proportions1, title2, sentiment_proportions2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))  
    
    # Increase the figure size here
    labels = list(sentiment_proportions1.keys())
    values1 = list(sentiment_proportions1.values())
    values2 = list(sentiment_proportions2.values())
    
    ax1.bar(labels, values1, color=['red', 'gray', 'green'])
    ax1.set_ylabel('Proportion')
    ax1.set_title(title1)

    ax2.bar(labels, values2, color=['red', 'gray', 'green'])
    ax2.set_ylabel('Proportion')
    ax2.set_title(title2)

    plt.subplots_adjust(wspace=0.5) 

    return fig

def main():
    st.title("DPR'S Sentiment Analyser")
    sentence = st.text_area("Enter a sentence:")

    if st.button("Analyze"):
        if isinstance(sentence, str) and sentence.strip():  
            st.subheader("Sentiment Analysis Results")
            
            # Analyze sentiment using TextBlob
            textblob_sentiment = analyze_textblob_sentiment(sentence)
            st.text(f"TextBlob Sentiment - Negative: {textblob_sentiment['negative']:.2f}, Neutral: {textblob_sentiment['neutral']:.2f}, Positive: {textblob_sentiment['positive']:.2f}")
            
            # Analyze sentiment using VADER
            vader_sentiment = analyze_vader_sentiment(sentence)
            st.text(f"VADER Sentiment - Negative: {vader_sentiment['negative']:.2f}, Neutral: {vader_sentiment['neutral']:.2f}, Positive: {vader_sentiment['positive']:.2f}")
            
            # Plot sentiment proportions side by side for TextBlob and VADER
            fig = plot_sentiment_proportions_side_by_side(
                "TextBlob Sentiment Analysis",
                {
                    'Negative': textblob_sentiment['negative'],
                    'Neutral': textblob_sentiment['neutral'],
                    'Positive': textblob_sentiment['positive']
                },
                "VADER Sentiment Analysis",
                {
                    'Negative': vader_sentiment['negative'],
                    'Neutral': vader_sentiment['neutral'],
                    'Positive': vader_sentiment['positive']
                }
            )
            
            st.pyplot(fig)
        else:
            # Error Handling
            st.error("Please enter a valid sentence for analysis.")

if __name__ == "__main__":
    main()
