# The Stack

The below sequence diagram shows how the frontend and backend stacks interact with each other on a high level to run the application. This diagram abstracts most of the inner workings of the application to show how the frontend uses the backend API to display to the user the relevant information.

```mermaid
sequenceDiagram
    box Frontend
        participant GameWindow
        participant Frontend
    end
    box Backend
        participant Flask
        participant SolutionService
    end

    Frontend->>+Flask: Request for summary of all levels
    Flask->>-Frontend: JSON containing level summaries
    Frontend->>+Flask: Request(level_1)
    Flask->>+SolutionService: Solve(level_1)
    SolutionService->>-Flask: Solution(level_1)
    Flask->>-Frontend: Solution(level_1)
    Frontend->>GameWindow: Animate(level_1)
```
