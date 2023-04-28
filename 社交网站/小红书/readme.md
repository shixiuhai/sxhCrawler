## 小红书逆向
* 运行的主代码是xiaohongshu.py

### 功能说明

* 获取接口调用里面需要传入的 web_session,x-s,x-t

### 系统说明

* 采用了requests实现请求模拟

* 采用了PyexecJs模拟js运算

* 安装部署了nodejs服务

### 补充说明
* 主要扣下来了网页的sign函数
* nodejs里自执行函数执行可能存在部分问题
* 浏览器网页变量可以console打印直接右击复制，或者 变量名.copy复制到剪切版
* 这里js补环境只用到了window
* 常用的js补环境有  navigator,window,location,document 
* 常用补nodejs环境 https://juejin.cn/post/7175071596976013369

