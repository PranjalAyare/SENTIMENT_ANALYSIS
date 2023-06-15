from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()


# Function to perform sentiment analysis on a given text
def analyze_sentiment(text):
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, compound_score


# Main method
def main():
    # Read customer reviews from a text file
    with open('feedbacks.txt', 'r') as file:
        reviews = file.readlines()

    # Analyze sentiment for each review
    for review in reviews:
        sentiment, compound_score = analyze_sentiment(review)

        # Print the sentiment and compound score
        print('Review:', review.strip())
        print('Sentiment:', sentiment)
        print('Compound Score:', compound_score)
        print('---')


if __name__ == '__main__':
    main()

