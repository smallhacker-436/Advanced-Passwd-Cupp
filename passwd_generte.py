import itertools

def get_leet_variants(word):
    """Word ko hacker style (Leet) mein badalta hai"""
    char_map = {
        'a': ['a', '@', '4'], 'e': ['e', '3'], 'i': ['i', '1', '!'],
        'o': ['o', '0'], 's': ['s', '$', '5'], 't': ['t', '7', '+']
    }
    variants = [""]
    for char in word.lower():
        if char in char_map:
            variants = [prefix + v for prefix in variants for v in char_map[char]]
        else:
            variants = [prefix + char for prefix in variants]
    return variants

def generate_custom_wordlist():
    print("==============================================")
    print("   TARGET PROFILE WORDLIST GENERATOR (HARD)   ")
    print("==============================================\n")

    # Target ki ek-ek detail collect karna
    data = {}
    data['first_name'] = input("[+] Target First Name: ").strip()
    data['last_name'] = input("[+] Target Last Name: ").strip()
    data['nick_name'] = input("[+] Nickname: ").strip()
    data['dob'] = input("[+] Birthday (DDMMYYYY): ").strip() # e.g. 15081947
    data['partner'] = input("[+] Partner/Spouse Name: ").strip()
    data['pet'] = input("[+] Pet's Name: ").strip()
    data['company'] = input("[+] Company/Workplace Name: ").strip()
    data['city'] = input("[+] Hometown/City: ").strip()
    data['vehicle'] = input("[+] Vehicle Number (Last 4 digits): ").strip()
    data['fav_team'] = input("[+] Favorite Sports Team/Hero: ").strip()
    data['extra'] = input("[+] Any other Keyword (comma separated): ").strip().split(',')

    # Base keywords ki list banana
    base_keywords = set()
    for key, value in data.items():
        if value and key != 'extra':
            base_keywords.add(value.lower())
    if data['extra']:
        for item in data['extra']:
            if item.strip(): base_keywords.add(item.strip().lower())

    # Date variations (DD, MM, YY, YYYY)
    dates = set()
    if len(data['dob']) == 8:
        dates.add(data['dob'])          # 15081947
        dates.add(data['dob'][:4])      # 1508
        dates.add(data['dob'][-4:])     # 1947
        dates.add(data['dob'][-2:])     # 47

    final_results = set()

    print("\n[*] Processing variations (this might take a moment)...")

    # 1. Sabhi keywords ke Leet aur Case variations
    refined_keywords = set()
    for word in base_keywords:
        refined_keywords.add(word)
        refined_keywords.add(word.capitalize())
        # Sirf main keywords ke liye leet variants (taaki file bohot badi na ho jaye)
        if len(word) > 3:
            for l in get_leet_variants(word):
                refined_keywords.add(l)

    # 2. Combinations (Keyword + Date / Keyword + Keyword)
    for word in refined_keywords:
        final_results.add(word)
        for date in dates:
            final_results.add(word + date)
            final_results.add(date + word)

    # 3. Common Special Character Padding
    special_chars = ['!', '@', '#', '123', '786', '@123', '!', '?', '_']
    temp_list = list(final_results)
    for p in temp_list:
        if len(p) < 12: # Logical length limit
            for char in special_chars:
                final_results.add(p + char)

    # File mein save karna
    filename = f"target_{data['first_name']}_wordlist.txt"
    with open(filename, "w") as f:
        for pwd in sorted(final_results):
            if len(pwd) >= 5: # Chote passwords delete
                f.write(pwd + "\n")

    print(f"\n[+] Success! Wordlist generated with {len(final_results)} combinations.")
    print(f"[+] Saved to: {filename}")

if __name__ == "__main__":
    generate_custom_wordlist()

