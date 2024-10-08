import allure
from allure_commons.types import Severity
from selene import browser, have, be


def test_github_issue():
    allure.dynamic.tag('WEB')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('Issues in a repository')
    allure.dynamic.story('Visibility of created issues')
    allure.dynamic.link('https://github.com', name='Testing site')
    allure.dynamic.label('owner', 'k.panfilova')

    with allure.step('Open GitHub main page'):
        browser.open('https://github.com')

    with allure.step('Look for repository'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('KseniaPanfilova/QA_GURU_HW_8').press_enter()

    with allure.step('Open repository\'s page by link from search result'):
        browser.element('[href="/KseniaPanfilova/QA_GURU_HW_8"]').click()

    with allure.step('Go to issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Check the visibility of the element'):
        browser.all('.js-issue-row').element_by(have.text('#1')).should(be.visible)
