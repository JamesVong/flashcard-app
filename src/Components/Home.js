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
            if(res.length==0){
                const requestOptions = {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ input:"6.2 deadlock\n\tlocks. Deadlock can occur when one thread holds the lock on the first object, and another thread holds the lock on the second object. If the first thread calls into the second object while still holding onto its lock, it will need to wait for the second object’s lock. If the other thread does the same thing in reverse, neither will be able to make progress.\n\n\tDeadlock and starvation are both liveness concerns. In starvation, a thread fails to make progress for an indefinite period of time. Deadlock is a form of starvation but with the stronger condition: a group of threads forms a cycle where none of the threads make progress because each thread is waiting for some other thread in the cycle to take action. Thus, deadlock implies starvation (literally, for the dining philosophers), but starvation does not imply deadlock.\n\n\n6.5.2 Necessary Conditions for Deadlock\n\tThere are four necessary conditions for deadlock to occur. Knowing these conditions is useful for designing solutions: if you can prevent any one of these conditions, then you can eliminate the possibility of deadlock.\n\t1.\n\tBounded resources. There are a finite number of threads that can simultaneously use a resource.\n\t2.\n\tNo preemption. Once a thread acquires a resource, its ownership cannot be revoked until the thread acts to release it.\n\t3.\n\tWait while holding. A thread holds one resource while waiting for another. This condition is sometimes called multiple independent requests because it occurs when a thread first acquires one resource and then tries to acquire another.\n\t4.\n\tCircular waiting. There is a set of waiting threads such that each thread is waiting for a resource held by another.\n\n\tIn the Banker’s Algorithm, a thread states its maximum resource requirements when it begins a task, but it then acquires and releases those resources incrementally as the task runs. The runtime system delays granting some requests to ensure that the system never deadlocks.\n\n\tA deadlocter what processing order is tried.\n\t• In a deadlocked state, the system has at least one deadlock.\n\tA system in a safe state controls its own destiny: for any workload, it can avoid deadlock by delaying the processing of some requests. In particular, the Banker’s Algorithm delays any request that takes it from a safe to an unsafe state. Once the system enters an unsafe state, it may not be able to avoid deadlock."})
                  };
                fetch('/api/deck', requestOptions)
                    .then(res => res.json())
                    .then(data => window.location = "/home"); 
            }
        })

    }, []);
    return (
        <div className="mt-10">
            <h1 className="text-primary font-bold text-left">My Decks</h1>
            <div className="grid md:grid-cols-4 sm:grid-cols-2 p-4 gap-4">
                {decks.map(deck =>                 
                    <a href={`/deck/${deck.id}`} className="w-[250px] h-[320px] flex flex-col text-left overflow-hidden p-4 bg-highlight bg-opacity-50 shadow hover:bg-opacity-100 justify-between">
                        <div className="h-full flex flex-col overflow-hidden">
                            <h5 className="mb-2 text-2xl  font-bold text-ellipsis">{deck.name}</h5>
                            <p className="text-base">{deck.description}</p>
                        </div>
                        <div className="">
                            <p className=" text-sm">{deck.card_count} Cards, Created {deck.last_edited}</p>
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