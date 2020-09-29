alias python=python3
alias pip=pip3

export PATH="/usr/local/opt/ruby/bin:$PATH"

alias te="open -a 'TextEdit'"
alias ecc="g++ -std=c++14 -Wall"

cj() {
  python "$1.py" < "test_$1"
}

export PATH=$PATH:~/.local/bin
