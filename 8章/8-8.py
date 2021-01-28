def make_album(singer_name,album_name):
	"""the names of singers and their albums"""
	album=singer_name+'--'+album_name
	return album.title()
while True:
	print("\n Please tell me the album:")
	print("(enter 'q' to quit)")
	singer_name=input(" singer's name:")
	if singer_name=='q':
		break
	album_name=input("the name of album")
	if album_name=='q':
		break
	describe=make_album(singer_name,album_name)
	print (describe)			
