# Validates elements on the homepage

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page): #tests page has title element
    page.goto("http://sdetchallenge.fetch.com/")
    expect(page).to_have_title(re.compile("React App"))

def test_has_reset_button(page: Page): #tests has reset button
    page.goto("http://sdetchallenge.fetch.com/")
    expect(page.get_by_role("button", name="Reset")).to_be_visible()

def test_has_weigh_button(page: Page): #tests has weigh button
    page.goto("http://sdetchallenge.fetch.com/")
    expect(page.get_by_role("button", name="Weigh")).to_be_visible()

def test_clicks_buttons(page: Page): #tests that reset and weigh button is clickable
    page.goto("http://sdetchallenge.fetch.com/")
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Weigh").click()