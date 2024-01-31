1# from collections import namedtuple

# def functions(peremetr1, peremetr2):

#     Sozlar = namedtuple('Sozlar','birinchi ikkinchi')

#     ayirilgan_sozlar = peremetr1.split()

#     sozlar_obyekti = Sozlar(birinchi=ayirilgan_sozlar[0], ikkinchi=ayirilgan_sozlar[1])

#     birlashtirilgan_sozlar = f"{sozlar_obyekti.birinchi}{peremetr2}{sozlar_obyekti.ikkinchi}"

#     return birlashtirilgan_sozlar

# peremetr1 = "Qalesan o'zingchi"
# peremetr2 = ",yaxshi "
# natija = functions(peremetr1, peremetr2)
# print(natija)
# from collections import namedtuple

2# def unli_harflar(satr):
#     Soz = namedtuple("Soz",'satr')
#     soz_obj = Soz(satr)

#     unli_harflar = "a,e,i,o,u,A,E,I,O,U"
#     unli_harflar_soni = sum(1 for harf in soz_obj.satr if harf in unli_harflar)
#     return unli_harflar_soni

# satr = "Qalesan yaxshi ozinchi"
# natija = unli_harflar(satr)
# print(f"{satr} ichidagi unli harflar soni : {natija}")
# from collections import namedtuple

3# def ruxsiz_sonlar(nol):
#     Zero = namedtuple("Zero", ["nol"])
#     zero_obj = Zero(nol)

#     ruxsatsiz_sonlar = "0" 
#     nollar_soni = sum(1 for son in zero_obj.nol if son in ruxsatsiz_sonlar)

#     return nollar_soni

# nol = "1205320530521000521030"
# natija = ruxsiz_sonlar(nol)
# print(f"{nol} ichidagi nollar soni: {natija}")
4# def check_unli_harflar(unli_soz, tekshiriladigan_soz):
#     unli_harflar = "a,e,i,o,u,A,E,I,O,U"  

#     unli_harflar_birinchi = sum(1 for harf in unli_soz if harf in unli_harflar)

#     unli_mavjud = all(harf in unli_harflar for harf in tekshiriladigan_soz)

#     return unli_mavjud

# birinchi_soz = "Salom"
# ikkinchi_soz = "Salom dunyo"
# natija = check_unli_harflar(birinchi_soz, ikkinchi_soz)
# print(f"Ikkinchi so'zda barcha birinchi so'zdagi unli harflar mavjud: {natija}")
# 5
# input_str = str(input("So`zlar kiritng:"))
# def sozs_sanar(input_str):
#     soz_count = 0
#     inside_word = 0
#     for varchar in input_str:
#         if varchar.isalnum():
#             inside_word = True
#         elif inside_word:
#             soz_count+=1
#             inside_word = False
#     if inside_word:
#         soz_count+=1
#     return soz_count
# res = sozs_sanar(input_str)
# print(f"{res}ta so`zdan iborat. [{input_str}]")