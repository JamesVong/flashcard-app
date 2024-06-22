import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class ChatBot():
    def __init__(self, model_name, system_prompt, default_max_tokens=2048):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.default_max_tokens = default_max_tokens
        self.messages = []

    def chat(self, message, remember=False, max_tokens=None):
        response = client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens or self.default_max_tokens,
            system=self.system_prompt,
            messages=self.messages + [{"role": "user", "content": message}]
        )
        
        assistant_message = response.content[0].text
        if remember:
            self.messages.extend([
                {"role": "user", "content": message},
                {"role": "assistant", "content": assistant_message}
            ])

        return assistant_message