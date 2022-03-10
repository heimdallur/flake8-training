"""THIS IS AN EXAMPLE IS FREE OF LINTING ERROR"""
def PrintWorkingDir():
    import os
    print(os.getcwd())  # Returns the current working directory of the process
def PrintSomethingNTimes(N):
    for i in range(N):  # Will repeat the content n times
        print('Something')
if __name__ == '__main__':
    PrintWorkingDir()
    PrintSomethingNTimes(3)