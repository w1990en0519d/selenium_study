# 多窗口切换，案例：test_window.py

多窗口处理： 点击某些链接，会重新打开一个窗口，对于这种情况，想在新页面上操作，就得先切换窗口了 获取窗口的唯一标识用句柄表示，所以只需要切换句柄，就可以在多个页面灵活操作 多窗口处理流程：
1.先获取到当前的窗口句柄（driver.current_window_handle） 2.再获取到所有的窗口句柄（driver.window_handles）
3.判断是否想要操作的窗口，如果是，就可以对窗口进行操作，如果不是，跳转到另一个窗口 ，对另一个窗口进行操作（driver.switch_to_window）

# frame介绍

一：什么是frame？ frame是html中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页面。 基于html的框架，又分为垂直框架和水平框架（cols，rows） 二：frame分类
1.frame标签包含frameset、frame、iframe三种 2.frameset和普通的标签一样，不会影响正常的定位，可以使用index、id、name、 webelement任意一种方式定位frame
3.而frame与iframe对selenium定位而言是一样的。selenium有一组方法对frame进行操作

# 多frame切换,案例：test_frame.py

一：frame存在两种 1.一种是嵌套的 2.一种是未嵌套的 二：切换frame 1.driver.switch_to.frame() #根据元素id或者index切换frame
2.driver.switch_to_default_content()/driver.switch_to.default_content()#切换 到默认frame 3.driver.switch_to.parent_frame()
#切换到父级frame

# 处理未嵌套的iframe

1.driver.switch_to.frame("frame的id")
2.driver.switch_to.frame("frame-index")frame无ID的时候依据索引来处理，索引从 0开始driver.switch_to.frame（0）

# 处理嵌套的iframe

1.对于嵌套的先进入到iframe的父节点，再进到子节点，然后可以对子节点里面的对象 进行处理和操作 2.driver.switch_to.frame（"父节点"） 3.driver.switch_to.frame("子节点")

# selenium处理多浏览器

代码： browser = os.getenv("browser")
if browser == 'chrome':
self.driver = webdriver.Chrome()
elif browser== 'firefox':
self.driver = webdriver.Firefox()
else:
self.driver = webdriver.PhantomJS()

1.chrome，firefox，headless等浏览器的自动化支持 2.传不同参数来测试不同的浏览器，用来做浏览器兼容性测试 3.windows的话用set命令设置： set browser=chrome pytest xxx.py
4.mac和linux的命令运行： browser=chrome pytest xxx.py

