from datetime import date

project = 'AnyData'
copyright = f"{date.today().year}, Sijin Information Technology Ltd."
author = 'Sijin Information Technology Ltd.'
master_doc = "index"

language = "en"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # ,'breathe', 'exhale'
    'myst_parser', "sphinx_design", "sphinxcontrib.mermaid", 'sphinxcontrib.bibtex'
]


source_suffix = ['.rst', '.md']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'node_modules']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/OpenCAXPlus/OpenCAXPlusSDK",
    "repository_url": "https://github.com/OpenCAXPlus/OpenCAXPlusSDK",
    "use_repository_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_edit_page_button": True,
}
# html_logo = "_static/ocp.png"
# html_favicon = "_static/logo.png"
html_title = "AnyData"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_image",
]
myst_number_code_blocks = ["typescript"]
myst_heading_anchors = 2
myst_footnote_transition = True
myst_dmath_double_inline = True

bibtex_bibfiles = ['references/refs.bib']