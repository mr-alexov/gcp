from gcp import *


def test_folder_name_clean_repository_url():
    assert "mr-alexov_aov_automation_docs" == folder_string(
        "https://github.com/mr-alexov/aov_automation_docs")


def test_folder_name_repository_url_plus_git():
    assert "mr-alexov_aov_automation_docs" == folder_string(
        "https://github.com/mr-alexov/aov_automation_docs.git")


def test_folder_name_file_url():
    assert "mr-alexov_aov_automation_docs" == folder_string(
        "https://github.com/mr-alexov/aov_automation_docs/blob/master/src/test/java/examples/FightThePopups.java")
