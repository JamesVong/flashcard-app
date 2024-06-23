import React, { useEffect, useState,useRef } from 'react';

function Conversation({id}){
  const [input, setInput] = useState("");
  const [messages,setMessages] = useState([]);
  const messagesEndRef = useRef(null);
  useEffect(() => {
    fetch(`/api/conversation/${id}`,{headers: { 'Content-Type': 'application/json' }}).then(res => res.json()).then(data =>{
      setMessages(data)
      scrollToBottom();
    });
    
    // redirect if user is not logged in
    fetch('/api/login').then(res => res.json()).then(res => {
      if(!res.loggedIn) 
          window.location ='/'
    });
    
  }, [id]);
  function scrollToBottom(){
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollTop = messagesEndRef.current.scrollHeight;
    }
  }
  function submit(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({"input":input})
    };
    fetch(`/api/conversation/${id}`, requestOptions)
      .then(res => res.json())
      .then(data => {
        setMessages(data);
        setInput("");
        scrollToBottom();
      });
  }

  return (
    <div className="mt-8">
        <p className="bg-red"></p>
        <h1 className="text-primary font-bold text-left">Study Group</h1>
        <div className="flippable flex flex-col md:w-[860px] md:h-[645px] sm:w-[315px] sm:h-[475px] bg-gray shadow bg-opacity-20">
          <div ref={messagesEndRef} className="overflow-scroll">
            {messages.map(message =>                 
              <div className="flex flex-col text-left overflow-hidden p-4 bg-highlight bg-opacity-50 shadow hover:bg-opacity-100 justify-between">
                  <div class="w-full flex flex-col overflow-hidden">
                      <h5 className="mb-2 text-2xl  font-bold text-ellipsis">{message.name}</h5>
                      <p className="text-base">{message.message}</p>
                  </div>
              </div>
            )}
          </div>
          <div className="flex w-full p-6">
            <input className="bg-highlight rounded w-full" value={input} placeholder="Say something to the group" onChange={(e)=>setInput(e.target.value)}/>
            <button onClick={submit} className="bg-primary rounded text-base bg-opacity-70 p-4 hover:bg-opacity-80">Send</button>
          </div>
        </div>
        <p className="text-sm mb-4">You are currently talking to AI personas, not real humans.</p>
    </div>

  )
}
export default Conversation;