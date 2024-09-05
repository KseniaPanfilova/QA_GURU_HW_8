import allure
from allure_commons.types import Severity
from selene import browser, have, be


@allure.tag('WEB')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'k.panfilova')
@allure.feature('Issues in a repository')
@allure.story('Visibility of created issues')
@allure.link('https://github.com', name='Testing site')
def test_github_issue():
    open_main_page()
    look_for_repo('KseniaPanfilova/QA_GURU_HW_8')
    open_repo_by_link('/KseniaPanfilova/QA_GURU_HW_8')
    open_issues_tab()
    should_see_issue_with_number(1)


@allure.step('Open GitHub main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Look for repository')
def look_for_repo(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Open repository\'s page by link from search result')
def open_repo_by_link(repo):
    browser.element(f'[href="{repo}"]').click()


@allure.step('Go to issues tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check the visibility of the element')
def should_see_issue_with_number(number):
    browser.all('.js-issue-row').element_by(have.text(f'#{number}')).should(be.visible)
