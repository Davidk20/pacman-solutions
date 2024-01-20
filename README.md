# Final Year Project - Solving Pacman using AI

![Pacman Logo](solving-pacman-frontend/src/assets/images/pacman_logo_small.png)

A full-stack application designed to solve levels from the original 1980's game Pac-Man using an Artificial Intelligence system.

## Documentation

### [The Code Base](docs/code-base.md)

### [Representing Levels](docs/level-representation.md)

### [The Stack](docs/the-stack.md)

### [The Game Cycle](docs/game-cycle.md)

## Requirements

- Python >= 3.10
  - Poetry >= 1.6.1
- npx / npm >= 10.2.0
- Docker >= 20.10.23
  - Docker Compose >= 3.8

## Development

In order to run both the front end and back end at the same time, both servers will need to be run in separate terminal instances.

### Flask Server

```bash
cd solving-pacman-backend
poetry install
poetry shell
cd solving_pacman_backend
python3 server/server.py
```

### React Server

```bash
cd solving-pacman-frontend
npm install
npm start
```

## Production

To build and run the application for production, a Docker image needs to be built for the Flask and React servers. The Docker Compose file will then compile this into a single, full-stack application.

Two tags are specified for each build so that any new version can be tagged as `latest` while also being given a specific version number

### Flask

```bash
cd solving-pacman-backend
docker build . --tag davidkidd/solving-pacman-backend:latest --tag davidkidd/solving-pacman-backend:{new-version-number}
docker run -p 1000:1000 -d davidkidd/solving-pacman-backend:latest
```

### React

```bash
cd solving-pacman-frontend
docker build . --tag davidkidd/solving-pacman-frontend:latest --tag davidkidd/solving-pacman-frontend:{new-version-number}
docker run -p 3000:80 -d davidkidd/solving-pacman-frontend:latest
```

### Docker Compose

```bash
docker compose up
```

## Troubleshooting

### `error:0308010C:digital envelope routines::unsupported`

```bash
npm cache clear --force
npm audit fix --force
```

## Acknowledgements

- [Pacman](https://www.pacman.com/en/) - For the inspiration to solve this game
- [Public Pixel Font](https://www.fontspace.com/public-pixel-font-f72305) - For the font used in the web application
