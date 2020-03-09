The Python Motivational-Making Library
======================================

This is a script for creating "motivational" posters from a given index and test. Created for Philly Pystar #3 Feb 2012.

It uses the `Python Imaging Library`_, which must be installed with freetype support

.. _Python Imaging Library: http://www.pythonware.com/products/pil/

Or you can use the included Dockerfile to create an image and just run it as a command.

First build the docker image with 

.. code:: bash

    docker build . -t motivational

Then run the command with any arguments you want. Run it without arguments to see the help. Note that you want to bind some directories so that the docker command can read and write somewhere useful.

.. code:: bash 

    docker run --rm --mount type=bind,source=/my/input/dir,target=/input --mount type=bind,source=/my/output/dir,target=/output motivational -i "/input/image.jpg" -m "Docker" -d "Containerize everything!" -o "/output/motivational.jpg"
