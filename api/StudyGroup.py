from ChatModule import ChatBot

def get_prompt(file_path):
    with open(file_path, "r") as fp:
        return fp.read()

class StudyGroup:
    characters = [
        {
            "name": "Ned",
            "description": "A mentor for your topic. Provides practical tips and tricks for efficient studying and problem-solving."
        },
        {
            "name": "George",
            "description": "Curious and inquisitive. Has a lot of questions he wants to get answered as he crams for the exam."
        },
        {
            "name": "Annie",
            "description": "Hardcore anime fan. Relates everything to anime if she can."
        },
        {
            "name": "Batman",
            "description": "Gotham City’s defender of peace and justice. World’s greatest detective. May be an interesting study partner."
        },
        {
            "name": "Todd",
            "description": "Captain of the football team. Big sports fan and likes to keeps topics and learning simple and foundational."
        },
        {
            "name": "Jeff",
            "description": "Huge tech enthusiast. Enjoys coding and morning coffee. Always has questions on the details of a topic."
        },
        {
            "name": "Vincent",
            "description": "A light-hearted and friendly artist. He focuses on the big picture topics and high level concepts. Would recommend diagrams over notes."
        },
        {
            "name": "Sally",
            "description": "Loves reading and is a novel writer. She remembers best way when a topic told as a story. Also a fan of mnemonics for studying."
        }
    ]

    def getCharacter(self, name):
        for character in self.characters:
            if name == character["name"]:
                return character

    def __init__(self, deck_string, characters=None):
        # Character Descriptions
        character_desc = "Utilize the following characters to help the user study:\n"
        for chararacter in [self.getCharacter(name) for name in characters]:
            character_desc += f"[{chararacter['name']}]\nDescription: {chararacter['description']}\n\n"

        # Conversation prompt
        conversation_prompt = get_prompt("./ConversationPrompt.txt")
        conversation_prompt += f"Utilize the following flashcards to help the user study:\n{deck_string}\n\n"
        conversation_prompt += character_desc

        self.conversationBot = ChatBot("claude-3-5-sonnet-20240620", conversation_prompt)

    def userMessage(self, message):
        self.conversationBot.chat(message, True)
        formatted_messages = self.formatMessages()
        return formatted_messages

    def formatMessages(self):
        formatted_messages = []
        for entry in self.conversationBot.messages:
            if entry['role'] == 'user':
                formatted_messages.append({
                    "name": "User",
                    "message": entry['content']
                })
            elif entry['role'] == 'assistant':
                segments = entry['content'].split('\n\n')
                current_speaker = ""
                for segment in segments:
                    if segment.startswith('[') and ']' in segment:
                        current_speaker = segment.split(']')[0][1:]
                        message = segment.split(']')[1].strip()
                    else:
                        message = segment.strip()
                    if current_speaker:
                        formatted_messages.append({
                            "name": current_speaker,
                            "message": message
                        })
        return formatted_messages
        
