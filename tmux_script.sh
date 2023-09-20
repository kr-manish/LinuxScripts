#!/bin/sh

# set session name
SESSION="ARAGORN"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

if [ "$SESSIONEXISTS" = "" ]
then
	tmux new-session -d -s $SESSION

	# name of the first window
	# tmux rename-window -t $SESSION:0 'work'
	# tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m

	tmux new-window -t $SESSION:1 -n 'vpn'
	# tmux send-keys -t 'Writing' "nvim" C-m
	
	tmux new-window -t $SESSION:2 -n 'discovery'
	tmux split-window -t 'GraphQL' -h

	tmux new-window -t $SESSION:3 -n 'exploit'
	tmux split-window -t 'apisec' -h

fi
tmux attach-session -t $SESSION:1
