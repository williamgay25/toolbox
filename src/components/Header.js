import React from 'react';
import './Header.css';

function Header() {
  return (
    <header>
      <div className="header-container">
        <h1>toolbox</h1>
        <h5>by <a href="https://williamgay.me">william gay</a></h5>
      </div>
      <p><a href="https://github.com/williamgay25/toolbox" className="source-code">source code</a></p>
    </header>
  );
}

export default Header;

