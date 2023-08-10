T = int(len(input("Digite o seu tweet")))

print(T)
if len(T) <= 140:
    print("TWEET")
elif len(T) > 140:
    print("MUTE")