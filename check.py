import subprocess
import time

def ping_url(url, timeout=3):
    try:
        # timeout değeri milisaniye cinsinden belirtilerek ping komutu çalıştırılıyor
        response = subprocess.run(
            ["ping", "-n", "1", "-w", str(timeout * 1000), url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # returncode 0 ise ping başarılı
        return response.returncode == 0
    except Exception as e:
        print(f"Ping sırasında bir hata oluştu: {e}")
        return False

def main():
    input_file = r"C:\Users\alper\OneDrive\scp\gout\cerge.txt"
    output_file = "reachable_urls.txt"
    
    with open(input_file, "r") as infile:
        for line in infile:
            url = line.strip()
            if url:  # Boş satırları atla
                if ping_url(url):
                    print(f"{url} is reachable")
                    with open(output_file, "a") as outfile:
                        outfile.write(url + "\n")
                time.sleep(3)

if __name__ == "__main__":
    main()
