# Kişinin kilo endeksini hesaplayan ve endeks değerine göre zayıf, 
# kilolu veya fazla kilolu sonucunu döndüren kodu yazın. 
# (Kilo endeksi hesaplaması için internete bakabilirsiniz) 
# Bunun için kullanıcıdan kilo ve boy ölçülerini isteyin. 
# Kilo endeksi 25'in altındaysa zayıf, 25-30 arasıysa normal, 
# 30-40'ın üzerindeyse kilolusunuz. 40'ın üzerindeyse kilolusunuz.


kilo = int(input("Kilonuz : "))
boy = float(input("Boyunuz : (1.75 gibi ) "))
endeks = kilo / (boy * boy)
endeks_f = f"{endeks:.2f}"
if endeks < 25:
    print("Endeksiniz : ", endeks_f, " olup siz ZAYIF kategorisindesiniz")
elif endeks >=25 and endeks <=30:
    print("Endeksiniz : ", endeks_f, " olup siz NORMAL kategorisindesiniz")
elif endeks >=31 and endeks<=40:
    print("Endeksiniz : ", endeks_f, " olup siz KİLOLU kategorisindesiniz")
else:
    print("Endeksiniz : ", endeks_f, " olup siz OBEZ kategorisindesiniz")
