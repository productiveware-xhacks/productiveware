import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

import Columns from 'react-bulma-companion/lib/Columns';
import Column from 'react-bulma-companion/lib/Column';
import Button from 'react-bulma-companion/lib/Button';
import Input from 'react-bulma-companion/lib/Input';

import { attemptAddTodo } from '_thunks/todos';
import useKeyPress from '_hooks/useKeyPress';

/**
 * This function is responible for building an input div and a button for creating each to-do
 * @returns A new add todo button
 */
export default function AddTodo() {
  const dispatch = useDispatch();
  const [text, setText] = useState('');

  // this is the function which gets called whenever the "add todo" button is pressed
  const handleAddTodo = () => {
    if (text) {
      // creating a new todo with the text within the input tag and a date timestamp (to be changed later)
      dispatch(attemptAddTodo(text, Date.now()));
      setText('');
    }
  };

  useKeyPress('Enter', handleAddTodo);

  const updateText = e => setText(e.target.value);

  // this is the add todo button
  return (
    <Columns className="add-todo" gapless>
      <Column size="10">
        <Input value={text} onChange={updateText} />
      </Column>
      <Column size="2">
        <Button color="success" onClick={handleAddTodo} fullwidth>
          Add
        </Button>
      </Column>
    </Columns>
  );
}
