import React, { useState, useEffect } from 'react';
import { Heart, Lock, Unlock } from 'lucide-react';
import './SecretLoveMessage.css';

const words = ["Hello", "Hi", "Hey", "Greetings", "Salutations"];
const adjectives = ["amazing", "wonderful", "fantastic", "incredible", "awesome"];
const nouns = ["day", "morning", "afternoon", "evening", "moment"];

const generateMessage = () => {
  return `${words[Math.floor(Math.random() * words.length)]}! I hope you're having a ${adjectives[Math.floor(Math.random() * adjectives.length)]} ${nouns[Math.floor(Math.random() * nouns.length)]}!`;
};

const revealSecret = (message) => {
  return Array.from(message.toLowerCase()).filter(char => "mayiloveyou".includes(char)).join('');
};

const SecretLoveMessage = () => {
  const [message, setMessage] = useState('');
  const [secret, setSecret] = useState('');
  const [isRevealed, setIsRevealed] = useState(false);
  const [heartEmojis, setHeartEmojis] = useState([]);
  const [password, setPassword] = useState('');
  const [isUnlocked, setIsUnlocked] = useState(false);

  useEffect(() => {
    generateNewMessage();
  }, []);

  const generateHeartBackground = () => {
    const screenWidth = window.innerWidth;
    const screenHeight = window.innerHeight;
    const emojiSize = 50; // Adjust this value to change the density of hearts
    const columns = Math.ceil(screenWidth / emojiSize);
    const rows = Math.ceil(screenHeight / emojiSize);
    
    const hearts = [];
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < columns; j++) {
        hearts.push({ row: i, col: j });
      }
    }
    return hearts;
  };

  useEffect(() => {
    if (isRevealed) {
      setHeartEmojis(generateHeartBackground());
    } else {
      setHeartEmojis([]);
    }
  }, [isRevealed]);

  const generateNewMessage = () => {
    const newMessage = generateMessage();
    setMessage(newMessage);
    setSecret(revealSecret(newMessage));
    setIsRevealed(false);
    setHeartEmojis([]);
    setIsUnlocked(false);
    setPassword('');
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    if (e.target.value.toLowerCase() === 'jagi') {
      setIsUnlocked(true);
    } else {
      setIsUnlocked(false);
    }
  };

  const handleReveal = () => {
    if (isUnlocked) {
      setIsRevealed(!isRevealed);
    }
  };

  return (
    <div className="container">
      {isRevealed && (
        <div className="heart-background">
          {heartEmojis.map((pos, index) => (
            <span 
              key={index} 
              className="heart-emoji animate-fade-in"
              style={{ 
                top: `${pos.row * 50}px`, 
                left: `${pos.col * 50}px`,
                animationDelay: `${(pos.row + pos.col) * 0.1}s`
              }}
            >
              🧡
            </span>
          ))}
        </div>
      )}
      <div className="card">
        <h1 className="title">Secret Love Message for May</h1>
        <p className="message">{message}</p>
        
        <div className="password-container">
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
            placeholder="Enter password"
            className="password-input"
          />
          {isUnlocked ? <Unlock className="lock-icon unlock" /> : <Lock className="lock-icon" />}
        </div>

        <div className="button-container">
          <button className={`button primary ${!isUnlocked && 'disabled'}`} onClick={handleReveal} disabled={!isUnlocked}>
            {isRevealed ? 'Hide' : 'Reveal'} Secret Message
          </button>
        </div>
        
        {isRevealed && (
          <div className="reveal-container">
            <p className="secret-message animate-pulse">May, أحبك</p>
            <p className="secret-translation">({secret})</p>
            <div className="emoji-container">
              <Heart className="heart-icon animate-pulse" size={48} />
              <span className="kissing-emoji animate-zoom">💏</span>
              <Heart className="heart-icon animate-pulse" size={48} />
            </div>
            <div className="firework-container">
              {[...Array(20)].map((_, i) => (
                <span
                  key={i}
                  className="firework"
                  style={{
                    '--x': `${Math.random() * 100 - 50}vw`,
                    '--initialY': '60vh',
                    '--finalY': `${Math.random() * 50 - 60}vh`,
                  }}
                />
              ))}
            </div>
          </div>
        )}
        
        <div className="button-container">
          <button className="button" onClick={generateNewMessage}>
            Generate New Message
          </button>
        </div>
        
        <p className="footer">Created with love by Juhyeun Lee</p>
      </div>
    </div>
  );
};

export default SecretLoveMessage;
