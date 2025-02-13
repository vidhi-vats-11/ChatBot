import React, { useState } from 'react';
import { Container } from '@mui/material';
import ChatHistory from './components/ChatHistory';
import QueryInput from './components/QueryInput';
import axios from 'axios';

const App = () => {
  const [responses, setResponses] = useState([]);

  const handleQuery = async (query) => {
    const response = await axios.post('http://localhost:8000/query', { query });
    setResponses([...responses, { query, response: response.data.response }]);
  };

  return (
    <Container>
      <h1>Chatbot Interface</h1>
      <QueryInput onQuery={handleQuery} />
      <ChatHistory responses={responses} />
    </Container>
  );
};

export default App;