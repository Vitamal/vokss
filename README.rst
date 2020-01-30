=============
VOKSS Atelier
=============

Atelier is a simple, responsive application suitable for ateliers, tailors, design studios or small sewing business .
It uses the best tailor practices, and on top of that, it’s fast, simple, and easy to use.



-----------
############################################################
Getting started with the Django app and/or the documentation
############################################################


************************
Install the requirements
************************
Install the following:

#. Python
#. PIP_
#. VirtualEnv_
#. virtualenvwrapper_
#. gettext for Django translations


***********************
Install in a virtualenv
***********************
Create a virtualenv using Python 3 (an isolated Python environment)::

    $ mkvirtualenv -p /usr/local/bin/python3 atelier

Install the development requirements::

    $ pip install -r requirements/develop.txt


.. _enable-virtualenv:

.. note::

    Whenever you start a new shell where you need to use the virtualenv we created
    with ``mkvirtualenv`` above, you have to run::

        $ workon atelier


*******************************************
Create or recreate the development database
*******************************************

Run::

    $ ievv recreate_devdb


**************************
Running development server
**************************
Run::

    $ ievv devrun

You can adjust what this command actually runs in the ``IEVVTASKS_DEVRUN_RUNNABLES``
setting (in ``develop_settings.py``).




****************************************
Add new data to the development database
****************************************
Always recreate the database (see the section above) before you add new data to the
development database. Furthermore, let the other developers know that you are doing this.
This avoids conflicts in the SQL dump (which is really hard to merge correctly).

To create a new dump of the development database from you local development
database, use::

    $ ievv dump_db_as_sql

This modifies ``mimirdb/project/develop/dumps/default.sql``, which you should commit and push.


*****************************************************
Creating private backups of your development database
*****************************************************
See the backup and restore chapter of the django_dbdev docs (http://django-dbdev.readthedocs.io).
This is especially useful when you are developing data migrations or working with
a combination of a production database clone and a development database.


*************
Running tests
*************
To run the tests, we need to use a different settings file. We tell Django to
do this using the ``DJANGOENV`` environent variable::

    $ DJANGOENV=test python manage.py test


**************
Build the docs
**************
:ref:`Enable the virtualenv <enable-virtualenv>`, and run::

    $ ievv docs -b -o

``-o`` opens the docs in your default browser. If you do not use ``-o`` the command
will print the location of the index.html file.


.. _PIP: https://pip.pypa.io
.. _VirtualEnv: https://virtualenv.pypa.io
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/
