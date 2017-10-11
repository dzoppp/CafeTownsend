from behave import *
from GitPage import *
#from features.steps.GitPage import *
#from features.steps.browser import Browser
from browser import Browser
from selenium import webdriver
from page_objects import PageObject, PageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


driver = Browser.driver

class GitPageStepsClass:

    @given('you are signed in to Github website')
    def step(self):

        driver.get('http://github.com/login')
        login_page = LoginPage(driver)
        login_page.input_login.send_keys('xxxxx')
        login_page.input_password.send_keys('xxxxx')
        login_page.btn_submit.click()

    @when('you click to create new repository')
    def steps(self):
        landing_page = LandingPage(driver)
        landing_page.btn_new_repository.click()

    @then('new repository site is shown')
    def steps(self):
        new_repo_page = NewRepoPage(driver)
        assert new_repo_page.input_new_repo_name

    @when('you put repository name as "{repo_name}" and submit')
    def steps(self, repo_name):
        new_repo_page = NewRepoPage(driver)
        new_repo_page.input_new_repo_name.send_keys(repo_name)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='new_repository']/div[4]/button")))

        new_repo_page.btn_submit_new_repo.click()

    @then('url to repository is shown')
    def steps(self):
        newly_created_repo = NewlyCreatedRepo(driver)
        repo_name = newly_created_repo.text
        assert repo_name == 'NowePioc6'

    @when('you push a new commit')
    def steps(self):
        os.system('python git_push.py')

    @when('you click to newly created repository')
    def steps(self):
        landing_page = LandingPage(driver)
        landing_page.row_first_repo.click()

    @when('you create new file for pull request')
    def steps(self):
        code_page = RepoCodePage(driver)
        code_page.btn_create_new_file.click()

    @when('you add filename and test text')
    def steps(self):
        create_new_file_page = CreateNewFilePage(driver)
        create_new_file_page.input_file_name.send_keys('new_file_pull_rq')
        create_new_file_page.input_code_editor.send_keys('test test test 3')
        create_new_file_page.radio_create_new_branch.click()
        create_new_file_page.btn_commit_new_file.click()

    @when('you create a pull request')
    def steps(self):
        create_pull_request_page = CreatePullRequestPage(driver)
        create_pull_request_page.btn_create_pull_request.click()

    @when('merge pull request')
    def steps(self):
        merge_pull_request_page = MergeRequestPage(driver)
        merge_pull_request_page.btn_merge_pull_request.click()
        merge_pull_request_page.btn_do_merge_pull_request.click()

    @when('you go to pull requests')
    def steps(self):
        code_page = RepoCodePage(driver)
        code_page.tab_pull_requests.click()

    @when('you select pull request')
    def steps(self):
        existing_pull_request_page = ExistingPullRequestsPage(driver)
        existing_pull_request_page.link_pull_request.click()

    @then('change is merged')
    def steps(self):
        existing_pull_request_page = ExistingPullRequestsPage(driver)
        assert existing_pull_request_page.mark_merged.contains('Merged')

    @when('you go to repository settings')
    def steps(self):
        code_page = RepoCodePage(driver)
        code_page.tab_settings.click()

    @when('you delete the repository "{repo_name}" and submit')
    def steps(self):
        repo_settings_page = RepoSettingsPage(driver)
        repo_settings_page.delete_the_repository.click()

    @then('Landing Page is shown')
    def steps(self):
        pass
        #assert true

    @then('logout')
    def steps(self):
        landing_page = LandingPage(driver)
        landing_page.dropdwn_user.click()
        landing_page.btn_logout.click()