# LabData

Lab data and scripts for AST 443.

Github basics:

To clone a repository, type "git pull [repository name]"

Typing "git pull" while in a local repository will update it to the most recent synced version. Make sure you git pull frequently so you stay up to date!!!

Any changes you make are local to your computer until you push them.

If you have added any new files, you will need to add them to the staging area (which contains the files that git is keeping track of) by typing "git add [filename]. To remove a file from the staging area, type "git rm [filename]". Files will remain in the staging area even after you delete them from your local repository until you rm them.

Typing "git add --all" will add all new files and remove all deleted files. (Be careful when doing this is you just deleted a bunch of files, they will all be removed from the staging area at once.)

After you have staged your changes, you will need to commit them. Type "git commit" and a Vim window will open prompting you to record your changes.

Start typing in Vim to enter insert mode. After you've written a short commit message, hit "Escape" then type ":x" to save and quit.

The commits you have made will be local until you push them to the remote repository, where they will be synced with Github.

If you have made an error while editing a file and want to rewind to a previously committed version, type "git checkout -- [filename]"

Type "git log" to see a log of everyone's previous commits.

Type "git push" to push your changes. You will be prompted to log into Github.

Now your changes should be synced with Github.


TLDR;

"git pull" - Sync your local repository with the remote one on Github

"git add [filename]" - Stage any changes you have made

"git rm [filename]" - Unstage any changes you've made

"git commit" - Commit your changes and write a short message about the changes you made

"git push" - Push your changes to the remote repository where they will be synced with Github