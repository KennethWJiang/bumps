# -*- coding: utf-8 -*-
#
# BUMPS documentation documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 13 15:11:19 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
from __future__ import print_function, with_statement

import sys, os
sys.dont_write_bytecode = True
print("python",sys.executable)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
sys.path.insert(0, os.path.abspath('_extensions')) # for sphinx extensions
sys.path.insert(0, os.path.abspath('.')) # for sitedoc

# Add the build directory for the project; this does mean we need to build
# before updating the documents each time, but this can be handled by the
# makefile
from distutils.util import get_platform
platform = '.%s-%s'%(get_platform(),sys.version[:3])
build_lib = os.path.abspath('../build/lib'+platform)
sys.path.insert(0, build_lib)
print("== path ==")
print("\n".join(sys.path))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.autosummary',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              #'sphinx.ext.pngmath',
              #'sphinx.ext.jsmath',
              'sphinx.ext.mathjax',
              #'only_directives',
              #'matplotlib.sphinxext.mathmpl',
              'matplotlib.sphinxext.only_directives',
              'matplotlib.sphinxext.plot_directive',
              #'inheritance_diagram',
              'dollarmath',
              'slink',
              #'wx_directive',
              #'numpydoc.numpydoc',
             ]
#plot_formats = [('png', 120), ('pdf', 50)] # Only make 80 dpi plots
#mathjax_path = 'MathJax/MathJax.js'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Bumps'
copyright = '2006-2014, Public domain'
#copyright = '2006-2011, University of Maryland'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
import bumps
release = bumps.__version__
# The short X.Y version.
#version = ".".join(release.split(".")[:2])
version = release
print("#### Using bumps version %s in %s"%(release, bumps.__file__))

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_trees = ['_*','build','plots']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'haiku'
#html_theme = 'default'
html_style = 'haiku-site.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bumps'


program_title = 'Bumps: Curve Fitting and Uncertainty Analysis'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Bumps.tex', program_title, 'Paul Kienzle', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''
LATEX_PREAMBLE=r"""
\usepackage[utf8]{inputenc}      % Allow unicode symbols in text
\DeclareUnicodeCharacter {00B7} {\ensuremath{\cdot}}   % cdot
\DeclareUnicodeCharacter {00B0} {\ensuremath{^\circ}}  % degrees
\DeclareUnicodeCharacter {212B} {\AA}                  % Angstrom
"""
latex_elements = {'preamble' : LATEX_PREAMBLE}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

if os.path.exists('rst_prolog'):
    with open('rst_prolog') as fid:
        rst_prolog = fid.read()

htmlroot="http://www.reflectometry.org/danse"
def download(name):
    subs = dict(file=name%dict(version=version), path=htmlroot)
    return "%(file)s <%(path)s/download.php?file=%(file)s>"%subs
slink_vars=dict(version=release, htmlroot=htmlroot,
                srczip=download("bumps-%(version)s.zip"),
                winexe=download("bumps-%(version)s-win32.exe"),
                macapp=download("Bumps %(version)s.dmg"),
                vcredist=download("vcredist_x86.exe"),
                wx4osx=download("osx64/wx-2.9.5.0-py27_0.tar.bz2"),
                )

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'bumps', program_title, ['Paul Kienzle'], 1)
]
