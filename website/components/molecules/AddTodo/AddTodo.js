import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

import Columns from 'react-bulma-companion/lib/Columns';
import Column from 'react-bulma-companion/lib/Column';
import Button from 'react-bulma-companion/lib/Button';
import Input from 'react-bulma-companion/lib/Input';

import { attemptAddTodo } from '_thunks/todos';
import useKeyPress from '_hooks/useKeyPress';

/**
 * this function takes a date string and determines whether or not its valid and can be sent through
 * 
 * @param {String} date a date string
 * @returns boolean
 */
const isValidDate = date => {
  let d = new Date(date);

  let isValid = d.getTime() === d.getTime();
  let inPast = d > new Date();

  return isValid && inPast;
}

/**
 * a function to generate a new date
 * 
 * @param {String} format the date format
 * @param {Number} offset how many days by default the to-do will be put into the future
 * @returns String
 */
const generateDueDate = (format = "%d-%b-%Y", offset = 1) => {
  let d = new Date();
  d.setDate(d.getDate() + offset);

  return d.toDateString(format).split(" ").slice(1).join(" ")
}

/**
 * This function is responible for building an input div and a button for creating each to-do
 * @returns A new add todo button
 */
export default function AddTodo() {
  const dispatch = useDispatch();
  const [text, setText] = useState('');
  const [dueDate, setDueDate] = useState(generateDueDate());

  // this is the function which gets called whenever the "add todo" button is pressed
  const handleAddTodo = () => {
    if (text) {
      if (isValidDate(dueDate)) {
        // creating a new todo with the text within the input tag and a date timestamp (to be changed later)
        dispatch(attemptAddTodo(text, dueDate));
  
        // after submitting the new todo, 
        setText('');
        setDueDate(generateDueDate());
      } else {
        console.log("invalid date:", dueDate)
      }
    }
  };

  useKeyPress('Enter', handleAddTodo);

  // this function updates the state of the component's text, just a nice wrapper
  const updateText = e => setText(e.target.value);
  // this function updates the state of the component's dueDate, just a nice wrapper
  const updateDueDate = e => setDueDate(e.target.value);

  // this is the add todo button
  return (
    <Columns className="add-todo" gapless>
      <Column size="7">
        <Input value={text} onChange={updateText} />
      </Column>
      <Column size="3">
        <Input value={dueDate} onChange={updateDueDate} />
      </Column>
      <Column size="2">
        <Button color="success" onClick={handleAddTodo} fullwidth>
          Add
        </Button>
      </Column>
    </Columns>
  );
}
