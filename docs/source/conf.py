project = 'tooltils'
copyright = 'Copyright © 2023 ebots'
author = 'feetbots'
release = '1.4.0'

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
]

source_suffix = '.md'

html_theme = 'alabaster'
html_theme_options = {
    "github_user": "feetbots",
    "github_repo": "tooltils",
    "github_banner": False,
    "show_powered_by": False,
    "show_related": False,
    "note_bg": "#9cedff",}
html_use_smartypants = False
html_static_path = ['']
