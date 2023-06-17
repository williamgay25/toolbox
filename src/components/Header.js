import React from 'react';
import './Header.css';

function Header() {
  return (
    <header>
      <h1>toolbox</h1>
      <p>by william gay</p>
      <nav>
        <ul>
          <li><a href="https://williamgay.me">home</a></li>
          <li><a href="https://github.com/williamgay25">github</a></li>
          <li><a href="https://twitter.com/williamgay25">twitter</a></li>
          <li><a href="https://www.linkedin.com/in/williamegay/">linkedIn</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
