clear && ls

echo "first load, remove before"
apk add coreutils tree ncurses go git

# bash
#alias tls="clear && tree -a -C -I \".venv|.git|node_modules|target\" -L 3"
#alias tlss="clear && tree -a -C -I \".venv|.git|node_modules!target\""
alias tlsss="clear && tree -a -C -I \".venv|.git|node_modules|target|.env|.gitignore\""
alias tlss="clear && tree -a -C -I \".venv|.git|node_modules|target\""
alias tls="tlss -L 3"

alias clss="clear && ls -a -I '__init__.py'"
alias cls="clear && ls -I '__init__.py'"

alias update="apk update && apk upgrade"

alias vi="vim"
alias kill_proc="kill -9 PID"

alias tool="vim ~/.profile"
alias viconf="vim ~/.vim/"
alias vicoc="vim ~/.vim/coc-settings.json"

alias apkls="apk list"
alias apku="apk del"
alias search="apk search"
alias ins="apk add"

alias re=". ~/.profile"
alias del="rm -rf"

alias xx="exit"

alias "........"="cd ../../../../../../.."
alias "......."="cd ../../../../../.."
alias "......"="cd ../../../../.."
alias "....."="cd ../../../.."
alias "...."="cd ../../.."
alias "..."="cd ../.."
alias ".."="cd .."


# golang
alias gols="clear && go run ."
alias gobld="go build main.go"


# java
alias mkjavmod="python ~/.toolchain/py_java.py"
alias javrun="./mvnw spring-boot:run"


# git
alias pregh="git init && git remote add origin"
alias ingh="git add . && git commit -m"
alias togh="git push -u origin"
alias topr="git push origin"
alias ghnew="git checkout -b"

alias ghmove="git switch"
alias ghls="git branch -a"
alias ghmoveroot="git switch master"

# python
alias testpy="pytest -v --color=yes --code-highlight=yes"
alias active="source ./.venv/bin/activate"
alias frun="uvicorn main:app --reload"
alias _pyapi="python3 -m http.server"
alias pinr="pip install -r req.txt"
alias pyls="cls && python main.py"
alias pycheck="pyrefly check"
alias nenv="python3.11 -m venv .venv"
alias pyrun="python main.py"
alias pyapp="python app.py"
alias pun="pip uninstall"
alias pin="pip install"
alias pls="pip list"

# django
alias dj_new="django-admin startproject"


# javascript
#alias astro="npm create astro@latest"
alias jsrun="npm run dev -- --host 0.0.0.0"
alias jsnew="npm create vite@latest"
alias npi="npm install"

# rust
alias cpatchelf="patchelf --set-rpath ./"
alias rsbldrel="cargo build --release"
alias tolib="cls && maturin develop"
alias rstest="cargo test"
alias rsbld="cargo build"
alias rschk="cargo check"
alias rsrun="cargo run"
alias rsnew="cargo new"

# turso
alias "turso-login"="turso auth login"
alias "turso-new"="turso db create"
alias "turso-ls"="turso db list"
alias "turso-db-url"="turso db show"


