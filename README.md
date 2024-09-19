
# dataton

This guide provides step-by-step instructions to set up and run the Docker container for this project and how to use it as a Jupyter kernel in Visual Studio Code.

## Prerequisites

***Docker** : Install from [here]().

***Visual Studio Code** : Download from [here](https://code.visualstudio.com/).

***VS Code Extensions** :

*[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by Microsoft

*[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) by Microsoft

## Setup Instructions

### 1. Build the Docker Image

Open a terminal in the root directory of the project (where the `Dockerfile` is located) and build the Docker image:

```

docker build -t my-python-jupyter .

```

### 2. Run the Docker Container

Run the container and mount the necessary directories using the following command:

```

docker run --rm --name my_jupyter_container -p 8888:8888 \

  -v "$(pwd)/raws":/app/raws \

  my-python-jupyter

```

### 3. Connect to the Jupyter Server in Visual Studio Code

#### 3.1. Open Visual Studio Code

Open Visual Studio Code in the root directory of the project.

#### 3.2. Install Required Extensions

Ensure the following extensions are installed:

***Python** by Microsoft

***Jupyter** by Microsoft

#### 3.3. Specify the Jupyter Server

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
2. Type and select  **"Jupyter: Specify Jupyter Server for Connections"** .
3. Enter the URL of the Jupyter server: `http://localhost:8888`
