# Diary

## 27/09/23

- Had first meeting with supervisor
- Discussed concepts for project
  - Settled on solving the Rush Hour puzzle
  - Solution would be deployed as a full-stack web application with a Python server backend to solve the problems and a React-based frontend.

## 02/12/23

- After some research, I emailed Matteo to propose a new game to solve, Pacman. He was happy with my proposal and so I have changed the target of my project to Pacman.

## 05/10/23

- Finished and submitted the Project Plan

## 06/10/23

- Initialised base repo
  - Created poetry project
  - Created react project

## 08/10/23

- Configured Dockerfile for respective parts of the project

## 09/10/23

- Attempted to configure Gitlab CI runner
  - Found an issue with the configuration of the shared runners that meant the npm version was too old to install and I was unable to update this.
    - As a result, I have temporarily disabled the frontend CI jobs as they are unable to run.

## 12/10/23

- Began researching game rules and how they would be implemented
- Created UML diagram to begin to break down what would be needed to implement the game programmatically

## 15/10/23

- Configured CI for backend successfully
- Researched running Gitlab Runner locally so that I have more control over the environment

## 18/10/23

- Started preparing report
- Continued working on frontend CI and environment setup
  - Configured eslint correctly and added updated pre-commit workflow to include the frontend jobs

## 20/10/23

- Continued report, UML and other preparation so that when the environment is correctly setup, I can move straight onto configuring game logic.

## 23/10/23

- Environment successfully setup
  - The issues faced in the previous two weeks were down to my configuration of the react project and its installation method.
    - I was attempting to use commands like `npm install` and `npm build` which are not suitable for the CI environment and should have been using `npm ci` instead
    - This, along with ensuring all dependencies were correctly managed and not installed globally on my machine, allowed me to correctly build lint and test my code on the Gitlab server
- Merged work into main so that I can move onto the next step - base game logic

## 24/10/23

- Configured initial draft of base game logic
  - Created all player agent models
  - Created all pickup item models
  - Implemented base scoring system for items and ghosts
- Begun working on a representation of levels
  - Created Wiki to document how levels are generated / rendered
  - Attempted to use Pillow image generation to preview levels quickly while developing
  - Testing different representations to find one which makes sense but is also practical
    - Decision needs to be made to see whether alphanumerical or solely numerical representations work best

## 31/10/23

- Branched the level preview script off of the current task as it is not in scope for this goal and so shouldn't be the focus right now
- Completed first encoding of a level into a text-based format

## 6/11/23

- Created `LevelHandler` to handle injection of levels into the game

## 7/11/23

- Completed first API endpoint to allow game boards to be returned in response to a `GET` request
- Had advisor meeting to update on the progress of the project
  - Used this meeting to inform the structure of the report and to ensure that development was continuing at a good pace

## 11/11/23

- Researched potential applications of CS3940 Multi-Agent Systems coursework and specifically VacuumWorld on my own project.

## 14/11/23

- Started work on frontend implementation.

## 15/11/23

- Completed basic routing for application.
- Carried on research for using Teleoreactive Programming within my project

## 20/11/23 - 25/11/23

- Continued working on interim report.

## 25/11/23

- Submitted draft copy of interim report for review.

## 27/11/23

- Implemented backend code to show an overview of the levels available.

## 29/11/23

- Implemented front-end code to fetch for API requests and handle the data.
- Implemented level selection screen
- Created basic canvas display for the game view.

## 30/11/23

- Finalised initial setup of frontend

## 06/12/23

- Temporarily disabled frontend coverage
  - This was done as testing views / components using certain packages such as `Link` was causing tests to break and it was decided that this should not be a priority as components could be visually seen to be working and therefore could be manually tested
