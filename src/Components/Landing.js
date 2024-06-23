import React, {useState,useEffect} from 'react';
import logo from '../Image.png';
function Landing(){
    const [loggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        fetch('/api/login').then(res => res.json()).then(res => {
            if(res.loggedIn) 
              setLoggedIn(true);
          })
    }, []);
    return (
        <div className="flex flex-col sm:p-8 p-32 text-left">
            <div className="flex">
                <div>
                    <h1 className=" text-primary font-bold text-left">A study partner at your fingerprints.</h1>
                    <p >Upcoming exams? Get the help you need fast and explore AI-powered studying with Flashcard App.</p>
                    <div className="mt-4">
                    {loggedIn?<a href="create" className="bg-gray bg-opacity-50 p-4 rounded hover:bg-opacity-35 cursor-pointer">Create</a >:<a href="/register" className="bg-gray bg-opacity-50 p-4 mt-4 rounded hover:bg-opacity-35 cursor-pointer">Register Now</a>}
                    </div>
                </div>
                <div className="">
                    <img className= "" src={logo}/>
                </div>
            </div>
            <div className="flex gap-4 p-8">
                <div className="flex-1 bg-highlight shadow rounded p-4">
                    <h1 className="font-semibold text-primary">AI Flashcard Generation</h1>
                    <p className="text-base">Upload your notes and let our AI make flashcards for you instantly.</p>
                </div>
                <div className="flex-1 bg-highlight shadow rounded p-4">
                    <h1 className="font-semibold text-primary">Quiz Mode</h1>
                    <p className="text-base">Get immediate feedback from our AI when you test yourself.</p>
                </div>
                <div className="flex-1 bg-highlight shadow rounded p-4">
                    <h1 className="font-semibold text-primary">AI Study Group</h1>
                    <p className="text-base">Organize a session with AI study partners. Ask questions and get answers just like a real group.</p>
                </div>
            </div>
        </div>
    )
}
export default Landing;