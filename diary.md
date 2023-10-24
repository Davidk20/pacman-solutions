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
