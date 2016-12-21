
# coding: utf-8

# In[66]:

class New_client():

    def __init__(self, first_name, last_name, country, city, address, index):
        if not (type(first_name)==str and type(last_name)==str and type(country)==str and type(city)==str and type(address)==str and type(index)==int) :
            print('err_incorrect_data_type')
            return None
        elif not(100000 <= index <= 1000000):
            print('err_incorrect_index_length')
            return None
        self.first_name, self.last_name, self.country, self.city, self.address, self.index = (
            first_name, last_name, country, city, address, index)
        self.smth = None
        
        file = open('clients.txt', 'a')
        file.write('{}|{}|{}|{}|{}|{}'.format(self.first_name, self.last_name, self.country, self.city, self.address, self.index))
        file.write("\n")
        file.close()

    def get_client_info(self):

        self.client_info = {'first_name': self.first_name,
                       'second_name': self.second_name,
                       'country': self.country,
                       'city': self.city,
                       'address': self.address,
                       'index': self.index}

        return self.client_info
    
    def output_info(txt):
        print('|{:<15}|{:<20}|{:<13}|{:<25}|{:<25}|{:<7}'.format("Name","Last Name","Country","City","Address","Index"))
        txt = open(txt, 'r')
        for line in txt.readlines():
            l = line[:len(line)-1]
            L = l.split('|')
            print('|{:<15}|{:<20}|{:<13}|{:<25}|{:<25}|{:<7}'.format(L[0],L[1],L[2],L[3],L[4],L[5]))
            
    @property
    def name(self):
        return ('{} {}'.format(self.first_name, self.last_name))

    @property
    def location(self):
        return ('{}, {}, {}, {}'.format(self.address, self.city, self.country, self.index))
        
    @property
    def sex(self):
        return self.smth
    
    @sex.setter
    def sex(self, var):
        if (type(var) != str):
            print('err_incorrect_data_type')
        elif (var == 'man' or var == 'woman'):
            self.smth = var
        else:
            print('Chose your sex!')
            
    @sex.deleter
    def sex(self):
        del self.smth


client = New_client('Konina', 'Konskaya', 'Keklandia', 'Kekchik', 'Keskaya, 35', 228777)
New_client.output_info('clients.txt')
print(client.location)
print(client.name)
client.sex = 'man'
print(client.sex)
del client.sex

