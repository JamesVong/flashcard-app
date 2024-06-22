from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from DbModels import Base, User, Deck, Card, Conversation, Chat
from datetime import datetime

load_dotenv()

class DbManager:
    def __init__(self):
        connection_string = URL.create(
            'postgresql',
            username='flashcards_owner',
            password=os.getenv("FLASHCARD_DB_PASSWORD"),
            host='ep-autumn-butterfly-a6gqmxwy.us-west-2.aws.neon.tech',
            database='flashcards',
            query={'sslmode': 'require'}
        )

        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, name):
        with self.Session() as session:
            new_user = User(name=name)
            session.add(new_user)
            session.commit()
            return new_user.id

    def get_user(self, user_id):
        with self.Session() as session:
            return session.query(User).filter(User.id == user_id).first()

    def add_deck(self, user_id, name, description):
        with self.Session() as session:
            new_deck = Deck(user_id=user_id, name=name, description=description)
            session.add(new_deck)
            session.commit()
            return new_deck.id

    def get_deck(self, deck_id):
        with self.Session() as session:
            return session.query(Deck).filter(Deck.id == deck_id).first()

    def add_card(self, deck_id, concept, detail):
        with self.Session() as session:
            new_card = Card(deck_id=deck_id, concept=concept, detail=detail)
            session.add(new_card)
            session.commit()
            return new_card.id

    def get_card(self, card_id):
        with self.Session() as session:
            return session.query(Card).filter(Card.id == card_id).first()

    # Conversation methods
    def add_conversation(self, deck_id, title, characters):
        with self.Session() as session:
            new_conversation = Conversation(deck_id=deck_id, title=title, characters=characters)
            session.add(new_conversation)
            session.commit()
            return new_conversation.id

    def get_conversation(self, conversation_id):
        with self.Session() as session:
            return session.query(Conversation).filter(Conversation.id == conversation_id).first()

    def update_conversation(self, conversation_id, title=None, characters=None):
        with self.Session() as session:
            conversation = session.query(Conversation).filter(Conversation.id == conversation_id).first()
            if conversation:
                if title:
                    conversation.title = title
                if characters:
                    conversation.characters = characters
                session.commit()
                return True
            return False

    def delete_conversation(self, conversation_id):
        with self.Session() as session:
            conversation = session.query(Conversation).filter(Conversation.id == conversation_id).first()
            if conversation:
                session.delete(conversation)
                session.commit()
                return True
            return False

    def get_conversations_by_deck(self, deck_id):
        with self.Session() as session:
            return session.query(Conversation).filter(Conversation.deck_id == deck_id).all()

    # Chat methods
    def add_chat(self, conversation_id, author, message):
        with self.Session() as session:
            new_chat = Chat(conversation_id=conversation_id, author=author, message=message, time=datetime.utcnow())
            session.add(new_chat)
            session.commit()
            return new_chat.id

    def get_chat(self, chat_id):
        with self.Session() as session:
            return session.query(Chat).filter(Chat.id == chat_id).first()

    def update_chat(self, chat_id, message):
        with self.Session() as session:
            chat = session.query(Chat).filter(Chat.id == chat_id).first()
            if chat:
                chat.message = message
                chat.time = datetime.utcnow()
                session.commit()
                return True
            return False

    def delete_chat(self, chat_id):
        with self.Session() as session:
            chat = session.query(Chat).filter(Chat.id == chat_id).first()
            if chat:
                session.delete(chat)
                session.commit()
                return True
            return False

    def get_chats_by_conversation(self, conversation_id):
        with self.Session() as session:
            return session.query(Chat).filter(Chat.conversation_id == conversation_id).order_by(Chat.time).all()

    def get_latest_chats(self, conversation_id, limit=10):
        with self.Session() as session:
            return session.query(Chat).filter(Chat.conversation_id == conversation_id).order_by(Chat.time.desc()).limit(limit).all()