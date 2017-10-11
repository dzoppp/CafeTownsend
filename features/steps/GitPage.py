__author__ = 'pioc'

from browser import Browser
from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    input_login = PageElement(id_='login_field')
    input_password = PageElement(id_='password')
    btn_submit = PageElement(name='commit')


class LandingPage(PageObject):
    btn_new_repository = PageElement(link_text='New repository')
    row_first_repo = PageElement(partial_link_text='NowePioc6')
    dropdwn_user = PageElement(class_name='avatar float-left mr-1')
    btn_logout = PageElement(class_name='dropdown-signout')

class NewRepoPage(PageObject):
    input_new_repo_name = PageElement(id_='repository_name')
    btn_submit_new_repo = PageElement(xpath="//*[@id='new_repository']/div[4]/button")

class NewlyCreatedRepo(PageObject):
    div_repo_name = PageElement(xpath="//*[@id='js-repo-pjax-container']/div[1]/div/h1/strong/a")

class RepoCodePage(PageObject):
    btn_create_new_file = PageElement(class_name='BtnGroup-form')
    tab_pull_requests = PageElement(link_text='Pull requests')
    tab_settings = PageElement(link_text='Settings')

class CreateNewFilePage(PageObject):
    input_file_name = PageElement(name='filename')
    input_code_editor = PageElement(class_name='CodeMirror-scroll')
    radio_create_new_branch = PageElement(class_name='form-checkbox pl-4 my-0')
    btn_commit_new_file = PageElement(id_='submit-file')

class CreatePullRequestPage(PageObject):
    btn_create_pull_request = PageElement(class_name='btn btn-primary')

class MergeRequestPage(PageObject):
    btn_merge_pull_request = PageElement(link_text='Merge pull request')
    btn_do_merge_pull_request = PageElement(name='do')

class ExistingPullRequestsPage(PageObject):
    link_pull_request = PageElement(xpath="//*[@id='issue_1']/div/div[3]/a")
    mark_merged = PageElement(xpath="//*[@id='partial-discussion-header']/div[2]/div[1]/div/text()")

class RepoSettingsPage(PageObject):
    btn_delete_the_repository = PageElement(link_text='Delete this repository')
    input_confirmation = PageElement(name='verify')
    btn_confirm_delete = PageElement(class_name='btn btn-block btn-danger')