import React, {useEffect, useState} from 'react';
function TextOutput({outtext}) { 
    return (
        <div>
            <p>요약 결과 </p>
            <hr/>
            <p background-color='blue'>{outtext}</p>
        </div>
    );
}
export default TextOutput;