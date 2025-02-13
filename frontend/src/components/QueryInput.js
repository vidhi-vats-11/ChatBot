import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';

const QueryInput = ({ onQuery }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = () => {
    onQuery(query);
    setQuery('');
  };

  return (
    <div>
      <TextField
        label="Enter your query"
        fullWidth
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <Button variant="contained" color="primary" onClick={handleSubmit}>
        Submit
      </Button>
    </div>
  );
};

export default QueryInput;