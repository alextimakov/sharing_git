### Basic commands
#### 3 stages of file in git
- Working locally

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/git_stages.png)

#### git config
- 3 levels of config, always apply the lowest one
- check existing config: `git config --list --show-origin`
- config global settings: 
    - `git config --global user.name <"git_login">`
    - `git config --global user.email <email>`
    - `git config --global core.editor <"editor">` 
    - [Different editors](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)
- ask for help if not sure:
    - `git help command`
    - `git command -h`

#### git aliases
- make an alias for simple command: `git config --global alias.<alias> <command>`
- make an alias for complex command: `git config --global alias.<alias> '<command>'`
- stick to similar aliases [here](https://confluence.biocad.ru/pages/viewpage.action?pageId=111907575)

#### getting a git repository
- initialize locally: 
    - go to directory: `cd /c/users/timakov/needed_dir`
    - create .git: `git init`
    - start VC: 
        - `git add .`
        - `git commit -m "initial commit"`
- clone existing repo
    - find repo on github and copy its link
    - clone repo:  `git clone <link_to_repo> <folder_to_clone>`
    - name a remote whatever you like: `git clone -o <remote_name>` 

#### recording changes to repo
- all files are either tracked (exist in last commit) or untracked (new or removed)

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/file_stages.png)
- check files’ statuses: `git status`
- adding files to tracked: `git add <filename> | git add <directory>`
- add selected content to the next commit: `git add <filename>`
- file being both staged and unstaged: add -> change
- ignoring files: _.gitignore_ (look for appropriate one [here](https://github.com/github/gitignore))
- see changes line-by-line: `git diff | git diff --staged`
- commit files: `git commit -m "commit_message"` 
- commit all files (inc. unstaged): `git commit -a -m "commit_message"`
- remove file from directory: `rm <filename>`
- remove file from directory & stage removal from git: `git rm <filename>`
- remove file only from staged: `git rm --cached README`
- remove file only from staged: `git reset <filename>`
- rename file: `git mv <file_from> <file_to>`

#### view the commit history
- bare history request: `git log`
- check diff for the last n commits: `git log -p -<n>`
- check stats of each commit: `git log --stat`
- print history up-to-format: `git log --pretty=format:"<format>"` 
- [formats here](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- get ASCII graph of changes: `git log --pretty=format:"%h %s" --graph`
- compact view for all history: `git log --oneline`

#### undoing things
- update the last made commit: `git commit --amend`
- move HEAD to another commit: `git reset --soft <commit_hash>`
- unstage selected file: `git reset HEAD <filename>`
- unstage all (return to stage of previous commit): `git reset`
- reset stage and working directory: `git reset --hard <commit_hash>`
- unmodify selected file locally: `git checkout -- <filename>`
- return files from previous commit to stage and working directory: `git checkout HEAD <file_name>`

#### working with remotes
- check remotes you're working on: `git remove -v`
- get info about remote: `git remote show <remote>`
- synchronize with remote: `git fetch <remote>`
![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/fetch_remote.PNG)
- fetch from all remotes: `git fetch --all`
- pull data (fetch + merge in respect to tracking branches): `git pull`
- push project upstream: `git push <remote> <branch_to_push>`
- you can't push to the same remote branch if someone pushed there already
    - error: failed to push some refs to 'https://github.com/<your_repo>.git'
    - `git fetch` -> `git push`
- be very careful with forcing: `git push --force` 
- rename remote: `git remote rename <old_remote> <new_remote>`
- create tracking branch: `git checkout -b <local_branch> <upstream_remote_branch>`
- delete remote branch: `git push <remote> --delete <branch>`
- if upstream is not set up to branch: `git push --set-upstream <remote_name> <branch_name>`

#### tagging version
- list all tags: `git tag`
- find and list tags by regex: `git tag -l "<*tag*>"`
- create lightweight tag: `git tag <tag>`
- create annotated tag: `git tag -a <tag> -m "tag_message"`
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
- HEAD is a pointer to current branch (your current position)
- branch is a pointer to commit

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/branching_model.PNG)

- list all existing branches (local & remote): `git branch -a`
- check the latest commit on each branch: `git branch -v`
- check the latest commit + tracking branches: `git branch -vv`
- checkout with creating new branch: `git checkout -b <branch>`
- check what is merged to current branch: `git branch --merged`
- check what is not merged to <branch-name>: `git branch --no-merged <branch_name>`
- delete remote branch: `git push --delete <remote_name> <branch_name>`
- delete local branch: `git branch -d <branch_name>`
- some more conventions to get better understanding:

![alt text]()

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
    
![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/recursive_merging.PNG)
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
- create new branch based old commit:
    - `git checkout <commit_hash>`
    - - `detached HEAD` state: HEAD is not pointing to any branch
    - `git checkout -b <branch_name>`
- make the branch manually point to any commit: `git reset --hard <commit_hash>`

#### branching workflows
- long-running branches
- topic branches

#### rebasing
- take the patch of change and reapply it on top of master's commit
- interactive rebasing: `git rebase --interactive`
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

#### workflows examples
- local workflow examples:
    - have up-to-date base code, want to start new feature:
    1. want to update all dependencies (easiest scenario)
        - create and checkout to new branch: `git checkout -b <branch_name>`
        - do all work locally and commit: `git commit -a -m "message"`
        - checkout to master and merge: `git checkout master; git merge <branch_name>`
        - delete used branch and profit!
    2. want to fix old bugs AND add new feature AND change master branch
        - create and checkout to new branch: `git checkout -b <bug>`
        - do all work locally and commit: `git commit -a -m "message"`
        - want to add new feature:
            - checkout to master
            - create and checkout to new branch: `git checkout -b <feature>`
            - do all work locally and commit: `git commit -a -m "message"`
            - checkout and do some changes to `<master>`
            - commit changes to `<master>`
            - rebase feature branch to master: 
                - `git checkout <feature>`
                - `git rebase <master>`
                - `git checkout <master>`
                - `git merge <feature>`
            - delete used branch
         - go back to `<bug>` branch and try to rebase it
         - MERGE conflict pops up
         - to see diff: `git am --show-current-patch`
         - conflicts to be resolved manually: `git mergetool`
         - [mergetool info](https://stackoverflow.com/questions/161813/how-to-resolve-merge-conflicts-in-git) 
         - `git rebase --continue`
         - `git checkout <master>`
         - `git merge <feature>`

#### distributed workflows' types:
- centralized workflow
    - single repository
    - each has rw access
    - pull & push
- integration-manager workflow
    - multiple repositories
    - each has w access to own and r to all others
    - integration manager push to public blessed repo
    - each clones repo and makes changes
    - each push changes to public own repo
    - integration manager add each's repo as remote and merges locally 
    - integration manager check commits and push to blessed repository
 - shared repository model
 - fork and pull model
    - pull requests: 
    - CLI: `git request-pull <remote_branch> <url> <branch_to_push>`
    - easier via GUI on github
    
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
- forking vs cloning:
    - fork share a connection with the original repo
    - if clone - not able to pull and push unless added as collaborator
    - if fork - can pull and push via pull requests
    - clone won't bring issues, pull requests and other repo info
- errors while pull \ fetch:
    - try to `git pull`
    - files in the same branch on remote and on local differs
    - error: `Automatic merge failed; fix conflicts and then commit the result`
    - diff automatically appears in working directory
    - fix conflict (remove unnecessary lines)
    - `git add <cleaned_file>`
    - `git commit` to finish merge 
- be careful with flags `-f --force --hard` it will delete uncommitted changes

#### useful resources
- [explanation of basic git concepts](http://marklodato.github.io/visual-git-guide/index-en.html) 
- [filter-branch](https://manishearth.github.io/blog/2017/03/05/understanding-git-filter-branch/)
