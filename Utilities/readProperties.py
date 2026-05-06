import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def get_ApplicationURL():
        URL = config.get('common info','baseURL')
        return URL

    @staticmethod
    def get_valid_email():
        valid_email = config.get('common info', 'valid email')
        return valid_email

    @staticmethod
    def get_Invalid_email():
        Invalid_email = config.get('common info', 'invalid email')
        return Invalid_email

    @staticmethod
    def get_FeaturesURL():
        features_url = config.get('common info', 'features_url')
        return features_url

    @staticmethod
    def get_PricingURL():
        pricing_url = config.get('common info', 'pricing_url')
        return pricing_url

    @staticmethod
    def get_button_pricing1():
        button_pricing1 = config.get('common info', 'button_pricing1')
        return button_pricing1

    @staticmethod
    def get_button_pricing2():
        button_pricing2 = config.get('common info', 'button_pricing2')
        return button_pricing2

    @staticmethod
    def get_BlogsURL():
        blogs_url = config.get('common info', 'blogs_url')
        return blogs_url

    @staticmethod
    def get_DocsURL():
        docs_url = config.get('common info', 'docs_url')
        return docs_url

    @staticmethod
    def get_FAQsURL():
        faqs_url = config.get('common info', 'faqs_url')
        return faqs_url

    @staticmethod
    def get_ContactUs_URL():
        contactus_url = config.get('common info', 'contactus_url')
        return contactus_url

    @staticmethod
    def get_signin_url():
        signin_url = config.get('common info', 'signin_page_url')
        return signin_url

    @staticmethod
    def get_signup_url():
        signup_url = config.get('common info', 'signup_page_url')
        return signup_url









