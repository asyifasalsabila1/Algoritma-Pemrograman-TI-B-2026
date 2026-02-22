
 
'''
umur
'''
umur = -1

try:
	if umur < 0:
		raise ValueError ("Umur tidak boleh negatif")
except ValueError as e:
	print("Terjadi kesalahan:" + str(e))