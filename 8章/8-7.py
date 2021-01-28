def make_album(singer_name,album_name):
	"""the names of singers and their albums"""
	album=singer_name+'--'+album_name
	return album.title()
album1=make_album('Kris Wu','Six')
album2=make_album('Zella Day','Crazy Train')
album3=make_album('Taylor Swift','willow')
print(album1)
print(album2)
print(album3)	
def make_album(singer_name,album_name,song_number=''):
	"""the names of singers and their album and the numbers of songs in album """
	album={'singer_name':singer_name,'album_name':album_name,'song_number':song_number}
	if song_number:
		album['song_number']=song_number
	return album
album4=make_album('Zella Day','Crazy Train','one')
album5=make_album('kris wu','six')
print(album4)
print(album5)	 
