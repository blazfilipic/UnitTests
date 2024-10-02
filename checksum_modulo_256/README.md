## Building the DLL

To compile `checksum.c` into a 64-bit DLL using `mingw-w64`, follow these steps:

1. **Open the Command Prompt**.
2. Navigate to the project directory where `checksum.c` is located.
3. Run the following command to compile the C file into a DLL:

   ```bash
   gcc -shared -o checksum.dll checksum.c -Wl,--out-implib,libchecksum.a
   
This command does the following:

-shared: Creates a shared library (DLL).
-o checksum.dll: Specifies the output file name for the DLL.
checksum.c: The input C source file.
-Wl,--out-implib,libchecksum.a: Generates an import library for linking (optional).
After successful compilation, you should see checksum.dll in the project directory.


## Unit testing with python

 Make sure you have checksum.dll file in the directory. 
 From CMD run command: {PATH}/python test_checksum.py

Output should be something like this:

![image](https://github.com/user-attachments/assets/d27622b6-45f7-40eb-9db1-4529e3d5b93d)


