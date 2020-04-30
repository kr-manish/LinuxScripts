# For setting terminal title, comment out following line in bashrc
# PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
# and add following function
function set-title() {
	echo -ne "\033]0;$1\007"
}
