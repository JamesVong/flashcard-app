import React, {useState,useEffect} from 'react';
import plus from '../Plus.png';

function Home(){
    const [decks, setDecks] = useState([]);

    useEffect(() => {
        // redirect if user is not logged in
        fetch('/api/login').then(res => res.json()).then(res => {
            if(!res.loggedIn) 
                window.location ='/';
        })
        fetch('/api/decks').then(res => res.json()).then(res => {
            setDecks(res);
        })

    }, []);
    return (
        <div className="mt-10">
            <h1 className="text-primary font-bold text-left">My Decks</h1>
            <div className="grid md:grid-cols-4 sm:grid-cols-2 p-4 gap-4">
                {decks.map(deck =>                 
                    <a href="#" className="w-[250px] h-[320px] flex flex-col text-left overflow-scroll p-4 bg-highlight bg-opacity-50 shadow hover:bg-opacity-100 justify-between">
                        <div class="h-full flex flex-col overflow-hidden">
                            <h5 className="mb-2 text-2xl  font-bold text-ellipsis">{deck.title}</h5>
                            <p className="text-base">{deck.description}</p>
                        </div>
                        <div className="">
                            <p className=" text-sm">{deck.length} Cards, Created {deck.date_created}</p>
                        </div>
                    </a>
                )}
                <a href="/create" className="w-[250px] h-[320px] bg-gray bg-opacity-35 shadow hover:bg-opacity-50 items-center">
                    <img src={plus} className="items-center" alt="logo" />
                </a>
            </div>
        </div>
    )
}
export default Home;