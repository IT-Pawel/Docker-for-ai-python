# Docker-for-ai-python
Simple docker image for python

With installed:

- **flask**
- **redis**
- **pandas**

## Installation

To run this, you will need:

- Docker

Start Docker containers:

```bash
docker-compose up
```

And you will have to instal a few extenstions to VSC

- [Docker Package](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Python Package](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Use
To use and run Pyhons scipts in terminal. You have to connect to remote container. To do that you have to open VSC **command palette** and check option to connect into container with python. After that you can run comands on terminal and all changes for web will be done on fly.
