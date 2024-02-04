names = []
for _ in range(5):
    name = input("What's your name: ")
    names.append(name)
    print(f"Hello! {name}")

for name in sorted(names):
    print(f"Hello! {name}")