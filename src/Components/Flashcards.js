import React, {useEffect} from 'react';

function Flashcards(){

    useEffect(() => {
        // redirect if user is not logged in
        fetch('/api/login').then(res => res.json()).then(res => {
            if(!res.loggedIn) 
                window.location ='/';
        })
        
    }, []);

    return(
        <p> This is for the a flash card deck. </p>
    )
}
export default Flashcards;