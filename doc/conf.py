# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.absolute()))

# -- Project information -----------------------------------------------------
project = "BioPAL"
author = "BioPAL team"
copyright = "2021, BioPAL team"

# -- General configuration ---------------------------------------------------
extensions = []  # no extensions, just to display Site Offline

exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "legacy",
    "api/*",
    "Notebooks/*",
    "api.rst",
    "documentation.md",
    "getting_started.rst",
    "overview.rst",
]

# -- HTML options ------------------------------------------------------------
html_static_path = ["_static"]
html_theme = "alabaster"  # default teme to avoid pip installations
