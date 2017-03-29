
## 0. Django文档

[http://python.usyiyi.cn/django/index.html](http://python.usyiyi.cn/django/index.html)

## 1. Django 和IntelliJ IDEA

### 1.1 IDEA无法提示models.Model子类的所有方法
在项目中需要添加 Django模块

![1_django_module_set.png](images/1_django_module_set.png)

效果：

![2_django_module_check.png](images/2_django_module_check.png)


### 1.2  IDEA无法显示templates的tag信息以及自动补全

修改Project目录下的ProjectName.xml文件添加如下：

```
  <component name="TemplatesService">
    <option name="TEMPLATE_CONFIGURATION" value="Django" />
    <option name="TEMPLATE_FOLDERS">
      <list>
        <option value="$MODULE_DIR$/templates" />
      </list>
    </option>
  </component>
```

重启IDEA即可

## 2. Django如何测试View
+ [http://python.usyiyi.cn/django/index.html](http://python.usyiyi.cn/django/index.html)
+ [http://www.dougalmatthews.com/2010/Jan/20/testing-your-first-django-app/](http://www.dougalmatthews.com/2010/Jan/20/testing-your-first-django-app/)
