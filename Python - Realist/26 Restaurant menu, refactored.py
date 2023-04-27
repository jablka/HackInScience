class Dish:   
    _dish_types = {'starter', 'dish', 'dessert'}

    def __init__(self, name, preparation_time, dish_type):
                                             # dish_type:list['starter', 'dish', 'dessert'] # ? skúsiť
        self.name = name
        
        self.preparation_time = preparation_time # implement comparing

        if (dish_type in Dish._dish_types):
            self.dish_type = dish_type # starter, dish, dessert
        else: 
            raise TypeError("Only: 'starter', 'dish', 'dessert' values allowed as a dish_type ")
    
    def __eq__(self, other):
        return self.preparation_time == other.preparation_time

    def __lt__(self, other):
        return self.preparation_time < other.preparation_time
    
    def __gt__(self,other):
        return self.preparation_time > other.preparation_time
    
    def __le__(self,other):
        return self.preparation_time <= other.preparation_time    
        
    def __ge__(self,other):
        return self.preparation_time >= other.preparation_time    

class Menu:
    def __init__(self, name):
        self.name = name
        self.list_of_dishes = []
    
    def add_dish(self, dish:Dish):
        self.list_of_dishes.append(dish)
        # if dish not in self.list_of_dishes:
        #     self.list_of_dishes.append(dish)
    
    def get_starters(self):
        return [ i for i in self.list_of_dishes if i.dish_type == 'starter' ]
    
    def get_dishes(self):
        return [ i for i in self.list_of_dishes if i.dish_type == 'dish' ]
                       
    def get_desserts(self):
        return [ i for i in self.list_of_dishes if i.dish_type == 'dessert' ]
    
    def get_minimum_preparation_time(self):
        _starters = sorted(self.get_starters())
        _dishes = sorted(self.get_dishes())
        _desserts = sorted(self.get_desserts())

        thisOne1 = _starters[0].preparation_time if _starters else 0
        thisOne2 = _dishes[0].preparation_time if _dishes else 0
        thisOne3 = _desserts[0].preparation_time if _desserts else 0

        return thisOne1 + thisOne2 + thisOne3
    
    def get_maximum_preparation_time(self):
        _starters = sorted(self.get_starters()) # could be done also by reverse=True
        _dishes = sorted(self.get_dishes())
        _desserts = sorted(self.get_desserts())

                        # -1 for the maximum
        thisOne1 = _starters[-1].preparation_time if _starters else 0
        thisOne2 = _dishes[-1].preparation_time if _dishes else 0
        thisOne3 = _desserts[-1].preparation_time if _desserts else 0

        return thisOne1 + thisOne2 + thisOne3

    def __add__(self,other): # implement add
        one = [i for i in self.list_of_dishes]
        two = [i for i in other.list_of_dishes]
        one.extend(two)
        newname = self.name+' & '+other.name
        newMenu = Menu(newname)
        newMenu.list_of_dishes = one
        return newMenu
        # musíme mať alternative constructor?
        # asi netreba...

    # finally, implement repr or str...
    def __repr__(self):
        return super().__repr__()

    def __str__(self):     
        _starters = sorted(self.get_starters())
        _dishes = sorted(self.get_dishes())
        _desserts = sorted(self.get_desserts())

        _starters_name = [i.name for i in _starters]
        _dishes_name = [i.name for i in _dishes]
        _desserts_name = [i.name for i in _desserts]
        a = "\n".join(_starters_name)
        b = "\n".join(_dishes_name)
        c = "\n".join(_desserts_name)
        result = 'STARTER\n'+a+'\n\nDISH\n'+b+'\n\nDESSERT\n'+c
        return result
