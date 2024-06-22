from FlashcardChat import FlashcardChat  # Ensure the FlashcardChat module is imported correctly

# Initialize the FlashcardChat
flashcard_chat = FlashcardChat()

# Test data for creating flashcards
notes_input = """
- Why Machine Learning?
    - Can provide better, customized services
    - Data collected and stored at enormous speeds
    - Helps scientists in automated analysis of massive datasets and hypothesis formation
    - Great opportunities to solve society's major problems
- What is Data Mining?
    - Exploring & analyzing large amounts of data to find patterns
    - Deals with large-scale, high dimensional, heterogeneous, complex, distributed data
    - Statistics: Hypothesis driven (Have idea of distribution ⇒ Find model)
    - Data Mining: Data driven (Rely on algorithm to find patterns), complex and large scale datasets
    - Machine Learning (v. Data Mining): Dealt with smaller datasets, tabular data
    - AI: Subset of ML, algorithm (Deep Neural Networks)
- What we will learn
    - General techniques to extract information from data
    - Which techniques work for what circumstance
    - How to measure success of your efforts
    - ID whether/when/how the solution is scalable
- Machine Learning Tasks
    - Descriptive methods: Find human-interpretable patterns that describe the data
        - Ex: Clustering, Pattern Mining
    - Predictive methods: Use some variables to predict unknown or future values of other variables
        - Ex: Recommender systems, Time series analysis
- Predictive Modeling: Classification
    - Ex: Decision Tree, Logistic regression, nearest neighbor
    - Training Set ⇒ Classifier (algorithm to get model) ⇒ Model (function given input sample gets output answer) ⇒ Use test set on model
    - Approach:
        - Use records to find attributes
        - Label each row with its class attribute
        - Make model
- Regression
    - Predict a value of a given continuous valued variable based on values of other variables, assume linear or nonlinear model of dependency
    - Extensively studied in statistics, neural network fields
- Clustering
    - Finding groups of objects such that the objects in a group will be similar (or related) to one another and different from (or unrelated to) the objects in other groups.
    - Inter-cluster distances maximized, intra-cluster difference minimized
- Association Rule Discovery
    - Given a set of records each of which contain some number of items from a given collection
        - Produce dependency rules which will predict occurrence of an item based on occurrences of other items
- Deviation/Anomaly/Change Detection
    - Detect significant deviations from normal behavior
"""

# Create flashcards from notes
created_flashcards = flashcard_chat.createFlashcard(notes_input)
print(f"Created Flashcards:\n{created_flashcards}")

# Test data for feedback
card_concept = "Efficiency of Insertion Sort"
card_detail = "Insertion Sort works best for small or mostly sorted arrays and has a time complexity of O(n^2) in the worst case."
user_response = "Insertion Sort is good for small arrays."

# Get feedback on user response
feedback = flashcard_chat.feedback(card_concept, card_detail, user_response)
print("\nFeedback:\n", feedback)
