def validate_email(e: str) -> bool:
    if "@" not in e:
        return False
    
    if "." not in e[e.index("@") + 1:]:
        return False

    if not (is_valid_str(e[:e.index("@")]) and is_valid_str(e[e.index("@") + 1:])):
        return False
    
    return True

def is_valid_str(s: str) -> bool:
    for i in s:
        if str(i).isalnum() or i == ".":
            continue
        return False
    return True

print(validate_email(input("Please enter your email: ")))