
# Dataton

This guide provides step-by-step instructions to set up and run the project using Docker Compose, access Jupyter notebooks in Visual Studio Code, and use RStudio in the browser.

## Prerequisites

* **Docker**: Install from [here](https://www.docker.com/get-started).
* **Docker Compose**: Usually comes with Docker Desktop for Windows and Mac. For Linux, you might need to install it separately.
* **Visual Studio Code**: Download from [here](https://code.visualstudio.com/).
* **VS Code Extensions**:
  * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by Microsoft
  *  [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) by Microsoft

## Setup Instructions

### 1. Start the Services

Open a terminal in the root directory of the project (where the `docker-compose.yml` file is located) and run:

```


docker-compose up --build


```

This command will build the necessary Docker images (if not already built) and start the services defined in your `docker-compose.yml` file.

### 2. Access Jupyter Notebooks

#### 2.1. Open Visual Studio Code

Open Visual Studio Code in the root directory of the project.

#### 2.2. Install Required Extensions

Ensure the following extensions are installed:

* **Python** by Microsoft
* **Jupyter** by Microsoft

#### 2.3. Specify the Jupyter Server

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
2. Type and select "Jupyter: Specify Jupyter Server for Connections".
3. Enter the URL of the Jupyter server: `http://localhost:8888`

### 3. Access RStudio in Browser

To use RStudio:

1. Open your preferred web browser.
2. Navigate to `http://localhost:8787`.
3. If prompted, enter the default username and password (usually "rstudio" for both).

You should now see the RStudio interface in your browser, ready for use.

## Usage

You can now use Jupyter notebooks in VS Code and access RStudio directly in your web browser. The necessary services are running in Docker containers managed by Docker Compose.

To stop the services, you can use `Ctrl+C` in the terminal where you ran `docker-compose up`, or run `docker-compose down` in a new terminal window in the same directory.

## Troubleshooting

If you encounter any issues:

1. Ensure all prerequisites are correctly installed.
2. Check that no other services are using the required ports (8888 for Jupyter, 8787 for RStudio).
3. Review the Docker Compose logs for any error messages.

If problems persist, please contact the project maintainer or raise an issue in the project repository.
