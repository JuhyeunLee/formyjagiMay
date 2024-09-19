import React from 'react';
import styled, { createGlobalStyle } from 'styled-components';
import SecretLoveMessage from './SecretLoveMessage';

const GlobalStyle = createGlobalStyle`
  @keyframes firework {
    0% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-50px) scale(0); opacity: 0; }
  }

  .animate-firework {
    animation: firework 1s ease-out forwards;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(-25%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); }
    50% { transform: translateY(0); animation-timing-function: cubic-bezier(0, 0, 0.2, 1); }
  }

  .animate-bounce {
    animation: bounce 1s infinite;
  }
`;

const AppContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f0f0;
`;

function App() {
  return (
    <>
      <GlobalStyle />
      <AppContainer className="App">
        <SecretLoveMessage />
      </AppContainer>
    </>
  );
}

export default App;
