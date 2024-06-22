import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import Navbar from './Components/Navbar.js';
import Landing from './Components/Landing.js';
import Home from './Components/Home.js';
import Flashcards from './Components/Flashcards.js';
import FrogotPage from './Components/Frogot.js';
import Register from './Components/Register.js';
import Login from './Components/Login.js';
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
                <FrogotPage/>
            </Route>
            <Route path="/register">
                <Register/>
            </Route>
            <Route path="/login">
                <Login/>
            </Route>
          </Switch>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
