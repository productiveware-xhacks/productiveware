import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { push } from 'connected-react-router';
import * as R from 'ramda';

import Section from 'react-bulma-companion/lib/Section';
import Container from 'react-bulma-companion/lib/Container';
import Title from 'react-bulma-companion/lib/Title';
import Box from 'react-bulma-companion/lib/Box';

export default function HomePage() {
  const dispatch = useDispatch();
  const { user } = useSelector(R.pick(['user']));

  useEffect(() => {
    if (R.isEmpty(user)) {
      dispatch(push('/login'));
    }
  }, []);

  const h6FontSize = {fontSize: "1.75em"};
  const h3FontSize = {fontSize: "1.2em"};
  const pFontSize = {fontSize: "1.12em"};

  return (
    <div className="home-page page">
      <Section>
        <Container>
          <Title size="1">
            Home Page
          </Title>
          <Box>
            <h3 style={h6FontSize}>Welcome to our project for XHacks 2021</h3>
            <h6 style={h3FontSize}>The goal of this program is to make you productive. How? Well if you're not your files will get encrypted!</h6>
          </Box>
          <Box>
            <p style={pFontSize}>This program is a MERN stack with a python-based client-side application which does the encryption and decryption of files.</p>
            <p style={pFontSize}>Your list of todos are stored on the backend MongoDB server for ease of access from a mobile device.</p>
            <p style={pFontSize}>Find the source code <a href="https://github.com/productiveware-xhacks/productiveware">here.</a></p>
          </Box>
        </Container>
      </Section>
    </div>
  );
}
