weight = float(input("请输入您的体重(kg):"))
height = float(input("请输入您的身高(m):"))
BMI = weight / height**2
print("您的BMI指数是:",BMI)
if(BMI < 18.5):
    print("您的体重过轻！")
elif(18.5 < BMI < 24):
    print("您的体重正常！")
else:
    print("您的体重已超标！")
