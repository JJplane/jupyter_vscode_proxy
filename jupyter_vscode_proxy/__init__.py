import logging
import os
import shutil
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_vscode():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg"
        )

    def _vscode_command(port):
        full_path = shutil.which("code-server")
        if not full_path:
            raise FileNotFoundError("Can not find code-server in $PATH")
        # lstrip is used as a hack to deal with using paths in environments
        # when using git-bash on windows

        return [
            full_path,
            "--bind-addr",
            "127.0.0.1:" + str(port),
            "--auth",
            "none",
            "--disable-telemetry"
        ]

    return {
        "command": _vscode_command,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {"title": "VS Code", "icon_path": _get_icon_path()},
    }
