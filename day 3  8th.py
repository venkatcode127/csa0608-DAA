def stringMatching(words):
    return [w for w in words if any(w in other for other in words if w != other)]


print(stringMatching(["mass", "as", "hero", "superhero"]))  
print(stringMatching(["leetcode", "et", "code"]))           
