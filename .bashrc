clear && ls

# bash
#alias tls="clear && tree -a -C -I \".venv|.git|node_modules|target\" -L 3"
#alias tlss="clear && tree -a -C -I \".venv|.git|node_modules!target\""
alias tlsss="clear && tree -a -C -I \".venv|.git|node_modules|target|.env|.gitignore\""
alias tlss="clear && tree -a -C -I \".venv|.git|node_modules|target\""
alias tls="tlss -L 3"

alias clss="clear && ls -a --ignore='__init__.py'"
alias cls="clear && ls --ignore='__init__.py'"

alias update="pkg update && pkg upgrade"

alias kill_proc="kill -9 PID"

alias tool="vim ~/.bashrc"
alias viconf="vim ~/.vim/"
alias vicoc="vim ~/.vim/coc-settings.json"

alias pkgls="pkg list-installed"
alias pkgu="pkg uninstall"
alias search="pkg search"
alias ins="pkg install"

alias re="exec bash"
alias del="rm -rf"

alias xx="exit"

alias "........"="cd ../../../../../../.."
alias "......."="cd ../../../../../.."
alias "......"="cd ../../../../.."
alias "....."="cd ../../../.."
alias "...."="cd ../../.."
alias "..."="cd ../.."
alias ".."="cd .."


# alpine
alias alpine="proot-distro login alpine"
alias alpine_reset="proot-distro remove alpine"
alias alpine_init="proot-distro install alpine"


# golang
alias gols="clear && go run ."
alias gobld="go build main.go"


# java
alias mkjavmod="python ~/.toolchain/py_java.py"
alias javrun="./mvnw spring-boot:run"


# toolchain
# alias ="python ~/.toolchain/"
alias tc="cd ~/.toolchain"

alias pyinibackend="python ~/.toolchain/py_backend.py"
alias tslitcomp="python ~/.toolchain/ts_pkg_lit_component.py"
alias littsini="python ~/.toolchain/lit_ts_init.py"

alias mkpyrouter="python ~/.toolchain/py_pkg_router.py"
alias mkpymod="python ~/.toolchain/py_module_init.py"

# toolchain.scripts
# alias ="python ~/.toolchain/scripts/"
alias countlines="python ~/.toolchain/scripts/countlines.py"
alias pytermux="python ~/.toolchain/scripts/pytermux.py"
alias delpy="python ~/.toolchain/scripts/delpy.py"


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
alias nenv="python3.13 -m venv .venv"
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

# postgresql
alias pg__ini="python ~/.toolchain/scripts/pg_init.py"
alias pg__job="pg_ctl status -D ~/._labs"
alias pg__stop="pg_ctl stop -D ~/._labs"
alias pg__clean="delpy ~/._labs"


export ANDROID_API_LEVEL=$(getprop ro.build.version.sdk)
export PATH=$HOME/.cargo/bin:$PATH

# mb
export RUST_ANALYZER_MEMORY_USAGE=4096
export RUST_ANALYZER_WORKER_COUNT=8
export CARGO_BUILD_JOBS=8
export RUST_ANALYZER_CHECK_WORKSPACE="false"
export RUSTC_WRAPPER=sccache

