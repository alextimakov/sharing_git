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
- stick to similar aliases [here]()
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
- rename file: `git mv <file_from> <file_to>`
#### view the commit history
- bare history request: `git log`
- check diff for the last n commits: `git log -p -<n>`
- check stats of each commit: `git log --stat`
- print history up-to-format: `git log --pretty=format:"<format>"` 
- [formats here](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
- get ASCII graph of changes: `git log --pretty=format:"%h %s" --graph`
#### undoing things
- update the last made commit: `git commit --amend`
- unstage selected file: `git reset HEAD <filename>`
- unmodify selected file: `git checkout -- <filename>`
#### working with remotes
- check remotes you're working on: `git remove -v`
- get info about remote: `git remote show <remote>`
- fetch data with all branches from remote: `git fetch <remote>`
- pull data from the identical branch: `git pull`
- push project upstream: `git push <remote> <branch_to_push>`
- you can't push to the same remote branch if someone pushed there already, fetch first
- rename remote: `git remote rename <old_remote> <new_remote>`
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
- HEAD is a pointer to current branch

![alt text](https://github.com/alextimakov/sharing_git/blob/master/media/branching_model.PNG)

- list all existing branches (local & remote): `git branch -a`
- checkout with creating new branch: `git checkout -b <branch>`
- it’s best to have a clean working state when you switch branches
- when switch branches, Git resets your working directory to look like the last commit on that branch
- easiest scenario: 
    - commit all changes
    - checkout to new branch
    - commit changes to it
    - merge with previous (fast-forward) commit
- not-so-easy scenario:
    - basic merging

#### possible errors and flaws
- removing modified files: 
    - cause: `git rm <modified>`
    - traceback: the following file has local modifications \ have changes staged in the index
    - solution: commit all changes -> remove files-> then commit removal
- trying to work with non-existing file \ pointer:
    - cause: `git checkout <branch_name>` 
    - error: pathspec 'testing' did not match any file(s) known to git
    - solution: add necessary files \ pointer
- if you don't have file, you can push and it still stays in remote repo
- 