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


def test_repo_url_clean_repository_url():
    assert "https://github.com/mr-alexov/aov_automation_docs" == repo_string(
        "https://github.com/mr-alexov/aov_automation_docs")


def test_repo_url_repository_url_plus_git():
    assert "https://github.com/mr-alexov/aov_automation_docs" == repo_string(
        "https://github.com/mr-alexov/aov_automation_docs.git")


def test_repo_url_file_url():
    assert "https://github.com/mr-alexov/aov_automation_docs" == repo_string(
        "https://github.com/mr-alexov/aov_automation_docs/blob/master/src/test/java/examples/FightThePopups.java")


def test_complete_string():
    assert ("git clone https://github.com/mr-alexov/aov_automation_docs mr-alexov_aov_automation_docs" ==
            compose_command_line_string(
                "https://github.com/mr-alexov/aov_automation_docs/blob/master/src/test/java/examples/FightThePopups.java"))
