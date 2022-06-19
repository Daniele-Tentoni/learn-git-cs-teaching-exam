# Calc

A simple calculator program made in Python.

**Table of Contents:**

* [Prepare the exercise](#prepare-the-exercise)
* [Exercise](#exercise)
    * [Repository creation (Exercise 1)](#repository-creation-exercise-1)
    * [Create some contents (Exercise 2)](#create-some-contents-exercise-2)
    * [Tag commits as versions (Exercise 3)](#tag-commits-as-versions-exercise-3)
    * [Add remote and push (Exercise 4)](#add-remote-and-push-exercise-4)
    * [To the infinite and beyond!](#to-the-infinite-and-beyond)

## Prepare the exercise

Create a directory named calc and copy here all files contained in this directory.

## Exercise

During those exercises you will create a repository that you have to push to a server at the end of the last one. Who doesn't reach that step, put every file inside this `calc` folder (including the hidden .git folder!) in a folder named `surname_name_git_calc` and put it in the shared folder of the lab.

> Note: submit every file, even if you think that is wrong, incorrect, bad or anything else, I'll evaluate both good results and your engagement.

### Repository creation (Exercise 1)

Create the repository with the command learned at lesson and look at the repository status and at the history. Add the output of the history command to a file named *es1.txt*. Start to track this file (README.md), see the status of the repository that is changed. Stop to track that file, see the status. Now track again that file, make a commit with a message "First commit" and see the status. See the history. Append the output of the history command to the file *es1.txt* (<ins>don't erase</ins> the previous contents).

### Create some contents (Exercise 2)

Complete following steps in order. After each step look at the status and understand what is changed.

1. Implement function described in the file *sum.py*

2. Modify file `calc.py` to invoke the function defined in the module `sum.py` when required as described inside `calc.py` file.

3. Save all that changes with a commit

Look at the history and understand what is changed.

Repeat those steps until the calc can't execute sum, sub, mul and div operations. You have to create a module with a dedicated function for each operation for this exercise.

Look at the history and understand what is changed.

Add the output of the history command to a file named *es2.txt*.

> Note: if you commit wrong files or changes, you can erase the last commit. If you have committed other changes after the wrong ones, you have to make a reverter commit.

### Tag commits as versions (Exercise 3)

Look at the history of the repository. Move to the commit where you have implemented the sum function of your calc. This could be the first version of our program for our customers! Let's `tag` that commit as `v1` and add a message with a description of changes you made. Then return to the last commit you've made and tag it as a successive version and add another useful message.

Add the output of the history command to a file named *es3.txt*.

### Add remote and push (Exercise 4)

Look at remote references of your repository. Add a remote reference, call it as you want, to a remote server at `192.168.100.100`. Track es*.txt files, commit them and push your repository to the remote server.

### To the infinite and beyond!

If you have completed all previous exercises, continue to modify your calc, commit each change to the repository each time you finish to implement one, tag versions when you think your work is stable and ready for a submit and push frequently to the remote repository.
