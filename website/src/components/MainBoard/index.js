import React from 'react';
import Board from '@asseinfo/react-kanban';
import "@asseinfo/react-kanban/dist/styles.css";

// this we can probably make like. an API request in a nicely formatted JSON
// since it's a proof of concept we can do this for now
let board = {
    columns: [
        {
            id: 1,
            title: "To do",
            cards: [
                {
                    id: 1,
                    title: "liam bad",
                    description: "amogus"
                },
            ]
        },
        {
            id: 2,
            title: "In progress",
            cards: [
                {
                    id: 2,
                    title: "destroy liam",
                    description: "imposer"
                },
            ]
        },
        {
            id: 3,
            title: "Done",
            cards: [
                {
                    id: 3,
                    title: "liam",
                    description: "liam"
                },
            ]
        },
    ]
};

function MainBoard() {
    return(
        <Board
            onLaneRemove={console.log}
            onCardRemove={console.log}
            onLaneRename={console.log}
            initialBoard={board}
            allowAddCard={{ on: "top" }}
            onNewCardConfirm={draftCard => ({
                id: new Date().getTime(),
                ...draftCard
            })}
            onCardNew={console.log}
        />
  );
}

export default MainBoard;