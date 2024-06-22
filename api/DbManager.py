from sqlalchemy import URL, create_engine, func
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from DbModels import Base, Deck, Card, Conversation, Chat
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

    # Deck methods
    def add_deck(self, uid, name, description):
        with self.Session() as session:
            new_deck = Deck(uid=uid, name=name, description=description, last_edited=datetime.utcnow())
            session.add(new_deck)
            session.commit()
            return new_deck.id
    
    def get_decks_with_count(self, uid):
        with self.Session() as session:
            decks_with_count = session.query(
                Deck,
                func.count(Card.id).label('card_count')
            ).outerjoin(Card).filter(Deck.uid == uid).group_by(Deck.id).all()

            return [{
                'id': deck.id,
                'name': deck.name,
                'description': deck.description,
                'last_edited': deck.last_edited,
                'card_count': card_count
            } for deck, card_count in decks_with_count]

    # Card methods
    def add_card(self, deck_id, concept, detail):
        with self.Session() as session:
            new_card = Card(deck_id=deck_id, concept=concept, detail=detail)
            session.add(new_card)
            session.commit()
            return new_card.id

    def get_cards_by_deck_id(self, deck_id, uid):
        with self.Session() as session:
            deck = session.query(Deck).filter(Deck.id == deck_id, Deck.uid == uid).first()
            if not deck:
                return None
            
            cards = session.query(Card).filter(Card.deck_id == deck_id).all()
            return [{
                'id': card.id,
                'concept': card.concept,
                'detail': card.detail,
                'attempts': card.attempts,
                'correct_attempts': card.correct_attempts
            } for card in cards]

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

    def get_chats_by_conversation(self, conversation_id):
        with self.Session() as session:
            return session.query(Chat).filter(Chat.conversation_id == conversation_id).order_by(Chat.time).all()

    def get_latest_chats(self, conversation_id, limit=10):
        with self.Session() as session:
            return session.query(Chat).filter(Chat.conversation_id == conversation_id).order_by(Chat.time.desc()).limit(limit).all()