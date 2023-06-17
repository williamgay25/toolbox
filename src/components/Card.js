import React from 'react';
import './Card.css';

function Card({ toolName, formComponent }) {
  return (
    <div className="card">
      <h2>{toolName}</h2>
      {formComponent}
    </div>
  );
}

export default Card;