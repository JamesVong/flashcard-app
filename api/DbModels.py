# DbModel.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    uid = Column(String(128), nullable=False)  # Firebase UID
    name = Column(String(100), nullable=False)
    description = Column(Text)
    last_edited = Column(DateTime)
    cards = relationship('Card', back_populates='deck')
    conversations = relationship('Conversation', back_populates='deck')

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('decks.id'), nullable=False)
    concept = Column(String(255), nullable=False)
    detail = Column(Text, nullable=False)
    attempts = Column(Integer, default=0)
    correct_attempts = Column(Integer, default=0)
    deck = relationship('Deck', back_populates='cards')

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('decks.id'), nullable=False)
    title = Column(String(255), nullable=False)
    characters = Column(Text)  # Comma-separated string of names
    deck = relationship('Deck', back_populates='conversations')
    chats = relationship('Chat', back_populates='conversation')

class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'), nullable=False)
    author = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    time = Column(DateTime, nullable=False)
    conversation = relationship('Conversation', back_populates='chats')