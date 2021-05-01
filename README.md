# Run any program or code inside vim with a single click

Currently vide supports javascript, python, c++, ruby, html(outputs result in firefox), txt(cats txt file).

## Dependencies
node for js
python3 for py
firefox for html
ruby for rb
gcc for c++

## Installation

Run this command inside your terminal: 

git clone https://github.com/particleofmass/vide/ ~/.vim/vide

Add these lines to your .vimrc :

nnoremap \<F8\> :w \<bar\> !clear && g++ -O2 -Wall -o  %:r.out % -std=c++17\<Enter\> 

nnoremap \<F9\> :w \<bar\> !clear && echo %:e \> ~/.vim/vide/filetype.txt && echo %:t \> ~/.vim/vide/tail.txt &&  echo %:p:h \> ~/.vim/vide/head.txt && echo %:p \> ~/.vim/vide/filepath.txt && python3 ~/.vim/vide/run.py\<Enter\>


