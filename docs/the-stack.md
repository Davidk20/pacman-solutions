# The Stack

The sequence diagram below shows how the user interacts with the application on a high level. This diagram abstracts most of the inner workings of the application to show how the frontend uses the backend API to display to the user the relevant information.

```mermaid
sequenceDiagram

    actor User

    box Frontend
        participant GameWindow
        participant WebApp
    end
    box Backend
        participant Flask
        participant GameManager
        participant LevelHandler
    end


    User->>+WebApp: User requests webpage
    WebApp->>+Flask: Request for summary of all levels
    Flask->>-WebApp: JSON containing level summaries
    WebApp->>-User: User displayed levels

    User->>+WebApp: User requests level
    WebApp->>Flask: Request(level)
    Flask->>GameManager: Solve(level)
    GameManager->>LevelHandler: Load(level)
    destroy LevelHandler
    LevelHandler->>GameManager: Return Loaded(Level)

    create actor Agent

    GameManager->>Agent: Load into level

    loop Every Game Tick until game complete
        GameManager->>+Agent: Update State
        Agent->>-GameManager: Communicate move
    end

    destroy Agent
    Agent->>GameManager: Unload Agents

    destroy GameManager
    GameManager->>Flask: Return level + simulation

    destroy Flask
    Flask->>WebApp: Return level + simulation

    WebApp->>-GameWindow: Render simulation
    GameWindow->>User: View Simulation
```
