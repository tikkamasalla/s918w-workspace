import json

d = json.load(open(
    r'C:\Users\Aows\Downloads\callshield-port\CallShield\data\spam_numbers.json'))
nums = d['numbers']
print(type(nums[0]), str(nums[0])[:120])
