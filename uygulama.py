"""Toplumsal Sorun Haber İzleyicisi.

Kamuya açık haber başlıklarını toplumsal sorun kategorilerine göre kaydeder
ve CSV dosyasındaki kayıtların kategori sayılarını raporlar.
"""

import csv
from datetime import datetime
from pathlib import Path


# Uygulamanın kullanacağı sabit kategori listesi.
KATEGORILER = ["Barınma", "Göç", "Gençlik", "Eğitim", "Çalışma hayatı"]

# CSV dosyası, bu Python dosyasının bulunduğu klasörde tutulur.
CSV_DOSYASI = Path(__file__).with_name("haber_kayitlari.csv")
CSV_ALANLARI = ["baslik", "kaynak", "yayin_tarihi", "kategori"]


def bos_olmayan_metin_al(soru):
    """Kullanıcıdan boş olmayan bir metin alır."""
    while True:
        metin = input(soru).strip()
        if metin:
            return metin
        print("Uyarı: Bu alan boş bırakılamaz. Lütfen yeniden girin.")


def tarih_al():
    """YYYY-AA-GG biçimindeki gerçek bir takvim tarihini alır.

    Gelecekteki geçerli tarihlere de izin verilir.
    """
    while True:
        tarih_metni = input("Yayın tarihi (YYYY-AA-GG): ").strip()
        try:
            tarih = datetime.strptime(tarih_metni, "%Y-%m-%d")
            # Bu kontrol, örneğin 2026-1-2 gibi eksik sıfırlı biçimleri reddeder.
            if tarih.strftime("%Y-%m-%d") != tarih_metni:
                raise ValueError
            return tarih_metni
        except ValueError:
            print("Uyarı: Geçerli tarihi YYYY-AA-GG biçiminde girin.")


def kategori_al():
    """Listeden bir kategori seçilene kadar kullanıcıya tekrar sorar."""
    while True:
        print("Toplumsal sorun kategorileri:")
        for sira, kategori in enumerate(KATEGORILER, start=1):
            print(f"{sira}. {kategori}")

        secim = input("Kategori numarası: ").strip()
        if secim.isdigit():
            kategori_sirasi = int(secim)
            if 1 <= kategori_sirasi <= len(KATEGORILER):
                return KATEGORILER[kategori_sirasi - 1]
        print("Uyarı: Listede bulunan 1-5 arasındaki bir numarayı girin.")


def haber_kaydi_al():
    """Bir haberin dört bilgisini alıp sözlük olarak döndürür."""
    print("\nYeni haber kaydı")
    return {
        "baslik": bos_olmayan_metin_al("Haber başlığı: "),
        "kaynak": bos_olmayan_metin_al("Kaynak adı: "),
        "yayin_tarihi": tarih_al(),
        "kategori": kategori_al(),
    }


def kayitlari_yukle(csv_yolu=CSV_DOSYASI):
    """CSV dosyası varsa kayıtları liste olarak okur."""
    if not csv_yolu.exists() or csv_yolu.stat().st_size == 0:
        return []

    with csv_yolu.open("r", newline="", encoding="utf-8") as dosya:
        okuyucu = csv.DictReader(dosya)
        return list(okuyucu)


def karsilastirma_metni(metin):
    """Başlık ve kaynak karşılaştırmasında harf büyüklüğünü yok sayar."""
    # Türkçedeki büyük I ve İ harflerini doğru küçük harflerle eşleştir.
    return metin.strip().replace("İ", "i").replace("I", "ı").casefold()


def kayit_ekle(kayit, csv_yolu=CSV_DOSYASI):
    """Kaydı ekler; tekrar eden haber varsa False döndürür."""
    mevcut_kayitlar = kayitlari_yukle(csv_yolu)

    # Başlık ve kaynakta yalnızca harf büyüklüğü farkı varsa da tekrarı yakala.
    for mevcut in mevcut_kayitlar:
        ayni_baslik = karsilastirma_metni(mevcut.get("baslik", "")) == karsilastirma_metni(kayit["baslik"])
        ayni_kaynak = karsilastirma_metni(mevcut.get("kaynak", "")) == karsilastirma_metni(kayit["kaynak"])
        ayni_tarih = mevcut.get("yayin_tarihi", "") == kayit["yayin_tarihi"]
        ayni_kategori = mevcut.get("kategori", "") == kayit["kategori"]
        if ayni_baslik and ayni_kaynak and ayni_tarih and ayni_kategori:
            return False

    # İlk kayıtta veya boş bir dosyada sütun adlarını bir kez yaz.
    baslik_gerekli = not csv_yolu.exists() or csv_yolu.stat().st_size == 0
    with csv_yolu.open("a", newline="", encoding="utf-8") as dosya:
        yazici = csv.DictWriter(dosya, fieldnames=CSV_ALANLARI)
        if baslik_gerekli:
            yazici.writeheader()
        yazici.writerow(kayit)
    return True


def rapor_metni_olustur(kayitlar):
    """Kayıt sayısı yoksa bilgi verir, varsa kategori raporu oluşturur."""
    if not kayitlar:
        return "Henüz haber kaydı yok."

    # Her kategori başlangıçta sıfırdır; kayıt geldikçe sayı artırılır.
    kategori_sayilari = {kategori: 0 for kategori in KATEGORILER}
    for kayit in kayitlar:
        kategori = kayit.get("kategori", "")
        if kategori in kategori_sayilari:
            kategori_sayilari[kategori] += 1

    satirlar = ["TOPLUMSAL SORUN HABER RAPORU", "-" * 34]
    for kategori in KATEGORILER:
        satirlar.append(f"{kategori:<20} {kategori_sayilari[kategori]} haber")
    satirlar.append("-" * 34)
    satirlar.append(f"Toplam kayıt: {len(kayitlar)}")
    return "\n".join(satirlar)


def ana_menu():
    """Menüyü kullanıcı çıkış seçeneğini seçene kadar çalıştırır."""
    while True:
        print("\n=== Toplumsal Sorun Haber İzleyicisi ===")
        print("1. Haber ekle")
        print("2. Kategori raporunu göster")
        print("3. Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            kayit = haber_kaydi_al()
            if kayit_ekle(kayit):
                print("Haber kaydı CSV dosyasına eklendi.")
            else:
                print("Bu haber zaten kayıtlı; ikinci kez eklenmedi.")
        elif secim == "2":
            kayitlar = kayitlari_yukle()
            print("\n" + rapor_metni_olustur(kayitlar))
        elif secim == "3":
            print("Program kapatıldı.")
            break
        else:
            print("Uyarı: Menüden 1, 2 veya 3 seçin.")


if __name__ == "__main__":
    ana_menu()
