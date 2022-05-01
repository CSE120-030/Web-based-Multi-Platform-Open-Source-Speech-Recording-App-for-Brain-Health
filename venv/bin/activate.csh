# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.
# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

<<<<<<< HEAD
alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; test "\!:*" != "nondestructive" && unalias deactivate'
=======
alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'
>>>>>>> 2646ade36c08f98d34a981595dd7bc3ec740dfcb

# Unset irrelevant variables.
deactivate nondestructive

<<<<<<< HEAD
setenv VIRTUAL_ENV "/Users/joceychan/Web-based-Multi-Platform-Open-Source-Speech-Recording-App-for-Brain-Health/venv"
=======
setenv VIRTUAL_ENV "/Users/benita/Documents/GitHub/Web-based-Multi-Platform-Open-Source-Speech-Recording-App-for-Brain-Health/venv"
>>>>>>> 2646ade36c08f98d34a981595dd7bc3ec740dfcb

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
<<<<<<< HEAD
    if ("venv" != "") then
        set env_name = "venv"
    else
        if (`basename "VIRTUAL_ENV"` == "__") then
            # special case for Aspen magic directories
            # see https://aspen.io/
            set env_name = `basename \`dirname "$VIRTUAL_ENV"\``
        else
            set env_name = `basename "$VIRTUAL_ENV"`
        endif
    endif
    set prompt = "[$env_name] $prompt"
    unset env_name
=======
    set prompt = "(venv) $prompt"
    setenv VIRTUAL_ENV_PROMPT "(venv) "
>>>>>>> 2646ade36c08f98d34a981595dd7bc3ec740dfcb
endif

alias pydoc python -m pydoc

rehash
