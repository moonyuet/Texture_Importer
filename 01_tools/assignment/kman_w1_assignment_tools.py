# TOOLS *********************************************************************
# content = assignment
#
# deliver = Upload the files to your git repository
#           and share it in the assignment submission form.
#
# date    = 2022-03-13
# email   = contact@alexanderrichtertd.com
#***************************************************************************
"""



NOTE: Give yourself the time to play around with the tools,
      make sure everything works properly and note down your questions for our Q&A.




#******************************************************************************
# 01. ADVANCED SCRIPT EDITOR
#******************************************************************************
Let's explore and advance in our use of the script editor:

    a) Install and try one unfamiliar but promising script editor
       that you will use through out the masterclass:

        * Sublime Text 3
        * Visual Studio Code
        * PyCharm
        * ATOM
        * VIM
        * ...


    b) Check out the settings and plugins and add these or more:
        * user settings
        * git
        * spell check
        * color theme
        * ...


    c) USE a few new shortcuts


    d) ADD one helpful snippet and use it through out the masterclass



NOTE: Nothing to upload in this task.









#******************************************************************************
# 02. SHELL
#******************************************************************************
1) Do the following steps only using a shell:

    a) Create the directory "shell_test"
    
    mkdir shell_test

    b) Create the file "test_print.py" with a simple print into the directory
    
    cd shell_test
    touch test_print.py
    cat > test_print.py << "END_SCRIPT"
    END_SCRIPT
 
    
    

    c) Rename the file to "new_test_print.py"
    
    mv test_print.py new_test_print.py

    d) List what is in the directory "shell_test" including their file permissions
    
    ls shell_test

    e) Execute the Python file and call the simple print
    
    python new_test_print.py
    

    f) Remove the directory "shell_test" with its content
   
    rm -r shell_test

    BONUS: Solve the tasks without looking them up.

See shell_script.ps1 for execution










2) CREATE a custom .bat or .sh that does the following:

    a) STARTS a DCC of your choice (Maya, Nuke, Houdini, ...)
    


    b) ADDS custom script paths
    

    c) ADDITIONAL overwrites (paths, menus, ...)


    d) Make sure everything works as intended

see start_nuke.bat








#******************************************************************************
# 03. GIT
#******************************************************************************

1) STUDY git example
-----------------------------------------------------------
Before we start to work with git let's make sure to get familiar with the workflow
and how a git project should look like.
Browse through the folders and Wiki of my Open Source Pipeline Plex
which also serves as a code and documentation example throughout this masterclass:

    a) EXPLORE the Plex git repository and look into the code:
    https://github.com/alexanderrichtertd/plex


    b) READ the Wiki to understand the basics of the pipeline:
    https://github.com/alexanderrichtertd/plex/wiki












2) CREATE an assignment repository
-----------------------------------------------------------
All the upcoming assignments must be uploaded to your git repository.
Use the git shell for the following tasks:

    a) Create a new repository for the assignments on GitHub/GitLab/... with the sub folders:
        * 01_tools
        * 02_style
        * 03_advanced
        * 04_ui

       NOTE: If you use sensitive (company) data make your repository private.
             Invite me using alexanderrichtertd@gmail.com
             (Keep the resources out of your repository.)


    b) ADD a README.mb file describing your application.


    c) ADD and fill out a .ignore file (must ignore all .pyc files)


    d) ADD, commit and push your initial code remote into "01_tools".

    IMPORTANT: In future assignments make sure to commit and push the original version
               before starting with the assignment so we have a before and after.
               The commit message must be: INIT 02_style/03_advanced/04_UI
               And: UPDATE 02_style/03_advanced/04_UI.


    e) MAKE changes, commit and push again


    f) CREATE a branch "develop", make small changes and push it remote


    g) MERGE your develop changes into master


    h) TEST and clone your remote repository into another directory (as if you are a user).


    i) SHARE your repository with our #python_advanced Discord community (if not private).

    https://github.com/moonyuet/Texture_Importer










3) DID YOU GET THAT?
-----------------------------------------------------------
ANSWER the following questions:

    a) Why should you use git instead of Google Drive for your (teams) code?
    
    git helps you to manage and track the codes easily when you are working with teammates.
    At the same time, it can help to restore lost data and 
    it has a history for each commit which shows all updates and changes.

    besides, you and your teammate can be working with different codes and merged with updated codes once finished.
    there is a version control within the git, allowing the developers and users to track the latest version easily.

    b) What does "git add" and "git commit" do? What is the difference?
    git add: define tracked files
    git commit: Create a commented package

    Git add is adding and tracking the files 
    while git commit is assigning the comment on the package which includes those files. 


    c) What is the difference between "git pull" and "git push"?
    git pull: Get and merge remote updates
    git push: Send and merge remote updates

    d) What does the command "git checkout" do?
       What can you do if you cannot checkout because you have untracked files?

    Switching to the branch 
    
    Git Stash  (you mentioned in Q & A)

    e) When do you need branches?

    The branches are created for testing new features or fix bugs. 
    Once the bug fixed or the feature passes the QA, it can be merged to original scripts and shares with the users.


    TIP: Create a practical example if you're unsure.



"""

