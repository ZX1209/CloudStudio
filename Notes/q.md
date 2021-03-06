ZSH(1)                                General Commands Manual                               ZSH(1)

NNAAMMEE
       zsh - the Z shell

OOVVEERRVVIIEEWW
       Because  zsh  contains  many  features, the zsh manual has been split into a number of sec‐
       tions:

       _z_s_h          Zsh overview (this section)
       _z_s_h_r_o_a_d_m_a_p   Informal introduction to the manual
       _z_s_h_m_i_s_c      Anything not fitting into the other sections
       _z_s_h_e_x_p_n      Zsh command and parameter expansion
       _z_s_h_p_a_r_a_m     Zsh parameters
       _z_s_h_o_p_t_i_o_n_s   Zsh options
       _z_s_h_b_u_i_l_t_i_n_s  Zsh built-in functions
       _z_s_h_z_l_e       Zsh command line editing
       _z_s_h_c_o_m_p_w_i_d   Zsh completion widgets
       _z_s_h_c_o_m_p_s_y_s   Zsh completion system
       _z_s_h_c_o_m_p_c_t_l   Zsh completion control
       _z_s_h_m_o_d_u_l_e_s   Zsh loadable modules
       _z_s_h_c_a_l_s_y_s    Zsh built-in calendar functions
       _z_s_h_t_c_p_s_y_s    Zsh built-in TCP functions
       _z_s_h_z_f_t_p_s_y_s   Zsh built-in FTP client
       _z_s_h_c_o_n_t_r_i_b   Additional zsh functions and utilities
       _z_s_h_a_l_l       Meta-man page containing all of the above

DDEESSCCRRIIPPTTIIOONN
       Zsh is a UNIX command interpreter (shell) usable as an interactive login  shell  and  as  a
       shell script command processor.  Of the standard shells, zsh most closely resembles kksshh but
       includes many enhancements.  Zsh has command line  editing,  builtin  spelling  correction,
       programmable  command  completion, shell functions (with autoloading), a history mechanism,
       and a host of other features.

AAUUTTHHOORR
       Zsh was originally written by Paul Falstad <<ppff@@zzsshh..oorrgg>>.  Zsh is now maintained by the mem‐
       bers  of  the zsh-workers mailing list <<zzsshh--wwoorrkkeerrss@@zzsshh..oorrgg>>.  The development is currently
       coordinated by Peter Stephenson <<ppwwss@@zzsshh..oorrgg>>.  The coordinator can be contacted at  <<ccoooorr‐‐
       ddiinnaattoorr@@zzsshh..oorrgg>>, but matters relating to the code should generally go to the mailing list.

AAVVAAIILLAABBIILLIITTYY
       Zsh  is available from the following anonymous FTP sites.  These mirror sites are kept fre‐
       quently up to date.  The sites marked with _(_H_) may be mirroring ffttpp..ccss..eellttee..hhuu  instead  of
       the primary site.

       Primary site
              ffttpp::////ffttpp..zzsshh..oorrgg//ppuubb//
              hhttttpp::////wwwwww..zzsshh..oorrgg//ppuubb//

       Australia
              ffttpp::////ffttpp..zzsshh..oorrgg//ppuubb//
              hhttttpp::////wwwwww..zzsshh..oorrgg//ppuubb//
              hhttttpp::////mmiirrrroorr..ddeejjaannsseeoo..ccoomm..aauu//ppuubb//zzsshh//

       Hungary
              ffttpp::////ffttpp..ccss..eellttee..hhuu//ppuubb//zzsshh//
              hhttttpp::////wwwwww..ccss..eellttee..hhuu//ppuubb//zzsshh//

       The  up-to-date  source  code  is  available  via Git from Sourceforge.  See hhttttpp::////ssoouurrccee‐‐
       ffoorrggee..nneett//pprroojjeeccttss//zzsshh// for details.  A summary of instructions  for  the  archive  can  be
       found at hhttttpp::////zzsshh..ssoouurrcceeffoorrggee..nneett//.

