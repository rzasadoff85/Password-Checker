import hashlib
import requests

def request_api_data(query_char):
    # API-yə yalnız hash-in ilk 5 simvolunu göndəririk
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Xəta baş verdi: {res.status_code}. API-ni yoxlayın.')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    # API-dən gələn cavabları sətirlərə bölürük
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # Əgər bizim hash-in qalan hissəsi API-dən gələnlərlə üst-üstə düşürsə, sayını qaytarır
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # Şifrəni SHA-1 alqoritmi ilə şifrələyirik
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Hash-i iki hissəyə bölürük: ilk 5 simvol və qalan hissə
    first5_char, tail = sha1password[:5], sha1password[5:]
    
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main():
    print("--- Sızdırılmış Şifrə Yoxlayıcısına Xoş Gəlmisiniz ---")
    password = input("Yoxlamaq istədiyiniz şifrəni daxil edin: ")
    
    count = pwned_api_check(password)
    
    if count:
        print(f"⚠️ DİQQƏT: Bu şifrə daha əvvəl {count} dəfə sızdırılıb! Təhlükəsizliyiniz üçün şifrəni dəyişin.")
    else:
        print("✅ Əla! Bu şifrə heç bir məlumat sızıntısında tapılmadı. Təhlükəsizdir.")

if __name__ == '__main__':
    main()
