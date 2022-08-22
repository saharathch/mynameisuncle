class UncleA:
    """
    คลาสนี้แสดงตัวอย่างเป็นข้อมูลที่เกี่ยวข้องกับการทำแพ็คเก็จ
    """
    def __init__(self):
        self.name = 'คุณเอ'
        self.page = 'https://www.ship4uapp.com'

    def show_name(self):
        print(f'สวัสดีฉันชื่อ{self.name}')

    def show_youtube(self):
        print('https://www.youtube.com/UncleEngineer')

    def about(self):
        text = """
        สวัสดีครับ ผมชื่อคุณสหรัฐ เป็นผู้ทดสอบโปรแกรมไพทอน  
        """
        print(text)

if __name__ == '__main__':
    uncle = UncleA()
    uncle.show_name()
    uncle.show_youtube()
    uncle.about()

