import React, { Component } from 'react';
import forward from '../Forward.png';
import backward from '../Back.png';
import line from '../Rectangle.png';

class Quiz extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: [],
      deck: {},
      content: "",
      selected: 0,
      text:"",
      feedback:"",
      color:"highlight",
    };
  }

  componentDidMount() {
    const { id } = this.props;

    fetch(`/api/deck/${id}/cards`)
      .then(res => res.json())
      .then(cards => {
        this.setState({
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
        text:"",
        feedback:"",
        color:"highlight",
        selected: newSelected,
        content: prevState.cards[newSelected].concept,
      };
    });
  };

  handleRight = () => {
    this.setState(prevState => {
      const newSelected = Math.min(prevState.selected + 1, prevState.cards.length - 1);
      return {
        text:"",
        feedback:"",
        color:"highlight",
        selected: newSelected,
        content: prevState.cards[newSelected].concept,
      };
    });
  };

  submit = () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ card_concept: this.state.content, card_detail:this.state.cards[this.state.selected].detail, user_response:this.state.text})
    };
    fetch('/api/feedback', requestOptions)
        .then(res => res.json())
        .then(data =>{
          let letter = data.feedback[0];
          let color;
          if(letter=="I"){
            color="red";
          }
          else if(letter=="C"){
            color="primary";
          }
          else{
            color="highlight";
          }
          this.setState({ 'feedback': data.feedback,'color':color })
        });
        
  };

  render() {
    const { deck, content } = this.state;

    return (
      <div className="mt-8">
        <p className="bg-red"></p>
        <h1 className="text-primary font-bold text-left">{deck.name}</h1>
        <div className="grid md:grid-cols-1 sm:grid-cols-1">
          <div
            className="flippable flex flex-col md:w-[750px] md:h-[415px] sm:w-[475px] sm:h-[275px] bg-highlight shadow bg-opacity-35 p-8"
          >
            <h2 className="text-center text-2xl">{content}</h2>
            <textarea rows={6} value={this.state.text} placeholder="Type your answer and click to submit." className="text-left w-full bg-highlight bg-opacity-50 text-base mt-4 p-4 rounded" onChange={(event) => this.setState({ text: event.target.value })} />
            <div onClick={this.submit} className={`flex flex-col text-left mt-4 text-base w-full rounded bg-opacity-50 bg-${this.state.color} cursor-pointer p-4`}>Feedback:
              <p>{this.state.feedback}</p>
            </div>
          </div>
        </div>
        <div className="flex justify-center gap-8">
          <button onClick={this.handleLeft}><img src={backward} className="items-center opacity-50 hover:opacity-100" alt="logo" /></button>
          <p>{this.state.selected+1}/{this.state.cards.length}</p>
          <button onClick={this.handleRight}><img src={forward} className="items-center opacity-50 hover:opacity-100" alt="logo" /></button>
        </div>
        <img src={line} className="items-center opacity-100" alt="logo" />
        <div className="flex justify-between mt-6">
            <a className="bg-highlight p-4 hover:bg-opacity-50 rounded" href={`/deck/${this.state.id}`}>Practice</a>
            <a className="bg-primary p-4 hover:bg-opacity-50 rounded" href={`/group/${this.state.id}`} >AI Study Group</a>
        </div>
        
      </div>
    );
  }
}

export default Quiz;