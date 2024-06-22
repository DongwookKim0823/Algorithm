from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    extension_dict = defaultdict(int)

    for _ in range(n):
        extension_dict[input().split('.')[1]] += 1

    for file_extension in sorted(extension_dict):
        print(file_extension, extension_dict[file_extension], sep=' ')
