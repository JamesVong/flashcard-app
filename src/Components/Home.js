import React, {useState,useEffect} from 'react';
import logo from '../logo.svg';

function Home(){
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        // redirect if user is not logged in
        fetch('/api/login').then(res => res.json()).then(res => {
            if(!res.loggedIn) 
                window.location ='/';
        })

    }, []);
    return (
        <div className="">
            <img src={logo} className="App-logo" alt="logo" />
            <h1>This will be the landing page.</h1>
            <p>
                Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
                className="App-link"
                href="https://reactjs.org"
                target="_blank"
                rel="noopener noreferrer"
            >
                Learn React
            </a>
            <p>The current time is {currentTime}.</p>
        </div>
    )
}
export default Home;