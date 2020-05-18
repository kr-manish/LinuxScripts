set nocompatible

" enable filetype detection
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'vim-syntastic/syntastic'
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
" Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'kien/ctrlp.vim'
Plugin 'tpope/vim-fugitive'
" Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
" Plugin 'Valloric/YouCompleteMe'
Plugin 'thiagoalessio/rainbow_levels.vim'

" All of your Plugins must be added before the following line
call vundle#end()            " required filetype plugin indent on    " required

"==========GENERAL CONFIG============

syntax enable
set background=dark
let g:solarized_termcolors=256
colorscheme solarized

let python_highlight_all=1
syntax on


" Spaces & Tabs
au BufNewFile,BufRead *.*
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

" UI CONFIG
" show line numbers
" set number
set number relativenumber

" show command in bottom bar
set showcmd

" highlight current line
set cursorline

" load filetype-specific indent files
filetype indent on

" highlight matching [{()}]
set showmatch

" SEARCHING
" search as characters are entered
set incsearch

" highlight matches
set hlsearch

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

" Turn Off Swap Files
set noswapfile
set nobackup
set nowb

" Split Layouts
set splitbelow
set splitright

" Stop using up and down arrows
noremap <Up> <NOP> 
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>
inoremap <UP> <NOP>
inoremap <Down> <NOP>
inoremap <Left> <NOP>
inoremap <Right> <NOP>

let python_highlight_all=1
syntax on

" YCM related
let g:ycm_autoclose_preview_window_after_insertion = 1

" persistent undo
set undofile " Maintain undo history between sessions
set undodir=~/.vim/undodir

" automatically turning rainbowlevels on
au FileType python,yaml :RainbowLevelsOn

" remap ESC
inoremap jj <ESC>

" ====================== statusline ===============================

function! GitBranch()
    return system("git rev-parse --abbrev-ref HEAD 2>/dev/null | tr -d '\n'")
endfunction

function! GetGitBranch()
    let l:branchname=GitBranch()
    return strlen(l:branchname) > 0?'  '.l:branchname.' ':'     '
endfunction

set laststatus=2                        " To show statusline all the time
set statusline=                         " To set
set statusline+=%#Pmenu#                " Background highlights (:so /usr/share/vim/vim82/syntax/hitest.vim )
set statusline+=%{&modified?'[+]':''}    " Whether modified or not
set statusline+=%{GetGitBranch()}       " Git branch
set statusline+=%#PmenuSel#             " Background
set statusline+=\ %f                    " file name
set statusline+=%=                      " shift to righside
set statusline+=%l                      " current line
set statusline+=/                       " Separator
set statusline+=%L\ |                      " Total lines
set statusline+=%#Pmenu#                " Background highlights (:so /usr/share/vim/vim82/syntax/hitest.vim )
set statusline+=\ %p%%                   " Percentage
