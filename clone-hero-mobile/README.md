# Clone Hero Mobile

### Background
When I was younger I loved playing Guitar Hero on the Wii. Recently, I discovered a huge online community dedicated to keeping Guitar Hero alive in new ways. A large part of the community transcribes modern songs into a "chart" format, which the format that a new open source version of Guitar Hero uses. You can find the song audio and the chart files for a huge number of songs. I searched through the song database [here](https://chorus.fightthe.pw/).

I couldn't find any details about the format of the chart files, so a large part of the time I spent on this project was figuring out the details of the format. The text in the files were thousands of lines of seemingly random letters and numbers.

### Creating the app
I chose Flutter over native Java for Android because Flutter simplified creating of a game loop, loading assets, and displaying animations. Another benefit of Flutter is that it allows cross-platform publishing with the same code, although I haven't yet tried publishing for iOS. I specifically used [Flame](https://pub.dev/packages/flame) to handle looping and animations. 

One especially challenging problem I faced was syncing the note on the screen to the song audio. Any delay in syncing is noticeable to the user because the whole game revolves around timing and accuracy with the song. The separate audio tracks for each instrument had to be loaded into memory before they started playing or else the process of loading the song would delay the other songs. After loading the songs, I used the song's properties in the chart file (like beats per minute and note resolution) to calculate a delay to offset the notes so that they hit the bottom of screen at exactly the right time in the song.

### Extensions
- Right now, users must manually download the song files from the online song database. A menu in the game that allowed searching and downloading of songs would help users play more songs more easily.
- The graphics now are just simple shapes. Adding some enhanced graphics and animations would help the game look a lot more professional.
