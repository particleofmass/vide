# vide
## Run/execute any program in vim with single click

Do you need to run multiple programs manually in the terminal using bunch of commands?
Don't worry now vide(vim is ide) is here. But "vide" isn't about making your program colorful and add autoformat and youcomplete stuff. Nope!
"vide" is about making your programs in different languages run with the same keybindings and also load your templates.

Currently "vide" is able to run: javascript, python, c++, html and txt.

Dependencies : node(javascript), python3(python), gcc(c++), firefox(html)

### Installation 

1. git clone
2. copy the vide directory to your ".vim" directory so that the path to vide becomes "~/.vim/vide"
3. cd ~/.vim/vide
4. chmod +777 *
5. Now add the below keybindings to your vimrc \
    nnoremap <F7> :!cp ~/Desktop/templates/template.%:e %<Enter> \
    nnoremap <F8> :w <bar> !clear && g++ -O2 -Wall -o  %:r.out % -std=c++17<Enter> \
    nnoremap <F9> :!clear && echo %:e > ~/.vim/vide/filetype.txt && echo %:t > ~/.vim/vide/tail.txt &&  echo %:p:h > ~/.vim/vide/head.txt && echo %:p > ~/.vim/vide/filepath.txt && python3 ~/.vim/vide/run.py<Enter>
6. If you want to load templates to a file currently open in vim then you could create a templates directory on your desktop and then create a template file you wish to load. You could also use my templates directory but make sure the templates have read permissions.
7. Now you're good to go. If you face any erros then they might be due to file permissions and directory cloned into your custom path so update vimrc and "vide/run.py" with your custom file locations.

Note: Make sure to compile c++ programs using <F8> before running them by pressing <F9>

### PEACE!
If you have any suggestions or want me to add support for other languages then let me know.
particleofmass@gmail.com or https://www.reddit.com/user/particleofmass
