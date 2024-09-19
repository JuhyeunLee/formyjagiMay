import React, { useState, useEffect } from 'react';
import styled, { keyframes } from 'styled-components';
import { Heart } from 'lucide-react';

const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
`;

const bounce = keyframes`
  0%, 100% { transform: translateY(-25%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); }
  50% { transform: translateY(0); animation-timing-function: cubic-bezier(0, 0, 0.2, 1); }
`;

const Container = styled.div`
  max-width: 28rem;
  margin: 2.5rem auto 0;
  padding: 1.5rem;
  background-color: white;
  border-radius: 0.5rem;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  position: relative;
  overflow: hidden;
`;

const Title = styled.h1`
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-align: center;
  color: #d53f8c;
`;

const Message = styled.p`
  font-size: 1.125rem;
  margin-bottom: 1rem;
  text-align: center;
`;

const Button = styled.button`
  padding: 0.5rem 1rem;
  background-color: ${props => props.primary ? '#d53f8c' : '#3b82f6'};
  color: white;
  border-radius: 0.25rem;
  transition: background-color 0.3s;
  
  &:hover {
    background-color: ${props => props.primary ? '#b83280' : '#2563eb'};
  }
`;

const SecretContainer = styled.div`
  text-align: center;
  position: relative;
  animation: ${fadeIn} 0.5s ease-out;
`;

const SecretMessage = styled.p`
  font-size: 1.875rem;
  font-weight: 600;
  color: #e53e3e;
  margin-bottom: 0.5rem;
`;

const SecretTranslation = styled.p`
  font-size: 1.25rem;
  color: #e53e3e;
`;

const EmojiContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 0.5rem;
  gap: 0.5rem;
`;

const KissingEmoji = styled.span`
  font-size: 2.25rem;
  animation: ${bounce} 1s infinite;
`;

const FireworkContainer = styled.div`
  position: absolute;
  width: 0.5rem;
  height: 0.5rem;
  background-color: #ecc94b;
  border-radius: 9999px;
  animation: ${props => props.animation} 0.75s ease-out forwards;
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

  useEffect(() => {
    generateNewMessage();
  }, []);

  const generateNewMessage = () => {
    const newMessage = generateMessage();
    setMessage(newMessage);
    setSecret(revealSecret(newMessage));
    setIsRevealed(false);
  };

  const fireworkAnimation = keyframes`
    0% { transform: translate(${Math.random() * 100}%, ${Math.random() * 100}%) scale(0); opacity: 1; }
    100% { transform: translate(${Math.random() * 100}%, ${Math.random() * 100}%) scale(1); opacity: 0; }
  `;

  return (
    <Container>
      <Title>Secret Love Message for May</Title>
      <Message>{message}</Message>
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1rem' }}>
        <Button primary onClick={() => setIsRevealed(!isRevealed)}>
          {isRevealed ? 'Hide' : 'Reveal'} Secret Message
        </Button>
      </div>
      {isRevealed && (
        <SecretContainer>
          <SecretMessage>May, أحبك</SecretMessage>
          <SecretTranslation>({secret})</SecretTranslation>
          <EmojiContainer>
            <Heart style={{ color: '#e53e3e', animation: `${pulse} 2s infinite` }} size={32} />
            <KissingEmoji>💋</KissingEmoji>
            <Heart style={{ color: '#e53e3e', animation: `${pulse} 2s infinite` }} size={32} />
          </EmojiContainer>
          {[...Array(20)].map((_, i) => (
            <FireworkContainer key={i} animation={fireworkAnimation} />
          ))}
        </SecretContainer>
      )}
      <div style={{ textAlign: 'center', marginTop: '1rem' }}>
        <Button onClick={generateNewMessage}>
          Generate New Message
        </Button>
      </div>
      <p style={{ textAlign: 'center', marginTop: '1rem', fontSize: '0.875rem', color: '#4b5563' }}>Created with love by Juhyeun Lee</p>
    </Container>
  );
};

export default SecretLoveMessage;
