from datetime import datetime
from operator import index
from datetime import datetime
from classes.Commit import Commit
from models.handling_files_and_folders import *
class Repository :
    def __init__(self,repository_path,user_name):
       self.dict_commits = {}
       self.repository_path=repository_path
       self.user_name=user_name
       self.count_commit=0

    def __str__(self):
        commits_str = "\n".join(
            f"{key}: {str(commit)}" for key, commit in self.dict_commits.items()
        )
        return (
            f"Repository:\n"
            f"  Path: {self.repository_path}\n"
            f"  User: {self.user_name}\n"
            f"  Commits:\n{commits_str if commits_str else '  No commits yet.'}"
        )

    def add_commit(self,message):
      current_time = datetime.now()
      formatted_time = current_time.strftime("%Y-%m-%d%H:%M:%S")
      c = Commit (formatted_time, self.user_name, message)
      self.dict_commits[self.count_commit] = c
      self.count_commit += 1
      print(self)
    def wit_init (self):
        try:
         create_folder(".wit",self.repository_path)
         new_path = os.path.join(self.repository_path, ".wit")
         create_folder("Staging Area",new_path)
        except FileExistsError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)

    def wit_add(self,file_name):
        try:
            new_path = os.path.join(self.repository_path, ".wit")
            new_path =  os.path.join(new_path, "Staging Area")
            source_path = os.path.join(self.repository_path,file_name)
            create_file(file_name,new_path)
            new_path = os.path.join(new_path, file_name)
            copy_file(source_path,new_path)
        except FileNotFoundError as  e:
            print(e)




repo=Repository(r"C:\Users\user1\Desktop\python\test","yaelRedlich")
#repo.wit_init()
repo.wit_add("index.html")
repo.wit_add("index1.html")

#repo.add_commit("hii")
#repo.add_commit("ghkuky")
#print(repo.add_commit("yael"))

