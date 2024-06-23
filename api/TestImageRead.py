from FlashcardChat import FlashcardChat
import os

flashcard_chat = FlashcardChat()
image_name = "TestNotes.jpg"
image_path = os.path.join(os.path.dirname(__file__), image_name)

try:
    result = flashcard_chat.readImage(image_name, image_path)
    print("Image read successfully:", result)
except Exception as e:
    print("Error reading image:", str(e))