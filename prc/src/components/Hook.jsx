import React, {useEffect, useState} from 'react';
function PRC() {

    const [count,setCount]=useState(0);
    useEffect(()=>{

            document.title=`You Clicked ${count} times`;

    });
    
    
    return (
        <div> 
            <p>You clickedd {count} times</p>
            <button onClick={()=>setCount(count+1)}>Click me</button>
        </div>
    )
}
export default PRC;