# nums = [1,2,3,4,5]
# letters = ["a", "b", "c", "d", "e"]
# names = ["John", "Eric", "Michael", "Graham", "Joe"]
# combo = list(zip(nums, letters, names))
# print(combo)



keys = "this parrot is deceased"
values = "denna papegojan ar avlaiden"
keys = keys.split()
values = values.split()
print(keys,values)
en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)
new_dict = {key:value for key, value in zip(keys, values)}
print(new_dict)
en,sv = list(en_sv_dict.keys())