MMAAIILLIINNGG LLIISSTTSS
       Zsh has 3 mailing lists:

       <<zzsshh--aannnnoouunnccee@@zzsshh..oorrgg>>
              Announcements  about releases, major changes in the shell and the monthly posting of
              the Zsh FAQ.  (moderated)

       <<zzsshh--uusseerrss@@zzsshh..oorrgg>>
              User discussions.

       <<zzsshh--wwoorrkkeerrss@@zzsshh..oorrgg>>
              Hacking, development, bug reports and patches.

       To subscribe or unsubscribe, send mail to the associated  administrative  address  for  the
       mailing list.

       <<zzsshh--aannnnoouunnccee--ssuubbssccrriibbee@@zzsshh..oorrgg>>
       <<zzsshh--uusseerrss--ssuubbssccrriibbee@@zzsshh..oorrgg>>
       <<zzsshh--wwoorrkkeerrss--ssuubbssccrriibbee@@zzsshh..oorrgg>>
       <<zzsshh--aannnnoouunnccee--uunnssuubbssccrriibbee@@zzsshh..oorrgg>>
       <<zzsshh--uusseerrss--uunnssuubbssccrriibbee@@zzsshh..oorrgg>>
       <<zzsshh--wwoorrkkeerrss--uunnssuubbssccrriibbee@@zzsshh..oorrgg>>

       YOU  ONLY  NEED  TO  JOIN  ONE OF THE MAILING LISTS AS THEY ARE NESTED.  All submissions to
       zzsshh--aannnnoouunnccee are automatically forwarded to zzsshh--uusseerrss.  All submissions  to  zzsshh--uusseerrss  are
       automatically forwarded to zzsshh--wwoorrkkeerrss.

       If  you  have  problems subscribing/unsubscribing to any of the mailing lists, send mail to
       <<lliissttmmaasstteerr@@zzsshh..oorrgg>>.    The   mailing   lists   are   maintained   by   Karsten   Thygesen
       <<kkaarrtthhyy@@kkoomm..aauucc..ddkk>>.

       The  mailing  lists  are  archived;  the  archives  can  be accessed via the administrative
       addresses listed above.  There is also  a  hypertext  archive,  maintained  by  Geoff  Wing
       <<ggccww@@zzsshh..oorrgg>>, available at hhttttpp::////wwwwww..zzsshh..oorrgg//mmllaa//.

TTHHEE ZZSSHH FFAAQQ
       Zsh  has  a  list  of  Frequently  Asked  Questions  (FAQ),  maintained by Peter Stephenson
       <<ppwwss@@zzsshh..oorrgg>>.   It  is  regularly  posted  to  the  newsgroup  ccoommpp..uunniixx..sshheellll   and   the
       zzsshh--aannnnoouunnccee mailing list.  The latest version can be found at any of the Zsh FTP sites, or
       at hhttttpp::////wwwwww..zzsshh..oorrgg//FFAAQQ//.  The  contact  address  for  FAQ-related  matters  is  <<ffaaqqmmaass‐‐
       tteerr@@zzsshh..oorrgg>>.

TTHHEE ZZSSHH WWEEBB PPAAGGEE
       Zsh  has a web page which is located at hhttttpp::////wwwwww..zzsshh..oorrgg//.  This is maintained by Karsten
       Thygesen <<kkaarrtthhyy@@zzsshh..oorrgg>>, of SunSITE Denmark.  The contact address for web-related matters
       is <<wweebbmmaasstteerr@@zzsshh..oorrgg>>.

