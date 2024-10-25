import cmd
import os
import shutil
import psutil

class FileManager(cmd.Cmd):
    prompt = os.getcwd() + ' $ '
    intro = 'File Manager, written by Grenadieren/Razu'
    
    def do_ls(self, line):
     print(os.listdir(os.getcwd()))
    
     def do_rmdir(self, line):
         var1 = input("PATH:")
         os.rmdir(var1)
    
    def do_mkdir(self, line):
        var1 = input("PATH:")
        os.mkdir(var1)
    
    def do_rnd(self, line):
        var1 = input("PATH:")
        os.rename(var1)
    
    def do_rmtr(self, line):
        var1 = input("PATH:")
        shutil.rmtree(var1)
    
    def do_copyfile(self, line):
        var1 = input("SRC")
        var2 = input("DST:")
        shutil.copyfile(var1, var2)
    
    def do_move(self, line):
        var1 = input("SRC:")
        var2 = input("DST:")
        shutil.move(var1, var2)
    
    def do_help(self, line):
        print("mkdir > make a directory")
        print("ls > list the directory contents")
        print("move > move a file/directory")
        print("copyfile > copy a file/directory")
        print("rmdir > remove a directory/file")
        print("rmtr > remove a directory tree")

    def do_ls(self, line):
        print(os.listdir(os.getcwd)())

if __name__ == '__main__':
    FileManager().cmdloop()
