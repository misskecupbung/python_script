a = "NolSatu hadir sebagai usAha untuk merespon masalah bersama yaitu banyak lulusan teknologi informatika atau profesional teknologi informatika yang kemampuannya kuranG sementara perusahaan-perusahaan membutuhkan profesional teknologi informatika terbaik dengan kemampuan terkini. Selain itu, perkembangan teknologi informatika global Berlangsung sangat cepat dan kemampuan profesional teknologi informatika disarankan selaras dengan perkembangan tersebut. Profesional teknologi informatika diharapkan dapat membantu perusahaan dalaM mengadopsi teknologi informatika terkini untuk mendOrong proses bisnis perusahaan. Imbal balik bagi profesional teknologi informatika dari proses ini adalah penghasilan yang cukup dan kesejahteraAN yang baik yang diberikan oleh perusahaaN. NolSatu adalah media untuk Talenta teknologi informatika dilatih agar memiliki kemampuan terkini kemudian disalurkan ke perusahaan yang membutuhkan. NolSatu juga media untuk Profesional teknologi informatika dilatih agar kemampuannya termutakhirkan kemudian disalurkan ke perusahaan baru yang membutuhkan"

upper = len(list(filter(lambda x: x.isupper(), a)))
kata = len(a.split())
kalimat = len(a.split("."))
x = a.split('.')
match = []
for i in x:
    if i.strip().lower().startswith("nolsatu") and i.strip().lower().endswith("membutuhkan"):
        match.append(i.strip())
sentence=a.split('.')
print ("Huruf kapital sebanyak: ", upper)
print ("Jumlah kata sebanyak : " +  str(kata)) 
print ("Jumlah kalimat sebanyak : ", kalimat) 
print ("Jumlah kalimat yang diawali dengan Nolsatu dan diakhiri dengan membutuhkan sebanyak", (len(match)))
#print(kapital)
for i in sentence:
    print (i.strip().capitalize()+". ",end='')
