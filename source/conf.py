# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rakizo-dev'
copyright = '2022, omar'
author = 'omar'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_multiversion",
]

templates_path = [
    "_templates",
]

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

smv_tag_whitelist = r'^.*$'
smv_branch_whitelist = r'^.*$'
smv_released_pattern = r'^tags/.*$'

smv_outputdir_format = '{ref.name}'