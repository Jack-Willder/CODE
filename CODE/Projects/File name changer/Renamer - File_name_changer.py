from subprocess import getoutput


def main():
    directory_file_list = getoutput('dir /b')
    directory_file_list = directory_file_list.splitlines()
    directory_file_list.sort(reverse=True)
    item_position_number = 143
    for file_names in directory_file_list:
        if file_names[-3:] == ".ts":
            print(file_names)
            getoutput(f'ren "{file_names}" "Hunter x Hunter - Episode - {item_position_number}.ts"')
            item_position_number -= 1


if __name__ == "__main__":
    main()
