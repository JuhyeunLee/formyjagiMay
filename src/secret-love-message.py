import React, { useState, useEffect } from 'react';
import styled, { keyframes, css } from 'styled-components';
import { Heart } from 'lucide-react';

const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;

const slideIn = keyframes`
  from { transform: translateY(-20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
`;

const bounce = keyframes`
  0%, 100% { transform: translateY(-25%); }
  50% { transform: translateY(0); }
`;

const zoomInOut = keyframes`
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.5); }
`;

const Container = styled.div`
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
`;

const Button = styled.button`
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background-color: ${props => props.primary ? '#ff4081' : '#3f51b5'};
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  }
`;

const RevealContainer = styled.div`
  animation: ${fadeIn} 1s ease-out;
`;

const SecretMessage = styled.p`
  font-size: 2rem;
  color: #ff4081;
  margin: 1rem 0;
  animation: ${slideIn} 1s ease-out, ${pulse} 2s infinite;
`;

const KissingEmoji = styled.span`
  font-size: 5rem;
  display: inline-block;
  animation: ${zoomInOut} 4s infinite;
`;

const FireworkContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 9999;
`;

const firework = keyframes`
  0% { transform: translate(var(--x), var(--initialY)); width: 0px; opacity: 1; }
  50% { width: 5px; opacity: 1; }
  100% { width: 0px; opacity: 0; transform: translate(var(--x), var(--finalY)); }
`;

const FireworkSpan = styled.span`
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border: 2px solid #ff4081;
  transform: translate(0, 0);
  animation: ${firework} 2s ease-out infinite;
`;

const HeartContainer = styled.div`
  font-size: 24px;
  line-height: 1;
  text-align: center;
  position: relative;
  height: 200px;
`;

const HeartEmoji = styled.span`
  position: absolute;
  animation: ${fadeIn} 0.5s ease-out forwards;
`;

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

  useEffect(() => {
    generateNewMessage();
  }, []);

  useEffect(() => {
    if (isRevealed) {
      drawHeart();
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
  };

  const drawHeart = () => {
    const heart = [
      '  🧡🧡  🧡🧡  ',
      '🧡🧡🧡🧡🧡🧡🧡',
      '🧡🧡🧡🧡🧡🧡🧡',
      ' 🧡🧡🧡🧡🧡🧡 ',
      '  🧡🧡🧡🧡🧡  ',
      '    🧡🧡🧡    ',
      '     🧡🧡     ',
      '      🧡      '
    ];

    heart.forEach((row, rowIndex) => {
      [...row].forEach((char, charIndex) => {
        if (char === '🧡') {
          setTimeout(() => {
            setHeartEmojis(prev => [...prev, { row: rowIndex, col: charIndex }]);
          }, (rowIndex * 8 + charIndex) * 100);
        }
      });
    });
  };

  return (
    <Container>
      <h1 style={{ fontSize: '2rem', color: '#ff4081', marginBottom: '1rem', textAlign: 'center' }}>Secret Love Message for May</h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '1rem', textAlign: 'center' }}>{message}</p>
      
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1rem' }}>
        <Button primary onClick={() => setIsRevealed(!isRevealed)}>
          {isRevealed ? 'Hide' : 'Reveal'} Secret Message
        </Button>
      </div>
      
      {isRevealed && (
        <RevealContainer>
          <SecretMessage>May, أحبك</SecretMessage>
          <p style={{ fontSize: '1.2rem', color: '#3f51b5', textAlign: 'center' }}>({secret})</p>
          <div style={{ fontSize: '2rem', margin: '1rem 0', textAlign: 'center' }}>
            <Heart style={{ color: '#ff4081', animation: `${pulse} 2s infinite` }} size={48} />
            <KissingEmoji>💏</KissingEmoji>
            <Heart style={{ color: '#ff4081', animation: `${pulse} 2s infinite` }} size={48} />
          </div>
          <HeartContainer>
            {heartEmojis.map((pos, index) => (
              <HeartEmoji key={index} style={{ top: `${pos.row * 24}px`, left: `${pos.col * 24}px` }}>🧡</HeartEmoji>
            ))}
          </HeartContainer>
          <FireworkContainer>
            {[...Array(20)].map((_, i) => (
              <FireworkSpan
                key={i}
                style={{
                  '--x': `${Math.random() * 100 - 50}vw`,
                  '--initialY': '60vh',
                  '--finalY': `${Math.random() * 50 - 60}vh`,
                }}
              />
            ))}
          </FireworkContainer>
        </RevealContainer>
      )}
      
      <div style={{ textAlign: 'center', marginTop: '1rem' }}>
        <Button onClick={generateNewMessage}>
          Generate New Message
        </Button>
      </div>
      
      <p style={{ textAlign: 'center', marginTop: '1rem', fontSize: '0.8rem', color: '#666' }}>Created with love by Juhyeun Lee</p>
    </Container>
  );
};

export default SecretLoveMessage;
