from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/aadil/Downloads/chromedriver-4")  # Enter the complete path of chrome webdriver here
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://todomvc.com/examples/react/#/")

todos_count = 4


def add_to_dos():  # This function will be called to add todos
    for i in range(0, todos_count):
        driver.find_element_by_xpath("//input[@class='new-todo']").send_keys("The Room")
        driver.find_element_by_xpath("//input[@class='new-todo']").send_keys(Keys.ENTER)


def update_all_todos():  # This function will be called to updated the existing todos in current tab
    todos = driver.find_elements_by_xpath("//li/div[@class='view']")
    edit_boxes = driver.find_elements_by_xpath("//li/input[@class='edit']")
    if len(todos) > 0:
        for todo, edit_box in zip(todos, edit_boxes):
            action = ActionChains(driver)
            action.double_click(on_element=todo)
            action.perform()
            edit_box.send_keys(" Updated")
    else:
        print("There are no todos present to be updated in the current tab")


def check_all():  # This function will be called to mark all the todos as completed or incomplete
    driver.find_element_by_xpath("//label[@for='toggle-all']").click()


def check_one_by_one():  # This function will be called to mark all the todos as complete or incomplete one by one
    checkboxes = driver.find_elements_by_xpath("//div/input[@type='checkbox']")
    if len(checkboxes) > 0:
        for checkbox in checkboxes:
            checkbox.click()
    else:
        print("There are no todos present in the current tab to be selected as completed")


def get_all():  # This function will be called to see all the active todos
    driver.find_element_by_link_text("All").click()


def get_active():  # This function will be called to see all the active todos
    driver.find_element_by_link_text("Active").click()


def get_completed():  # This function will be called to see all the completed todos
    driver.find_element_by_link_text("Completed").click()


def clear_completed():  # This function will be called to clear all the completed todos
    completed_visible = driver.find_elements_by_xpath("//button[@class='clear-completed']")
    if len(completed_visible) > 0:
        driver.find_element_by_xpath("//button[@class='clear-completed']").click()
    else:
        print("There are no completed todos")


def delete_all():  # This function will be called to delete all the todos present in the current tab
    total_todos = driver.find_elements_by_xpath("//li/div[@class='view']")
    if len(total_todos) > 0:
        for todos in total_todos:
            action = ActionChains(driver)
            click_delete = todos.find_element_by_xpath("button[@class='destroy']")
            action.move_to_element(to_element=todos).perform()
            click_delete.click()
    else:
        print("There are no todos to be deleted in the current tab")


add_to_dos()
update_all_todos()
clear_completed()
delete_all()
check_one_by_one()
driver.close()
