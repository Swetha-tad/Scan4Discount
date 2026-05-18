import configparser

config = configparser.RawConfigParser()
config.read(r'.\Configurations\config.ini', encoding='utf-8-sig')

class ReadConfig:
    # website info
    @staticmethod
    def get_ApplicationURL():
        URL = config.get('website info','baseURL')
        return URL

    @staticmethod
    def get_valid_email():
        valid_email = config.get('website info', 'valid email')
        return valid_email

    @staticmethod
    def get_Invalid_email():
        Invalid_email = config.get('website info', 'invalid email')
        return Invalid_email

    @staticmethod
    def get_FeaturesURL():
        features_url = config.get('website info', 'features_url')
        return features_url

    @staticmethod
    def get_PricingURL():
        pricing_url = config.get('website info', 'pricing_url')
        return pricing_url

    @staticmethod
    def get_button_pricing1():
        button_pricing1 = config.get('website info', 'button_pricing1')
        return button_pricing1

    @staticmethod
    def get_button_pricing2():
        button_pricing2 = config.get('website info', 'button_pricing2')
        return button_pricing2

    @staticmethod
    def get_BlogsURL():
        blogs_url = config.get('website info', 'blogs_url')
        return blogs_url

    @staticmethod
    def get_DocsURL():
        docs_url = config.get('website info', 'docs_url')
        return docs_url

    @staticmethod
    def get_FAQsURL():
        faqs_url = config.get('website info', 'faqs_url')
        return faqs_url

    @staticmethod
    def get_ContactUs_URL():
        contactus_url = config.get('website info', 'contactus_url')
        return contactus_url

    @staticmethod
    def get_signin_url():
        signin_url = config.get('website info', 'signin_page_url')
        return signin_url

    @staticmethod
    def get_signup_url():
        signup_url = config.get('website info', 'signup_page_url')
        return signup_url

    # register info

    @staticmethod
    def get_loginURL():
        loginURL = config.get('register info', 'loginURL')
        return loginURL

    @staticmethod
    def get_register_btn():
        register_btn = config.get('register info', 'register_btn')
        return register_btn

    @staticmethod
    def get_full_name():
        full_name = config.get('register info', 'full_name')
        return full_name

    @staticmethod
    def get_phone_number():
        phone_num = config.get('register info', 'phone_num')
        return phone_num

    @staticmethod
    def get_email_id():
        email_id = config.get('register info', 'email_id')
        return email_id

    @staticmethod
    def get_verify_btn():
        verify_btn = config.get('register info', 'verify_btn')
        return verify_btn

    @staticmethod
    def get_cancel_btn():
        cancel_btn = config.get('register info', 'cancel_btn')
        return cancel_btn

    @staticmethod
    def get_upload_btn():
        upload_btn = config.get('register info', 'upload_btn')
        return upload_btn

    @staticmethod
    def get_submit_btn():
        submit_btn = config.get('register info', 'submit_btn')
        return submit_btn

    @staticmethod
    def get_plan_card1():
        plan_card1 = config.get('register info', 'plan_card1')
        return plan_card1

    @staticmethod
    def get_plan_card2():
        plan_card2 = config.get('register info', 'plan_card2')
        return plan_card2

    @staticmethod
    def get_plan_card3():
        plan_card3 = config.get('register info', 'plan_card3')
        return plan_card3

    @staticmethod
    def get_proceed_btn():
        proceed_btn = config.get('register info', 'proceed_btn')
        return proceed_btn

    @staticmethod
    def get_back_btn():
        back_btn = config.get('register info', 'back_btn')
        return back_btn

    # login info


    @staticmethod
    def get_login_email():
        login_email = config.get('login info', 'login_email')
        return login_email

    @staticmethod
    def get_login_pass():
        login_pass = config.get('login info', 'login_pass')
        return login_pass

    @staticmethod
    def get_owner_id():
        owner_id = config.get('login info', 'owner_id')
        return owner_id

    @staticmethod
    def get_forgot_pass_link():
        forgot_pass_link = config.get('login info', 'forgot_pass_link')
        return forgot_pass_link

    @staticmethod
    def get_email_field():
        email_field = config.get('login info', 'email_field')
        return email_field

    @staticmethod
    def get_send_link_button():
        send_button = config.get('login info', 'send_link')
        return send_button

    @staticmethod
    def get_cancel_link_button():
        cancel_button = config.get('login info', 'cancel_link')
        return cancel_button

    @staticmethod
    def get_login_button():
        login_button = config.get('login info', 'login_btn')
        return login_button

    @staticmethod
    def get_logout_button():
        logout_button = config.get('login info', 'logout_btn')
        return logout_button

    @staticmethod
    def get_confirm_logout_button():
        confirm_logout_button = config.get('login info', 'confirm_logout')
        return confirm_logout_button

    @staticmethod
    def get_cancel_logout_button():
        cancel_logout_button = config.get('login info', 'cancel_logout')
        return cancel_logout_button

    #dashboard info

    @staticmethod
    def get_dashboard_url():
        dashboardURL = config.get('dashboard info', 'dashboardURL')
        return dashboardURL

    @staticmethod
    def get_mode_btn():
        mode_btn = config.get('dashboard info', 'mode_btn')
        return mode_btn

    @staticmethod
    def get_guide_btn():
        guide_btn = config.get('dashboard info', 'guide_btn')
        return guide_btn

    @staticmethod
    def get_overview_page():
        overview_page = config.get('dashboard info', 'overview_btn')
        return overview_page

    @staticmethod
    def get_customers_page():
        customers_page = config.get('dashboard info', 'customers_btn')
        return customers_page

    @staticmethod
    def get_stores_page():
        stores_page = config.get('dashboard info', 'stores_btn')
        return stores_page

    @staticmethod
    def get_discounts_page():
        discounts_page = config.get('dashboard info', 'discounts_btn')
        return discounts_page

    @staticmethod
    def get_rewards_page():
        rewards_page = config.get('dashboard info', 'rewards_btn')
        return rewards_page

    @staticmethod
    def get_coupons_page():
        coupons_page = config.get('dashboard info', 'coupons_btn')
        return coupons_page

    @staticmethod
    def get_activity_page():
        activity_page = config.get('dashboard info', 'activity_btn')
        return activity_page


    # stores info
    @staticmethod
    def get_stores_URL():
        stores_URL = config.get('stores info', 'storesURL')
        return stores_URL

    @staticmethod
    def get_add_store_btn():
        add_store_btn = config.get('stores info', 'add_store_btn')
        return add_store_btn

    @staticmethod
    def get_store_name():
        store_name = config.get('stores info', 'store_name')
        return store_name

    @staticmethod
    def get_store_code():
        store_code = config.get('stores info', 'store_code')
        return store_code

    @staticmethod
    def get_store_status():
        store_status = config.get('stores info', 'store_status')
        return store_status

    @staticmethod
    def get_store_address():
        store_address = config.get('stores info', 'store_address')
        return store_address

    @staticmethod
    def get_store_city():
        store_city = config.get('stores info', 'store_city')
        return store_city

    @staticmethod
    def get_store_state():
        store_state = config.get('stores info', 'store_state')
        return store_state

    @staticmethod
    def get_store_zipcode():
        store_zipcode = config.get('stores info', 'store_zipcode')
        return store_zipcode

    @staticmethod
    def get_owner_phone():
        owner_phone = config.get('stores info', 'owner_phone')
        return owner_phone

    @staticmethod
    def get_owner_email():
        owner_email = config.get('stores info', 'owner_email')
        return owner_email

    @staticmethod
    def get_create_store_btn():
        create_store_btn = config.get('stores info', 'create_store_btn')
        return create_store_btn

    @staticmethod
    def get_cancel_store_btn():
        cancel_store_btn = config.get('stores info', 'cancel_store_btn')
        return cancel_store_btn

    @staticmethod
    def get_store_search():
        store_search = config.get('stores info', 'store_search')
        return store_search

    @staticmethod
    def get_store_filter():
        store_filter = config.get('stores info', 'store_filter')
        return store_filter

    @staticmethod
    def get_store_actions():
        store_actions = config.get('stores info', 'store_actions_btn')
        return store_actions

    @staticmethod
    def get_store_view_btn():
        store_view_btn = config.get('stores info', 'store_view_btn')
        return store_view_btn

    @staticmethod
    def get_store_edit_btn():
        store_edit_btn = config.get('stores info', 'store_edit_btn')
        return store_edit_btn

    @staticmethod
    def get_store_deactivate_btn():
        store_deactivate_btn = config.get('stores info', 'store_deactivate_btn')
        return store_deactivate_btn

    @staticmethod
    def get_store_delete_btn():
        store_delete_btn = config.get('stores info', 'store_delete_btn')
        return store_delete_btn

    @staticmethod
    def get_view_qrcode_btn():
        view_qrcode_btn = config.get('stores info', 'view_qrcode_btn')
        return view_qrcode_btn




















