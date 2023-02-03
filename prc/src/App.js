import React, { useState, useRef, useCallback } from "react";
import TextInput from "./components/TextInput"
import Button  from "./components/Button";
import TextOutput from "./components/TextOutput";
function App(){
  const [text,setText]=useState('');
  const [resultText,setResultText]=useState('');
  
  const changeText=(value)=> {
    setText(value);
  };
  const summaryText=(e)=>{
    e.preventDefault(); //API 따와서  요약해주기. ..
    setResultText(text);
  }
  const clearText=(e)=>{
    e.preventDefault();
    setText('');
    setResultText('');
  }


  return (
    <div>
      <h3>Summarizer</h3>
      <TextInput changeText={changeText} text={text}/>
      <Button summaryText={summaryText} clearText={clearText}/>
      <TextOutput outtext={resultText}/>
    </div>
  );
};

export default App;