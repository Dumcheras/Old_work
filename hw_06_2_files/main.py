import os

# path_to_test_file_1 = os.path.normpath(r'C:\Users\Константин\Desktop\Old_work_1\hw_06_2_files'
#                                        r'\data_path_1\test_file_1.txt')
# print(path_to_test_file_1)

into_hw_06 = os.path.abspath(r'C:\Users\Константин\Desktop\Old_work_1\hw_06_2_files')
print(into_hw_06)

for path, dirnames, filenames in os.walk(into_hw_06):
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")
