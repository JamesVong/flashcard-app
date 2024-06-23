from StudyGroup import StudyGroup

# Example JSON data
data = {
    "cards": [
        {
            "concept": "Machine Learning Benefits",
            "detail": "Machine Learning can provide better customized services, analyze massive datasets rapidly, and help solve major societal problems.",
            "id": 1
        },
        {
            "concept": "Data Collection in Machine Learning",
            "detail": "Data is collected and stored at enormous speeds, enabling machine learning algorithms to work with large datasets.",
            "id": 2
        },
        {
            "concept": "Scientific Applications of Machine Learning",
            "detail": "Machine Learning helps scientists in automated analysis of massive datasets and hypothesis formation.",
            "id": 3
        },
        {
            "concept": "Definition of Data Mining",
            "detail": "Data Mining is the process of exploring and analyzing large amounts of data to find patterns.",
            "id": 4
        },
        {
            "concept": "Characteristics of Data Mining",
            "detail": "Data Mining deals with large-scale, high dimensional, heterogeneous, complex, and distributed data.",
            "id": 5
        },
        {
            "concept": "Statistics vs Data Mining",
            "detail": "Statistics is hypothesis-driven, while Data Mining is data-driven and works with complex, large-scale datasets.",
            "id": 6
        },
        {
            "concept": "Machine Learning vs Data Mining",
            "detail": "Machine Learning traditionally dealt with smaller, tabular datasets, while Data Mining handles larger, more complex data.",
            "id": 7
        },
        {
            "concept": "Artificial Intelligence in Machine Learning",
            "detail": "AI is a subset of Machine Learning, focusing on algorithms like Deep Neural Networks.",
            "id": 8
        },
        {
            "concept": "Key Learning Objectives in Machine Learning",
            "detail": "Learn general techniques to extract information from data, identify suitable techniques for different circumstances, and measure success.",
            "id": 9
        },
        {
            "concept": "Scalability in Machine Learning",
            "detail": "Learn to identify whether, when, and how a machine learning solution is scalable.",
            "id": 10
        },
        {
            "concept": "Descriptive Methods in Machine Learning",
            "detail": "Descriptive methods find human-interpretable patterns that describe the data, such as clustering and pattern mining.",
            "id": 11
        },
        {
            "concept": "Predictive Methods in Machine Learning",
            "detail": "Predictive methods use some variables to predict unknown or future values of other variables, like recommender systems and time series analysis.",
            "id": 12
        },
        {
            "concept": "Classification in Predictive Modeling",
            "detail": "Classification uses algorithms like Decision Trees, Logistic Regression, and Nearest Neighbor to predict discrete class labels.",
            "id": 13
        },
        {
            "concept": "Classification Process",
            "detail": "Classification involves using a training set to create a classifier, which produces a model to make predictions on a test set.",
            "id": 14
        },
        {
            "concept": "Regression in Machine Learning",
            "detail": "Regression predicts continuous values based on other variables, assuming linear or nonlinear dependency models.",
            "id": 15
        },
        {
            "concept": "Clustering in Machine Learning",
            "detail": "Clustering finds groups of similar objects, maximizing inter-cluster distances and minimizing intra-cluster differences.",
            "id": 16
        },
        {
            "concept": "Association Rule Discovery",
            "detail": "Association Rule Discovery produces dependency rules to predict item occurrences based on other item occurrences in a set of records.",
            "id": 17
        },
        {
            "concept": "Anomaly Detection in Machine Learning",
            "detail": "Anomaly Detection identifies significant deviations from normal behavior in datasets.",
            "id": 18
        }
    ],
    "conversations": [],
    "description": "Introductory lesson from the first week of class",
    "id": 1,
    "last_edited": "Sat, 22 Jun 2024 23:53:12 GMT",
    "name": "Machine Learning"
}

def format_flashcards(data):
    cards = data.get("cards", [])
    formatted_cards = []
    for card in cards:
        concept = card.get("concept", "")
        detail = card.get("detail", "")
        formatted_cards.append(f"{concept}|||{detail}")
    return formatted_cards

flashcard_strings = format_flashcards(data)
deck_string = "\n".join(flashcard_strings)

# List of characters to include in the study group
characters = ["Ned", "Batman"]

# Initialize the StudyGroup with the deck_string and selected characters
study_group = StudyGroup(deck_string, characters)

# Continuous loop to get user messages and print responses
while True:
    user_input = input("[You] \n")
    print("\n")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting study session.")
        break
    print(study_group.userMessage(user_input))