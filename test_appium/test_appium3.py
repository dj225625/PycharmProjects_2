from time import sleep

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = "true"

#不需要每次运行脚本  都要先关闭应用程序 再打开；页面在哪个页面 就继续操作；但是执行完以后不会关闭页面
desired_caps['dontStopAppOnReset'] = 'true'
#跳过设置等
desired_caps['skipDeviceInitialization']  = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#隐式等待 是全局的动态的  每次查到元素  每0.5秒查找1次  最多查找5秒
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
#直接等待 强制等待3秒
sleep(3)
#页面进行返回 和dontStopAppOnReset结合使用
driver.back()
driver.back()
driver.quit()
