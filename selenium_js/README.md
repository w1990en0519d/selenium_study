# js的处理，案例：test_js.py

1.selenium能够执行js，这使得selenium拥有更为强大的能力。既然能执行js，那么jsneng 做的事，selenium应该大部分也能做  
2.直接使用js操作也买你，能够解决很多click()bu不生效的问题   
3.页面滚动到底部，顶部 4.处理富文本、时间控件的输入

# selenium中如何调用js

一.例如js代码：

* window.alert("selenium弹窗测试")
* a=document.getElementById("kw").value
* document.title
* JSON.stringify(performance.timing)
* document.documentElement.scrollTop=10000

二.selenium如何调用js，selenium提供了一个内置的方法execute_script()

* driver.execute_script("window.alert("selenium弹窗测试")")
* driver.execute_script("a=document.getElementById("kw").value;window.alert(a)")

三.如何返回呢？

* driver.execute_script("return document.getElementById("kw").value")

四.总结

* execute_script:执行js
* return:可以返回js的返回结果
* execute_script:arguments传参

# js处理时间控件

一.大部分时间控件都是readonly属性，需要手动去选择对应的时间，手工测试中很容易做到，自动化 中对控件的操作可以使用js来操作  
二.处理时间控件思路：

* 1.要取消日期的readonly属性
* 2.给value赋值
* 3.写js代码来实现如上的1，2两点，再webdriver对js进行处理