- Created base `Node` structure
- Implemented the initial draft of the Flood Fill algorithm
  - Inspired by [Flood Fill Inspiration](https://lvngd.com/blog/flood-fill-algorithm-python/)
- Tested [networkx](https://networkx.org/) package as potential solution to graph storage problem
  - Needed a way to store the graphs accurately and efficiently

## 07/12/23

- Extended flood fill to be able to connect edges to nodes
- Decided to drop the use of networkx and instead go with an adjacency list to store values
  - networkx package was useful for representing graphs but took too much functionaltiy away where it was needed to traverse graphs in a customised way
  - An adjacency list allowed me to traverse as needed and with far less overhead than using networkx
- Extended flood fill again to populate nodes with what is stored in the position (agent / pickup)

## 08/12/23

- Implemented initial bfs algorithm
- Added a function to test for connectedness of graphs
  - Important as all of the levels in Pac-Man should be connected graphs.

## 10/01/24

- Tidied code and fixed small bugs

## 11/01/24

- Created components to render the walls and all agents on the canvas
- Rendered a static view of the initial state of the map onto the canvas
- Completed task "Render Game Board"

## 15/01/24

- Added detailed documentation for the project
- Updated `flood_fill` to dynamically find first non-wall node rather than a hardcoded position

## 16/01/24

- Implemented additional utility functions for graphs and arrays
  - Graph -> Array conversion
  - Iterator of all Nodes
  - Remaining pickup counters
- Created model to store game snapshots as well as a store for these snapshots
- Begun work on Game Management

## 18/01/24

- Implemented base win / loss conditions

## 20/01/24

- Refactored code to move appropriate functions into utility classes

## 23/01/24

- Converted `Agent` into an abstract class.
  - This creates an overarching wrapper which allows for all agents to function the same.
- Refactored Pac-Man and Ghost agents to use this new wrapper.

## 25/01/24

- Added the ghost's home paths to the level configuration
- Refactored `LevelHandler` to be a set of functions not a class
  - Using a class meant that the app was cluttered with single-use instances of LevelHandler which meant that the file was also being opened and left open multiple times.
  - By using a generator it is now able to open and use the file only when necessary and while this may result in more reads, this means that the file is safer and leaves less clutter in memory.

## 29/01/24

- Refined agent cycle functions to take in `GameState`.
- Improved agent collision logic.

## 30/01/24

- Continued collision logic.
- Developed death logic for when Pac-Man dies.

## 31/01/24

- Had first meeting of the term with supervisor.
  - Discussed where the project is at and my performance last term.
  - Discussed the issue I had related to state communication between API and client.
    - Decided that it was best to send a list of the full arrays instead of trying to work out a way to reduce this and rebuild on the client.
    - This was because the API will usually have more computing power than the client and also the increase in file size should be negligible as it is only a few arrays of single numbers and the data shouldn't be too large to cause a bottleneck in this format.
  - I also had the idea during the meeting for how to calculate the Heuristic function for using with an A* implementation
    - Idea is that each edge has a uniform cost of 1 which is then increased by the score of each pickup within that path.
      - Ghosts would usually prune a path, however if Pac-Man is energised it would mean that ghosts increment the score the same as pickups
      - This is designed to reward Pac-Man for venturing down higher scoring paths and prioritising collecting dots when traversing
      - This also allows for expansion should I develop a reinforcement model, as this would act as the reward function
        - This should mean that Pac-Man would learn a level of risk taking as with also having three lives, it may attempt to go down higher scoring paths even if the risk of being caught by a ghost is high.

## 01/02/24

- Implemented check to identify repeated cyclic paths
  - While cyclic paths are valid, the path finding algorithm needs a way to prevent paths which endlessly repeat the same cycles. This function achieves this by checking for a two-node repeated sequence within the path which would indicate the algorithm attemping to go down the same path twice.

## 07/02/24

- Created `find_all_paths` function
  - Given two points, the function will recursively attempt to find all valid paths between these points.
  - Initially, can only find a single, simple path

## 08/02/24

- Developed `find_all_path` to be able to find multiple paths
- Refactored `find_all_path` function from recursive function to iterative function
  - While a recursive approach works on simple graphs, the graphs created from the levels were too complex and often caused a `RecursionError`
- Was also decided that no filtering would be applied to the paths returned, and so this would be down to the agents own mind to decide
  - This allows for decision making to be left to the agents, where they can decide whether it is worth taking a valid or 'safe' path.
- Added home path attributes to all agents

## 15/02/24

- Refactored `GameManager` to take an `integer` as a starting argument rather than an already instantiated `Graph`
  - There was no need to handle this externally as the graph is not used other than in the game and so prevents unnecessary coupling.
- Implemented a `setup_game` function to inject the agents into the game state
- Implemented a `start` game function
- Implemented an external entry point to the class

## 22/02/24

- Simplified `setup_game`
- Added call to agents movement within game's `tick` function

## 26/02/24

- Created a model to represent a `Path`
  - Added magic methods for length, representation and equality
  - Implemented a path cost function
- Used `Path` to create a shortest path function in `Graph`
- Begun implementing logic for `PacmanAgent`
  - The first version of the agent will keep Pac-Man static and simply eliminate the `NotImplementedError` so that the game methods can be tested correctly.
  - After this, I will be looking at basic and well-documented patterns from original strategies
    - This will be discussed further in [Path Finding](docs/agent-minds.md)

## 27/02/24

- Decided instead of trying to implement Pac-Man logic that I should instead implement a Ghost as they are pre-defined and easier
- I have temporarily removed the `NotImplementedError` uses in the agents methods so that I could test the game running
- I implemented some basic logic for the ghost based on its current state and then using the `find_all_paths` method to target Pac-Man
- I was attempting to run the game but it was hanging on the first iteration of the game
  - After some debugging, I found this to be because there were so many valid paths that even within a few seconds it was reaching 500 possible paths.
    - Most of my testing so far had taken place on mock graphs with far less nodes and so this wasn't spotted sooner
- I have had an idea to limit the number of paths by using a length check idea
  - Once the first valid path is found, its length is used as a comparison
  - Any path being built which reaches a length 1.5 times bigger than the first valid list will be ignored and a new path will be explored
  - The idea is that this gives enough of a buffer to allow a variety of paths to be generated while also pruning unnecessarily long paths
  - *The margin can be adapted later depending on its performance*
- After more testing, the length limiting idea didn't work, even when reducing this margin to any path that is even 1 node longer than the first found path.
  - This is because, in the first path found, the path taken is going sideways towards the teleporter and then coming at Pac-Man from the right hand side, creating the unexpectedly long path.
- To fix this, the length filter will have to be more intelligent, The first test I am attempting will use the average length of the lists as a marker instead of the length of the first.
  - This should bring down the threshold for filtering as shorter paths are found as the average will lower over time, while never allowing longer lists.
- This new threshold was successful and the simulation is now running in much more reasonable time.

- A new bug was then discovered once I had the simulation actually running
  - Once the Ghost started moving, for some reason, it begun to target the teleporter as the quickest path
    - I am unsure why this is the case as this is definitely not the quickest path
  - Once the ghost reaches the teleporter, it appears to get caught in an endless loop of moving between the two teleporters
    - I have one idea to fix this which involves adding a `path_history` attribute to agents which will give me the ability to identify when these loops are occurring.

## 28/02/24

- I have begun to look at alternatives to using DFS in my path finding algorithm.
  - My priority for this algorithm is to find a collection of paths that are reasonably short (within an acceptable range)
  - Assuming the systems that will be running this application, memory is not an issue
  - Because of the above, I am leaning towards BFS instead (there is already an existing bfs function within `Graph`)
- I also looked into IDDFS however this is incompatible with my needs
  - I do not just want the single-shortest path, but a collection so that they can be evaluated to ensure they are compatible with the needs of the agent.

- I now plan to modify the `find_all_paths` function to use BFS
  - As this will now provide the most optimal paths first, I will no longer look to iterate through all paths until exhausted, but instead I will set a hard cap to only provide the agent with a limited set of paths.
  - I will start this cap at 5 but I will change if necessary
    - This is not an expectation that all calls to the function will return 5 (as this may not always be possible) but rather that if this cap is hit, the function can return early and stop unnecessary computation.

- I refactored `find_all_paths` using a combination of my `bfs` function and the exiting "multi-path" dfs solution I had been using previously.
  - It was instantly more efficient than using dfs and so this will be adopted moving forward.
