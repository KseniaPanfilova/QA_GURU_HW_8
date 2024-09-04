from selene import browser, have, be


def test_github_issue():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('KseniaPanfilova/QA_GURU_HW_8').press_enter()

    browser.element('[href="/KseniaPanfilova/QA_GURU_HW_8"]').click()

    browser.element('#issues-tab').click()

    browser.all('.js-issue-row').element_by(have.text('#1')).should(be.visible)
