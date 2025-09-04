file = open('C:\\Users\\Priyanka Gupta\\Desktop\\Python Programming\\Python Mini Projects\\File Management App\\sample.txt','r')
content = file.read()
file.close()
print(f"Content of 'sample.txt': {content}")