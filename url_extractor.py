__author__ = 'andreychernyshev'

class UrlExtractor:
    link_marker = '<a href="'
    link_end_marker = '">'
    current_position = 0

    def getNextLink(self, page):
        next_start = page.find(self.link_marker, self.current_position)
        next_end = page.find(self.link_end_marker, next_start + len(self.link_marker))
        self.current_position = next_end
        if next_start == -1:
            return ''
        return page[next_start + len(self.link_marker): next_end]

    def getLinks(self, page):
        url = 'empty'
        links = []
        while url != '':
            url = self.getNextLink(page)
            if url != '':
                links.append(url)

        return links

page = 'some page <a href="http://google.com">Google</a> <a href="http://ya.ru">Yandex</a>'
a = UrlExtractor()

print(a.getLinks(page))