import re

def match_a_b(string):
    return bool(re.fullmatch(r'a*b*', string))

def match_a_b_limited(string):
    return bool(re.fullmatch(r'a{1}b{2,3}', string))

def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

def find_upper_followed_by_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)

def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

def replace_special_chars(string):
    return re.sub(r'[ ,.]', ':', string)

def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

def insert_spaces_between_caps(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

# examples
print(match_a_b("abbb"))  # True
print(match_a_b_limited("abb"))  # True
print(find_lowercase_with_underscore("hello_world test_example"))  # ['hello_world', 'test_example']
print(find_upper_followed_by_lower("HelloWorld Python"))  # ['Hello', 'World', 'Python']
print(match_a_anything_b("a123b"))  # True
print(replace_special_chars("Hello, world. Welcome"))  # 'Hello:world:Welcome'
print(snake_to_camel("hello_world"))  # 'HelloWorld'
print(split_at_uppercase("HelloWorldPython"))  # ['', 'Hello', 'World', 'Python']
print(insert_spaces_between_caps("HelloWorldPython"))  # 'Hello World Python'
print(camel_to_snake("HelloWorldPython"))  # 'hello_world_python'
