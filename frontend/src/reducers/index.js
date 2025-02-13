import { combineReducers } from 'redux';

// Example reducer
const exampleReducer = (state = {}, action) => {
  switch (action.type) {
    case 'EXAMPLE_ACTION':
      return { ...state, data: action.payload };
    default:
      return state;
  }
};

// Combine all reducers here
const rootReducer = combineReducers({
  example: exampleReducer,
});

export default rootReducer;