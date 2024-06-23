import React, {useState} from 'react';

function Create(){
    const [notes, setNotes] = useState("");
    const [spinner, setSpinner] = useState(false);  
    function uploadNotes(){
        setSpinner(true);
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input:notes })
          };
        fetch('/api/deck', requestOptions)
            .then(res => res.json())
            .then(data =>{
                setSpinner(false);
                window.location = `/deck/${data.deck_id}`
                

        }); 
    }
    return (
        <div className="p-10 lg:w-[1000px] md:w-[800px] sm:w-[400px]">
            <h1 className="text-primary font-bold text-left">Upload Flashcards</h1>
            <textarea placeholder="Paste your notes in here." rows={10} className="bg-highlight bg-opacity-50 text-base w-full rounded-lg p-4" onChange={(e)=>setNotes(e.target.value)}/>
            <button onClick={uploadNotes} className="bg-primary rounded items-left conetent-end text-base bg-opacity-70 p-4 hover:bg-opacity-80 conetent-end">Create Flashcards</button>
        </div>
    )
}
export default Create;