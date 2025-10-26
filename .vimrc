filetype plugin indent on
syntax on
set t_Co=256 number relativenumber backspace=indent,eol,start noswapfile expandtab shiftwidth=2 softtabstop=2 tabstop=2 smartindent
let g:codedark_italics=1
let g:codedark_transparent=1
let s:plugin_dir = expand('~/plugged')
function! s:ensure(repo)
  let name = split(a:repo, '/')[-1]
  let path = s:plugin_dir . '/' . name

  if !isdirectory(path)
    if !isdirectory(s:plugin_dir)
      call mkdir(s:plugin_dir, 'p')
    endif
    execute '!git clone --depth=1 https://github.com/' . a:repo . ' ' . shellescape(path)
  endif

  execute 'set runtimepath+=' . fnameescape(path)
endfunction

call s:ensure('tomasiser/vim-code-dark')
call s:ensure('github/copilot.vim')
call s:ensure('DanBradbury/copilot-chat.vim')
colorscheme codedark
nnoremap cc :CopilotChatOpen<CR>
