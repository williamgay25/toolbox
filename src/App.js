import React from 'react';
import './App.css';
import Header from './components/Header';
import Card from './components/Card';

function App() {
  const tools = [
    {
      toolName: 'generate qr code',
      formComponent: <input type="text" placeholder="enter a website"/>,
    },
    {
      toolName: 'remove image background',
      formComponent: <input type="file"/>,
    },
  ];

  return (
    <div className="App">
      <Header />
      <div className="card-container">
        {tools.map((tool, index) => (
          <Card key={index} toolName={tool.toolName} formComponent={tool.formComponent} />
        ))}
      </div>
    </div>
  );
}

export default App;

