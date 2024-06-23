import React, {useState,useEffect} from 'react';
function Landing(){
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/api/time').then(res => res.json()).then(data => {
            setCurrentTime(data.time);
        });
    }, []);
    return (
        <div className="">
            <p>I do the langing page top of the morning tomorrow {currentTime}</p>
        </div>
    )
}
export default Landing;