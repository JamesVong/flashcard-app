import React, {useState} from 'react';

function Create(){
    const [notes, setNotes] = useState("");
    function uploadNotes(){
        console.log(notes);
        console.log("Upload Notes here some how. Most likely call the API.");
    }
    return (
        <div className="p-10 lg:w-[1000px] md:w-[800px] sm:w-[400px]">
            <h1 className="text-primary font-bold text-left">Upload Flashcards</h1>
            <textarea placeholder="Paste your notes in here." rows={10} className="bg-highlight bg-opacity-50 text-base w-full rounded-lg" onChange={(e)=>setNotes(e.target.value)}/>
            <button onClick={uploadNotes} className="bg-primary rounded items-left conetent-end text-base bg-opacity-70 p-4 hover:bg-opacity-80 conetent-end">Create Flashcards</button>
        </div>
    )
}
export default Create;