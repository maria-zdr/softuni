class Website:
    def __init__(self, host, domain):
        self.host = host
        self.domain = domain
        self.queries = []

    def add_queries(self, queries):
        self.queries.append(queries)


while True:
    data = input()
    if data == 'end':
        break

    list_data = data.split(' | ')
    site = Website(list_data[0], list_data[1])

    if len(list_data) == 3:
        for item in list_data[2].split(','):
           site.add_queries('[' + item + ']')

    if site.queries:
        print('https://www.{}.{}/query?={}'.format(site.host, site.domain, '&'.join(site.queries)))
    else:
        print('https://www.{}.{}'.format(site.host, site.domain))