import os

LINE = "My agent runs my money, my calendar and my inbox from a sandbox that's demolished every 30 minutes — he's not a butler, he's a goldfish with admin access."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
