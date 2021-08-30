import os
os.chdir("images")
# print(os.getcwd())
i = 1
for f in os.listdir():
    os.rename(f, str(1))
    i += 1
# for f in os.listdir():
#     # print(f.split())
#     f_name, f_ext = os.path.splitext(f)
#     # print(f_name)
#     print("task-{}"
