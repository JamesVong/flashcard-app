import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Navbar from './Components/Navbar.js';
import Landing from './Components/Landing.js';
import Home from './Components/Home.js';
import Flashcards from './Components/Flashcards.js';
import ForgotPage from './Components/Forgot.js';
import Register from './Components/Register.js';
import Login from './Components/Login.js';
import Create from './Components/Create.js';
import Card from './Components/Card.js';
import Quiz from './Components/Quiz.js';
import Group from './Components/Group.js';
import Conversation from './Components/Conversation.js';
import './App.css';

function App() {

  return (
    <div className="App font-raleway bg-background">
      <header className="App-header">
        <BrowserRouter>
          <Navbar/>
          <Switch>
            <Route exact path="/" >
              <Landing/>
            </Route>
            <Route path="/flashcards">
                <Flashcards/>
            </Route>
            <Route path="/home">
                <Home/>
            </Route>
            <Route path="/forgot">
                <ForgotPage/>
            </Route>
            <Route path="/register">
                <Register/>
            </Route>
            <Route path="/login">
                <Login/>
            </Route>
            <Route path="/create">
                <Create/>
            </Route>
            <Route path="/deck/:id" render={({match}) => <Card id={match.params.id}/>}></Route>
            <Route path="/quiz/:id" render={({match}) => <Quiz id={match.params.id}/>}></Route>
            <Route path="/group/:id" render={({match}) => <Group id={match.params.id}/>}></Route>
            <Route path="/conversation/:id" render={({match}) => <Conversation id={match.params.id}/>}></Route>
          </Switch>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
