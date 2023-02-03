import React, {useEffect, useState} from 'react';
function TextInput({changeText,text}) { 
    return (
    <form>
        <textarea type='textarea' className='langText inputText' rows='10' cols='50' value={text}
        onChange={(e)=> changeText(e.target.value)}/>
    </form>
    );
}
export default TextInput;