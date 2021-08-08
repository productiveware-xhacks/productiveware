import React from 'react';
import { useSelector } from 'react-redux';
import * as R from 'ramda';

import Todo from '_molecules/Todo';
import Column from 'react-bulma-companion/lib/Column';
import Columns from 'react-bulma-companion/lib/Columns';
import Box from 'react-bulma-companion/lib/Box';

/**
 * This function subscribes to the store, specifically the list of todos, on any change, 
 * it will take the list of todos and try to render them on the screen
 * @param {Object} overdue a boolean to detemine the text displayed
 * @returns A unordered list tag filled with todos
 */
export default function TodoList({ overdue }) {
  const { todos } = useSelector(R.pick(['todos']));

  /// this here is responsible for building the list of Todos and putting them onto the screen
  return (
    <ul className="todo-list">
      {todos.length
        ? R.reverse(todos).map(todo => <Todo key={todo.id} {...todo} />)
        : <Columns className="no-todo" gapless>
            <Column size="12">
              <Box>
                <p>No {overdue ? "overdue" : ""} todos, you're all set!</p>
              </Box>
            </Column>
          </Columns>}
    </ul>
  );
}
