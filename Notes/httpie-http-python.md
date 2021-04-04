# create repo via github api
http -a {name[:pass]} https://api.github.com/user/repos name=githubApiTest

#  basic schema
[METHOD] URL [REQUEST_ITEM [REQUEST_ITEM ...]]
':' HTTP headers:

          Referer:http://httpie.org  Cookie:foo=bar  User-Agent:bacon/1.0
'==' URL parameters to be appended to the request URI:

          search=='httpie str'

'=' Data fields to be serialized into a JSON object (with --json, -j)
          or form data (with --form, -f):
          josn:json

':=' Non-string JSON data fields (only with --json, -j):

          awesome:=true  amount:=42  colors:='["red", "green", "blue"]'

'@' Form file fields (only with --form, -f):

          cs@~/Documents/CV.pdf


# download
  --output FILE, -o FILE
      Save output to FILE instead of stdout. If --download is also set, then only
      the response body is saved to FILE. Other parts of the HTTP exchange are
      printed to stderr.

  --download, -d
      Do not print the response body to stdout. Rather, download it and store it
      in a file. The filename is guessed unless specified with --output
      [filename]. This action is similar to the default behaviour of wget.

#


usage: http [--json] [--form] [--pretty {all,colors,format,none}]
            [--style STYLE] [--print WHAT] [--headers] [--body] [--verbose]
            [--all] [--history-print WHAT] [--stream] [--output FILE]
            [--download] [--continue]
            [--session SESSION_NAME_OR_PATH | --session-read-only SESSION_NAME_OR_PATH]
            [--auth USER[:PASS]] [--auth-type {basic,digest}]
            [--proxy PROTOCOL:PROXY_URL] [--follow]
            [--max-redirects MAX_REDIRECTS] [--timeout SECONDS]
            [--check-status] [--verify VERIFY]
            [--ssl {ssl2.3,tls1,tls1.1,tls1.2}] [--cert CERT]
            [--cert-key CERT_KEY] [--ignore-stdin] [--help] [--version]
            [--traceback] [--default-scheme DEFAULT_SCHEME] [--debug]
            [METHOD] URL [REQUEST_ITEM [REQUEST_ITEM ...]]

HTTPie - a CLI, cURL-like tool for humans. <http://httpie.org>

Positional Arguments:

  These arguments come after any flags and in the order they are listed here.
  Only URL is required.


  METHOD
      The HTTP method to be used for the request (GET, POST, PUT, DELETE, ...).

      This argument can be omitted in which case HTTPie will use POST if there
      is some data to be sent, otherwise GET:

          $ http example.org               # => GET
          $ http example.org hello=world   # => POST

  URL
      The scheme defaults to 'http://' if the URL does not include one.
      (You can override this with: --default-scheme=https)

      You can also use a shorthand for localhost

          $ http :3000                    # => http://localhost:3000
          $ http :/foo                    # => http://localhost/foo

  REQUEST_ITEM
      Optional key-value pairs to be included in the request. The separator used
      determines the type:

      ':' HTTP headers:

          Referer:http://httpie.org  Cookie:foo=bar  User-Agent:bacon/1.0

      '==' URL parameters to be appended to the request URI:

          search==httpie

      '=' Data fields to be serialized into a JSON object (with --json, -j)
          or form data (with --form, -f):

          name=HTTPie  language=Python  description='CLI HTTP client'

      ':=' Non-string JSON data fields (only with --json, -j):

          awesome:=true  amount:=42  colors:='["red", "green", "blue"]'

      '@' Form file fields (only with --form, -f):

          cs@~/Documents/CV.pdf

      '=@' A data field like '=', but takes a file path and embeds its content:

           essay=@Documents/essay.txt

      ':=@' A raw JSON field like ':=', but takes a file path and embeds its content:

          package:=@./package.json

      You can use a backslash to escape a colliding separator in the field name:

          field-name-with\:colon=value


Predefined Content Types:
  --json, -j
      (default) Data items from the command line are serialized as a JSON object.
      The Content-Type and Accept headers are set to application/json
      (if not specified).

  --form, -f
      Data items from the command line are serialized as form fields.

      The Content-Type is set to application/x-www-form-urlencoded (if not
      specified). The presence of any file fields results in a
      multipart/form-data request.


