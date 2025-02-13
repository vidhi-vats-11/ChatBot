import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';

const ChatHistory = ({ responses }) => (
  <List>
    {responses.map((res, index) => (
      <ListItem key={index}>
        <ListItemText primary={`You: ${res.query}`} secondary={`Bot: ${res.response}`} />
      </ListItem>
    ))}
  </List>
);

export default ChatHistory;