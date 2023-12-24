import xml.dom.minidom
def main():
    path ="d:/python nâng cao/chuong_2/baitap_chuong2/bai2.3.xml"
    # Sử dụng hàm parse() để đọc và phân tích file và chuyển đổi thành đối tượng 'doc'
    doc =xml.dom.minidom.parse(path)
    # In ra In ra tên của node gốc và tag name của node đầu tiên trong file .xml
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    # Lấy danh sách các thẻ XML từ tài liệu và in từng thẻ
    expertise= doc.getElementsByTagName("expertise")
    print("%d expertise: " %expertise.length)
    for skill in expertise :
        print(skill.getAttribute("name"))

if __name__=='__main__':
    main()