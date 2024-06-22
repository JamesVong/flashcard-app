import React, {useState,useEffect} from 'react';
import logo from '../logo.svg';

function Landing(){
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/api/time').then(res => res.json()).then(data => {
        setCurrentTime(data.time);
        });
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
export default Landing;