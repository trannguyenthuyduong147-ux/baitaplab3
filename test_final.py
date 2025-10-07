 
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginForm(unittest.TestCase):
    """Test cases cho Login Form"""
    
    @classmethod
    def setUpClass(cls):
        print("\n" + "="*70)
        print("BẮT ĐẦU CHẠY TEST LOGIN FORM - LAB 03")
        print("="*70)
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
         
        html_file = os.path.join(current_dir, "login.html")
        self.url = f"file:///{html_file.replace(os.sep, '/')}"
        
        self.driver.get(self.url)
        
        self.wait = WebDriverWait(self.driver, 5)  
    
    def tearDown(self):
        time.sleep(1.5)
        self.driver.quit()
    
  
    def test_01_login_success(self):
        print("\n[TEST 1] Đăng nhập thành công")
        self.driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
        self.driver.find_element(By.ID, "btnLogin").click()
        
      
        success_msg = self.wait.until(
            EC.visibility_of_element_located((By.ID, "msg-success"))
        )
        self.assertTrue(success_msg.is_displayed(), "Message thành công không hiển thị")
        print(" ✓ Hiển thị message: 'Login success!'")
        
        
        self.wait.until(EC.url_contains("dashboard.html"))
        self.assertIn("dashboard.html", self.driver.current_url)
        print(" ✓ Đã chuyển hướng đến trang dashboard.html")
        
        print("✅ PASS: Đăng nhập thành công!")
    
     
    def test_02_login_wrong_password(self):
        print("\n[TEST 2] Đăng nhập với password sai")
        self.driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.ID, "password").send_keys("wrongpassword123")
        self.driver.find_element(By.ID, "btnLogin").click()
        
        error_msg = self.wait.until(EC.visibility_of_element_located((By.ID, "msg-error")))
        self.assertIn("Invalid credentials", error_msg.text)
        print(f" ✓ Hiển thị lỗi: '{error_msg.text}'")
        
        print("✅ PASS: Hiển thị lỗi khi sai password!")
    
    def test_03_empty_fields(self):
        print("\n[TEST 3] Bỏ trống các trường bắt buộc")
        self.driver.find_element(By.ID, "btnLogin").click()
        
        error_msg = self.wait.until(EC.visibility_of_element_located((By.ID, "msg-error")))
        self.assertIn("Please fill all required fields", error_msg.text)
        print(f" ✓ Hiển thị validation: '{error_msg.text}'")
        
        print("✅ PASS: Validation hoạt động đúng!")
        
    def test_04_forgot_password_link(self):
        print("\n[TEST 4] Kiểm tra link Forgot Password")
        forgot_link = self.driver.find_element(By.ID, "linkForgot")
        self.assertTrue(forgot_link.is_displayed() and forgot_link.is_enabled())
        print(" ✓ Link 'Forgot password?' hiển thị và có thể click.")
        
        print("✅ PASS: Link Forgot Password hoạt động!")
        
    def test_05_signup_link(self):
        print("\n[TEST 5] Kiểm tra link Sign Up")
        signup_link = self.driver.find_element(By.ID, "linkSignup")
        self.assertTrue(signup_link.is_displayed() and signup_link.is_enabled())
        print(" ✓ Link 'SIGN UP' hiển thị và có thể click.")
        
        print("✅ PASS: Link SIGN UP hoạt động!")

    def test_06_social_login_buttons(self):
        print("\n[TEST 6] Kiểm tra các nút Social Login")
        buttons = ["btnFacebook", "btnTwitter", "btnGoogle"]
        for btn_id in buttons:
            button = self.driver.find_element(By.ID, btn_id)
            self.assertTrue(button.is_displayed() and button.is_enabled(), f"Nút {btn_id} có vấn đề.")
            print(f" ✓ Nút {btn_id} hiển thị và có thể click.")
            
        print("✅ PASS: Social login buttons đầy đủ!")

    @classmethod
    def tearDownClass(cls):
        print("\n" + "="*70)
        print("HOÀN THÀNH TẤT CẢ TEST CASES")
        print("="*70 + "\n")

 
if __name__ == "__main__":
    unittest.main(verbosity=2)