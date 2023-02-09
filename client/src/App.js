import React, { useState, useRef, useCallback } from "react";
import TextInput from "./components/TextInput"
import Button  from "./components/Button";
import TextOutput from "./components/TextOutput";
function App() {
  const [text,setText]=useState('');
  const [resultText,setResultText]=useState('');
  const changeText=(value)=> {
    setText(value);
  };
  const summaryText=async(e)=> {
    e.preventDefault(); //API 따와서  요약해주기. ..
    //여기서 POST 의 과정이 수행되야함
    const data={input:{text}}; 
    const response=await fetch("/summary",{
      method:'POST',
      body:JSON.stringify(data),
    })
    const output=await response.json();
    console.log(JSON.stringify(data));
    console.log(JSON.stringify(text));
    setResultText(output);
  }
  const clearText=(e)=> {
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