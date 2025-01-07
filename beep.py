import winsound


def play_beep():
    winsound.Beep(1000, 1000)

def main():
     while True:
        print("type beep for beep rgeg")
        beep = input().lower()
        if beep == "beep":
            play_beep()
        continue

if __name__ == "__main__":
    main()
