import React, {useEffect, useState} from 'react';
function Button ({summaryText, clearText}) {
    return (
        <div>
            <button onClick={summaryText}> 요약하기 </button>
            <button onClick={clearText}> 초기화 </button>
        </div>
    );

}
export default Button;