import React, { useState, useEffect } from 'react';
import styled, { keyframes } from 'styled-components';
import { Heart, Lock } from 'lucide-react';

const words = ["Hello", "Hi", "Hey", "Greetings", "Salutations"];
const adjectives = ["amazing", "wonderful", "fantastic", "incredible", "awesome"];
const nouns = ["day", "morning", "afternoon", "evening", "moment"];

const generateMessage = () => {
  return `${words[Math.floor(Math.random() * words.length)]}! I hope you're having a ${adjectives[Math.floor(Math.random() * adjectives.length)]} ${nouns[Math.floor(Math.random() * nouns.length)]}!`;
};

const revealSecret = (message) => {
  const secret = "May أحبك"; // "May, I love you" with Arabic
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


  const Firework = () => (
    <div className="absolute w-2 h-2 bg-yellow-500 rounded-full animate-firework" style={{
      left: `${Math.random() * 100}%`,
      top: `${Math.random() * 100}%`,
      animationDuration: `${0.5 + Math.random() * 0.5}s`,
      animationDelay: `${Math.random() * 0.2}s`
    }} />
  );

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-xl relative overflow-hidden">
      <h1 className="text-2xl font-bold mb-4 text-center text-pink-600">Secret Love Message for May</h1>
      <p className="text-lg mb-4 text-center">{message}</p>
      <div className="flex justify-center mb-4">
        <button
          onClick={() => setIsRevealed(!isRevealed)}
          className="px-4 py-2 bg-pink-500 text-white rounded hover:bg-pink-600 transition-colors"
        >
          {isRevealed ? 'Hide' : 'Reveal'} Secret Message
        </button>
      </div>
      {isRevealed && (
        <div className="text-center relative">
          <p className="text-3xl font-semibold text-red-500 mb-2">May, أحبك</p>
          <p className="text-xl text-red-500">({secret})</p>
          <div className="flex justify-center items-center mt-2 space-x-2">
            <Heart className="text-red-500 animate-pulse" size={32} />
            <span className="text-4xl animate-bounce">💋</span>
            <Heart className="text-red-500 animate-pulse" size={32} />
          </div>
          {[...Array(20)].map((_, i) => <Firework key={i} />)}
        </div>
      )}
      <div className="text-center mt-4">
        <button
          onClick={generateNewMessage}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        >
          Generate New Message
        </button>
      </div>
      <p className="text-center mt-4 text-sm text-gray-500">Created with love by Juhyeun Lee</p>
    </div>
  );
};

export default SecretLoveMessage;
