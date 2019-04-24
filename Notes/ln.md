#创造软连接
ln -s /path/to/the/target/file/ofdirectory name_of_symlink

#删除软连接
unlink name_of_symlink
//rm -rf name_of_symlink

# To create a symlink:
ln -s path/to/the/target/directory name-of-symlink

# Symlink, while overwriting existing destination files
ln -sf /some/dir/exec /usr/bin/exec
