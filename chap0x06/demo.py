# coding = utf-8

data = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0x1D, 0x1B, 0x48, 0x2C, 0x0C, 0x24, 0x02, 0x02, 0x09, 0x3A, 0x0B, 
    0x3B, 0x0E, 0x03, 0x3A, 0x39, 0x0C, 0x08, 0x11, 0x00, 0x00, 0x1A, 0x09, 0x0C, 0x29, 0x20, 0x58, 
    0x44, 0x00, 0x00]

old_flag = "0ctf{Too_Simple_Sometimes_Naive!!!}"

def main():
    flag = []
    for i in range(len(old_flag)):
        flag.append(chr(ord(old_flag[i]) ^ data[i]))
    print ("".join(flag))

if __name__ == '__main__':
    main()