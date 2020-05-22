## 基本顺序

rsync -av /from /to

## somthing/ and something



## --delete



## -P

show process



## -a

all



## -v

visual



## -z

zip??





## To copy files from remote to local, maintaining file properties and sym-links (-a), zipping for faster transfer (-z), verbose (-v).

rsync -avz host:file1 :file1 /dest/
rsync -avz /source host:/dest

Copy files using checksum (-c) rather than time to detect if the file has changed. (Useful for validating backups).

rsync -avc /source/ /dest/

## Copy contents of /src/foo to destination:

This command will create /dest/foo if it does not already exist

rsync -auv /src/foo /dest



## Explicitly copy /src/foo to /dest/foo

rsync -auv /src/foo/ /dest/foo


# rsync

> Transfer files either to or from a remote host (not between two remote hosts).
> Can transfer single files, or multiple files matching a pattern.

- Transfer file from local to remote host:

`rsync {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- Transfer file from remote host to local:

`rsync {{remote_host_name}}:{{remote_file_location}} {{local_file_location}}`

- Transfer file in archive (to preserve attributes) and compressed (zipped) mode:

`rsync -az {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- Transfer a directory and all its children from a remote to local:

`rsync -r {{remote_host_name}}:{{remote_folder_location}} {{local_folder_location}}`

- Transfer only updated files from remote host:

`rsync -ru {{remote_host_name}}:{{remote_folder_location}} {{local_folder_location}}`

- Transfer file over SSH and show progress:

`rsync -e ssh --progress {{remote_host_name}}:{{remote_file}} {{local_file}}`
