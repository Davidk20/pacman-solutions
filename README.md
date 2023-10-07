# Final Year Project - Solving Pacman using AI

## Prerequisites

- Python >= 3.10
  - Poetry >= 1.6.1
- npx / npm >= 10.2.0
- Docker >= 20.10.23
  - Docker Compose >= 2.15.1

## Development

In order to run both the front end and back end at the same time, both servers will need to be run in separate terminal instances.

### Flask Server

```bash
cd solving-pacman-backend
poetry install
cd solving_pacman_backend
poetry run flask run --debug
```

### React Server

```bash
cd solving-pacman-frontend
npm install
npm start
```

## Production

To build and run the application for production, a Docker image needs to be built for the Flask and React servers. The Docker Compose file will then compile this into a single, full-stack application.

### Flask

TODO

### React

```bash
# This builds the react server into an image. The tag parameter is used twice to allow two tags to be used.
# The latest tag is used to specify that this is the latest version while the specific numbering of the image is used for archiving once this is no longer the latest
docker build . --tag davidkidd/solving-pacman-frontend:latest --tag davidkidd/solving-pacman-frontend:{new-version-number}
docker run -p 3000:80 -d davidkidd/solving-pacman-frontend:latest
```

### Docker Compose

TODO

## Troubleshooting

### `error:0308010C:digital envelope routines::unsupported`

```bash
npm cache clear --force
npm audit fix --force
```

## Acknowledgements

- [Pacman](https://www.pacman.com/en/) - For the inspiration to solve this game