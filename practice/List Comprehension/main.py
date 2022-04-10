numbers = [1,2,3,4]
new_numbers = [ num+1 for num in numbers]
print(new_numbers)

new_list = [items*2 for items in range(1,5)]
print(new_list)

names = ['aaa','bbbb','ccccc','dd','eeee']
short_names = [n.upper() for n in names if len(n)>=4]
print(short_names)