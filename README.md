# Final Year Project - Pac-Man Solutions

<div align="center">
  <img src=docs/images/solutions-logo.png alt="Pac-Man Solutions Logo" width="25%"/>
</div>

<div align="center">
  <a href="[docs-link]"><strong>Documentation</strong></a>
  <strong>·</strong>
  <a href="license.txt"><strong>License</strong></a>
  <strong>·</strong>
  <strong>Demo (Coming Soon)</strong>
  <br/>
  <br/>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python logo"/>
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="flask logo"/>
  <img src="https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D" alt="poetry logo"/>
  <br/>
  <img src="https://shields.io/badge/react-black?logo=react&style=for-the-badge" alt="react logo"/>
  <img src="https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white" alt="typescript logo"/>
  <br/>
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="docker logo"/>
</div>

An artificial intelligence environment enabling users to watch simulated solutions to the original 1980's Pac-Man arcade game.

## Key Features

- Simulate intelligent agents attempting to solve Pac-Man levels in a custom-built environment
- Watch these solutions in an interactive React application
- Develop agents to compete against the pre-built models

## Getting Started

Below are the instructions required to get the application running locally. Only the back-end is required for a minimum application which will run on the command line, while the front-end is optional to aesthetically render solutions.

### Back-End (Solutions)

There are two options for installation once the repository has been cloned, both options require an installation of Python >= 3.10 and the `venv` package to be installed.

```bash
# once Python is successfully installed
pip install venv
```

#### 1) Using Poetry (Recommended for development)

[Poetry][poetry] must be installed before attempting these steps.

```bash
# navigate to the backend directory
cd solving-pacman-backend
# install dependencies using poetry
poetry install
# spawn a new virtual environment using poetry
poetry shell
```


#### 2) Using requirements.txt with `venv` (Recommended for quick builds)

```bash
# navigate to the backend directory
cd solving-pacman-backend
# create the virtual environment
python3 -m venv venv

# activate the virtual environment (windows)
venv\Scripts\activate
# activate the virtual environment (unix)
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

Once the environment is setup and activated, the driver script can be run:

```bash
❯ python3 main.py -h
usage: main.py [-h] [-l LEVEL] [-v] [-d] [-o OUTPUT_FILE] [-r RUNS] {server,local,analytics}

Pac-Man Solutions - Back-End: AI solutions to abstractions of Pac-Man levels.

positional arguments:
  {server,local,analytics}
                        server = Run Flask server, local = Run single game, analytics = Run analytics tool

options:
  -h, --help            show this help message and exit
  -l LEVEL, --level LEVEL
                        specify level number as an integer

Local Script Options:
  -v, --verbose         enable verbose output - full final state printing
  -d, --debug           enable debug output - full final state printing + all noteworthy events

Analytics Options:
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        write the output data to a file
  -r RUNS, --runs RUNS  the number of runs completed to assess performance
```

### Front-End (React)

To setup and run the react application, [npm >= 10.2.0][npm-install] must be installed. For the React app to function correctly, the Flask server must be running.

```bash
# navigate to the front-end directory
cd solving-pacman-frontend
# install dependencies
npm install
# start the local server
npm start
```

## Development

### Pre-Commit

This project makes use of [pre-commit](https://pre-commit.com/) as a tool for development. Usage requires Python to be installed, however, this should already be installed should you have followed the [installation steps](#back-end-solutions).

```shell
# only run this if not already installed
pip install pre-commit
# the following command should be successful
pre-commit --version
# inside the project directory, run this command to install the git hook scripts
pre-commit install --hook-type pre-commit --hook-type pre-push
```

With this now configured, a series of jobs will now run upon every commit and push. Commit jobs will consist of linting whilst push jobs involve testing. See [pre-commit-config.yaml][pre-commit-path] for more detailed information.

## Deployment

Docker has been utilised to deploy the full-stack application. Docker images for the front and back-end applications are brought together using a Docker Compose file. Before following these steps, ensure [Docker >= 20.10.23][docker-install] and [Docker Compose >= 3.8][docker-compose-install] are installed correctly.

### Publishing a new version

When a new version of the application is ready, a new version of the docker images must also be generated. The version of the image must match the version given within the repository, and the `latest` tag should always be used to ensure the pointer is up to date.

```bash
# build the back-end image

# navigate to the directory
cd solving-pacman-backend
# building the image
docker build . --tag davidkidd/solving-pacman-backend:latest --tag davidkidd/solving-pacman-backend:{new-version-number}

#####################################################

# building the front-end image

# navigate to the directory
cd solving-pacman-frontend
# building the image
docker build . --tag davidkidd/solving-pacman-frontend:latest --tag davidkidd/solving-pacman-frontend:{new-version-number}
```

### Running the images (individually)

```bash
# running the back-end
docker run -p 4000:4000 -d davidkidd/solving-pacman-backend:latest
# running the front-end
docker run -p 3000:80 -d davidkidd/solving-pacman-frontend:latest
```
### Running the images (Using Docker Compose)

```bash
# run the following command from the project's root directory
docker compose up
```


## Known Bugs

### React

#### Stuttering Render

- There is currently a visual bug where, whilst rendering the simulation, the state will jump suddenly and continue from a seemingly random point with agents in new positions not near their previous.
- Once the same simulation is restarted, this event does not occur and so it appears to be a front-end issue with the way that the states are rendered.
- It is not a commonly-occurring bug and so it has not been pinpointed yet, nor does it constitute a major issue


## Acknowledgements

- [Pacman](https://www.pacman.com/en/) - For the inspiration to solve this game
- [Public Pixel Font](https://www.fontspace.com/public-pixel-font-f72305) - For the font used in the web application


<!-- MARKDOWN LINKS & IMAGES -->

[docs-link]: https://david-kidd.gitbook.io/ai-solutions-to-pac-man/
[react-badge]: https://shields.io/badge/react-black?logo=react&style=for-the-badge
[pre-commit-path]: /solving-pacman-backend/.pre-commit-config.yaml
[poetry]: https://python-poetry.org/docs/
[npm-install]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
[docker-install]: https://docs.docker.com/get-docker/
[docker-compose-install]: https://docs.docker.com/compose/install/