TTHHEE ZZSSHH UUSSEERRGGUUIIDDEE
       A  userguide  is  currently  in preparation.  It is intended to complement the manual, with
       explanations and hints on issues where the manual  can  be  cabbalistic,  hierographic,  or
       downright  mystifying  (for  example,  the  word `hierographic' does not exist).  It can be
       viewed in its current state at hhttttpp::////zzsshh..ssoouurrcceeffoorrggee..nneett//GGuuiiddee//.  At the time of  writing,
       chapters  dealing  with startup files and their contents and the new completion system were
       essentially complete.

TTHHEE ZZSSHH WWIIKKII
       A `wiki' website for zsh has been created at hhttttpp::////wwwwww..zzsshhwwiikkii..oorrgg//.  This is a site which
       can be added to and modified directly by users without any special permission.  You can add
       your own zsh tips and configurations.

IINNVVOOCCAATTIIOONN
       The following flags are interpreted by the shell when invoked to determine where the  shell
       will read commands from:

       --cc     Take the first argument as a command to execute, rather than reading commands from a
              script or standard input.  If any further arguments are  given,  the  first  one  is
              assigned to $$00, rather than being used as a positional parameter.

       --ii     Force shell to be interactive.  It is still possible to specify a script to execute.

       --ss     Force shell to read commands from the standard input.  If the --ss flag is not present
              and an argument is given, the first argument is taken to be the pathname of a script
              to execute.

       If there are any remaining arguments after option processing, and neither of the options --cc
       or --ss was supplied, the first argument is taken as the file name  of  a  script  containing
       shell  commands  to  be executed.  If the option PPAATTHH__SSCCRRIIPPTT is set, and the file name does
       not contain a directory path (i.e. there is no `//' in the name), first the  current  direc‐
       tory  and then the command path given by the variable PPAATTHH are searched for the script.  If
       the option is not set or the file name contains a `//' it is used directly.

       After the first one or two arguments have been appropriated as described above, the remain‐
       ing arguments are assigned to the positional parameters.

       For further options, which are common to invocation and the sseett builtin, see _z_s_h_o_p_t_i_o_n_s(1).

       Options may be specified by name using the --oo option.  --oo acts like a single-letter option,
       but takes a following string as the option name.  For example,

              zzsshh --xx --oo sshhwwoorrddsspplliitt ssccrr

       runs the script ssccrr, setting the XXTTRRAACCEE option by the corresponding  letter  `--xx'  and  the
       SSHH__WWOORRDD__SSPPLLIITT option by name.  Options may be turned _o_f_f by name by using ++oo instead of --oo.
       --oo can be stacked up with preceding single-letter options, so for example `--xxoo sshhwwoorrddsspplliitt'
       or `--xxoosshhwwoorrddsspplliitt' is equivalent to `--xx --oo sshhwwoorrddsspplliitt'.

       Options may also be specified by name in GNU long option style, `----_o_p_t_i_o_n_-_n_a_m_e'.  When this
       is done, `--' characters in the option name are permitted: they are translated into `__', and
       thus  ignored.   So,  for example, `zzsshh ----sshh--wwoorrdd--sspplliitt' invokes zsh with the SSHH__WWOORRDD__SSPPLLIITT
       option turned on.  Like other option syntaxes, options can be turned off by  replacing  the
       initial  `--'  with  a  `++';  thus  `++--sshh--wwoorrdd--sspplliitt' is equivalent to `----nnoo--sshh--wwoorrdd--sspplliitt'.
       Unlike other option syntaxes, GNU-style long options  cannot  be  stacked  with  any  other
       options,  so  for  example `--xx--sshhwwoorrddsspplliitt' is an error, rather than being treated like `--xx
       ----sshhwwoorrddsspplliitt'.

       The special GNU-style option `----vveerrssiioonn' is  handled;  it  sends  to  standard  output  the
       shell's  version  information, then exits successfully.  `----hheellpp' is also handled; it sends
       to standard output a list of options that can be used when invoking the shell,  then  exits
       successfully.

       Option  processing may be finished, allowing following arguments that start with `--' or `++'
       to be treated as normal arguments, in two ways.  Firstly, a lone `--' (or `++') as  an  argu‐
       ment  by  itself  ends option processing.  Secondly, a special option `----' (or `++--'), which
       may be specified on its own (which is the standard POSIX usage) or may be stacked with pre‐
       ceding  options  (so  `--xx--'  is  equivalent  to  `--xx ----').  Options are not permitted to be
       stacked after `----' (so `--xx--ff' is an error), but note the GNU-style  option  form  discussed
       above, where `----sshhwwoorrddsspplliitt' is permitted and does not end option processing.

       Except  when  the sshh/kksshh emulation single-letter options are in effect, the option `--bb' (or
       `++bb') ends option processing.  `--bb' is like `----', except that further single-letter options
       can be stacked after the `--bb' and will take effect as normal.

CCOOMMPPAATTIIBBIILLIITTYY
       Zsh  tries  to  emulate  sshh  or kksshh when it is invoked as sshh or kksshh respectively; more pre‐
       cisely, it looks at the first letter of the name by which it  was  invoked,  excluding  any
       initial  `rr'  (assumed  to  stand for `restricted'), and if that is `bb', `ss' or `kk' it will
       emulate sshh or kksshh.  Furthermore, if invoked as ssuu (which happens on  certain  systems  when
       the  shell  is  executed by the ssuu command), the shell will try to find an alternative name
       from the SSHHEELLLL environment variable and perform emulation based on that.

       In sshh and kksshh compatibility modes the following parameters are not special and not initial‐
       ized  by  the shell: AARRGGCC, aarrggvv, ccddppaatthh, ffiiggnnoorree, ffppaatthh, HHIISSTTCCHHAARRSS, mmaaiillppaatthh, MMAANNPPAATTHH, mmaann‐‐
       ppaatthh, ppaatthh, pprroommpptt, PPRROOMMPPTT, PPRROOMMPPTT22, PPRROOMMPPTT33, PPRROOMMPPTT44, ppssvvaarr, ssttaattuuss, wwaattcchh.

       The usual zsh startup/shutdown scripts are not executed.  Login shells source  //eettcc//pprrooffiillee
       followed  by $$HHOOMMEE//..pprrooffiillee.  If the EENNVV environment variable is set on invocation, $$EENNVV is
       sourced after the profile scripts.  The value of EENNVV is subjected to  parameter  expansion,
       command  substitution,  and  arithmetic  expansion  before being interpreted as a pathname.
       Note that the PPRRIIVVIILLEEGGEEDD option also affects the execution of startup files.

       The following options are set if the  shell  is  invoked  as  sshh  or  kksshh:  NNOO__BBAADD__PPAATTTTEERRNN,
       NNOO__BBAANNGG__HHIISSTT,  NNOO__BBGG__NNIICCEE,  NNOO__EEQQUUAALLSS,  NNOO__FFUUNNCCTTIIOONN__AARRGGZZEERROO,  GGLLOOBB__SSUUBBSSTT, NNOO__GGLLOOBBAALL__EEXXPPOORRTT,
       NNOO__HHUUPP,    IINNTTEERRAACCTTIIVVEE__CCOOMMMMEENNTTSS,    KKSSHH__AARRRRAAYYSS,    NNOO__MMUULLTTIIOOSS,    NNOO__NNOOMMAATTCCHH,    NNOO__NNOOTTIIFFYY,
       PPOOSSIIXX__BBUUIILLTTIINNSS,     NNOO__PPRROOMMPPTT__PPEERRCCEENNTT,    RRMM__SSTTAARR__SSIILLEENNTT,    SSHH__FFIILLEE__EEXXPPAANNSSIIOONN,    SSHH__GGLLOOBB,
       SSHH__OOPPTTIIOONN__LLEETTTTEERRSS, SSHH__WWOORRDD__SSPPLLIITT.  Additionally the BBSSDD__EECCHHOO and IIGGNNOORREE__BBRRAACCEESS options  are
       set  if  zsh  is  invoked  as  sshh.  Also, the KKSSHH__OOPPTTIIOONN__PPRRIINNTT, LLOOCCAALL__OOPPTTIIOONNSS, PPRROOMMPPTT__BBAANNGG,
       PPRROOMMPPTT__SSUUBBSSTT and SSIINNGGLLEE__LLIINNEE__ZZLLEE options are set if zsh is invoked as kksshh.

RREESSTTRRIICCTTEEDD SSHHEELLLL
       When the basename of the command used to invoke zsh starts with the letter `rr' or the  `--rr'
       command  line  option  is  supplied at invocation, the shell becomes restricted.  Emulation
       mode is determined after stripping the letter `rr' from the invocation name.  The  following
       are disabled in restricted mode:

       ·      changing directories with the ccdd builtin

       ·      changing  or  unsetting  the  PPAATTHH, ppaatthh, MMOODDUULLEE__PPAATTHH, mmoodduullee__ppaatthh, SSHHEELLLL, HHIISSTTFFIILLEE,
              HHIISSTTSSIIZZEE, GGIIDD, EEGGIIDD, UUIIDD,  EEUUIIDD,  UUSSEERRNNAAMMEE,  LLDD__LLIIBBRRAARRYY__PPAATTHH,  LLDD__AAOOUUTT__LLIIBBRRAARRYY__PPAATTHH,
              LLDD__PPRREELLOOAADD and  LLDD__AAOOUUTT__PPRREELLOOAADD parameters

       ·      specifying command names containing //

       ·      specifying command pathnames using hhaasshh

       ·      redirecting output to files

       ·      using the eexxeecc builtin command to replace the shell with another command

       ·      using jjoobbss --ZZ to overwrite the shell process' argument and environment space

       ·      using the AARRGGVV00 parameter to override aarrggvv[[00]] for external commands

       ·      turning off restricted mode with sseett ++rr or uunnsseettoopptt RREESSTTRRIICCTTEEDD

       These  restrictions  are  enforced  after  processing the startup files.  The startup files
       should set up PPAATTHH to point to a directory of commands which can be safely invoked  in  the
       restricted  environment.   They  may  also  add  further restrictions by disabling selected
       builtins.

       Restricted mode can also be activated any time by  setting  the  RREESSTTRRIICCTTEEDD  option.   This
       immediately  enables  all  the restrictions described above even if the shell still has not
       processed all startup files.

SSTTAARRTTUUPP//SSHHUUTTDDOOWWNN FFIILLEESS
       Commands are first read from //eettcc//zzsshheennvv; this cannot be overridden.  Subsequent  behaviour
       is  modified by the RRCCSS and GGLLOOBBAALL__RRCCSS options; the former affects all startup files, while
       the second only affects global startup files (those shown here with an path starting with a
       //).   If  one  of  the options is unset at any point, any subsequent startup file(s) of the
       corresponding type will not be read.  It is  also  possible  for  a  file  in  $$ZZDDOOTTDDIIRR  to
       re-enable GGLLOOBBAALL__RRCCSS. Both RRCCSS and GGLLOOBBAALL__RRCCSS are set by default.

       Commands  are then read from $$ZZDDOOTTDDIIRR//..zzsshheennvv.  If the shell is a login shell, commands are
       read from //eettcc//zzpprrooffiillee and then $$ZZDDOOTTDDIIRR//..zzpprrooffiillee.  Then, if the  shell  is  interactive,
       commands  are  read  from  //eettcc//zzsshhrrcc and then $$ZZDDOOTTDDIIRR//..zzsshhrrcc.  Finally, if the shell is a
       login shell, //eettcc//zzllooggiinn and $$ZZDDOOTTDDIIRR//..zzllooggiinn are read.

       When a login shell exits, the files $$ZZDDOOTTDDIIRR//..zzllooggoouutt and then //eettcc//zzllooggoouutt are read.  This
       happens  with  either an explicit exit via the eexxiitt or llooggoouutt commands, or an implicit exit
       by reading end-of-file from the terminal.  However, if the shell terminates due to eexxeecc'ing
       another  process,  the  logout  files are not read.  These are also affected by the RRCCSS and
       GGLLOOBBAALL__RRCCSS options.  Note also that the RRCCSS option affects the  saving  of  history  files,
       i.e. if RRCCSS is unset when the shell exits, no history file will be saved.

       If  ZZDDOOTTDDIIRR  is unset, HHOOMMEE is used instead.  Files listed above as being in //eettcc may be in
       another directory, depending on the installation.

       As //eettcc//zzsshheennvv is run for all instances of zsh, it is important that it be kept as small as
       possible.   In  particular,  it is a good idea to put code that does not need to be run for
       every single shell behind a test of the form `iiff [[[[ --oo rrccss ]]]];; tthheenn ......' so  that  it  will
       not be executed when zsh is invoked with the `--ff' option.

       Any  of  these  files  may  be  pre-compiled  with  the  zzccoommppiillee builtin command (see _z_s_h_‐
       _b_u_i_l_t_i_n_s(1)).  If a compiled file exists (named for the original file plus the ..zzwwcc  exten‐
       sion) and it is newer than the original file, the compiled file will be used instead.

FFIILLEESS
       $$ZZDDOOTTDDIIRR//..zzsshheennvv
       $$ZZDDOOTTDDIIRR//..zzpprrooffiillee
       $$ZZDDOOTTDDIIRR//..zzsshhrrcc
       $$ZZDDOOTTDDIIRR//..zzllooggiinn
       $$ZZDDOOTTDDIIRR//..zzllooggoouutt
       $${{TTMMPPPPRREEFFIIXX}}**   (default is /tmp/zsh*)
       //eettcc//zzsshheennvv
       //eettcc//zzpprrooffiillee
       //eettcc//zzsshhrrcc
       //eettcc//zzllooggiinn
       //eettcc//zzllooggoouutt    (installation-specific - //eettcc is the default)

SSEEEE AALLSSOO
       _s_h(1),  _c_s_h(1),  _t_c_s_h(1),  _r_c(1),  _b_a_s_h(1), _k_s_h(1), _z_s_h_b_u_i_l_t_i_n_s(1), _z_s_h_c_o_m_p_w_i_d(1), _z_s_h_c_o_m_p_‐
       _s_y_s(1), _z_s_h_c_o_m_p_c_t_l(1), _z_s_h_e_x_p_n(1), _z_s_h_m_i_s_c(1), _z_s_h_m_o_d_u_l_e_s(1),  _z_s_h_o_p_t_i_o_n_s(1),  _z_s_h_p_a_r_a_m(1),
       _z_s_h_z_l_e(1)

       IIEEEEEE  SSttaannddaarrdd  ffoorr  iinnffoorrmmaattiioonn TTeecchhnnoollooggyy -- PPoorrttaabbllee OOppeerraattiinngg SSyysstteemm IInntteerrffaaccee ((PPOOSSIIXX)) --
       PPaarrtt 22:: SShheellll aanndd UUttiilliittiieess, IEEE Inc, 1993, ISBN 1-55937-255-9.

zsh 5.1.1                               September 11, 2015                                  ZSH(1)
