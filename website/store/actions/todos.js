export const SET_TODOS = 'SET_TODOS';
export const ADD_TODO = 'ADD_TODO';
export const TOGGLE_COMPLETE_TODO = 'TOGGLE_COMPLETE_TODO';
export const UPDATE_TODO = 'UPDATE_TODO';
export const REMOVE_TODO = 'REMOVE_TODO';
export const INCREMENT_TODO_ID = 'INCREMENT_TODO_ID';

// these are the actions dispatched to the react store
export const setTodos = todos => ({
  type: SET_TODOS,
  todos,
});

// these are the actions dispatched to the react store
export const addTodo = ({ id, text, createdAt, dueAt, encrypted }) => ({
  type: ADD_TODO,
  createdAt,
  dueAt,
  id,
  text,
  encrypted
});

// these are the actions dispatched to the react store
export const toggleCompleteTodo = id => ({
  type: TOGGLE_COMPLETE_TODO,
  id,
});

// these are the actions dispatched to the react store
export const updateTodo = ({ id, text, updatedAt }) => ({
  type: UPDATE_TODO,
  updatedAt,
  id,
  text,
});

// these are the actions dispatched to the react store
export const removeTodo = id => ({
  type: REMOVE_TODO,
  id,
});
