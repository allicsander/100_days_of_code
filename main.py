
# def greet():
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()    


# def greet_with_name(name):
#     print(f"hello, {name}")
#     print(f"how do you do, {name}?")

# greet_with_name('Billie')    
def paint_calc(height, width, cover):
    return (width * height)/cover

test_h = int(input("heigth of the wall: "))
test_w = int(input("width of the wall: "))
coverage = 5
number_of_cans = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"Number of cans: {number_of_cans}")