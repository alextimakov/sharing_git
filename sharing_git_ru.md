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
        - начинаем отслеживать всё: `git add .`
        - делаем первый коммит: `git commit -m "initial commit"`
- клонируем существующий репо:
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
- показать выбранный тег: `git show <tag>`
- затегировать имеющийся коммит: `git tag -a <tag> <commit_hash_7>`
- расшарить тег: `git push <remote> <tag>`
- расшарить все теги: `git push <remote> --tags`
- удалить локальный тег: `git tag -d <tag>`
- удалить тег с удалённого репо: `git push origin --delete <tag>`
- перейти на тег: `git checkout <tag>`
### Branching and merging
#### Branching logic
- создать новую ветку: `git branch <branch_name>`
- HEAD - это указатель на текущую ветку

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/branching_model.PNG)

- показать все ветки (локальные и удалённые): `git branch -a`
- показать крайний коммит на каждой ветке: `git branch -v`
- показать крайние коммиты и трековые ветки: `git branch -vv`
- создать новую ветку и перейти в неё: `git checkout -b <branch>`
- показать замерженные ветки: `git branch --merged`
- показать незамерженные ветки к ветке <branch-name>: `git branch --no-merged <branch_name>`
 
- перед сменой ветки, лучше всего очистить рабочую зону
- при смене веток, git возвращает рабочую зону в состоянии, соответствующе крайнего коммиту выбранной ветки
- простейший сценарий мёржа: 
    - коммитим все изменения на мастер
    - переключаемся на новую ветку
    - кделаем и коммитим все изменения в ней
    - переходим обратно на мастер
    - делаем мёрж с крайним (fast-forward) коммитом
    - удаляем новую ветку, если в будущем будет не нужна
- сценарий мёржа посложнее:
    - тот же сценарий
    - делаем мёрж с общим коммитом двух веток (recursive strategy)
    - удаляем новую ветку, если в будущем будет не нужна
    
![alt text]()
- решаем мёрж конфликты:
    - ошибка: Automatic merge failed; fix conflicts and then commit the result
    - проверяем статус файлов в конфликте: `git status`
    - пытаемся сделать мёрж: `git merge <branch>`
    - идём в IDE или `git mergetool`
    - всё выше `====` - версия в HEAD
    - разрешаем все противоречия и оставляем в мастер ветке
    - удаляем все `<<<<`, `>>>>`, и `====`
    - подтверждаем изменения: `git commit`
    - если лишь один файл является решением конфликта: `git add <filename>`
    - больше о сложных схемах мёржа [тут](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_advanced_merging) 

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
    - added new line
    
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