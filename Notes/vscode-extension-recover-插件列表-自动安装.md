So as treehead's edit or MarkP's answer showed you can now list all extensions installed so the way to install that list of extensions would be to:

code --list-extensions >> vs_code_extensions_list.txt
Transfer the newly created file to the machine that you want to install those extensions to. On that machine you would:

cat vs_code_extensions_list.txt | xargs -n 1 code --install-extension
Which will then go through each extension in that file and install the extension.

If you want a clean install (AKA remove all existing extensions on that machine) you could run this before you install the new extensions (otherwise you will remove those new extensions too). BE CAREFUL as this will remove all extensions in VS Code:

code --list-extensions | xargs -n 1 code --uninstall-extension