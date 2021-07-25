class Login:

    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self, driver):
        self.driver=driver