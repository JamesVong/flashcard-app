from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

class ChatBot():
    def __init__(self, model_name, system_prompt):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.conversation = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, message, remember=False):
        completion = client.chat.completions.create(
            model=self.model_name,
            messages=self.conversation + [{"role": "user", "content": message}]
        )
        
        response = completion.choices[0].message.content
        if remember:
            self.conversation.extend([
                {"role": "user", "content": message},
                {"role": "assistant", "content": response}
            ])

        return response