django-pipeline-csscompressor
==============

A https://github.com/jazzband/django-pipeline css compressor
to compress css files using https://github.com/sprymix/csscompressor.

This allows you to use django-pipeline to compress CSS files without having to
rely on an external binary like YUI compressor, Uglify, etc.

Installation
------------

    pip install django-pipeline-csscompressor

Configure django-pipeline to use django_pipeline_csscompressor.CssCompressor
as its `CSS_COMPRESSOR` in your `settings.py`:

    CSS_COMPRESSOR = 'django_pipeline_csscompressor.CssCompressor '
