import click
import json
from datetime import datetime
from datetime import datetime
from os import listdir
from classes.Commit import Commit
from models.handling_files_and_folders import *
import os
class Repository :


    def __init__(self,repository_path,user_name):
       self.dict_commits = {}
       self.repository_path = os.getcwd()
       self.user_name = user_name
       self.wit_path = os.path.join(self.repository_path, ".wit")
       self.commits_path = os.path.join(self.wit_path, "commits")
       self.staging_area_path = os.path.join(self.wit_path, "Staging Area")
       self.commits_json_path = os.path.join(self.wit_path, "commits.json")
       self._load_commits()

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


    def _load_commits(self):
        if os.path.exists(self.commits_json_path):
            try:
                with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)
                if isinstance(existing_data, dict):
                    self.count_commit = len(existing_data)
                    self.dict_commits = existing_data
            except Exception as e:
                print(f"Error loading commits: {e}")


    def append_changing_file (self):
        list_change = []
        last_commit = find_last_created_folder(self.commits_path)
        path_last_commit = os.path.join(self.commits_path,last_commit)
        print(os.path.getctime(path_last_commit))
        for item in os.listdir(self.repository_path):
            if item != ".wit" and is_file_modified_after(os.path.join(self.repository_path,item),path_last_commit):
                list_change.append(item)
        return list_change


    def add_commit(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        new_commit = Commit(formatted_time, self.user_name, message)
        self.dict_commits[self.count_commit] = new_commit
        self.count_commit += 1
        try:
            if os.path.exists(self.commits_json_path):
                with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)
            else:
                existing_data = {}
            existing_data[self.count_commit] = new_commit.to_dict()
            with open(self.commits_json_path, "w", encoding="utf-8") as json_file:
                json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
        except Exception as e:

            print(f"Error updating JSON file: {e}")


    def wit_init (self):
        try:
         create_folder(".wit",self.repository_path)
         create_folder("Staging Area",self.wit_path)
         create_folder("commits",self.wit_path)
         create_file("commits.json",self.wit_path)
         write_file(self.commits_json_path,"{}")
        except FileExistsError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)


    def wit_add(self,file_name):
        try:
            source_path = os.path.join(self.repository_path,file_name)
            create_file(file_name,self.staging_area_path)
            new_path = os.path.join(self.staging_area_path, file_name)
            copy_file(source_path,new_path)######check!!! self.staging_area_path
        except FileNotFoundError as  e:
            print(e)

    def wit_commit(self, message):  # לא בדקנו אם אין שינויים ואז אם אין שינויים אז א עושים COMMIT
        print(folder_is_empty(self.staging_area_path))
        print(self.staging_area_path)
        if  folder_is_empty(self.staging_area_path):
            print("No changes to commit. Staging area is empty.")
            return False
        message += "(" + str(self.count_commit) + ")"
        self.add_commit(message)
        path_new_folder = os.path.join(self.commits_path, message)
        if not os.listdir(
                self.commits_path):  # בדיקה האם הקומיט שנוצר הוא הגרסה הראשונה אם כן ניצור תיקיה חדשה בלי להעתיק את הגרסה הקודמת
            create_folder(message, self.commits_path)
        else:  # בכל מקרה אחר ניצור תיקיה חדשה של הגרסה החדשה ונעתיק אליה את הגרסה הקודמת
            last_folder = find_last_created_folder(self.commits_path)
            path_last_folder = os.path.join(self.commits_path, last_folder)
            copy_folder(path_last_folder, path_new_folder)
        copy_files_and_overwrite(self.staging_area_path, path_new_folder)
        emptying_folder(self.staging_area_path)
        return True

    def wit_log(self):
        try:
            with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                all_commits = json.load(json_file)
                for key, value in all_commits.items():
                    print(json.dumps({key: value}, indent=4, ensure_ascii=False))
                    print("\n")
                return all_commits
        except FileNotFoundError as e:
            print(e)


    def wit_status(self):
        list_names_file_in_staging_area = []
        if folder_is_empty(self.staging_area_path):
            print("No changes added to commit")
        else:
            list_names_file_in_staging_area = read_names_all_files_in_folder(self.staging_area_path)
        list_file_changing = self.append_changing_file()
        list_file_changing = [item for item in list_file_changing if item not in list_names_file_in_staging_area]
        return list_names_file_in_staging_area,list_file_changing


    def wit_checkout(self,commit_id):
        all_commit = {}
        message_commit = ""
        if os.path.exists(self.commits_json_path):
            try:
                with open(self.commits_json_path, "r", encoding="utf-8") as json_file:
                    all_commit = json.load(json_file)
            except Exception as e:
                print(f"Error loading commits: {e}")
        for key,value in all_commit.items():
            if key == str(commit_id) :
                message_commit = value["message"]
        if message_commit == "":
            return False
        for item in listdir(self.commits_path):
            if item == message_commit :
                commit_path = os.path.join(self.commits_path,message_commit)
                copy_folder_without_parm(commit_path,self.repository_path,".wit")
                return True
            return False


repo=Repository(r"C:\Users\user1\Desktop\python\test","yaelRedlich")
#repo.wit_init()
repo.wit_add("index.html")
#repo.wit_add("index1.html")
#repo.wit_commit("commit 1")
#repo.wit_commit("commit 2")
#repo.wit_log()
#repo.add_commit("yael")
#repo.add_commit("hadasa")
#repo.add_commit("yael")
#repo.append_changing_file()

#print(repo.wit_status())
repo.wit_checkout("2")