# find the heights of the top three buildings in descending order from eight given buildings:

# Method 1:
building_count=10
large_height=[]
for i in range(building_count):
    height=int(input("Enter the height of the building:"))
    large_height.append(height)
large_height.sort(reverse=True)
top_three=large_height[:3]
print((top_three))

# Method 2:
print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l = sorted(l)
print(*l[:4:-1], sep='\n')



