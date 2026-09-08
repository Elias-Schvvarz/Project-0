from get_by_index import get_by_index
import random
import string

characters = string.ascii_letters + string.digits + '@!=*'

length = random.randint(0, 70)

the_elements = "".join(random.choices(characters, k=length))

the_index = random.randint(0, 100)

the_default = 'stop'

if get_by_index(the_elements, the_index, the_default)