import requests

def check_for_pushes(repo_url, repo_name):
  """Checks if there are any pushes to the specified repository.

  Args:
    repo_url: The URL of the repository.
    repo_name: The name of the repository.

  Returns:
    True if there are any pushes, False otherwise.
  """

  url = "https://api.github.com/repos/{}/{}/commits".format(repo_url, repo_name)
  response = requests.get(url)

  if response.status_code == 200:
    commits = response.json()
    return len(commits) > 0

  return False

if __name__ == "__main__":
  repo_url = "https://github.com/mohanvedase/CICDrepo.git"
  repo_name = "CICDrepo"
  has_pushes = check_for_pushes(repo_url, repo_name)

  if has_pushes:
    print("There are pushes to the repository.")
  else:
    print("There are no pushes to the repository.")
