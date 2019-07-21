transcrypt -b -n py2js.py

2.1.1. Installation troubleshooting checklist
Transcrypt was installed using pip, but import transcrypt fails. Transcrypt isn’t a library but a compiler. Install and run it as described in this chapter.
Transcrypt reports an error containing the word ‘java’. Transcrypt produces both prettyfied and minified JavaScript output. For the minification it makes use of the Google Closure Compiler, which is included in the distribution and requires Java to run. You can check proper installation of Java by typing the word java on the command line. This should give you a list of options: Usage: java [-options] class []args…] and so on. If you can’t or won’t install Java, you can run Transcrypt without minification by using the -n command line switch.
The static checker doesn’t find all errors it could. The static checks, performed by the PyFlakes package that’s part of the distribution, are of a ‘light’ variety. Style checks and false positives are avoided. The accent is on finding undefined identifiers and unused variables.
