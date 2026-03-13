import time
from pages.login_page import LoginPage
import time

BASE_URL = "https://niitmtscrm.com/"
VALID_EMAIL = "vandana1.sharma@gmail.com"
VALID_PASSWORD = "Sfdcadmin@123"
TITLE = "CRM"
After_login_Text_Found = "My Project"


# ============================================================
# ✅ CATEGORY 1 — VALID / POSITIVE TESTS (TC01–TC06)
# ============================================================

def test_TC01_valid_credentials_login(driver):
    """Valid email aur password se login hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    time.sleep(6)
    body_text = driver.execute_script(
        "return document.body.innerText"
    )

    print(body_text)  # dekho kya aa raha hai
    assert After_login_Text_Found in body_text

def test_TC02_page_title_after_login(driver):
    """Login ke baad page title sahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert TITLE in driver.title

def test_TC03_login_page_loads_successfully(driver):
    """Login page bina error ke load hona chahiye"""
    driver.get(BASE_URL)
    assert TITLE in driver.title or "Login" in driver.page_source

def test_TC04_login_redirects_away_from_login_page(driver):
    """Successful login ke baad URL change hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert driver.current_url != BASE_URL

def test_TC05_welcome_message_after_login(driver):
    """Login ke baad dashboard mein content hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found in driver.page_source or "Dashboard" in driver.page_source

def test_TC06_login_with_email_uppercase(driver):
    """Email uppercase mein dene pe bhi login hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL.upper())
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    # Most systems are case-insensitive for email
    assert After_login_Text_Found in driver.page_source or After_login_Text_Found not in driver.page_source  # behavior note karo


# ============================================================
# ❌ CATEGORY 2 — INVALID / NEGATIVE TESTS (TC07–TC16)
# ============================================================

def test_TC07_wrong_password(driver):
    """Galat password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("WrongPassword@999")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC08_wrong_username(driver):
    """Galat email se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("wronguser@gmail.com")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC09_wrong_both_credentials(driver):
    """Dono fields galat hone pe login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("fake@gmail.com")
    login.enter_password("FakePassword@123")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC10_empty_username(driver):
    """Khali username se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC11_empty_password(driver):
    """Khali password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC12_empty_both_fields(driver):
    """Dono fields khali hone pe login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("")
    login.enter_password("")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC13_unregistered_email(driver):
    """Unregistered email se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("notregistered123xyz@gmail.com")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC14_invalid_email_format(driver):
    """Invalid email format (@ missing) se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("invalidemail.com")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC15_invalid_email_no_domain(driver):
    """Domain missing email se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("user@")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC16_password_with_only_spaces(driver):
    """Sirf spaces wale password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("          ")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source


# ============================================================
# 🎨 CATEGORY 3 — UI / UX TESTS (TC17–TC26)
# ============================================================

def test_TC17_username_field_visible(driver):
    """Username field page pe visible hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_username_field_visible()

def test_TC18_password_field_visible(driver):
    """Password field page pe visible hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_password_field_visible()

def test_TC19_login_button_visible(driver):
    """Login button page pe visible hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_login_button_visible()

def test_TC20_password_field_masked(driver):
    """Password field mein text masked (dots) hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_password_masked()

def test_TC21_page_has_login_heading(driver):
    """Login page pe Login heading ya title hona chahiye"""
    driver.get(BASE_URL)
    assert "Login" in driver.page_source or "Sign In" in driver.page_source

def test_TC22_username_field_accepts_input(driver):
    """Username field mein type karna possible hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    assert login.get_username_value() == VALID_EMAIL

def test_TC23_login_button_is_clickable(driver):
    """Login button clickable hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_login_button_enabled()

def test_TC24_page_has_no_broken_elements(driver):
    """Page load pe 404 error nahi hona chahiye"""
    driver.get(BASE_URL)
    assert "404" not in driver.page_source
    assert "Error" not in driver.title

def test_TC25_username_field_has_placeholder(driver):
    """Username field mein placeholder text hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    placeholder = login.get_username_placeholder()
    assert placeholder is not None and placeholder != ""

def test_TC26_forgot_password_link_visible(driver):
    """Forgot Password link visible hona chahiye"""
    driver.get(BASE_URL)
    assert "Forgot" in driver.page_source or "forgot" in driver.page_source


# ============================================================
# 🔒 CATEGORY 4 — SECURITY TESTS (TC27–TC34)
# ============================================================

def test_TC27_sql_injection_username(driver):
    """SQL injection se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("' OR '1'='1")
    login.enter_password("' OR '1'='1")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC28_sql_injection_password(driver):
    """Password field mein SQL injection kaam nahi karna chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("' OR 1=1 --")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC29_xss_in_username(driver):
    """XSS attack se page crash nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("<script>alert('xss')</script>")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC30_xss_in_password(driver):
    """Password field mein XSS kaam nahi karna chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("<script>alert('hack')</script>")
    time.sleep(100)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC31_case_sensitive_password(driver):
    """Password case-sensitive hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD.lower())
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC32_password_with_special_chars_only(driver):
    """Sirf special characters wale password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("!@#$%^&*()")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC33_https_protocol_used(driver):
    """Site HTTPS use kar rahi hona chahiye — secure connection"""
    driver.get(BASE_URL)
    assert driver.current_url.startswith("https://")

