class BaiSi:
    def __init__(self, username, create_time, content, img_url):
        self.username = username
        self.create_time = create_time
        self.content = content
        self.img_url = img_url

    def display(self):
        print(self.username, self.create_time, self.content, self.img_url)
