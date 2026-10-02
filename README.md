# WeavEHR Project Template

This is a template for creating [WeavEHR](https://github.com/aidh-ms/WeavEHR) projects. It includes a basic project structure, configuration files, and setup scripts to help you get started quickly.


## Getting Started

> [!NOTE]
> Use the included dev container to automatically install all the necessary dev tools and dependencies. To use this you first need to install docker under Linux or WSL2 under windows.

1. **Clone the repository:**
    ```sh
    git clone https://github.com/aidh-ms/weavehr-project-template
    cd weavehr-project-template
    ```

2. **Open the project in Visual Studio Code:**
    ```sh
    code .
    ```

3. **Reopen in container:**
    - Press `F1` to open the command palette.
    - Type `Remote-Containers: Reopen in Container` and select it.
    - VS Code will build the Docker container defined in the `.devcontainer` folder and open the project inside the container.

# TODOs

1. change `DATA_FOLDER` in the [.env](./.devcontainer/.env) file of the .devcontainer
