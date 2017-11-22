# https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python
import unittest
import os
import shutil

from p_tree import utilities as utlis
from p_tree import dbox

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        files_list = ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']
        utlis.handle_directories(files_list=files_list)

    def tearDown(self):

        print('tearDown')

        """Delete all contents"""
        files_list = ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']
        for f in files_list:
            shutil.rmtree(f,ignore_errors=True)

    def test_directory_creation(self):
        files_list = ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']
        utlis.handle_directories(files_list=files_list)
        files = ['./p_tree/'+f for f in os.listdir('./p_tree')]
        # print(files_list, files)
        for f in files_list:
            if any(f in s for s in files):
                continue
            else:
                assert True==False
                break
            # os.rmdir(f)

    def test_data_contents_erase(self):

        files_list = ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']
        utlis.handle_directories(files_list=files_list)

        f = open('./p_tree/data/test.txt','w')
        f.writelines('test')
        f.close()
        f = open('./p_tree/seed_images/test.txt','w')
        f.writelines('test')

        f.close()
        f = open('./p_tree/temp/test.txt','w')
        f.writelines('test')

        f.close()
        print(os.listdir('./p_tree/data/'))

        # utlis.erase_directory_contents('./p_tree/data/')
        for f in files_list:
            if any('test.txt' in s for s in os.listdir(f)):
                continue
            else:
                assert True==False
                break

        for f in files_list:
            utlis.erase_directory_contents(f)
            if any('test.txt' in s for s in os.listdir(f)):
                assert True==False
            else:
                continue


    def test_dropbox_download_photos(self):

        files_list = ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']
        utlis.handle_directories(files_list=files_list)

        url = 'https://www.dropbox.com/sh/vq4wb9fd9k1fz49/AADLR3IIgj8lMWs8m9QLzdPoa?dl=1'

        dbox.get_files(url=url, loc='./p_tree/data/photos.zip')

        assert True==True

    def test_seed_image_creation(self):
        assert True==True


    def test_temp_image_creation(self):
        assert True==True




if __name__ == '__main__':
    unittest.main()
