# ActionChains方法列表，案例：test_ActionChains.py

链接：https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html?highlight=actionchains
1 click(on_element=None) ——单击鼠标左键 2 click_and_hold(on_element=None) ——点击鼠标左键，不松开 3 context_click(on_element=None)
——点击鼠标右键 4 double_click(on_element=None) ——双击鼠标左键 5 drag_and_drop(source, target) ——拖拽到某个元素然后松开 6
drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开 7 key_down(value, element=None) ——按下某个键盘上的键 8 key_up(
value, element=None) ——松开某个键 9 move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标 10 move_to_element(to_element)
——鼠标移动到某个元素 11 move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置 12 perform()
——执行链中的所有动作 13 release(on_element=None) ——在某个元素位置松开鼠标左键 14 send_keys(*keys_to_send) ——发送某个键到当前焦点的元素 15
send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素

# 动作链接ActionChains

一.执行原理 调用ActionChains的方法时，不会立即执行，而是将所有的操作，按顺序存放在一个队列里，当你调用 perform()方法时，队列中的事件会依次执行 二.基本用法 1.生成一个动作action=ActionChains(
driver)
2.动作添加方法1action.方法1 3.动作添加方法2action.方法2 4.调用perform()方法执行（action.perform()）

# ActionChains两种写法

一.链式写法： ActionChains(driver).move_to_element(element).click(element).perform()
二.分布写法： action=ActionChains(driver)
action.move_to_element(element)
action.click(element)
action.perform()

# TouchAction方法，案例：test_TouchAction.py

链接：https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.touch_actions.html
一.类似于ActionChains，ActionChains只是针对PC端程序鼠标模拟的一系列操作，对于H5页面操作是无效的，
TouchAction可以对H5页面操作，通过TouchAction可以实现点击，滑动，拖拽，多点触控，以及模拟手势的各种操作 二.手势控制 tap---在指定元素上敲击 double_tap---在指定元素上双击
tap_and_hold---在指定元素上点击但不释放 move---手势移动指定偏移（未释放） release---释放手势 scroll---手势点击并滚动
scroll_from_element---从某个元素位置开始手势点击并滚动（向下滑动为附属，向上滑动为正数） long_press---长按元素 flick---手势滑动
flick_element---从某个元素位置开始手势滑动（向上滑动为负数，向下滑动为正数） Perform---执行

# 表单定义，案例：test_form.py

一.什么是表单？ 表单是一个包含表单元素的区域 表单元素是允许用户在表单中（比如：文本域、下拉列表、单选框、复选框等等）输入信息的元素 表单使用表单标签（<form>）定义。例如：<from><input/></from>
二.操作表单元素步骤： 首先要定位到表单元素 然后去操作元素（清空、输入或者点击等）
