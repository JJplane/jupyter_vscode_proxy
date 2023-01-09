# Jupyter Server Proxy with VSCode

pip-installable package to add VSCode to JupyterLab's Launcher menu using [jupyter-server-proxy.](https://github.com/jupyterhub/jupyter-server-proxy). Modified from the example [here](https://github.com/vnijs/jupyter-gitgadget-proxy).

## Setup

First make sure code-server (i.e. VS Code) is properly installed in your JupyterLab environment and available on the system path. Next, install `jupyter-server-proxy` using either `conda` or `pip` (see link above), then

    pip install git+https://github.com/NIVANorge/jupyter_vscode_proxy.git

A button to launch VS Code should be added to the JupyterLab Launcher menu.