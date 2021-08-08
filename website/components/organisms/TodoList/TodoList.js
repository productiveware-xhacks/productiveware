import React from 'react';
import { useSelector } from 'react-redux';
import * as R from 'ramda';

import Todo from '_molecules/Todo';

/**
 * This function subscribes to the store, specifically the list of todos, on any change, 
 * it will take the list of todos and try to render them on the screen
 * @returns A unordered list tag filled with todos
 */
export default function TodoList() {
  const { todos } = useSelector(R.pick(['todos']));

  /// this here is responsible for building the list of Todos and putting them onto the screen
  return (
    <ul className="todo-list">
      {R.reverse(todos).map(todo => <Todo key={todo.id} {...todo} />)}
    </ul>
  );
}
