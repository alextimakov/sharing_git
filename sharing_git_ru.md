### Basic commands
#### 3 stages of file in git
- Стадии работы с файлами

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/git_stages.png)
#### git config
- есть 3 уровня конфигов, применяется наиболее локальный
- проверить текущий конфиг: `git config --list --show-origin`
- настроить глобальный конфиг: 
    - `git config --global user.name <"git_login">`
    - `git config --global user.email <email>`
    - `git config --global core.editor <"editor">` 
    - [Разные редакторы](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)
- есть функционал помощи по командам:
    - `git help command`
    - `git command -h`
#### git aliases
- сделать alias для простой команды: `git config --global alias.<alias> <command>`
- сделать alias для сложной команды: `git config --global alias.<alias> '<command>'`
- можем сразу обусловиться на единых aliases [тут](https://confluence.biocad.ru/pages/viewpage.action?pageId=111907575)
#### getting a git repository
- инициализируем репо с 0: 
    - идём в нужную директорию: `cd /c/users/timakov/needed_dir`
    - создаём файл .git: `git init`
    - запускаем контроль версий: 
        - `git add .`
        - `git commit -m "initial commit"`
- клонируем существующий репо
    - находим репо на github и копируем ссылку на него
    - клонируем репо по ссылке: `git clone <link_to_repo> <folder_to_clone>`
    - можем назвать его локально как требуется: `git clone -o <remote_name>` 
#### recording changes to repo
- все файлы в git могут быть отслеживаемые (были в крайнем коммите) или неотслеживаемые (новые или удалённые файлы)

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/file_stages.png)
- проверить статусы файлов: `git status`
- добавление файлов в отслеживаемые: `git add <filename> | git add <directory>`
- добавить версию файла в следующий коммит: `git add <filename>`
- если файл сразу в 2-х статусах: `git add`, а потом меняем
- все игноры пишем в файле: _.gitignore_ (лучшие практики [тут](https://github.com/github/gitignore))
- смотрим изменения построчно: `git diff | git diff --staged`
- коммитим отслеживаемые файлы: `git commit -m "commit_message"` 
- коммитим все файлы: `git commit -a -m "commit_message"`
- убрать файл из директории: `rm <filename>`
- убрать файл из директории и отследить это удаление: `git rm <filename>`
- убрать файл только из отслеживаемых: `git rm --cached README`
- переименовать файл: `git mv <file_from> <file_to>`
#### view the commit history
- простой запрос истории: `git log`
- посмотреть разницу в последних n коммитах: `git log -p -<n>`
- проверить статистику коммитов: `git log --stat`
- показать историю согласно формату: `git log --pretty=format:"<format>"` 
- варианты форматов [тут](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- получить ASCII граф изменений: `git log --pretty=format:"%h %s" --graph`
#### undoing things
- апдейтнуть крайний коммит:
    - `git commit -m "commit_message"`
    - `git add <forgotten_file>`
    - `git commit --amend`
- убрать выбранный файл из отслеживаемых: `git reset HEAD <filename>`
- откатить изменения в выбранной файле: `git checkout -- <filename>`
#### working with remotes
- проверить удалённые репо и ветки: `git remove -v`
- получить информацию об удалённом репо: `git remote show <remote>`
- забрать данные с удалённого репо: `git fetch <remote>`
![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/fetch_remote.PNG)
- забрать все данные и указатели: `git fetch --all`
- умно забрать данные (`git fetch` + `git merge`): `git pull`
- отправить изменения на удалённый репо: `git push <remote> <branch_to_push>`
- git не даст отправить изменения на удалённый репо, если кто-то уже отправил что-то
    - ошибка: failed to push some refs to 'https://github.com/<your_repo>.git'
    - `git fetch` -> `git push`
- очень аккуратно с флагом force: `git push --force` 
- переименовать удалённый репо: `git remote rename <old_remote> <new_remote>`
- начать отслеживать ветку (синхрон): `git checkout -b <local_branch> <upstream_remote_branch>`
- удалить ветку в удалённом репо: `git push <remote> --delete <branch>`
#### tagging version
- показать все теги: `git tag`
- найти теги через регекс: `git tag -l "<*tag*>"`
- создать лёгкий тег: `git tag <tag>`
- создать аннотированный тег: `git tag -a <tag> -m "tag_message"`
- show selected tag: `git show <tag>`
- tag commit later: `git tag -a <tag> <commit_hash_7>`
- share tag: `git push <remote> <tag>`
- share all tags: `git push <remote> --tags`
- delete local tag: `git tag -d <tag>`
- delete remote tag: `git push origin --delete <tag>`
- checkout on tag: `git checkout <tag>`
### Branching and merging
#### Branching logic
- create new branch: `git branch <branch_name>`
- HEAD is a pointer to current branch

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/branching_model.PNG)

- list all existing branches (local & remote): `git branch -a`
- check the latest commit on each branch: `git branch -v`
- check the latest commit + tracking branches: `git branch -vv`
- checkout with creating new branch: `git checkout -b <branch>`
- check what is merged to current branch: `git branch --merged`
- check what is not merged to <branch-name>: `git branch --no-merged <branch_name>`
 
- it’s best to have a clean working state when you switch branches
- when switch branches, Git resets your working directory to look like the last commit on that branch
- easiest scenario: 
    - commit all changes
    - checkout to new branch
    - commit changes to it
    - checkout back to master
    - merge with previous (fast-forward) commit
    - delete new branch if not needed in future
- not-so-easy scenario:
    - checkout to new branch 
    - commit changes to it
    - checkout back to master
    - merge with the common ancestor (recursive strategy)
    - delete new branch if not needed in future
    
![alt text]()
- merging conflicts solving:
    - error: Automatic merge failed; fix conflicts and then commit the result
    - check the reason of conflict: `git status`
    - solution: `git merge <branch>`
    - go to IDE or `git mergetool`
    - everything above `====` is for HEAD version
    - resolve all the differences and leave final version in master branch
    - delete all `<<<<`, `>>>>`, and `====`
    - confirm changes: `git commit`
    - if need to add only one file as resolution: `git add <filename>`
    - [info about advanced merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_advanced_merging) 

#### branching workflows
- long-running branches
- topic branches

#### rebasing
- take the patch of change and reapply it on top of master's commit
- rebase feature branch it to master: 
    - `git checkout <feature>`
    - `git rebase <master>`
    - `git checkout <master>`
    - `git merge <feature>`
- complex rebase:
    - `git rebase --onto <basebranch> <topic_branch> <subtopic_branch>`
    - `git checkout <basebranch>`
    - `git merge <subtopic_branch>`
- do not rebase commits that exist outside your repository and people may have based work on them
- if this happened:
    - check info upon patch-id
    - when fetching data, try: `git pull --rebase`
    
#### topics for later
- [filter-branch](https://manishearth.github.io/blog/2017/03/05/understanding-git-filter-branch/)
- distributed workflows:
    - centralized workflow
        - single repository
        - each has rw access
        - pull & push
    - integration-manager workflow
        - multiple repositories
        - each has w access to own and r to all others
        - integration manager check commits and push to blessed repository
    
#### errors / conflicts / common phrases 
- removing modified files: 
    - cause: `git rm <modified>`
    - traceback: the following file has local modifications \ have changes staged in the index
    - solution: commit all changes -> remove files-> then commit removal
- trying to work with non-existing file \ pointer:
    - cause: `git checkout <branch_name>` 
    - error: pathspec 'testing' did not match any file(s) known to git
    - solution: add necessary files \ pointer
- if you don't have file, you can push and it still stays in remote repo
- trying to delete --no-merged branch:
    - error: The branch 'testing' is not fully merged.  
    - solution: merge branch -> delete or `git branch -D <branch_name>`
- branch <name> set up to track remote branch <name> from <remote>
    - cause: `git checkout <branch_name>`
    - track remote branch
    - set up upstream to current branch: `git branch -u <remote>/<branch_name>`