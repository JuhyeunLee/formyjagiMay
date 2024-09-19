import React, { useState, useEffect } from 'react';
import { Heart, Lock, Unlock } from 'lucide-react';
import './SecretLoveMessage.css';

// ... (previous code remains the same)

const SecretLoveMessage = () => {
  // ... (previous state and functions remain the same)

  const drawHeart = () => {
    const heart = [
      '    🧡🧡🧡    🧡🧡🧡    ',
      '  🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡  ',
      '🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡',
      '🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡',
      '🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡',
      ' 🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡 ',
      '  🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡  ',
      '    🧡🧡🧡🧡🧡🧡🧡🧡    ',
      '      🧡🧡🧡🧡🧡🧡      ',
      '        🧡🧡🧡🧡        ',
      '          🧡🧡          ',
      '           🧡           '
    ];

    setHeartEmojis(heart.map((row, rowIndex) => 
      [...row].map((char, colIndex) => 
        char === '🧡' ? { row: rowIndex, col: colIndex } : null
      ).filter(Boolean)
    ).flat());
  };

  return (
    <div className="container">
      <div className="heart-background">
        {heartEmojis.map((pos, index) => (
          <span 
            key={index} 
            className="heart-emoji animate-fade-in"
            style={{ 
              top: `${pos.row * 4}%`, 
              left: `${pos.col * 4}%`,
              animationDelay: `${index * 0.05}s`
            }}
          >
            🧡
          </span>
        ))}
      </div>
      <div className="card">
        {/* ... (rest of the JSX remains the same) */}
      </div>
    </div>
  );
};

export default SecretLoveMessage;
