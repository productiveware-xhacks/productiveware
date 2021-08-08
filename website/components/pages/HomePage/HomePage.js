import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { push } from 'connected-react-router';
import * as R from 'ramda';

import Section from 'react-bulma-companion/lib/Section';
import Container from 'react-bulma-companion/lib/Container';
import Title from 'react-bulma-companion/lib/Title';
import Columns from 'react-bulma-companion/lib/Columns';
import Column from 'react-bulma-companion/lib/Column';

import TodoList from '_organisms/TodoList';
import { attemptGetOverdueTodo } from '_thunks/todos';

export default function HomePage() {
  const dispatch = useDispatch();
  const { user } = useSelector(R.pick(['user']));

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (R.isEmpty(user)) {
      dispatch(push('/login'));
    } else {
      dispatch(attemptGetOverdueTodo())
        .catch(R.identity)
        .then(() => setLoading(false));
    }
  }, []);

  return !loading && (
    <div className="home-page page">
      <Section>
        <Container>
          <Title size="1">
            Home Page
          </Title>
          <Section className="todo-section">
            <Title size="1" className="has-text-centered">
              Overdue Todo List:
            </Title>
            <Columns>
              <Column size="8" offset="2" className="has-text-left">
                <TodoList {...{overdue: true}}/>
              </Column>
            </Columns>
          </Section>
        </Container>
      </Section>
    </div>
  );
}
