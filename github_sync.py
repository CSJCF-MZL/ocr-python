import git 

repo = git.Repo('C:/Sites/ocr-python')
repo.git.reset('--hard')

origin = repo.remote(name='origin')
origin.pull('main')
print("El repositorio ha sido actualizado")