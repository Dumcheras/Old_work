import os

# path_to_test_file_1 = os.path.normpath(r'C:\Users\Константин\Desktop\Old_work_1\hw_06_2_files'
#                                        r'\data_path_1\test_file_1.txt')
# print(path_to_test_file_1)

# into_hw_06 = os.path.abspath(r'C:\Users\Константин\Desktop\Old_work_1\hw_06_2_files')
# print(into_hw_06)
#
# for path, dirnames, filenames in os.walk(into_hw_06):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

disk = 'c:\\'
dir_1 = 'Users'
dir_2 = 'Константин'
dir_3 = 'Desktop'
dir_4 = 'Old_work_1'
dir_5 = 'hw_06_2_files'
dir_6 = 'data_path_2'
dir_7 = 'test_file_3.txt'
path_to_test_file_3 = os.path.join(disk, dir_1, dir_2, dir_3, dir_4, dir_5, dir_6, dir_7)
print(path_to_test_file_3)
