> https://www.reddit.com/r/Anki/comments/abvcnr/change_mathjax_syntax_in_anki_21/ed3ji2v/

You can do that by changing the MathJax congifuration file in /usr/share/anki/web/mathjax/conf.js.

To use \( and \[ for equations, change the lines:

inlineMath: [['$','$'], ['\\(','\\)'] ],
displayMath: [ ['$$','$$'], ['\\[','\\]'] ],
Note this won't work on AnkiDroid or AnkiWeb.

I would also recommend to set processEnvironments: true in the config file. That way, it is possible to use align* environments.

anki drop setting
> https://niklaskorz.de/2017/06/studying-mathematics-with-anki-and-mathjax.html