import React from 'react';
import styled from 'styled-components';
import SecretLoveMessage from './SecretLoveMessage';

const AppContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f0f0;
`;

function App() {
  return (
    <AppContainer className="App">
      <SecretLoveMessage />
    </AppContainer>
  );
}

export default App;
