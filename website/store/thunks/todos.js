import { snakeToCamelCase } from 'json-style-converter/es5';
import * as R from 'ramda';

import { getTodos, postTodo, putToggleCompleteTodo, putTodo, deleteTodo } from '_api/todos';
import { setTodos, addTodo, toggleCompleteTodo, updateTodo, removeTodo } from '_actions/todos';

import { dispatchError } from '_utils/api';

/**
 * this function makes a call to the backend API to get the list of all todos,
 * it then updates the list of to-dos within the react store
 * @returns a list of unformatted todos
 */
export const attemptGetTodos = () => dispatch =>
  getTodos()
    .then(data => {
      const todos = R.map(todo =>
        R.omit(['Id'], R.assoc('id', todo._id, snakeToCamelCase(todo))), data.todos);

      dispatch(setTodos(todos));
      return data.todos;
    })
    .catch(dispatchError(dispatch));

/**
 * this function makes a call to the backend API to add a todo,
 * it then updates the list of to-dos within the react store
 * @param {String} text the text of a todo
 * @param {String} dueAt the due date of a todo
 * @returns the current user
 */
export const attemptAddTodo = (text, dueAt) => dispatch =>
  postTodo({ text, due_at: dueAt })
    .then(data => {
      const todo = R.omit(['Id'], R.assoc('id', data.todo._id, snakeToCamelCase(data.todo)));

      dispatch(addTodo(todo));
      return data.user;
    })
    .catch(dispatchError(dispatch));

/**
 * this function makes a call to the backend API to toggle the complete state of a todo,
 * it then updates the list of to-dos within the react store
 * @param {String} id the id of a todo
 * @returns the returned todo
 */
export const attemptToggleCompleteTodo = id => dispatch =>
  putToggleCompleteTodo({ id })
    .then(data => {
      dispatch(toggleCompleteTodo(id));
      return data;
    })
    .catch(dispatchError(dispatch));

/**
 * this function makes a call to the backend API to update a todo,
 * it then updates the list of to-dos within the react store
 * @param {String} id the id of the todo
 * @param {String} text the text of the todo
 * @returns a list of todos
 */
export const attemptUpdateTodo = (id, text) => dispatch =>
  putTodo({ id, text })
    .then(data => {
      dispatch(updateTodo({ id, text, updatedAt: data.todo.updated_at }));
      return data;
    })
    .catch(dispatchError(dispatch));

/**
 * this function makes a call to the backend API to delete a todo,
 * it then updates the list of to-dos within the react store
 * @param {String} id the id of a todo
 * @returns a deleted todo
 */
export const attemptDeleteTodo = id => dispatch =>
  deleteTodo({ id })
    .then(data => {
      dispatch(removeTodo(id));
      return data;
    })
    .catch(dispatchError(dispatch));
