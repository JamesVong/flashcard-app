import base64
from ChatModule import ChatBot


def get_prompt(file_path):
    with open(file_path, "r") as fp:
        return fp.read()
    
def image_to_base64(image_path):
  """Convert the image to base64."""
  with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    return base64.b64encode(image_data).decode("utf-8")

def get_media_type(image_name):
    """Get the media type of the uploaded image based on its file extension."""
    if image_name.lower().endswith(".jpg") or image_name.lower().endswith(".jpeg"):
        return "image/jpeg"
    elif image_name.lower().endswith(".png"):
        return "image/png"
    else:
        raise ValueError(f"Unsupported image format: {image_name}")

class FlashcardChat():
    def __init__(self):
        create_prompt = get_prompt("./CreatePrompt.txt")
        self.create_flashcard_bot = ChatBot("claude-3-5-sonnet-20240620", create_prompt)

        title_prompt = get_prompt("./CreateTitleAndDescription.txt")
        self.title_bot = ChatBot("claude-3-5-sonnet-20240620", title_prompt)

        feedback_prompt = get_prompt("./FeedbackPrompt.txt")
        self.feedback_bot = ChatBot("claude-3-5-sonnet-20240620", feedback_prompt)

       
        self.read_img_bot = ChatBot("claude-3-5-sonnet-20240620", "")

    def getTitleAndDescription(self, text_input):
        return self.title_bot.chat(text_input, False)

    def createFlashcard(self, text_input):
        return self.create_flashcard_bot.chat(text_input, False)

    def feedback(self, card_concept, card_detail, text_input):
        text_format = f"Front of card (Concept): {card_concept}\n\Back of card (Detail): {card_detail}\n\nUser Response: {text_input}"
        return self.feedback_bot.chat(text_format, False)

    def readImage(self, image_name, image_path):
        read_img_prompt = get_prompt("./ReadImgPrompt.txt")
        return self.read_img_bot.readImage(read_img_prompt, image_to_base64(image_path), get_media_type(image_name))