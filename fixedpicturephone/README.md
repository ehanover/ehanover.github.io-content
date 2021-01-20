# FixedPicturePhone: Pictionary + Telephone

The Coronavirus quarantine caused my family to spend a lot more time together, and we often ended up played games to pass the time. One of the games we particularly enjoyed is called BrokenPicturePhone. We thought the concept of the game was entertaining, but the user interface was so difficult to use that playing it became frustrating. I decided to make a clone of the game with a clearer interface and enhanced gameplay options. Naturally, the name FixedPicturePhone came to mind.

## The front-end
My number one priority in making the interface for this game was simplicity and usability because that's what the original BrokenPicturePhone lacked the most. I used React because I recently started learning it and this project was an opportunity to practice using it. I normally use Bootstrap along side a web framework but since Bootstrap seemed like overkill for this simpler app, I researched Bootstrap alternatives and chose [Pure CSS](https://purecss.io/). I enjoyed its simplicity and light weight. 

## The back-end
This is the first project I've made that relies heavily on backend logic. In addition to normal HTTP requests, I utilized the [socket.io](https://socket.io/) library to handle the asynchronous events between the client and the server. 

The server keeps track of the progress of every book and also which players are occupied with a task. Whenever any player finishes a task, the state of each book is reevaluated to see if any of the unoccupied players are eligible to contribute to it. If so, that player is sent the new task. When all of the books are completed, the users are redirected to the game over screen. 

When I had people try playing the game for the first time, I hadn't added handling for players that disconnected in the middle of the game. When one of the players did disconnect and all of the game progress got lost, I admitted that this was a necessary addition to the server code. I was able to use the socket library to catch disconnections and reset the task that the disconnected player was previously working on. That way, no tasks would get lost and the game would always be able to progress once the players reconnect.

## Extensions
* For players that are waiting, show a list of players that are occupied
* Play a sound when a player receives a new task
* Show the progress through the game, like percentage of total tasks done
* Fix small bugs (can't scroll on canvas, first stroke disappears sometimes)

<br />
<br />

## How to play the game
Each player in the game is assigned one "book." Each book is an alternating sequence of drawings and captions. A book always starts with a caption. 

All of the books in the game get randomly passed around to all the players until every player has contributed to every book once (can be customized configuration files). When a player is contributing to a book, the player sees only the last entry to the book, which is either one picture or one drawing. If the player sees a drawing, he or she must write a caption of that drawing. If the player sees a caption, he or she must create a drawing of what that caption says.

When the game ends, everyone looks through all of the book entries together to enjoy the silly drawings and captions made throughout the game.
