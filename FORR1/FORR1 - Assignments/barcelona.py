listi = input().split(" ")
töskur = input().split(" ")
fjoldi_taska = int(listi[0])
benna_taska = int(listi[1])
i = fjoldi_taska
n = 0 
for taska in töskur:
    i -= 1
    n += 1
    if int(taska) == benna_taska:
        break
if i == fjoldi_taska - 1:
    print("fyrst")
elif i == fjoldi_taska -2:
    print("naestfyrst")
else:
    print(f"{n} fyrst")