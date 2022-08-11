Feature: Laptops in cart

  # 1
  Scenario: Lenovo Laptop
    Given launch chrome browser
    When open scanmalta page
    Then verify that the logo present on page
    Then search for Lenovo laptop
    Then add the product to your shopping cart
    Then assert that the item has been added to your cart
    Then the product pricing matches the one listed in the single product page view.
    And close browser

    # 2
  Scenario: Apple Macbook
    Given launch chrome browser2
    When open scanmalta page2
    Then verify that the logo present on page2
    Then search for Apple Macbook2
    Then add the products twice to your shopping cart2
    Then assert that the items have been added to your cart2
    Then assert the total price is correct2
    And close browser2