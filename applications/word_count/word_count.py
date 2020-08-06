# x = word_count('":;,.-+=/\\|[]{}()*^&')
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignore = [":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\""]

def word_count(s):
    cache = {}
    new_string = s.lower()
    for c in ignore:
        new_string = new_string.replace(c, "")
    new_string = new_string.split()
    for c in new_string:
        if c in cache:
            cache[c] += 1
        else:
            cache[c] = 1
    return cache

# Output

# It returns a dictionary of words and their counts:

# ```
# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
# ```

# Case should be ignored. Output keys must be lowercase.

# Key order in the dictionary doesn't matter.

# Split the strings into words on any whitespace.

# Ignore each of the following characters:

# ```
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```

# If the input contains no ignored characters, return an empty dictionary.


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))