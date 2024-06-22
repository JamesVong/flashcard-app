from ChatModule import ChatBot

def get_prompt(file_path):
    with open(file_path, "r") as fp:
        return fp.read()

class FlashcardChat():
    def __init__(self):
        create_prompt = get_prompt("./CreatePrompt.txt")
        self.create_flashcard_bot = ChatBot("gpt-4o", create_prompt)
        
        feedback_prompt = get_prompt("./FeedbackPrompt.txt")
        self.feedback_bot = ChatBot("gpt-4o", feedback_prompt)

    def createFlashcard(self, text_input):
        return self.create_flashcard_bot.chat(text_input, False)

    def feedback(self, card_concept, card_detail, text_input):
        text_format = f"Front of card (Concept): {card_concept}\n\Back of card (Detail): {card_detail}\n\nUser Response: {text_input}"
        return self.feedback_bot.chat(text_format, False)