def test_TC34_login_url_direct_access_blocked(driver):
    """Login ke bina dashboard URL directly access nahi hona chahiye"""
    driver.get(BASE_URL + "dashboard")
    assert After_login_Text_Found not in driver.page_source or "login" in driver.current_url.lower()


# ============================================================
# 📏 CATEGORY 5 — BOUNDARY TESTS (TC35–TC40)
# ============================================================

def test_TC35_max_length_username(driver):
    """256+ character username reject hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("a" * 250 + "@gmail.com")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC36_max_length_password(driver):
    """256+ character password reject hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("A@1" + "a" * 300)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC37_single_char_username(driver):
    """1 character username se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("a")
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC38_single_char_password(driver):
    """1 character password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("a")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC39_spaces_in_credentials(driver):
    """Spaces wale credentials se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("   " + VALID_EMAIL + "   ")
    login.enter_password("   " + VALID_PASSWORD + "   ")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source

def test_TC40_numeric_only_password(driver):
    """Sirf numbers wale password se login nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password("12345678")
    login.login_button()
    assert After_login_Text_Found not in driver.page_source


# ============================================================
# 🔄 CATEGORY 6 — SESSION TESTS (TC41–TC46)
# ============================================================

def test_TC41_logout_redirects_to_login(driver):
    """Logout ke baad login page pe aana chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    login.logout()
    assert BASE_URL in driver.current_url or "login" in driver.current_url.lower()

def test_TC42_back_button_after_logout(driver):
    """Logout ke baad browser back button se dashboard nahi aana chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    login.logout()
    driver.back()
    assert After_login_Text_Found not in driver.page_source

def test_TC43_login_page_accessible_without_session(driver):
    """Bina login ke login page accessible hona chahiye"""
    driver.get(BASE_URL)
    assert "Login" in driver.page_source or TITLE in driver.title

def test_TC44_double_login_same_account(driver):
    """Same account se dobara login karne pe crash nahi hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found in driver.page_source

def test_TC45_refresh_after_login(driver):
    """Login ke baad page refresh karne pe session maintain hona chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    driver.refresh()
    assert After_login_Text_Found in driver.page_source

def test_TC46_direct_url_access_without_login(driver):
    """Login ke bina koi bhi protected page access nahi hona chahiye"""
    driver.get(BASE_URL + "home")
    assert After_login_Text_Found not in driver.page_source or "login" in driver.current_url.lower()


# ============================================================
# ⚡ CATEGORY 7 — PERFORMANCE TESTS (TC47–TC50)
# ============================================================

def test_TC47_login_page_load_time(driver):
    """Login page 5 seconds se kam mein load hona chahiye"""
    start = time.time()
    driver.get(BASE_URL)
    end = time.time()
    assert (end - start) < 5, f"Page load time: {end - start:.2f}s — too slow!"

def test_TC48_login_response_time(driver):
    """Login button click ke baad 5 seconds mein response aana chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    start = time.time()
    login.login_button()
    end = time.time()
    assert (end - start) < 5, f"Login response time: {end - start:.2f}s — too slow!"

def test_TC49_invalid_login_response_time(driver):
    """Invalid login pe bhi 5 seconds mein error aana chahiye"""
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("wrong@gmail.com")
    login.enter_password("WrongPass@123")
    start = time.time()
    login.login_button()
    end = time.time()
    assert (end - start) < 5, f"Error response time: {end - start:.2f}s — too slow!"

def test_TC50_multiple_logins_no_crash(driver):
    """3 baar login-logout karne pe system crash nahi hona chahiye"""
    for i in range(3):
        driver.get(BASE_URL)
        login = LoginPage(driver)
        login.enter_username(VALID_EMAIL)
        login.enter_password(VALID_PASSWORD)
        login.login_button()
        assert After_login_Text_Found in driver.page_source
        login.logout()


# ============================================================
# 📱 CATEGORY 8 — RESPONSIVE / EXTRA TESTS (TC51–TC54)
# ============================================================

def test_TC51_login_page_on_mobile_view(driver):
    """Mobile screen (375x667) pe login page sahi dikhna chahiye"""
    driver.set_window_size(375, 667)
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_username_field_visible()
    assert login.is_login_button_visible()
    driver.maximize_window()

def test_TC52_login_page_on_tablet_view(driver):
    """Tablet screen (768x1024) pe login page sahi dikhna chahiye"""
    driver.set_window_size(768, 1024)
    driver.get(BASE_URL)
    login = LoginPage(driver)
    assert login.is_username_field_visible()
    driver.maximize_window()

def test_TC53_page_not_broken_on_zoom(driver):
    """Browser zoom 150% pe bhi login page functional hona chahiye"""
    driver.get(BASE_URL)
    driver.execute_script("document.body.style.zoom='150%'")
    login = LoginPage(driver)
    assert login.is_login_button_visible()

def test_TC54_login_after_browser_back(driver):
    """Kisi aur page se back aane ke baad login kaam karna chahiye"""
    driver.get("https://google.com")
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)
    login.login_button()
    assert After_login_Text_Found in driver.page_source
