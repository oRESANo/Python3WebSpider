from lxml import etree

if __name__ == '__main__':
    h=etree.parse('/media/caoxiangxing/6T/Python3WebSpider/Code/auth_code/gee_test.html',etree.HTMLParser())
    g=etree.parse('/media/caoxiangxing/6T/Python3WebSpider/Code/auth_code/html_test.xml',etree.HTMLParser())
    # result=etree.tostring(h)   #解析成字节
    # result = h.xpath('//*[type=password]')
    result = []
    # result.append(g.xpath('//ul'))
    # result.append(g.xpath('//li'))
    # result.append(g.xpath('//li/b[@href="link2.html"]/../@class'))
    # result.append(g.xpath('//li/b'))
    result.append(h.xpath('//input[@placeholder="请输入邮箱"]'))
    result.append(h.xpath('//span[@class="geetest-icons"]/text()'))
    # result.append(g.xpath('li'))
    # result.append(g.xpath('//li'))
    for r in result:
        print(r)