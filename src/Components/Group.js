import React, { useEffect, useState } from 'react';
import forward from '../Forward.png';
import backward from '../Back.png';
import line from '../Rectangle.png';

function Group({id}){
  console.log(id);
  const [characters,setCharacters] =useState([]);
  const [selectedCharacters, setSelectedCharacters] = useState([]);
  useEffect(() => {
    fetch(`/api/conversation/${id}`, {'Content-Type':"application/json"}).then(res => res.json()).then(res =>{
      if(!res.error) 
        window.location=`/conversation/${id}`;
      });
    // redirect if user is not logged in
    fetch('/api/login').then(res => res.json()).then(res => {
      if(!res.loggedIn) 
          window.location ='/';
    });
    fetch('/api/conversation/characters').then(res => res.json()).then(res => setCharacters(res));
  }, []);
  function submit(){
    const namesArray = selectedCharacters.map(obj => obj.name);
    if (selectedCharacters.length !=2) return;
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ "deck_id": id, "characters":namesArray})
    };
    fetch('/api/conversation/create', requestOptions)
      .then(res => res.json())
      .then(data => window.location=`/conversation/${id}`);
  }
  function select(character){
    if (selectedCharacters.length >=2) return;
    //maybe add functionality to remove an character select
    setSelectedCharacters(prevItems => [...prevItems, character]);

  }
  return (
    <div className="mt-8">
        <p className="bg-red"></p>
        <h1 className="text-primary font-bold text-left">Character Select</h1>
        <div className="flippable flex flex-col md:w-[860px] md:h-[645px] sm:w-[315px] sm:h-[475px] bg-gray shadow bg-opacity-20 p-8">
          <div className="grid md:grid-cols-4 sm:grid-cols-4 content-center gap-4">
          {characters.map(character =>                 
            <a className={`flex flex-col text-left overflow-scroll bg-highlight bg-opacity-${selectedCharacters.includes(character)?50:100} shadow hover:bg-opacity-50 p-4`} onClick={()=>select(character)}>
                <div className="h-full flex flex-col overflow-hidden">
                    <h5 className="text-2xl  font-bold text-ellipsis">{character.name}</h5>
                    <p className="text-base">{character.description}</p>
                </div>
            </a>
          )}
          </div>
          <div className="flex justify-center mt-6">
            <button onClick={submit} className="bg-primary rounded text-base bg-opacity-70 p-4 hover:bg-opacity-80">Start Chatting</button>
          </div>
        </div>
    </div>
  )
}
export default Group;