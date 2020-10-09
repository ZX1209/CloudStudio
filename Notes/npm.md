## install permission
> https://stackoverflow.com/questions/33725639/npm-install-g-less-does-not-work-eacces-permission-denied

    To minimize the chance of permissions errors, you can configure npm to use a different directory. In this example, it will be a hidden directory on your home folder.

    Make a directory for global installations:

     mkdir ~/.npm-global

    Configure npm to use the new directory path:

     npm config set prefix '~/.npm-global'

    Open or create a ~/.profile file and add this line:

     export PATH=~/.npm-global/bin:$PATH

    Back on the command line, update your system variables:

     source ~/.profile

    Test: Download a package globally without using sudo.

    npm install -g jshint

    If still show permission error run (mac os):

    sudo chown -R $USER ~/.npm-global   




# npm

> JavaScript and Node.js package manager.
> Manage Node.js projects and their module dependencies.

- Download and install a module globally:

`npm install -g {{module_name}}`

- Download all dependencies referenced in package.json:

`npm install`

- Download a given dependency required for the application to run, and add it to the package.json:

`npm install {{module_name}}@{{version}} --save`

- Download a given dependency for development purposes, and add it to the package.json:

`npm install {{module_name}}@{{version}} --save-dev`

- Uninstall a module:

`npm uninstall {{module_name}}`

- List a tree of installed modules:

`npm list`

- Interactively create a package.json file:

`npm init`
