import React, { Component } from 'react';
import forward from '../Forward.png';
import backward from '../Back.png';
import line from '../Rectangle.png';

class Card extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: [],
      deck: {},
      content: "",
      selected: 0,
    };
  }

  componentDidMount() {
    const { id } = this.props;

    fetch(`/api/deck/${id}/cards`)
      .then(res => res.json())
      .then(cards => {
        this.setState({
          wobble:0,
          id:id,
          cards: cards,
          content: cards[0]?.concept || "",
        });
      })
      .catch(error => console.error('Error fetching cards:', error));

    fetch(`/api/deck/${id}`)
      .then(res => res.json())
      .then(deck => {
        this.setState({ deck });
      })
      .catch(error => console.error('Error fetching deck:', error));
  }

  handleLeft = () => {
    this.setState(prevState => {
      const newSelected = Math.max(prevState.selected - 1, 0);
      return {
        selected: newSelected,
        content: prevState.cards[newSelected].concept,
      };
    });
  };

  handleRight = () => {
    this.setState(prevState => {
      const newSelected = Math.min(prevState.selected + 1, prevState.cards.length - 1);
      return {
        selected: newSelected,
        content: prevState.cards[newSelected].concept,
      };
    });
  };

  flip = () => {
    this.setState(prevState => {
      const currentCard = prevState.cards[prevState.selected];
      return {
        wobble:1,
        content: prevState.content === currentCard.concept ? currentCard.detail : currentCard.concept,
      };
    });
  };
  resetWobble = () => {
    this.setState(prevState =>{
        return {wobble:0};
    });
  }

  render() {
    const { deck, content } = this.state;

    return (
      <div className="mt-10">
        <h1 className="text-primary font-bold text-left">{deck.name}</h1>
        <div className="grid md:grid-cols-1 sm:grid-cols-1">
          <div
            onClick={this.flip}
            onAnimationEnd={this.resetWobble}
            wobble={this.state.wobble}
            className="flippable md:w-[750px] md:h-[415px] sm:w-[475px] sm:h-[275px] bg-highlight shadow bg-opacity-35 hover:bg-opacity-50 flex justify-center items-center cursor-pointer"
          >
            <p className="text-center">{content}</p>
          </div>
        </div>
        <div className="flex justify-center gap-8">
        <button onClick={this.handleLeft}><img src={backward} className="items-center opacity-50 hover:opacity-100" alt="logo" /></button>
        <p>{this.state.selected+1}/{this.state.cards.length}</p>
        <button onClick={this.handleRight}><img src={forward} className="items-center opacity-50 hover:opacity-100" alt="logo" /></button>
        </div>
        <img src={line} className="items-center opacity-100" alt="logo" />
        <div className="flex justify-between mt-6">
            <a className="bg-highlight p-4 hover:bg-opacity-50 rounded" href={`/quiz/${this.state.id}`}>Quiz</a>
            <a className="bg-primary p-4 hover:bg-opacity-50 rounded" href={`/group/${this.state.id}`} >AI Study Group</a>
        </div>
        
      </div>
    );
  }
}

export default Card;
