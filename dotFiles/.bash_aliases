alias get='sudo pacman -S'
alias remove='sudo pacman -R'
alias cls='clear'
alias yeet='clear'
alias pacsearch='sudo pacman -Ss'
alias update='sudo pacman -Syu'
alias banner='neofetch'
alias oc='gwe'
alias bim='vim'

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
