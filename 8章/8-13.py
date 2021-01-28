def build_profile(first, last, **user_info):
	profile ={}
	profile['first_name']=first
	profile['last_name']=last
	for key, value in user_info.items():
		profile[key]=value
		return profile
user_profile1=build_profile('zeng', 'yundan',
                           location='chengdu',
                           field='Electronic' )
user_profile2=build_profile('zeng','yundan',location='neijiang',
                            field='programming')
user_profile3=build_profile('zeng','yundna',location='weiyuan',
                            field='python')                            
print(user_profile1)
print(user_profile2)
print(user_profile3)