Output Processing:
  --pretty {all,colors,format,none}
      Controls output processing. The value can be "none" to not prettify
      the output (default for redirected output), "all" to apply both colors
      and formatting (default for terminal output), "colors", or "format".

  --style STYLE, -s STYLE
      Output coloring style (default is "fruity"). One of:

          abap, algol, algol_nu, arduino, auto, autumn, borland, bw,
          colorful, default, emacs, friendly, fruity, igor, lovelace,
          manni, monokai, murphy, native, paraiso-dark, paraiso-light,
          pastie, perldoc, rainbow_dash, rrt, solarized, tango, trac,
          vim, vs, xcode

      The "auto" style follows your terminal's ANSI color styles.

      For non-auto styles to work properly, please make sure that the
      $TERM environment variable is set to "xterm-256color" or similar
      (e.g., via `export TERM=xterm-256color' in your ~/.bashrc).


Output Options:
  --print WHAT, -p WHAT
      String specifying what the output should contain:

          'H' request headers
          'B' request body
          'h' response headers
          'b' response body

      The default behaviour is 'hb' (i.e., the response headers and body
      is printed), if standard output is not redirected. If the output is piped
      to another program or to a file, then only the response body is printed
      by default.

  --headers, -h
      Print only the response headers. Shortcut for --print=h.

  --body, -b
      Print only the response body. Shortcut for --print=b.

  --verbose, -v
      Verbose output. Print the whole request as well as the response. Also print
      any intermediary requests/responses (such as redirects).
      It's a shortcut for: --all --print=HbBh

  --all
      By default, only the final request/response is shown. Use this flag to show
      any intermediary requests/responses as well. Intermediary requests include
      followed redirects (with --follow), the first unauthorized request when
      Digest auth is used (--auth=digest), etc.

  --history-print WHAT, -P WHAT
      The same as --print, -p but applies only to intermediary requests/responses
      (such as redirects) when their inclusion is enabled with --all. If this
      options is not specified, then they are formatted the same way as the final
      response.

  --stream, -S
      Always stream the output by line, i.e., behave like `tail -f'.

      Without --stream and with --pretty (either set or implied),
      HTTPie fetches the whole response before it outputs the processed data.

      Set this option when you want to continuously display a prettified
      long-lived response, such as one from the Twitter streaming API.

      It is useful also without --pretty: It ensures that the output is flushed
      more often and in smaller chunks.

  --output FILE, -o FILE
      Save output to FILE instead of stdout. If --download is also set, then only
      the response body is saved to FILE. Other parts of the HTTP exchange are
      printed to stderr.

  --download, -d
      Do not print the response body to stdout. Rather, download it and store it
      in a file. The filename is guessed unless specified with --output
      [filename]. This action is similar to the default behaviour of wget.

  --continue, -c
      Resume an interrupted download. Note that the --output option needs to be
      specified as well.


Sessions:
  --session SESSION_NAME_OR_PATH
      Create, or reuse and update a session. Within a session, custom headers,
      auth credential, as well as any cookies sent by the server persist between
      requests.

      Session files are stored in:

          C:\Users\14049\AppData\Roaming\\httpie\sessions/<HOST>/<SESSION_NAME>.json.

  --session-read-only SESSION_NAME_OR_PATH
      Create or read a session without updating it form the request/response
      exchange.


Authentication:
  --auth USER[:PASS], -a USER[:PASS]
      If only the username is provided (-a username), HTTPie will prompt
      for the password.

  --auth-type {basic,digest}, -A {basic,digest}
      The authentication mechanism to be used. Defaults to "basic".

      "basic": Basic HTTP auth
      "digest": Digest HTTP auth


Network:
  --proxy PROTOCOL:PROXY_URL
      String mapping protocol to the URL of the proxy
      (e.g. http:http://foo.bar:3128). You can specify multiple proxies with
      different protocols.

  --follow, -F
      Follow 30x Location redirects.

  --max-redirects MAX_REDIRECTS
      By default, requests have a limit of 30 redirects (works with --follow).

  --timeout SECONDS
      The connection timeout of the request in seconds. The default value is
      30 seconds.

  --check-status
      By default, HTTPie exits with 0 when no network or other fatal errors
      occur. This flag instructs HTTPie to also check the HTTP status code and
      exit with an error if the status indicates one.

      When the server replies with a 4xx (Client Error) or 5xx (Server Error)
      status code, HTTPie exits with 4 or 5 respectively. If the response is a
      3xx (Redirect) and --follow hasn't been set, then the exit status is 3.
      Also an error message is written to stderr if stdout is redirected.


SSL:
  --verify VERIFY
      Set to "no" (or "false") to skip checking the host's SSL certificate.
      Defaults to "yes" ("true"). You can also pass the path to a CA_BUNDLE file
      for private certs. (Or you can set the REQUESTS_CA_BUNDLE environment
      variable instead.)

  --ssl {ssl2.3,tls1,tls1.1,tls1.2}
      The desired protocol version to use. This will default to
      SSL v2.3 which will negotiate the highest protocol that both
      the server and your installation of OpenSSL support. Available protocols
      may vary depending on OpenSSL installation (only the supported ones
      are shown here).

  --cert CERT
      You can specify a local cert to use as client side SSL certificate.
      This file may either contain both private key and certificate or you may
      specify --cert-key separately.

  --cert-key CERT_KEY
      The private key to use with SSL. Only needed if --cert is given and the
      certificate file does not contain the private key.


Troubleshooting:
  --ignore-stdin, -I
      Do not attempt to read stdin.

  --help
      Show this help message and exit.

  --version
      Show version and exit.

  --traceback
      Prints the exception traceback should one occur.

  --default-scheme DEFAULT_SCHEME
      The default scheme to use if not specified in the URL.

  --debug
      Prints the exception traceback should one occur, as well as other
      information useful for debugging HTTPie itself and for reporting bugs.


For every --OPTION there is also a --no-OPTION that reverts OPTION
to its default value.

Suggestions and bug reports are greatly appreciated:

    https://github.com/jakubroztocil/httpie/issues