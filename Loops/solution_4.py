# string = "Hello"
# reversed_string = ""   # empty string to build the result
# ```

# **The loop iterates character by character:**

# | Iteration | `i` | Operation | `reversed_string` |
# |---|---|---|---|
# | 1 | `'H'` | `'H' + ""` | `"H"` |
# | 2 | `'e'` | `'e' + "H"` | `"eH"` |
# | 3 | `'l'` | `'l' + "eH"` | `"leH"` |
# | 4 | `'l'` | `'l' + "leH"` | `"lleH"` |
# | 5 | `'o'` | `'o' + "lleH"` | `"olleH"` |

# **Output:**
# ```
# olleH





string="Hello"
reversed_string=""
for i in string:
    reversed_string=i+reversed_string
print(reversed_string)