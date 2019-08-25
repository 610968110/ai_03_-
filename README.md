## xPath

@是属性，()是方法

| 路径表达式                             | 结果                                                  |
| -------------------------------------- | ----------------------------------------------------- |
| /bookstore/book                        | 选取属于bookstore标签的第一个book元素                 |
| /bookstore/a//text()                   | 选取属于bookstore标签下的a标签下的所有标签的text      |
| /bookstorebook[last() - 1]             | 选取属于bookstore标签的倒数第二个book元素             |
| /bookstorebook[position() < 3]         | 选取属于bookstore标签的前二个book元素,position从0开始 |
| //title[@class]                        | 选取所有class属性的title                              |
| //title[@class = "box"]                | 选取所有class属性为box的title                         |
| /bookstorebook[price > 35]             | 取属于bookstore标签且price大于35的book元素            |
| //ul/li/a/@href                        | 选取所有ul/li下的a标签的href属性                      |
| /bookstore/book[text() = "白雪公主"]   | 选取bookstore下所有text为白雪公主的book元素           |
| /bookstore/*                           | 选取属于bookstore标签的所有元素                       |
| //title@*                              | 选取所有带有title属性的元素                           |
| html/node()/meta/@*                    | 选取html下任意节点下meta节点下的所有属性              |
| \|                                     | 或，两个表达式之间使用                                |
| .     ..                               | .当前节点，..父节点，../..爷节点                      |
| /bookstore/book[contacts(@class, "i")] | 选取所有class包含i属性的book元素                      |

## lxml

- lxml 可以自动修正html 代码，比如将不完整的标签自动补全，可能出错哦

- 导入lxml的 etree库

    fromlxml import etree

- 利用etree.HTML，将字符串转化为Element对象

- Element对象具有xpath的方法

    html= etree.HTML(text) 

    print(etree.tostring(html).decode())

    result = etree.xpath("表达式")  # 返回一个列表

   

## selenium

