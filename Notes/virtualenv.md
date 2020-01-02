# virtualenv
#init virtual env
mkdir flaskdir
cd flaskdir
virtualenv venv

#active virtual env
. venv/bin/activate    # bash
venv\Scripts\activate    # cmd

#deactive vitual env
deactivate


> Create virtual isolated Python environments.

- Create a new environment:

`virtualenv {{path/to/venv}}`

- Start (select) the environment:

`source {{path/to/venv}}/bin/activate`

- Stop the environment:

`deactivate`
