# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "tms_micro"
copyright = "2024, Sabbir Ahmed"
author = "Sabbir Ahmed"
release = "v0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinxcontrib.mermaid",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

mermaid_d3_zoom = True
mermaid_params = ["--theme", "forest", "--backgroundColor", "transparent"]
# html_js_files = [
#     "js/mermaid.js",
# ]


autoapi_type = "python"
autoapi_dirs = ["../../src/main_service", "../../src/auth_service"]
