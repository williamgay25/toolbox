import React from 'react';
import Header from './components/Header';
import Card from './components/Card';

function App() {
  const tools = [
    {
      toolName: 'Tool 1',
      formComponent: <input type="text" placeholder="Enter text" />,
    },
    {
      toolName: 'Tool 2',
      formComponent: <textarea placeholder="Enter text" />,
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

