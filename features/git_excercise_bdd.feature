Feature: git_basic_steps
  #Piotr O.#

Scenario: Creating a repository at git
  Given you are signed in to Github website
  When you click to create new repository
  Then new repository site is shown
  When you put repository name as "NowePioc6" and submit
  Then url to repository is shown
  Then logout

Scenario: Push commits
  When you push a new commit

Scenario: New pull request
  Given you are signed in to Github website
  When you click to newly created repository
  And you create new file for pull request
  And you add filename and test text and submit
  When you create a pull request
  Then logout

Scenario: Merge pull request
  Given you are signed in to Github website
  When you click to newly created repository
  And you go to pull requests
  And you select pull request
  And merge pull request
  Then change is merged
  Then logout

Scenario: Delete the repository
  Given you are signed in to Github website
  When you click to newly created repository
  And you go to repository settings
  And you delete the repository "NowePioc6" and submit
  Then Landing Page is shown
  Then logout




	  
