import re
text = ("hello 1997     this is just     test mesaage      @#%$%$")
result = re.sub(r"[#,@\'?\.$%_\d\s+]", "", text)
print(result)