import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <header className="App-header">
        <p>Simple React Counter</p>
        <div>
          <button onClick={() => setCount(count - 1)}>-</button>
          <span style={{ margin: '0 10px' }}>{count}</span>
          <button onClick={() => setCount(count + 1)}>+</button>
        </div>
      </header>
    </div>
  );
}

export default App;