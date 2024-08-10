# Validates functionality of scale

import time
from playwright.sync_api import Page, expect, sync_playwright

# function to handle the success dialog window
def handle_dialog_window_success(page: Page):
    page.get_by_role("button", name="Ok").click()
    page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)

# function to handle the fail dialog window
def handle_dialog_window_fail(page: Page):
    page.get_by_role("button", name="Ok").click()
    page.add_locator_handler(page.get_by_text("Oops! Try Again!"), handle_dialog_window_success)

# scale test
def test_fill_scale(page: Page):
    page.goto("http://sdetchallenge.fetch.com/")
    page.locator("#left_0").fill("0")
    page.locator("#left_1").fill("1")
    page.locator("#left_2").fill("2")
    page.locator("#left_3").fill("3")
    page.locator("#right_0").fill("5")
    page.locator("#right_1").fill("6")
    page.locator("#right_2").fill("7")
    page.locator("#right_3").fill("8")
    page.get_by_role("button", name="Weigh").click()
    time.sleep(3)

    first_results = page.get_by_role("listitem").inner_text()

    #if 1st attempt left > right
    if "[0,1,2,3] > [5,6,7,8]" in first_results:
        page.get_by_role("button", name="Reset").click()
        page.locator("#left_0").fill("5")
        page.locator("#left_1").fill("6")
        page.locator("#right_0").fill("7")
        page.locator("#right_1").fill("8")
        page.get_by_role("button", name="Weigh").click()
        time.sleep(4)

        #if 2nd attempt left > right
        if page.locator("text=[5,6] > [7,8]").is_visible():
            page.get_by_role("button", name="Reset").click()
            page.locator("#left_0").fill("7")
            page.locator("#right_0").fill("8")
            page.get_by_role("button", name="Weigh").click()
            time.sleep(3)

            #3rd attempt/results
            if page.locator("text=[7] > [8]"):
                page.get_by_role("button", name="8").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
            
            elif page.locator("text=[7] < [8]"):
                page.get_by_role("button", name="7").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success) 


        elif page.locator("text=[5,6] < [7,8]").is_visible():
            page.get_by_role("button", name="Reset").click()
            page.locator("#left_0").fill("5")
            page.locator("#right_0").fill("6")
            page.get_by_role("button", name="Weigh").click()
            time.sleep(3)

            #3rd attempt/results
            if page.locator("text=[5] > [6]"):
                page.get_by_role("button", name="6").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
            
            elif page.locator("text=[5] < [6]"):
                page.get_by_role("button", name="5").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
    
    #if 1st attempt left < right
    elif "[0,1,2,3] < [5,6,7,8]" in first_results:
        page.get_by_role("button", name="Reset").click()
        page.locator("#left_0").fill("0")
        page.locator("#left_1").fill("1")
        page.locator("#right_0").fill("2")
        page.locator("#right_1").fill("3")
        page.get_by_role("button", name="Weigh").click()
        time.sleep(4)

        #if 2nd attempt left > right
        if page.locator("text=[0,1] > [2,3]").is_visible():
            page.get_by_role("button", name="Reset").click()
            page.locator("#left_0").fill("2")
            page.locator("#right_0").fill("3")
            page.get_by_role("button", name="Weigh").click()
            time.sleep(3)

            #3rd attempt/results
            if page.locator("text=[2] > [3]"):
                page.get_by_role("button", name="3").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
            
            elif page.locator("text=[2] < [3]"):
                page.get_by_role("button", name="2").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)

        elif page.locator("text=[0,1] < [2,3]").is_visible():
            page.get_by_role("button", name="Reset").click()
            page.locator("#left_0").fill("0")
            page.locator("#right_0").fill("1")
            page.get_by_role("button", name="Weigh").click()
            time.sleep(3)

            #3rd attempt/results
            if page.locator("text=[0] > [1]"):
                page.get_by_role("button", name="1").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
            
            elif page.locator("text=[0] < [1]"):
                page.get_by_role("button", name="0").click()
                page.locator("text=Yay! You find it!").is_visible()
                page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
    
    #if 1st attempt left = right
    elif "[0,1,2,3] = [5,6,7,8]" in first_results:
        #tests oops message
        page.get_by_role("button", name="7").click()
        page.locator("text=Oops! Try Again!").is_visible()
        page.add_locator_handler(page.get_by_text("Oops! Try Again!"), handle_dialog_window_fail)
        #tests success message
        page.get_by_role("button", name="4").click()
        page.locator("text=Yay! You find it!").is_visible()
        page.add_locator_handler(page.get_by_text("Yay! You find it!"), handle_dialog_window_success)
